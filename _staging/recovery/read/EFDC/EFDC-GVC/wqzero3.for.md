---
file: models/EFDC/raw/source_code/EFDC-GVC/wqzero3.for
lines: 76
sha256: 33838893fe153779a773fa33a95b9c3a13e9f40a8faee13acd79addc3cf43f91
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# wqzero3.for — 판독 구간 기록

구간은 1행부터 76행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `WQZERO3` 시작(6). 조류 제한(limitation)·용존산소(dissolved oxygen, DO) 성분 분석 배열의 초기화 목적, 작성·수정 날짜·버전·변경 기록 틀을 적는다(10–27). `EFDC.PAR`·`EFDC.CMN`을 포함한다(29–30). |
| 32–54 | 시작 시 6행 WQZERO3 루틴 안. 셀 LL=2..LA·층 K=1..KC 루프를 연다(32–33). XLIMI의 네 군, XLIMV·XLIMD의 M군, XLIMN·XLIMP·XLIMT의 네 군 배열을 모두 0으로 둔다(37–54). 구간 안 설명 주석은 일변화 DO 변수의 초기화로 적는다(35). 원문 조건·계산식·반복·호출: `DO LL=2,LA` (32), `DO K=1,KC` (33), `XLIMIC(LL,K) = 0.0` (37), `XLIMID(LL,K) = 0.0` (38), `XLIMIG(LL,K) = 0.0` (39), `XLIMIM(LL,K) = 0.0` (40), `XLIMVM(LL,K) = 0.0` (41), `XLIMDM(LL,K) = 0.0` (42), `XLIMNC(LL,K) = 0.0` (43), `XLIMND(LL,K) = 0.0` (44), `XLIMNG(LL,K) = 0.0` (45), `XLIMNM(LL,K) = 0.0` (46), `XLIMPC(LL,K) = 0.0` (47), `XLIMPD(LL,K) = 0.0` (48), `XLIMPG(LL,K) = 0.0` (49), `XLIMPM(LL,K) = 0.0` (50), `XLIMTC(LL,K) = 0.0` (51), `XLIMTD(LL,K) = 0.0` (52), `XLIMTG(LL,K) = 0.0` (53), `XLIMTM(LL,K) = 0.0` (54). |
| 55–71 | 시작 시 6행 WQZERO3 루틴·32행 LL 루프·33행 K 루프 안. XDOSAT·XDODEF·XDOPSL·XDOSOD·XDOKAR·XDODOC·XDONIT·XDOCOD·XDOPPB·XDORRB·XDOPPM·XDORRM·XDOTRN·XDOALL·XDODZ를 0으로 초기화한다(55–69). K·LL 루프를 닫는다(70–71). 원문 조건·계산식·반복·호출: `XDOSAT(LL,K) = 0.0` (55), `XDODEF(LL,K) = 0.0` (56), `XDOPSL(LL,K) = 0.0` (57), `XDOSOD(LL,K) = 0.0` (58), `XDOKAR(LL,K) = 0.0` (59), `XDODOC(LL,K) = 0.0` (60), `XDONIT(LL,K) = 0.0` (61), `XDOCOD(LL,K) = 0.0` (62), `XDOPPB(LL,K) = 0.0` (63), `XDORRB(LL,K) = 0.0` (64), `XDOPPM(LL,K) = 0.0` (65), `XDORRM(LL,K) = 0.0` (66), `XDOTRN(LL,K) = 0.0` (67), `XDOALL(LL,K) = 0.0` (68), `XDODZ(LL,K)  = 0.0` (69). |
| 72–76 | 시작 시 6행 WQZERO3 루틴 안. TIMESUM3=0·NLIM=0으로 시간 합과 제한/산소 성분 누적 횟수를 초기화한다(72–73). 빈 주석·RETURN·END를 포함한다(74–76). 원문 조건·계산식·반복·호출: `TIMESUM3 = 0.0` (72), `NLIM = 0` (73). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·35·37–54: 머리말은 제한·DO 성분 분석 배열을 설명한다. 35행의 구간 주석은 일변화 DO 변수라고 적지만 바로 아래는 XLIM 계열 초기화이다.
