---
file: models/EFDC/raw/source_code/EFDC-GVC/bal2t1.for
lines: 213
sha256: 275539780c11dd0176ff46791c217b66ef7a417714521f987ebe5ed0a23a99c4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# bal2t1.for — 판독 구간 기록

구간은 1행부터 213행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 구분 주석과 `SUBROUTINE BAL2T1` 입구(1–7). EFDC-FULL 1.0a·수정일 주석(9–11). 변경 기록은 두 시각 단계(two time-level)의 퇴적물·모래·독성물질 수지(balance) 추가를 적는다(18–19). 전역 부피·질량·운동량·에너지 수지 안내(22–23). `INCLUDE 'EFDC.PAR'` (27), `INCLUDE 'EFDC.CMN'` (28). `IF(NBAL.GT.1) RETURN` (32). 초기값·플럭스(flux) 안내와 구분 주석(34–40). 포함 파일 내부는 이번 판독 대상이 아니다. |
| 41–72 | 시작 시 7행 BAL2T1 안. BAL2T.INT open은 주석 처리(41). 시작 부피·수층 부피·바닥 부피, 염분·염료 질량, 운동량·운동에너지(kinetic energy)·위치에너지(potential energy) 누적값=0(43–56). NS=1..NSED, NS=1..NSND, NT=1..NTOX의 별도 루프에서 SEDBEG2T·SNDBEG2T·TOXBEG2T와 각 W·B 누적값을 0으로 초기화한다(57–71). 끝 주석(72). |
| 73–105 | 시작 시 7행 BAL2T1 안. 유출 부피·수층·바닥 부피, 염분·염료·운동량·에너지 유출과 지형 변화(morphology) 부피=0(73–86). NS=1..NSED에서 SEDOUT2T·SEDFLUX2T=0(87–90). NS=1..NSND에서 SNDOUT2T·SNDFLUX2T·SBLOUT2T·SNDFBL2T=0(91–96). NT=1..NTOX에서 TOXOUT2T·TOXFLUXW2T·TOXFLUXB2T·TADFLUX2T·TOXBLB2T·TOXFBL2T=0(97–104). 끝 주석(105). |
| 106–120 | 시작 시 7행 BAL2T1 안. L=2..LA에서 LN=LNC(L)(106–107). `VOLBEG=VOLBEG+SPB(L)*DXYP(L)*HP(L)` (108), `VOLBEG2T=VOLBEG2T+SPB(L)*DXYP(L)*HP(L)` (109), `WVOLBEG2T=WVOLBEG2T+SPB(L)*DXYP(L)*HP(L)` (110). 운동량은 `UMOBEG=UMOBEG+SPB(L)*0.5*DXYP(L)*HP(L)*(DYIU(L)*HUI(L)*UHDYE(L)` (111), `&                                 +DYIU(L+1)*HUI(L+1)*UHDYE(L+1))` (112), `VMOBEG=VMOBEG+SPB(L)*0.5*DXYP(L)*HP(L)*(DXIV(L)*HVI(L)*VHDXE(L)` (113), `&                                 +DXIV(LN)*HVI(LN)*VHDXE(LN))` (114). `PPEBEG=PPEBEG+SPB(L)*0.5*DXYP(L)` (115), `&             *(GI*P(L)*P(L)-G*BELV(L)*BELV(L))` (116). 루프 종료(117). `AMOBEG=SQRT(UMOBEG*UMOBEG+VMOBEG*VMOBEG)` (119). 주석도 포함한다(118·120). |
| 121–140 | 시작 시 7행 BAL2T1 안. K=1..KC, L=2..LA에서 LN=LNC(L)(121–123). `DYEBEG=DYEBEG+SCB(L)*DXYP(L)*HP(L)*DYE(L,K)*DZC(K)` (124), `DYEBEG2T=DYEBEG2T+SCB(L)*DXYP(L)*HP(L)*DYE(L,K)*DZC(K)` (125), `SALBEG=SALBEG+SCB(L)*DXYP(L)*HP(L)*SAL(L,K)*DZC(K)` (126). 대체 운동에너지 식은 주석(127–130). 실행식은 `UUEBEG=UUEBEG+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (131), `&      *( (U(L,K)+U(L+1,K))*(U(L,K)+U(L+1,K)) )` (132), `VVEBEG=VVEBEG+SPB(L)*0.125*DXYP(L)*HP(L)*DZC(K)` (133), `&      *( (V(L,K)+V(LN,K))*(V(L,K)+V(LN,K)) )` (134). 부력(buoyancy) 에너지 식은 `BBEBEG=BBEBEG+SPB(L)*GP*DXYP(L)*HP(L)*DZC(K)*( BELV(L)` (135), `&      +0.5*HP(L)*(Z(K)+Z(K-1)) )*B(L,K)` (136). 루프 종료·주석(137–140). |
| 141–170 | 시작 시 7행 BAL2T1 안. 퇴적물 NS=1..NSED, 모래 NS=1..NSND, 독성물질 NT=1..NTOX의 각 루프에서 K=1..KC, L=2..LA 수층 질량을 전체·수층 누적값에 더한다. 원문은 `SEDBEG2T(NS)=SEDBEG2T(NS)` (144), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*SED(L,K,NS)` (145), `SEDBEG2TW(NS)=SEDBEG2TW(NS)` (146), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*SED(L,K,NS)` (147), `SNDBEG2T(NS)=SNDBEG2T(NS)` (154), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*SND(L,K,NS)` (155), `SNDBEG2TW(NS)=SNDBEG2TW(NS)` (156), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*SND(L,K,NS)` (157), `TOXBEG2T(NT)=TOXBEG2T(NT)` (164), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*TOX(L,K,NT)` (165), `TOXBEG2TW(NT)=TOXBEG2TW(NT)` (166), `&                +SCB(L)*DXYP(L)*HP(L)*DZC(K)*TOX(L,K,NT)` (167). 각 세 중첩 루프 종료(148–150·158–160·168–170). |
| 171–196 | 시작 시 7행 BAL2T1 안. 주석(171). NS=1..NSED, NS=1..NSND, NT=1..NTOX의 각 루프에서 L=2..LA, K=1..KBT(L)의 바닥 질량을 더한다(172–195). `SEDBEG2T(NS)=SEDBEG2T(NS)+SCB(L)*DXYP(L)*SEDB(L,K,NS)` (175), `SEDBEG2TB(NS)=SEDBEG2TB(NS)+SCB(L)*DXYP(L)*SEDB(L,K,NS)` (176), `SNDBEG2T(NS)=SNDBEG2T(NS)+SCB(L)*DXYP(L)*SNDB(L,K,NS)` (183), `SNDBEG2TB(NS)=SNDBEG2TB(NS)+SCB(L)*DXYP(L)*SNDB(L,K,NS)` (184), `TOXBEG2T(NT)=TOXBEG2T(NT)+SCB(L)*DXYP(L)*TOXB(L,K,NT)` (191), `TOXBEG2TB(NT)=TOXBEG2TB(NT)+SCB(L)*DXYP(L)*TOXB(L,K,NT)` (192). 끝 주석(196). |
| 197–213 | 시작 시 7행 BAL2T1 안. KK=0(197), 출력을 주석 처리(198). L=2..LA, K=1..KBT(L)에서 `VOLBEG2T=VOLBEG2T+SPB(L)*DXYP(L)*HBED(L,K)` (201), `BVOLBEG2T=BVOLBEG2T+SPB(L)*DXYP(L)*HBED(L,K)` (202). 공극률(porosity) PORBED를 곱하여 WVOLBEG2T를 더하는 문장과 출력은 주석(203–204). 두 루프 종료(205–206), `CLOSE(1)` (208), 구분 주석(207·209–211), `RETURN` (212), `END` (213). 외부 루틴 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41·208: 이 파일의 OPEN(1)은 주석 처리되어 있다. CLOSE(1)은 실행문이다.
- 108–110·201–204: VOLBEG2T에는 수층 부피와 전체 바닥 부피를 더한다. WVOLBEG2T에는 수층 부피를 더한다. PORBED를 곱한 바닥 공극수 부피의 WVOLBEG2T 대입은 주석 처리되어 있다.
- 197–204: KK=0을 대입한다. KK를 참조하는 두 WRITE 문장은 주석 처리되어 있다.
