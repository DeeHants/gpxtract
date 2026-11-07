from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

from reader.dji.djmd_raw import DjmdRaw


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


def parse_file(path: Path) -> int:
    data = path.read_bytes()
    print(f"Reading: {path} ({len(data)} bytes)", file=sys.stderr)

    meta_count = 0
    last_data = None
    reader = DjmdRaw(data)
    for gps_data in reader.reader_iter():
        meta_count += 1

        if last_data is not None and gps_data == last_data:
            continue
        last_data = gps_data

        print(friendly_gps(gps_data))

    if meta_count == 0:
        print("No meta records found", file=sys.stderr)

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
