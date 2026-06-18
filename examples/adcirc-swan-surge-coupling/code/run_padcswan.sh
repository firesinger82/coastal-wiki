#!/usr/bin/env bash
# ============================================================================
# run_padcswan.sh — ADCIRC+SWAN 결합 실행 순서 OUTLINE (절차 템플릿)
# ----------------------------------------------------------------------------
# 핵심: 결합은 'padcswan' 바이너리로만 동작. 'padcirc' 는 NWS=3xx 라도 SWAN 이
#       링크되지 않아 파 없이 조용히 실행됨 (makefile:195-233).
#       근거: models/ADCIRC/source-analysis/adcirc-swan-coupling.md (§G)
# 입력: fort.14(공유 비정형 메시) · fort.15(ADCIRC) · fort.26(SWAN)
#       (+ fort.13 nodal attr / fort.22 기상, 도메인 따라)
# <...> 자리는 실제 값으로 대체.
# ============================================================================
set -euo pipefail

NP=<N>                      # MPI 프로세스 수
ADCIRC_BIN=<path>/padcswan  # 결합 바이너리 (반드시 padcswan)
ADCPREP=<path>/adcprep

# 0) 입력 확인 — ADCIRC 와 SWAN 이 같은 fort.14 를 봐야 함 (단일 메시)
test -f fort.14 && test -f fort.15 && test -f fort.26

# 1) 메시 분할 + 입력 prep (병렬 실행 시)
"$ADCPREP" --np "$NP" --partmesh    # metis 분할 → partmesh.txt
"$ADCPREP" --np "$NP" --prepall     # fort.14/15/(13/22) 를 PE 별로 분배
# 주: SWAN 결합 입력(fort.26)도 prep 단계에서 PE 별 처리됨
#     (SWAN switch -pun -adcirc 로 빌드된 padcswan 기준)

# 2) 결합 실행
mpirun -np "$NP" "$ADCIRC_BIN"

# 3) 산출 (병렬 결과 병합은 버전에 따라 자동/별도 adcpost)
#    ADCIRC: fort.63 (수위 η = surge + tide + wave setup), fort.64 (유속),
#            maxele.63 (최대 수위)
#    SWAN  : fort.26 의 BLOCK/TABLE 출력 (Hs, Tp, Dir)

# 검증 포인트는 results/README.md 참조.
