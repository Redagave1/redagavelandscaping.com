#!/bin/bash
cd "$(dirname "$0")"
echo ""
echo "==========================================="
echo "  Red Agave Photo Exporter"
echo "  GBP (≤5 MB, geotagged) + Gallery (fast)"
echo "==========================================="
echo ""
echo "  Organize photos in input/ subfolders for SEO names:"
echo "    input/xeriscape-blazyk/  → austin-xeriscape-blazyk-001"
echo "    input/landscape-lighting/ → austin-landscape-lighting-001"
echo ""
python3 export_for_google.py
echo ""
echo "Press any key to close..."
read -n 1
