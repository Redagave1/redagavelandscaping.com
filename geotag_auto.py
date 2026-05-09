"""
Auto-geotagger for Red Agave gallery images.
Triggered by launchd whenever the gallery folder changes.
Only processes WebP files that don't already have GPS EXIF data.
Coordinates: 30.2672 N, 97.7431 W — Austin, Texas
"""

from PIL import Image
import piexif
import os
import sys
from datetime import datetime

import time
time.sleep(2)  # Let any in-progress file writes finish before we scan

GALLERY_DIR = '/Users/jensenmehrens/Desktop/redagave-deploy/images/gallery/'
LOG_FILE    = '/Users/jensenmehrens/Desktop/redagave-deploy/geotag.log'
LAT  =  30.2672
LON  = -97.7431


def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')


def to_dms(decimal):
    d = int(abs(decimal))
    m = int((abs(decimal) - d) * 60)
    s = round((abs(decimal) - d - m / 60) * 3600 * 10000)
    return [(d, 1), (m, 1), (s, 10000)]


def already_tagged(filepath):
    """Return True if the file already has GPS latitude in its EXIF."""
    try:
        img = Image.open(filepath)
        exif_data = img.info.get('exif', b'')
        if not exif_data:
            return False
        exif_dict = piexif.load(exif_data)
        return bool(exif_dict.get('GPS', {}).get(piexif.GPSIFD.GPSLatitude))
    except Exception:
        return False


gps_ifd = {
    piexif.GPSIFD.GPSLatitudeRef:  b'N',
    piexif.GPSIFD.GPSLatitude:     to_dms(LAT),
    piexif.GPSIFD.GPSLongitudeRef: b'W',
    piexif.GPSIFD.GPSLongitude:    to_dms(abs(LON)),
}
exif_bytes = piexif.dump({"GPS": gps_ifd})

files = [f for f in os.listdir(GALLERY_DIR) if f.lower().endswith('.webp')]
tagged, skipped = 0, 0

for fname in sorted(files):
    fpath = os.path.join(GALLERY_DIR, fname)
    if already_tagged(fpath):
        skipped += 1
        continue
    try:
        img = Image.open(fpath)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        img.save(fpath, 'WEBP', quality=92, exif=exif_bytes)
        log(f"Tagged: {fname}")
        tagged += 1
    except Exception as e:
        log(f"ERROR {fname}: {e}")

if tagged:
    log(f"Done — {tagged} new file(s) tagged, {skipped} already had GPS.")
else:
    log(f"No new files to tag ({skipped} already tagged).")
