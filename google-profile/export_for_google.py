"""
Red Agave Photo Exporter — GBP + Website Gallery

1. Drop photos into input/
2. Double-click "Geotag Photos"
3. It asks: "Describe these photos" → type something like:
     xeriscape blazyk
     landscape lighting westlake
     concrete patio cedar park

Output:
    output/gbp/      — Geotagged JPEGs ≤ 5 MB for Google Business Profile
    output/gallery/  — Speed-optimized WebP for website gallery
"""

from PIL import Image
import piexif
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR  = os.path.join(SCRIPT_DIR, 'input')
GBP_DIR    = os.path.join(SCRIPT_DIR, 'output', 'gbp')
GALLERY_DIR = os.path.join(SCRIPT_DIR, 'output', 'gallery')

IMAGE_EXTS = ('.webp', '.jpg', '.jpeg', '.png', '.heic', '.tiff', '.tif', '.bmp')

GBP_MAX_BYTES = 5 * 1024 * 1024
GBP_MAX_PX    = 4000
GBP_QUALITY   = 92

GALLERY_WIDTH  = 1200
GALLERY_QUALITY = 80

LOCATIONS = {
    'blazyk':     (30.1715, -97.8581, 'Circle C'),
    'hopeland':   (30.1715, -97.8581, 'Circle C'),
    'axehandle':  (30.4486, -97.6201, 'Pflugerville'),
    'madison':    (30.3080, -97.7390, 'North Austin'),
    'riverview':  (30.3750, -97.6800, 'Pflugerville'),
    'flycatcher': (30.2950, -97.7700, 'Austin'),
    'ulit':       (30.2630, -97.7150, 'East Austin'),
    'dormarion':  (30.2950, -97.7720, 'Tarrytown'),
}

DEFAULT_LOC = (30.2672, -97.7431, 'Austin')


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


def guess_project(text):
    text_lower = text.lower()
    for project in LOCATIONS:
        if project in text_lower:
            return project
    return None


def make_slug(description):
    slug = description.lower().strip()
    slug = slug.replace('  ', ' ').replace(' ', '-').replace('_', '-')
    for ch in '.,;:!?\'\"()[]{}':
        slug = slug.replace(ch, '')
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug.strip('-')


def seo_name(slug, project, index):
    parts = ['austin']

    if slug:
        parts.append(slug)
    elif project:
        parts.append(f'landscaping-{project}')
    else:
        parts.append('landscaping')

    if project and project not in slug:
        loc = LOCATIONS[project]
        city = loc[2].lower().replace(' ', '-')
        if city != 'austin':
            parts.append(city)

    parts.append(f'{index:03d}')
    return '-'.join(parts)


def get_location(description, filename):
    project = guess_project(description) or guess_project(filename)
    if project:
        loc = LOCATIONS[project]
        return loc[0], loc[1], f'{loc[2]}, Austin TX', project
    return DEFAULT_LOC[0], DEFAULT_LOC[1], 'Austin TX', None


def resize_to_fit(img, max_dim):
    w, h = img.size
    if max(w, h) <= max_dim:
        return img
    scale = max_dim / max(w, h)
    return img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)


def resize_to_width(img, max_w):
    w, h = img.size
    if w <= max_w:
        return img
    scale = max_w / w
    return img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)


def save_gbp(img, dst, exif_bytes):
    sized = resize_to_fit(img, GBP_MAX_PX)
    quality = GBP_QUALITY

    sized.save(dst, 'JPEG', quality=quality, exif=exif_bytes)
    while os.path.getsize(dst) > GBP_MAX_BYTES and quality > 60:
        quality -= 5
        sized.save(dst, 'JPEG', quality=quality, exif=exif_bytes)

    if os.path.getsize(dst) > GBP_MAX_BYTES:
        w, h = sized.size
        sized = sized.resize((int(w * 0.8), int(h * 0.8)), Image.LANCZOS)
        sized.save(dst, 'JPEG', quality=quality, exif=exif_bytes)

    return os.path.getsize(dst)


def save_gallery(img, dst):
    sized = resize_to_width(img, GALLERY_WIDTH)
    sized.save(dst, 'WEBP', quality=GALLERY_QUALITY)
    return os.path.getsize(dst)


def main():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(GBP_DIR, exist_ok=True)
    os.makedirs(GALLERY_DIR, exist_ok=True)

    files = sorted([f for f in os.listdir(INPUT_DIR)
                    if os.path.isfile(os.path.join(INPUT_DIR, f))
                    and f.lower().endswith(IMAGE_EXTS)])

    if not files:
        print(f'No images found in {INPUT_DIR}/')
        print('Drop photos there and re-run.')
        sys.exit(0)

    print(f'\nFound {len(files)} photos in input/\n')
    print('Describe these photos for SEO naming.')
    print('Examples:')
    print('  xeriscape blazyk')
    print('  landscape lighting westlake')
    print('  concrete patio fire pit')
    print('  outdoor living hopeland')
    print()
    description = input('Description: ').strip()

    if not description:
        print('No description entered — using "landscaping"')
        description = 'landscaping'

    slug = make_slug(description)
    project = guess_project(description)
    lat, lon, label, project = get_location(description, '')

    exif_bytes = build_gps_exif(lat, lon)

    print(f'\n  Slug:     austin-{slug}-###')
    print(f'  Geotag:   {label} ({lat:.4f}, {lon:.4f})')
    print(f'  Photos:   {len(files)}')
    print()

    count = 0
    for idx, fname in enumerate(files, 1):
        fpath = os.path.join(INPUT_DIR, fname)
        name = seo_name(slug, project, idx)

        try:
            img = Image.open(fpath)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')

            gbp_path = os.path.join(GBP_DIR, name + '.jpg')
            gbp_size = save_gbp(img, gbp_path, exif_bytes)

            gal_path = os.path.join(GALLERY_DIR, name + '.webp')
            gal_size = save_gallery(img, gal_path)

            gbp_mb = gbp_size / (1024 * 1024)
            gal_kb = gal_size / 1024
            print(f'  ✓ {fname}')
            print(f'    → {name}.jpg  ({gbp_mb:.1f} MB)')
            print(f'    → {name}.webp ({gal_kb:.0f} KB)')
            count += 1

        except Exception as e:
            print(f'  ✗ {fname}: {e}')

    print(f'\n{"="*50}')
    print(f'Done! {count}/{len(files)} photos exported.')
    print(f'  GBP:     {GBP_DIR}/')
    print(f'  Gallery: {GALLERY_DIR}/')
    print(f'  Geotag:  {label}')


if __name__ == '__main__':
    main()
