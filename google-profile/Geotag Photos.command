#!/bin/bash
cd "$(dirname "$0")"
echo ""
echo "==========================================="
echo "  Red Agave Photo Exporter"
echo "  GBP (≤5 MB, geotagged) + Gallery (fast)"
echo "==========================================="
python3 export_for_google.py
echo ""
echo "Press any key to close..."
read -n 1
