from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

from reader.dji.djmd_raw import DjmdRaw
from writer.debug.text import StdoutWriter
from writer.gpx.gpx import GpxWriter


def parse_file(path: Path, output) -> int:
    data = path.read_bytes()
    print(f"Reading: {path} ({len(data)} bytes)", file=sys.stderr)

    meta_count = 0
    last_data = None
    reader = DjmdRaw(data)
    # output = GpxWriter("foo")
    for gps_data in reader.reader_iter():
        meta_count += 1

        if last_data is not None and gps_data == last_data:
            continue
        last_data = gps_data

        output.write(gps_data)

    if meta_count == 0:
        print("No meta records found", file=sys.stderr)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Decode DJI djmd streams.")
    parser.add_argument("paths", nargs="+", help="Path(s) to the binary .dat file(s)")
    args = parser.parse_args()

    output = GpxWriter()

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

        output.start_section()
        rc = parse_file(path, output)
        if rc != 0:
            return rc
        output.end_section()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
