class StdoutWriter:
    def __init__(self):
        pass

    def write(self, gps_data):
        print(self._format_gps(gps_data))

    def _format_gps(self, gps_data) -> str:
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
