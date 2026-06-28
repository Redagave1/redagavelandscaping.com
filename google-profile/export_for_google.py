"""
Export geotagged JPEGs for Google Business Profile.

Drop any .webp or .jpg/.jpeg files into the google-profile/input/ folder,
then run:  python3 google-profile/export_for_google.py

Output: google-profile/output/ — geotagged JPEGs ready to upload to Google.

Uses project-specific coordinates when the filename matches a known project,
otherwise defaults to Red Agave's Austin, TX coordinates.
"""

from PIL import Image
import piexif
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR  = os.path.join(SCRIPT_DIR, 'input')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')

LOCATIONS = {
    'blazyk':     (30.1715, -97.8581, 'Circle C, Austin TX'),
    'hopeland':   (30.1715, -97.8581, 'Circle C, Austin TX'),
    'axehandle':  (30.4486, -97.6201, 'Pflugerville TX'),
    'madison':    (30.3080, -97.7390, 'North Austin TX'),
    'riverview':  (30.3750, -97.6800, 'Pflugerville TX'),
    'flycatcher': (30.2950, -97.7700, 'Austin TX'),
    'ulit':       (30.2630, -97.7150, 'East Austin TX'),
    'dormarion':  (30.2950, -97.7720, 'Tarrytown, Austin TX'),
}

DEFAULT_LOC = (30.2672, -97.7431, 'Austin TX')


def to_dms(decimal):
    d = int(abs(decimal))
    m = int((abs(decimal) - d) * 60)
    s = round((abs(decimal) - d - m / 60) * 3600 * 10000)
    return [(d, 1), (m, 1), (s, 10000)]


def build_gps_exif(lat, lon):
    gps_ifd = {
        piexif.GPSIFD.GPSLatitudeRef:  b'N' if lat >= 0 else b'S',
        piexif.GPSIFD.GPSLatitude:     to_dms(lat),
        piexif.GPSIFD.GPSLongitudeRef: b'W' if lon < 0 else b'E',
        piexif.GPSIFD.GPSLongitude:    to_dms(abs(lon)),
    }
    return piexif.dump({"GPS": gps_ifd})


def guess_location(filename):
    fname_lower = filename.lower()
    for project, loc in LOCATIONS.items():
        if project in fname_lower:
            return loc
    return DEFAULT_LOC


def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = [f for f in os.listdir(INPUT_DIR)
             if f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png', '.heic', '.tiff', '.tif', '.bmp'))]

    if not files:
        print(f"No images found in {INPUT_DIR}/")
        print("Drop .webp, .jpg, or .png files there and re-run.")
        sys.exit(0)

    print(f"Processing {len(files)} images...\n")

    for fname in sorted(files):
        src = os.path.join(INPUT_DIR, fname)
        out_name = os.path.splitext(fname)[0] + '.jpg'
        dst = os.path.join(OUTPUT_DIR, out_name)

        lat, lon, label = guess_location(fname)
        exif_bytes = build_gps_exif(lat, lon)

        try:
            img = Image.open(src)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.save(dst, 'JPEG', quality=92, exif=exif_bytes)
            print(f"  ✓ {fname} → {out_name}  [{label}]")
        except Exception as e:
            print(f"  ✗ {fname}: {e}")

    print(f"\nDone! Geotagged JPEGs are in: {OUTPUT_DIR}/")


if __name__ == '__main__':
    main()
