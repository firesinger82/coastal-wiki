#!/bin/bash
S=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad
cd /home/firesinger/coastal-wiki
source ~/.venvs/pdfocr/bin/activate
for f in models/ADCIRC/raw/manuals/pdfs/*.pdf; do
  b=$(basename "$f" .pdf); [ -f _staging/recovery/extract/ADCIRC/marker/$b/$b.md ] && continue
  marker_single "$f" --output_dir _staging/recovery/extract/ADCIRC/marker --paginate_output --disable_image_extraction >> $S/admarker.log 2>&1
done
echo "MARKER-ADCIRC-DONE $(date +%T)" >> $S/progress.txt
