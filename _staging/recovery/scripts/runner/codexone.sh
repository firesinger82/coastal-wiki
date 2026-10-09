#!/bin/bash
# usage: codexone.sh TAG  — runs $S/TAG.txt via codex exec, logs to $S/TAG.log, progress line in progress.txt
S=/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad
cd /home/firesinger/coastal-wiki
echo "START $1 $(date +%T)" >> $S/progress.txt
codex exec -m gpt-6.1-sol -s workspace-write --json - < $S/$1.txt > $S/$1.log 2>$S/$1.err
echo "DONE $1 exit=$? $(date +%T)" >> $S/progress.txt
