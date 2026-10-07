---
file: models/EFDC/raw/source_code/EFDC-GVC/wqzero2.for
lines: 58
sha256: 948e85ba0c38a54a1c4ddc46d8b135237e8cc922a18bebabaf61ba9377c729ca
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wqzero2.for — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `WQZERO2` 시작(6). 일변화(diurnal) 용존산소(dissolved oxygen, DO) 누적 배열 초기화 목적, 작성·수정 날짜·버전·변경 기록 틀을 적는다(10–27). `EFDC.PAR`·`EFDC.CMN`을 포함한다(29–30). |
| 32–47 | 시작 시 6행 WQZERO2 루틴 안. 셀 LL=2..LA·층 K=1..KC 루프를 연다(32–33). SODSUM·RKASUM·SWQSUM·TEMSUM·DZSUM·DOOSUM·DOSSUM과 조류 배열 CYASUM·DIASUM·GRNSUM·XMACSUM을 0으로 둔다(35–47). 원문 조건·계산식·반복·호출: `DO LL=2,LA` (32), `DO K=1,KC` (33), `SODSUM(LL,K) = 0.0` (37), `RKASUM(LL,K) = 0.0` (38), `SWQSUM(LL,K) = 0.0` (39), `TEMSUM(LL,K) = 0.0` (40), `DZSUM(LL,K)  = 0.0` (41), `DOOSUM(LL,K) = 0.0` (42), `DOSSUM(LL,K) = 0.0` (43), `CYASUM(LL,K) = 0.0` (44), `DIASUM(LL,K) = 0.0` (45), `GRNSUM(LL,K) = 0.0` (46), `XMACSUM(LL,K) = 0.0` (47). |
| 48–53 | 시작 시 6행 WQZERO2 루틴·32행 LL 루프·33행 K 루프 안. I=1..4 루프에서 RESPSUM·PRODSUM의 셋째 인덱스 네 개를 0으로 초기화한다(48–51). I·K·LL 루프를 닫는다(51–53). 원문 조건·계산식·반복·호출: `DO I=1,4` (48), `RESPSUM(LL,K,I) = 0.0` (49), `PRODSUM(LL,K,I) = 0.0` (50). |
| 54–58 | 시작 시 6행 WQZERO2 루틴 안. TIMESUM2=0·NDOCNT=0으로 시간 합과 횟수를 초기화한다(54–55). 빈 주석·RETURN·END를 포함한다(56–58). 원문 조건·계산식·반복·호출: `TIMESUM2 = 0.0` (54), `NDOCNT = 0` (55). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–50: RESPSUM·PRODSUM의 셋째 인덱스 초기화 범위는 고정 1..4이다.
