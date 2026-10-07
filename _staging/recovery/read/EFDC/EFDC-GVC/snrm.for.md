---
file: models/EFDC/raw/source_code/EFDC-GVC/snrm.for
lines: 35
sha256: 3239cea2f530f648a13e108925dd9378a2753393b45efa290e6bdb9e9596e16e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# snrm.for — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 구분 주석과 `FUNCTION SNRM(N,SX,ITOL)` 입구(1–6). EFDC-FULL 1.0a·2001년 수정일·변경 기록 머리말(7–18). `INCLUDE 'EFDC.PAR'` (19), `DIMENSION SX(LCM)` (20). 포함 파일 내부는 이 판독 대상이 아니다. |
| 21–26 | 시작 시 6행 SNRM 함수 안. `IF(ITOL.LE.3)THEN` (21)이면 반환값 SNRM=0 초기화(22). `DO 11 I=1,N` (23)에서 `SNRM=SNRM+SX(I)**2` (24)로 제곱합을 누적하고 11 CONTINUE로 반복 종료(25). `SNRM=SQRT(SNRM)` (26)로 유클리드 노름(Euclidean norm)을 계산한다. |
| 27–35 | 시작 시 6행 SNRM 함수·21행 IF 조건문 안. ELSE(27)는 ITOL.LE.3 조건 불성립 경로이다. ISAMAX=1 초기화(28). `DO 12 I=1,N` (29)에서 `IF(ABS(SX(I)).GT.ABS(SX(ISAMAX))) ISAMAX=I` (30)로 최대 절댓값 위치를 갱신한다. 12 CONTINUE 뒤 `SNRM=ABS(SX(ISAMAX))` (32)로 최대 노름(maximum norm)을 반환한다. IF 종료·RETURN·END(33–35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–32: 이 함수에는 N의 양수 여부 및 N<=LCM 검사가 없다. N=0일 때 ITOL<=3 경로는 0을 유지한다. ITOL>3 경로는 ISAMAX=1 초기화 뒤 SX(1)을 참조한다.
- 28–30: 최대 절댓값 위치 갱신은 엄격한 GT 비교이다. 같은 절댓값의 원소는 기존 ISAMAX를 바꾸지 않는다.
