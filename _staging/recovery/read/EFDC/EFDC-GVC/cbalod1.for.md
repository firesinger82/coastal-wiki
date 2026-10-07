---
file: models/EFDC/raw/source_code/EFDC-GVC/cbalod1.for
lines: 92
sha256: 792d9db31e84d99571e095c49f645d7d62e7ab6bf6024590066fdb0e493a7ed3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cbalod1.for — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 구분 주석과 CBALOD1 선언을 포함한다(1–6). 머리말은 EFDC-FULL 1.0a와 2001-11-01 수정일을 적는다(8–10). CBALOD 루틴들이 전체 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지(balance)를 계산한다는 주석이 있다(19–20). EFDC.PAR와 EFDC.CMN을 포함한다(24–25). 포함 파일 내부는 이 기록의 판독 대상이 아니다. |
| 28–57 | 시작 시 6행 CBALOD1 루틴 안. NBALO>1이면 즉시 반환한다(29). 체적·염분(salt) 질량·염료(dye) 질량·운동량·운동 에너지(kinetic energy)·위치 에너지(potential energy)와 유량(flux) 초기화 안내 주석을 포함한다(33–36). BEGO 저장량과 OUTO 누적값을 모두 0으로 설정한다(38–56). 원문 실행문: `IF(NBALO.GT.1) RETURN` (29); `VOLBEGO=0.` (38); `SALBEGO=0.` (39); `DYEBEGO=0.` (40); `UMOBEGO=0.` (41); `VMOBEGO=0.` (42); `UUEBEGO=0.` (43); `VVEBEGO=0.` (44); `PPEBEGO=0.` (45); `BBEBEGO=0.` (46); `VOLOUTO=0.` (48); `SALOUTO=0.` (49); `DYEOUTO=0.` (50); `UMOOUTO=0.` (51); `VMOOUTO=0.` (52); `UUEOUTO=0.` (53); `VVEOUTO=0.` (54); `PPEOUTO=0.` (55); `BBEOUTO=0.` (56). |
| 58–70 | 시작 시 6행 CBALOD1 루틴 안. L=2..LA에서 북쪽 이웃 LN을 구한다(58–59). SPB·DXYP·H1P로 VOLBEGO를 누적한다(60). 수송량 UHDY1E·VHDX1E와 수심 H1U·H1V로 UMOBEGO와 VMOBEGO를 누적한다(61–64). P1과 BELV의 제곱으로 PPEBEGO를 누적한다(65–67). AMOBEGO는 두 운동량 성분 제곱 합의 제곱근이다(69). 원문 실행문: `DO L=2,LA` (58); `LN=LNC(L)` (59); `VOLBEGO=VOLBEGO+SPB(L)*DXYP(L)*H1P(L)` (60); `UMOBEGO=UMOBEGO+SPB(L)*0.5*DXYP(L)*H1P(L)` (61); `&       *(DYIU(L)*UHDY1E(L)/H1U(L)+DYIU(L+1)*UHDY1E(L+1)/H1U(L+1))` (62); `VMOBEGO=VMOBEGO+SPB(L)*0.5*DXYP(L)*H1P(L)` (63); `&       *(DXIV(L)*VHDX1E(L)/H1V(L)+DXIV(LN)*VHDX1E(LN)/H1V(LN))` (64); `PPEBEGO=PPEBEGO+SPB(L)*0.5*DXYP(L)` (65); `&             *(GI*P1(L)*P1(L)-G*BELV(L)*BELV(L))` (66); `AMOBEGO=SQRT(UMOBEGO*UMOBEGO+VMOBEGO*VMOBEGO)` (69). |
| 71–88 | 시작 시 6행 CBALOD1 루틴 안. K=1..KC와 L=2..LA에서 SAL1·DYE1의 질량을 SCB·DXYP·H1P·DZC로 가중 합산한다(71–75). 격자 면적 DXYU·DXYV를 사용하는 기존 운동 에너지 식은 주석이다(76–79). 실행되는 UUEBEGO와 VVEBEGO 식은 인접한 두 속도의 합을 제곱하며 계수는 0.125다(80–83). BBEBEGO 식은 BELV 및 평균 층 높이와 B1을 사용한다(84–85). 두 루프를 닫는다(86–87). 원문 실행문: `DO K=1,KC` (71); `DO L=2,LA` (72); `LN=LNC(L)` (73); `SALBEGO=SALBEGO+SCB(L)*DXYP(L)*H1P(L)*SAL1(L,K)*DZC(K)` (74); `DYEBEGO=DYEBEGO+SCB(L)*DXYP(L)*H1P(L)*DYE1(L,K)*DZC(K)` (75); `UUEBEGO=UUEBEGO+SPB(L)*0.125*DXYP(L)*H1P(L)*DZC(K)` (80); `&      *( (U1(L,K)+U1(L+1,K))*(U1(L,K)+U1(L+1,K)) )` (81); `VVEBEGO=VVEBEGO+SPB(L)*0.125*DXYP(L)*H1P(L)*DZC(K)` (82); `&      *( (V1(L,K)+V1(LN,K))*(V1(L,K)+V1(LN,K)) )` (83); `BBEBEGO=BBEBEGO+SPB(L)*GP*DXYP(L)*H1P(L)*DZC(K)*( BELV(L)` (84); `&      +0.5*H1P(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (85). 주석 처리된 원문(실행되지 않음): `C     UUEBEGO=UUEBEGO+SPB(L)*0.25*(DXYU(L)*H1U(L)*U1(L,K)*U1(L,K)` (76); `C    &      +DXYU(L+1)*H1U(L+1)*U1(L+1,K)*U1(L+1,K))*DZC(K)` (77); `C     VVEBEGO=VVEBEGO+SPB(L)*0.25*(DXYV(L)*H1V(L)*V1(L,K)*V1(L,K)` (78); `C    &      +DXYV(LN)*H1V(LN)*V1(LN,K)*V1(LN,K))*DZC(K)` (79). |
| 89–92 | 시작 시 6행 CBALOD1 루틴 안. 구분 주석과 RETURN·END를 포함한다(89–92). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 74–75: SAL1과 DYE1의 질량 계산은 ISTRAN 조건 없이 실행된다. 이 파일에는 염분 또는 염료 수송 활성 여부를 검사하는 조건이 없다.
