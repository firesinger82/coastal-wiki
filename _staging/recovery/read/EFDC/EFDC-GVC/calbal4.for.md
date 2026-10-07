---
file: models/EFDC/raw/source_code/EFDC-GVC/calbal4.for
lines: 62
sha256: 859f347d70da9c6cd8ee45d4bcd98061118c7cfa379a07ca0d4901159fc1de17
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbal4.for — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 `SUBROUTINE CALBAL4` (6) 입구. 버전·수정일·변경 이력 머리말과 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지 목적 주석이다(8–20). `INCLUDE 'EFDC.PAR'` (24); `INCLUDE 'EFDC.CMN'` (25)로 공통 선언을 포함한다. 운동량·에너지 소산(dissipation) 계산 주석이다(29). |
| 33–44 | 시작 시 6행 CALBAL4 루틴 안. L=2..LA(33), LN=LNC(L)(34)로 북쪽 이웃을 얻는다. 35–38행 면별 응력(stress)·속도 에너지 대체식은 주석이다. 실행 바닥·표면 응력 기여 누적은 `UUEOUT=UUEOUT+0.5*SPB(L)*DXYP(L)*(U(L,1)*TBX(L)+U(L+1,1)*TBX(L+1)` (39); `&       -U(L,KC)*TSX(L)-U(L+1,KC)*TSX(L+1))` (40); `VVEOUT=VVEOUT+0.5*SPB(L)*DXYP(L)*(V(L,1)*TBY(L)+V(LN,1)*TBX(LN)` (41); `&       -V(L,KC)*TSY(L)-V(LN,KC)*TSX(LN))` (42). 루프를 닫는다(43). |
| 45–62 | 시작 시 6행 CALBAL4 루틴 안. K=1..KS·L=2..LA(45–46), LN=LNC(L)(47)로 북쪽 이웃을 얻는다. 평균 수직 속도차는 `DUTMP=0.5*( U(L,K+1)+U(L+1,K+1)-U(L,K)-U(L+1,K) )` (48); `DVTMP=0.5*( V(L,K+1)+V(LN,K+1)-V(L,K)-V(LN,K) )` (49). 점성(viscosity)에 의한 운동에너지(kinetic energy) 소산 누적은 `UUEOUT=UUEOUT+SPB(L)*2.0*DXYP(L)*AV(L,K)` (50); `&      *( DUTMP*DUTMP )/(DZC(K+1)+DZC(K))` (51); `VVEOUT=VVEOUT+SPB(L)*2.0*DXYP(L)*AV(L,K)` (52); `&      *( DVTMP*DVTMP )/(DZC(K+1)+DZC(K))` (53). 밀도 관련 위치에너지(potential energy) 누적은 `BBEOUT=BBEOUT+SCB(L)*DXYP(L)*HP(L)` (54); `&      *GP*AB(L,K)*(B(L,K+1)-B(L,K))` (55). 두 루프를 닫고 RETURN·END로 종료한다(56–62). 실행 IF·CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–42: VVEOUT 바닥 항은 V(L,1)*TBY(L)와 V(LN,1)*TBX(LN)을 함께 사용한다. 표면 항은 V(L,KC)*TSY(L)와 V(LN,KC)*TSX(LN)을 함께 사용한다.
- 39–55: 이 파일은 UUEOUT·VVEOUT·BBEOUT를 누적한다. 머리말이 적은 운동량에 대응하는 UMOOUT·VMOOUT 대입은 이 파일에 없다(29).
