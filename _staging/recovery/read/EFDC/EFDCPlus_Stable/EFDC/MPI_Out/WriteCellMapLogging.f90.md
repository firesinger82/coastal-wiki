---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Out/WriteCellMapLogging.f90
lines: 39
sha256: abfde9f8fc3577e34e918fb84c9c396c6432818d42305c140e0720b8240b3e23
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# WriteCellMapLogging.f90 — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | EFDC+ 표제·저작권·GPLv2 안내와 비어 있는 details/author/date 주석(1–11). WriteCellMapLogging 입구(13). GLOBAL·Variables_MPI 사용·implicit none(15–18). 정수 L과 실수 GRADW/GRADE/GRADS/GRADN을 선언한다(20–22). 빈 줄 포함(12·14·17·19·23). |
| 24–39 | 셀 매핑(cell mapping) 로그의 머리글은 I/J/L/BELV/HP/DX/DY와 네 방향 경사(gradient)를 출력한다(24–26). 2..LA 루프(27)에서 기본값은 `GRADW = -999.` (28), `GRADE = -999.` (29), `GRADS = -999.` (30), `GRADN = -999.` (31)이다. 조건과 경사식은 `if( SUBO(L) > 0.      ) GRADW = ( BELV(LWC(L))+HP(LWC(L) ) - ( BELV(L)+HP(L) )           )/DXU(L)` (32), `if( SUBO(LEC(L)) > 0. ) GRADE = ( BELV(L)+HP(L)            - ( BELV(LEC(L))+HP(LEC(L)) ) )/DXU(LEC(L))` (33), `if( SVBO(L) > 0.      ) GRADS = ( BELV(LSC(L))+HP(LSC(L) ) - ( BELV(L)+HP(L) )           )/DYV(L)` (34), `if( SVBO(LNC(L)) > 0. ) GRADN = ( BELV(L)+HP(L)            - ( BELV(LNC(L))+HP(LNC(L)) ) )/DYV(LNC(L))` (35)이다. 각 식은 이웃과 현재 셀의 BELV+HP 차이를 DXU 또는 DYV로 나눈다. IL/JL/L·BELV/HP·DXP/DYP·네 경사를 3I6,4F10.3,4F14.5 형식으로 mpi_efdc_out_unit에 출력한다(36). 루프·루틴 종료·빈 줄(37–39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–35: 네 방향 경사의 기본값은 모두 -999.이다. 해당 SUBO 또는 SVBO 조건이 참일 때만 그 방향 값을 계산한다.
- 32–35: 경사식의 분모는 DXU 또는 DYV이다. 이 네 문장의 조건은 SUBO 또는 SVBO가 0보다 큰지를 검사한다. 분모 자체의 0 여부를 검사하는 문장은 이 루틴에 없다.

