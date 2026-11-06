from __future__ import annotations

import argparse

from pathlib import Path

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


def iter_product_meta_records(blob: bytes):
    """Scan the file for repeated ProductMeta records and yield each decoded message."""
    pos = 0
    count = 0

    while pos < len(blob):
        try:
            tag, pos = read_varint(blob, pos)
        except EOFError as e:
            print(f"Error occurred while reading varint: {e}")
            break

        field_no = tag >> 3
        wire_type = tag & 0x7

        if field_no in [1, 2, 3] and wire_type == 2:
            try:
                length, pos = read_varint(blob, pos)
            except EOFError as e:
                print(f"Error occurred while reading varint: {e}")
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
                print(f"Error occurred while skipping field: {e}")
                break


def fmt_enum_name(value, enum_type):
    if value is None:
        return "unknown"
    try:
        return enum_type.Name(value)
    except Exception:
        return str(value)


def friendly_gps(gps_basic) -> str:
    if gps_basic is None:
        return "GPS: unavailable"

    coords = gps_basic.gps_coordinates
    lat = lon = None
    if coords:
        lat = coords.latitude
        lon = coords.longitude

    if lat is None and lon is None:
        lat_lon = "n/a"
    else:
        lat_lon = f"lat={lat:.6f}, lon={lon:.6f}"

    status = fmt_enum_name(gps_basic.gps_status, gps_basic.__class__.GpsStatus)
    alt_type = fmt_enum_name(gps_basic.gps_altitude_type, gps_basic.__class__.GpsAltType)

    altitude_m = gps_basic.gps_altitude_mm / 1000.0 if gps_basic.gps_altitude_mm else None
    altitude_text = f"alt={altitude_m:.3f} m" if altitude_m is not None else "alt=n/a"
    time_text = gps_basic.gps_time.time if gps_basic.has_gps_time and gps_basic.gps_time else "time=n/a"

    return f"GPS: {lat_lon}; {altitude_text}; status={status}; " f"alt_type={alt_type}; time={time_text}"


def print_record_summary(index: int, msg: dvtm_oq101_pb2.FrameMeta) -> None:
    # print (str(msg))
    gimbal = getattr(msg, "gimbal_frame_meta", None)
    gps_basic = getattr(gimbal, "gps_basic", None)

    if gps_basic is not None:
        print(f"Chunk {index}: {friendly_gps(gps_basic)}")
    else:
        print(f"Chunk {index}: GPS: no GpsBasic found in gimbal_frame_meta")


def parse_file(path: Path) -> int:
    data = path.read_bytes()
    print(f"Reading: {path} ({len(data)} bytes)")

    meta_count = 0
    for index, msg in iter_product_meta_records(data):
        meta_count += 1
        if type(msg) is dvtm_oq101_pb2.FrameMeta:
            print_record_summary(index, msg)
        else:
            print(f"Chunk {index}: Found a non-FrameMeta record of type {type(msg).__name__}")

    if meta_count == 0:
        print("No meta records found. Checking whether the file is a single ProductMeta payload...")
        try:
            msg = dvtm_oq101_pb2.ProductMeta()
            msg.ParseFromString(data)
            print_record_summary(1, msg.frame_meta)
            return 0
        except Exception as e:
            print(f"Could not decode any ProductMeta messages from the file: {e}")
            return 1

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Decode DJI djmd streams.")
    parser.add_argument("path", nargs="?", help="Path to the binary .dat file")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"File not found: {path}")
        return 1

    return parse_file(path)


if __name__ == "__main__":
    raise SystemExit(main())
