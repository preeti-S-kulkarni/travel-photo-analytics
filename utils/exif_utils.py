from __future__ import annotations

import os
from typing import Optional, Dict, Any

import exifread

# Timestamp tags to try, in priority order
TIMESTAMP_TAGS = [
    ("EXIF DateTimeOriginal", "DateTimeOriginal"),
    ("EXIF DateTimeDigitized", "DateTimeDigitized"),
    ("Image DateTime", "ImageDateTime"),
]

GPS_TAGS = {
    "lat": "GPS GPSLatitude",
    "lat_ref": "GPS GPSLatitudeRef",
    "lon": "GPS GPSLongitude",
    "lon_ref": "GPS GPSLongitudeRef",
}


def _safe_get(tags: dict, tag_name: str) -> Optional[str]:
    v = tags.get(tag_name)
    return str(v) if v is not None else None


def extract_exif(photo_path: str) -> Dict[str, Any]:
    """
    Robust EXIF extraction with:
    - fallback timestamp tags
    - status/error capture
    - consistent schema
    """
    base = {
        "photo_path": photo_path,
        "file_name": os.path.basename(photo_path),
        "file_ext": os.path.splitext(photo_path)[1].lower(),
        "timestamp_raw": None,
        "timestamp_source": None,
        "camera": None,
        "gps_lat": None,
        "gps_lat_ref": None,
        "gps_lon": None,
        "gps_lon_ref": None,
        "exif_present": False,
        "status": "ok",          # ok | error
        "error_message": None,   # only if status == error
    }

    try:
        with open(photo_path, "rb") as f:
            tags = exifread.process_file(f, details=False)

        base["exif_present"] = bool(tags)

        base["camera"] = _safe_get(tags, "Image Model")

        # Timestamp with fallbacks + source
        for tag, source in TIMESTAMP_TAGS:
            ts = _safe_get(tags, tag)
            if ts:
                base["timestamp_raw"] = ts
                base["timestamp_source"] = source
                break

        # GPS fields
        base["gps_lat"] = _safe_get(tags, GPS_TAGS["lat"])
        base["gps_lat_ref"] = _safe_get(tags, GPS_TAGS["lat_ref"])
        base["gps_lon"] = _safe_get(tags, GPS_TAGS["lon"])
        base["gps_lon_ref"] = _safe_get(tags, GPS_TAGS["lon_ref"])

        return base

    except Exception as e:
        base["status"] = "error"
        base["error_message"] = f"{type(e).__name__}: {e}"
        return base
