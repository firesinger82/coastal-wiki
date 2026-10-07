---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calpser.f90
lines: 72
sha256: f7dfc7bb560a80d3e6d941020d8f5135a0cd1e930a4e7c1c03e4f97236299935
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calpser.f90 — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | EFDC+·저장소 주소·저작권·GPLv2 머리말(1–8). `SUBROUTINE CALPSER` 시작(9). 시간에 따라 변하는 수면 높이(surface elevation) 경계조건을 갱신한다는 주석(12–13). GLOBAL 사용·implicit none(15–16). NS·M2·M1, real(RKD) TIME·TDIFF, real 보간 가중치·Y1..Y4 선언(18–21). PSERT(0)을 0으로 초기화한다(23). 빈 줄을 포함한다. |
| 25–40 | 시작 시 9행 CALPSER 안. `do NS = 1,NPSER` (25)에서 `TIME = TIMESEC/DBLE(TSPS(NS).TMULT)` (26). MTSPLAST에서 M2를 가져온다(28). `do while (TIME > TSPS(NS).TIM(M2) )` (29)에서 `M2 = M2+1` (30). `if( M2 > TSPS(NS).NREC )then` (31)이면 M2를 NREC로 설정하고 exit한다(32–33). MTSPLAST 갱신(36) 뒤 `M1 = M2-1` (37), `TDIFF = TSPS(NS).TIM(M2) - TSPS(NS).TIM(M1)` (39). 빈 줄(40). |
| 41–47 | 시작 시 9행 CALPSER·25행 NS 루프 안. `if( INTPSER(NS) == 0 .or. M1 < 2 .or. M2 > TSPS(NS).NREC-1 )then` (41)은 선형 보간(linear interpolation) 경로다(42). `WTM1 = (TSPS(NS).TIM(M2) - TIME)/TDIFF` (43), `WTM2 = (TIME - TSPS(NS).TIM(M1))/TDIFF` (44). `PSERT(NS)  = WTM1*TSPS(NS).VAL(M1,1) + WTM2*TSPS(NS).VAL(M2,1) + PDGINIT  ! *** ADD OFFSET    (m2/s2)` (45), `PSERST(NS) = WTM1*TSPS(NS).VAL(M1,2) + WTM2*TSPS(NS).VAL(M2,2) + PDGINIT  ! *** ADD OFFSET    (m2/s2)` (46). `else` (47)로 스플라인 분기를 시작한다. |
| 48–59 | 시작 시 9행 CALPSER·25행 NS 루프·47행 else 안. Catmull–Rom 스플라인(spline)이라는 주석(48). `WTM1 = (TIME - TSPS(NS).TIM(M1))/TDIFF` (49). Y1..Y4에 첫 값 열의 M1-1·M1·M2·M2+1 값을 가져온다(50–53). `PSERT(NS) = 0.5*( (2.*Y2) + (-Y1 + Y3)*WTM1 + (2.*Y1 - 5.*Y2 + 4.*Y3 - Y4)*WTM1**2 + (-Y1 + 3.*Y2 - 3.*Y3 + Y4)*WTM1**3 )` (54). QC 출력 안내와 출력문 두 개는 주석이다(56–58). 빈 줄(55·59). |
| 60–72 | 시작 시 9행 CALPSER·25행 NS 루프·47행 else 안. Y1..Y4에 두 번째 값 열의 M1-1·M1·M2·M2+1 값을 가져온다(60–63). `PSERST(NS) = 0.5*( (2.*Y2) + (-Y1 + Y3)*WTM1 + (2.*Y1 - 5.*Y2 + 4.*Y3 - Y4)*WTM1**2 + (-Y1 + 3.*Y2 - 3.*Y3 + Y4)*WTM1**3 )` (64). 조건·NS 루프 종료(66–67). return·END·빈 줄(68–72). 이 파일에는 외부 루틴 call 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23: 인덱스 0 초기화문은 PSERT(0)에만 있다. 이 파일에는 PSERST(0) 대입문이 없다.
- 28–37: 시각 탐색은 저장된 M2에서 증가하는 방향으로만 진행한다. 이 파일에는 M2를 감소시키는 탐색문이 없다.
- 37–44·49: M1은 M2-1이다. 이 파일에는 M1의 하한 검사나 TDIFF가 0인지 확인하는 조건문이 없다.
- 45–46·54·64: 선형 보간 결과에는 PDGINIT를 더한다. 스플라인 결과 대입식에는 PDGINIT가 없다.
