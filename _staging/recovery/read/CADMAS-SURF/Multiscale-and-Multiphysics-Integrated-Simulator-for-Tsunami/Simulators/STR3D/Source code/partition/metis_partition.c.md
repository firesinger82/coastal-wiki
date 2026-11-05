---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/metis_partition.c
lines: 34
sha256: 9fe72dbeaabfbde4dc40984a49e05257498645619887d7e214077787352bf55d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# metis_partition.c — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | METIS_NOPTIONS를 40으로 정의한다. 옵션 배열을 -1로 채운 뒤 METIS_SetDefaultOptions를 호출한다. vwgt·vsize·tpwgts를 NULL로 두고 METIS_PartMeshDual을 호출한다. 해석: 함수명은 이중 그래프 분할을 뜻하는 것으로 읽힌다. 원문: `#include <stdio.h>` (1); `#define METIS_NOPTIONS 40` (2); `void metis_partition(int *ne, int *nn, int *eptr, int *eind, ` (4); `					 int *ncommon, int *nparts, int *epart, int *npart) ` (5); `{` (6); `	int *vwgt = NULL;` (7); `	int *vsize = NULL;` (8); `	int options[METIS_NOPTIONS];` (9); `	int objval;` (10); `	float *tpwgts = NULL;` (11); `	int i;` (12); `	for (i=0; i<METIS_NOPTIONS; i++)` (14); `		options[i] = -1;` (15); `	METIS_SetDefaultOptions(options); ` (17); `	METIS_PartMeshDual(ne, nn, eptr, eind, vwgt, vsize, ncommon, nparts, tpwgts, ` (19); `					   options, &objval, epart, npart);` (20); `}` (21). [11-04 전수 검증 정정] |
| 22–34 | 대문자 METIS_PARTITION과 후행 밑줄 metis_partition_ 진입점은 같은 인수로 metis_partition을 호출한다. 원문: `void METIS_PARTITION(int *ne, int *nn, int *eptr, int *eind, ` (23); `					 int *ncommon, int *nparts, int *epart, int *npart) ` (24); `{` (25); `	metis_partition(ne, nn, eptr, eind, ncommon, nparts, epart, npart);` (26); `}` (27); `void metis_partition_(int *ne, int *nn, int *eptr, int *eind, ` (29); `					  int *ncommon, int *nparts, int *epart, int *npart) ` (30); `{` (31); `	metis_partition(ne, nn, eptr, eind, ncommon, nparts, epart, npart);` (32); `}` (33). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–20: 포함하는 헤더는 stdio.h뿐이다. METIS 함수 호출의 반환값을 받는 대입이나 검사문은 없다.
- 2·9·19–20: 옵션 배열 길이는 40으로 직접 정의한다. objval은 호출 인수로 전달하고 이후 이 파일에서 사용하지 않는다.
