from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

import dvtm_oq101_pb2


def read_varint(data: bytes, pos: int) -> tuple[int, int]:
    """Read a protobuf varint from the buffer at the given offset."""
    value = 0
    shift = 0
    while True:
        if pos >= len(data):
            raise EOFError("Unexpected end of data while reading varint")
        b = data[pos]
        pos += 1
        value |= (b & 0x7F) << shift
        if (b & 0x80) == 0:
            return value, pos
        shift += 7
        if shift > 64:
            raise ValueError("Varint exceeds 64 bits")


def skip_field(data: bytes, pos: int, wire_type: int) -> int:
    """Advance position past a single field in a protobuf stream."""
    if wire_type == 0:  # varint
        _, pos = read_varint(data, pos)
    elif wire_type == 1:  # fixed64
        pos += 8
    elif wire_type == 2:  # length-delimited
        length, pos = read_varint(data, pos)
        pos += length
    elif wire_type == 5:  # fixed32
        pos += 4
    else:
        raise ValueError(f"Unsupported wire type {wire_type} in stream")
    return pos


def djmd_meta_records_iter(blob: bytes):
    """Scan the file for repeated ProductMeta records and yield each decoded message."""
    pos = 0
    count = 0

    while pos < len(blob):
        try:
            tag, pos = read_varint(blob, pos)
        except EOFError as e:
            print(f"Error occurred while reading varint: {e}", file=sys.stderr)
            break

        field_no = tag >> 3
        wire_type = tag & 0x7

        if field_no in [1, 2, 3] and wire_type == 2:
            try:
                length, pos = read_varint(blob, pos)
            except EOFError as e:
                print(f"Error occurred while reading varint: {e}", file=sys.stderr)
                break

            end = pos + length
            if end > len(blob):
                break
            payload = blob[pos:end]
            pos = end

            if field_no == 1:
                msg = dvtm_oq101_pb2.ClipMeta()
            elif field_no == 2:
                msg = dvtm_oq101_pb2.StreamMeta()
            else:
                msg = dvtm_oq101_pb2.FrameMeta()

            try:
                msg.ParseFromString(payload)
            except Exception:
                # Some files might contain a non-FrameMeta length-delimited record at this offset.
                # Skip it rather than failing the whole extraction pass.
                continue

            count += 1
            yield count, msg
        else:
            try:
                pos = skip_field(blob, pos, wire_type)
            except (EOFError, ValueError) as e:
                print(f"Error occurred while skipping field: {e}", file=sys.stderr)
                break


def friendly_gps(gps_data) -> str:
    if gps_data is None:
        return "GPS: unavailable"

    lat = gps_data.get("latitude", None)
    lon = gps_data.get("longitude", None)

    if lat is None and lon is None:
        lat_lon = "n/a"
    else:
        lat_lon = f"lat={lat:.6f}, lon={lon:.6f}"

    status = gps_data.get("status", "unknown")
    alt_type = gps_data.get("altitude_type", "unknown")

    altitude_m = gps_data.get("altitude") if gps_data.get("altitude") is not None else None
    altitude_text = f"alt={altitude_m:.3f} m" if altitude_m is not None else "alt=n/a"
    time_text = gps_data.get("time") if gps_data.get("time") is not None else "time=n/a"

    return f"GPS: {lat_lon}; {altitude_text}; status={status}; " f"alt_type={alt_type}; time={time_text}"


def extract_gps_point_data(msg: dvtm_oq101_pb2.FrameMeta) -> None:
    # print (str(msg))
    gimbal = getattr(msg, "gimbal_frame_meta", None)
    gps_basic = getattr(gimbal, "gps_basic", None)
    gps_coordinates = getattr(gps_basic, "gps_coordinates", None)

    if gps_basic is None:
        return None

    point_data = {}

    # Extract the status into a friendly string representation
    status_labels = {
        0: "Normal",  # The GPS status is normal.
        1: "Invalid",  # The GPS status is invalid.
        2: "RTK",  # The GPS status is RTK.
    }
    point_data["status"] = status_labels.get(gps_basic.gps_status, "Unknown")

    # Coordinates are in degrees, so we can use them directly
    if (
        gps_coordinates is not None
        and gps_coordinates.position_coord_unit == gps_coordinates.__class__.PositionCoordUnit.UNIT_DEG
    ):
        point_data["latitude"] = gps_coordinates.latitude
        point_data["longitude"] = gps_coordinates.longitude

    # Altitude is in millimeters, so we convert to meters for easier reading
    if gps_basic.gps_altitude_mm:
        point_data["altitude"] = gps_basic.gps_altitude_mm / 1000
        altitude_type_labels = {
            0: "Pressure",  # The altitude is provided by barometer which is not ellipsoidal height.
            1: "GPS fusion",  # Fuse GPS and barometer height, which based on ellipsoidal coordinate.
            2: "RTK",  # The altitude is ellipsoidal height (WGS-84) provided by RTK.
        }
        point_data["altitude_type"] = altitude_type_labels.get(gps_basic.gps_altitude_type, "Unknown")

    # If the GPS time is available, we can include it in the point data
    if gps_basic.has_gps_time and gps_basic.gps_time is not None:
        point_data["time"] = gps_basic.gps_time.time

    return point_data


def parse_file(path: Path) -> int:
    data = path.read_bytes()
    print(f"Reading: {path} ({len(data)} bytes)", file=sys.stderr)

    meta_count = 0
    for index, msg in djmd_meta_records_iter(data):
        meta_count += 1
        if type(msg) is dvtm_oq101_pb2.FrameMeta:
            gps_data = extract_gps_point_data(msg)
            if gps_data is not None:
                print(friendly_gps(gps_data))
            else:
                print(f"Chunk {index}: GPS: no GpsBasic found in gimbal_frame_meta", file=sys.stderr)
        else:
            print(f"Chunk {index}: Found a non-FrameMeta record of type {type(msg).__name__}", file=sys.stderr)

    if meta_count == 0:
        print("No meta records found. Checking whether the file is a single ProductMeta payload...", file=sys.stderr)
        try:
            msg = dvtm_oq101_pb2.ProductMeta()
            msg.ParseFromString(data)
            print_record_summary(1, msg.frame_meta)
            return 0
        except Exception as e:
            print(f"Could not decode any ProductMeta messages from the file: {e}", file=sys.stderr)
            return 1

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Decode DJI djmd streams.")
    parser.add_argument("paths", nargs="+", help="Path(s) to the binary .dat file(s)")
    args = parser.parse_args()

    for path_arg in args.paths:
        path = Path(path_arg)
        if not path.exists():
            print(f"File not found: {path}", file=sys.stderr)
            return 1

        # OSV files, we can extract the data streams
        if path.suffix == ".OSV":
            dat_path = Path(f"{path.parent}/{path.stem}_djmd.dat")
            print(f"Detected .OSV file: {path}. Will extract the data stream to {dat_path}", file=sys.stderr)
            if not dat_path.exists():
                # Generate the .dat file from the .OSV file using ffmpeg, then rename it to have a .dat suffix
                print(f"Converting {path} to .dat format using ffmpeg...", file=sys.stderr)
                subprocess.run(
                    ["ffmpeg", "-i", str(path), "-map", "0:d:0", "-c", "copy", "-f", "data", str(dat_path)], check=True
                )
            else:
                print(f"Using existing .dat file: {dat_path}", file=sys.stderr)

            path = dat_path

        rc = parse_file(path)
        if rc != 0:
            return rc

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
