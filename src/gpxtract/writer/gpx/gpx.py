class GpxWriter:
    def __init__(self):
        print('<?xml version="1.0" ?>')
        print(
            '<gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="OSV2GPX" version="1.1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">'
        )

    def start_section(self):
        print("  <trk>")
        print("    <trkseg>")

    def write(self, gps_data):
        print(f'      <trkpt lat="{gps_data.get("latitude", 0)}" lon="{gps_data.get("longitude", 0)}">')
        print(f'        <ele>{gps_data.get("altitude", 0)}</ele>')
        print(f'        <time>{gps_data.get("time", "")}</time>')
        print(f"      </trkpt>")

    def end_section(self):
        print("    </trkseg>")
        print("  </trk>")

    def __del__(self):
        print("</gpx>")
