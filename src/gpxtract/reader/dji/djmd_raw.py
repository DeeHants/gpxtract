import sys

from . import dvtm_oq101_pb2


class DjmdRaw:
    def __init__(self, data: bytes):
        self.data = data

    def meta_records_iter(self):
        """Scan the file for repeated ProductMeta records and yield each decoded message."""
        pos = 0
        count = 0

        blob = self.data  # Use the instance's data attribute

        while pos < len(blob):
            try:
                tag, pos = self.read_varint(blob, pos)
            except EOFError as e:
                print(f"Error occurred while reading varint: {e}", file=sys.stderr)
                break

            field_no = tag >> 3
            wire_type = tag & 0x7

            if field_no in [1, 2, 3] and wire_type == 2:
                try:
                    length, pos = self.read_varint(blob, pos)
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

    def read_varint(self, data: bytes, pos: int) -> tuple[int, int]:
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

    def skip_field(self, data: bytes, pos: int, wire_type: int) -> int:
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

    def extract_gps_point_data(self, msg: dvtm_oq101_pb2.FrameMeta) -> None:
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
