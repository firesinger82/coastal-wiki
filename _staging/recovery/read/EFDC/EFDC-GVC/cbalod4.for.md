---
file: models/EFDC/raw/source_code/EFDC-GVC/cbalod4.for
lines: 63
sha256: a4cf8a02cc735e8f3bda61a15c310fbf52bed5e2398a9e1051c367ce8a3646b6
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cbalod4.for — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 CBALOD4 선언을 포함한다(1–6). 머리말은 EFDC-FULL 1.0a와 2001-11-01 수정일을 적는다(8–10). CBALOD 루틴들이 전체 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지(balance)를 계산한다는 주석이 있다(19–20). EFDC.PAR와 EFDC.CMN을 포함한다(24–25). 포함 파일 내부는 이 기록의 판독 대상이 아니다. 운동량과 에너지 소산(dissipation) 계산을 안내한다(29–31). |
| 33–45 | 시작 시 6행 CBALOD4 루틴 안. L=2..LA에서 북쪽 이웃 LN을 구한다(33–34). 기존 DXYU·DXYV 기반 응력(stress) 일의 식은 주석이다(35–38). 실행식은 SPB·DXYP와 계수 0.5로 두 인접 면의 저면 응력 일에서 표면 응력 일을 뺀다(39–43). UUEOUTO와 VVEOUTO를 누적하고 L 루프를 닫는다(44). 원문 실행문: `DO L=2,LA` (33); `LN=LNC(L)` (34); `UUEOUTO=UUEOUTO+0.5*SPB(L)*DXYP(L)*(U(L,1)*TBX(L)` (39); `&       +U(L+1,1)*TBX(L+1)` (40); `&       -U(L,KC)*TSX(L)-U(L+1,KC)*TSX(L+1))` (41); `VVEOUTO=VVEOUTO+0.5*SPB(L)*DXYP(L)*(V(L,1)*TBY(L)+V(LN,1)*TBX(LN)` (42); `&       -V(L,KC)*TSY(L)-V(LN,KC)*TSX(LN))` (43). 주석 처리된 원문(실행되지 않음): `C     UUEOUTO=UUEOUTO+SPB(L)*SPB(L+1)*DXYU(L)` (35); `C    &      *(U(L,1)*TBX(L)-U(L,KC)*TSX(L))` (36); `C     VVEOUTO=VVEOUTO+SPB(L)*SPB(LN)*DXYV(L)` (37); `C    &      *(V(L,1)*TBY(L)-V(L,KC)*TSY(L))` (38). |
| 46–59 | 시작 시 6행 CBALOD4 루틴 안. K=1..KS와 L=2..LA에서 인접한 두 수평 면의 층간 속도 차이로 DUTMP와 DVTMP를 계산한다(46–50). AV와 속도 차이의 제곱 및 두 DZC의 합으로 UUEOUTO와 VVEOUTO를 누적한다(51–54). SCB·DXYP·HP·GP·AB와 B의 층간 차이로 BBEOUTO를 누적한다(55–56). 두 루프를 닫는다(57–58). 원문 실행문: `DO K=1,KS` (46); `DO L=2,LA` (47); `LN=LNC(L)` (48); `DUTMP=0.5*( U(L,K+1)+U(L+1,K+1)-U(L,K)-U(L+1,K) )` (49); `DVTMP=0.5*( V(L,K+1)+V(LN,K+1)-V(L,K)-V(LN,K) )` (50); `UUEOUTO=UUEOUTO+SPB(L)*2.0*DXYP(L)*AV(L,K)` (51); `&      *( DUTMP*DUTMP )/(DZC(K+1)+DZC(K))` (52); `VVEOUTO=VVEOUTO+SPB(L)*2.0*DXYP(L)*AV(L,K)` (53); `&      *( DVTMP*DVTMP )/(DZC(K+1)+DZC(K))` (54); `BBEOUTO=BBEOUTO+SCB(L)*DXYP(L)*HP(L)` (55); `&      *GP*AB(L,K)*(B(L,K+1)-B(L,K))` (56). |
| 60–63 | 시작 시 6행 CBALOD4 루틴 안. 구분 주석과 RETURN·END를 포함한다(60–63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 42–43: VVEOUTO 식의 L 지점은 TBY와 TSY를 사용한다. 같은 식의 북쪽 이웃 LN 지점은 TBX와 TSX를 사용한다.
