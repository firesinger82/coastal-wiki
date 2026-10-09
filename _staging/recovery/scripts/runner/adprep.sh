#!/bin/bash
S=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad
cd /home/firesinger/coastal-wiki
E=_staging/recovery/extract/ADCIRC
find models/ADCIRC/raw/manuals/website -name "*.pptx" -print0 | xargs -0 -I{} soffice --headless --convert-to pdf --outdir $E/office "{}" >> $S/adprep.log 2>&1
for f in models/ADCIRC/raw/manuals/pdfs/*.pdf $E/office/*.pdf; do
  .venv/bin/opendataloader-pdf -q -o $E/pdf -f text --text-page-separator '<<<PAGE %page-number%>>>' --content-safety-off all --include-header-footer "$f" >> $S/adprep.log 2>&1
  .venv/bin/opendataloader-pdf -q -o $E/pdf-md -f markdown --use-struct-tree --markdown-page-separator '<<<PAGE %page-number%>>>' --content-safety-off all --include-header-footer "$f" >> $S/adprep.log 2>&1
  b=$(basename "$f" .pdf); pdftoppm -r 300 -png "$f" "$S/apages/$b"
done
echo "ADPREP-DONE $(date +%T) pages=$(ls $S/apages | wc -l)" >> $S/progress.txt
