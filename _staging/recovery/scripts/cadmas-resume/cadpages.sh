#!/bin/bash
# 쪽 이미지(300 dpi, 179 MB, 550쪽) 재생성. 작업 프롬프트가 $S/cadpages/<접두어>-NNN.png 를 연다.
S=${S:?set S to scratchpad}; mkdir -p $S/cadpages
K=/home/firesinger/coastal-wiki/_staging/recovery/scripts/cadmas-resume
R="/home/firesinger/coastal-wiki/models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami"
while IFS=$'\t' read b p; do pdftoppm -r 300 -png "$R/$p" "$S/cadpages/$b"; done < $K/cadlist.tsv
cd $S/cadpages; for p in *.png; do n=$(echo $p | sed -E 's/.*-0*([0-9]+)\.png/\1/'); b=$(echo $p | sed -E 's/-[0-9]+\.png//'); t=$(printf "%s-%03d.png" $b $n); [ "$p" != "$t" ] && mv "$p" "$t"; done
