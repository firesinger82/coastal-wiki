#!/bin/bash
# 5 worker groups × 3 stations = 15 stations parallel
# 각 worker가 정점 3개를 순차로 처리, 5 worker가 동시 실행
set -e
cd "$(dirname "$0")"
PY=/home/firesinger/coastal-wiki/.venv-tools/bin/python

# Group A (서해 1)
(${PY} fetch_one.py DT_0001 인천 && ${PY} fetch_one.py DT_0018 군산 && ${PY} fetch_one.py DT_0007 목포) &

# Group B (서해 2)
(${PY} fetch_one.py DT_0025 보령 && ${PY} fetch_one.py DT_0067 안흥) &

# Group C (남해 1)
(${PY} fetch_one.py DT_0005 부산 && ${PY} fetch_one.py DT_0020 울산 && ${PY} fetch_one.py DT_0014 통영) &

# Group D (남해 2)
(${PY} fetch_one.py DT_0016 여수 && ${PY} fetch_one.py DT_0049 광양) &

# Group E (동해 + 제주)
(${PY} fetch_one.py DT_0006 묵호 && ${PY} fetch_one.py DT_0091 포항 && ${PY} fetch_one.py DT_0012 속초 && ${PY} fetch_one.py DT_0004 제주 && ${PY} fetch_one.py DT_0010 서귀포) &

wait
echo "All workers completed at $(date)"
