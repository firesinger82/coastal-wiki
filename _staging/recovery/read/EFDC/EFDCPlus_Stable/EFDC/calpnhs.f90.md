---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calpnhs.f90
lines: 197
sha256: 8f98346686f147f5c59b7460c0379683f8cfd5b665579e8002789c4f550abf77
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calpnhs.f90 — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | EFDC+·저장소 주소·저작권·GPLv2 머리말(1–8). `SUBROUTINE CALPNHS` 시작(9). 준 비정수압(quasi-nonhydrostatic pressure)을 계산한다는 주석(12). PNHYDS 단위는 M2/S2라는 주석(14). GLOBAL 사용·implicit none(16–18). 정수·실수 작업 변수와 save allocatable PNHYDSS·FWJET·WZ·WZ1 선언(20–27). 빈 줄을 포함한다. |
| 29–49 | 시작 시 9행 CALPNHS 안. `if( .not. allocated(PNHYDSS) )then` (29)에서 PNHYDSS·FWJET를 (LCM,KCM), WZ·WZ1을 (LCM,0:KCM)로 할당하고 모두 0으로 초기화한다(30–37). `if( ISDYNSTP == 0 )then` (40)은 DELT=DT(41), `DELTD2 = 0.5*DT` (42), `DELTI = 1./DELT` (43). `else` (44)는 DELT=DTDYN(45), `DELTD2 = 0.5*DTDYN` (46), `DELTI = 1./DELT` (47). 조건 종료·빈 줄(48–49). |
| 50–78 | 시작 시 9행 CALPNHS 안. 물리적 수직 속도(physical vertical velocity) 계산 주석(50). L=2..LA 루프(51–59)에서 동서남북 이웃을 가져온다(52–55). `WZ(L,0) = DELTI*(BELV(L)-BELV1(L))` (56). 수면 경계식은 `WZ(L,KC) = GI*( DELTI*(P(L)-P1(L)) + 0.5*U(LE,KC)*(P(LE)-P(L))*DXIU(LE) + 0.5*U(L,KC)*(P(L)-P(LW))*DXIU(L) &` (57); `+ 0.5*V(LN,KC)*(P(LN)-P(L))*DYIV(LN) + 0.5*V(L,KC)*(P(L)-P(LS))*DYIV(L) )` (58). `if( KC > 2 )then` (61) 안에서 K=1..KS·LP=1..LLWET(K,0) 루프(62–76)는 LKWET으로 셀을 선택한다(64). 내부 경계식은 `WZ(L,K) = W(L,K)+GI*ZZ(L,K)*( DELTI*(P(L)-P1(L)) &` (69); `+ 0.5*U(LE,K)*(P(LE)-P(L))*DXIU(LE) + 0.5*U(L,K)*(P(L)-P(LW))*DXIU(L) &` (70); `+ 0.5*V(LN,K)*(P(LN)-P(L))*DYIV(LN) + 0.5*V(L,K)*(P(L)-P(LS))*DYIV(L) ) &` (71); `+ (1.-ZZ(L,K))*( DELTI*(BELV(L)-BELV1(L)) &` (72); `+ 0.5*U(LE,K)*(BELV(LE)-BELV(L))*DXIU(LE) + 0.5*U(L,K)*(BELV(L)-BELV(LW))*DXIU(L) &` (73); `+ 0.5*V(LN,K)*(BELV(LN)-BELV(L))*DYIV(LN) + 0.5*V(L,K)*(BELV(L)-BELV(LS))*DYIV(L) )` (74). 조건 종료·빈 줄(77–78). |
| 79–105 | 시작 시 9행 CALPNHS 안. 유량 플럭스(flux) 계산 주석(79). K=1..KC·L=1..LC에서 PNHYDS를 PNHYDSS에 보관하고 FUHU·FVHU·FWQQ를 0으로 초기화한다(80–87). K=1..KS·L=2..LA에서 `UHUW = 0.5*(UHDY(L,K)+UHDY(L,K+1))` (92), `VHVW = 0.5*(VHDX(L,K)+VHDX(L,K+1))` (93), `FUHU(L,K) = max(UHUW,0.)*WZ(LW,K) + min(UHUW,0.)*WZ(L,K)` (94), `FVHU(L,K) = max(VHVW,0.)*WZ(LS,K)  + min(VHVW,0.)*WZ(L,K)` (95). K=1..KC·L=2..LA에서 `WB = 0.5*DXYP(L)*(W(L,K-1)+W(L,K))` (100), `FWQQ(L,K) = max(WB,0.)*WZ(L,K-1) + min(WB,0.)*WZ(L,K)` (101). FWJET는 0으로 초기화한다(102). 루프 종료·빈 줄(103–105). |
| 106–135 | 시작 시 9행 CALPNHS 안. 취수·방류(withdrawal/return) 운동량 플럭스 추가 주석(106). `do NWR = 1,NQWR` (107). `if( WITH_RET(NWR).NQWRMFU > 0 )then` (108) 안에서 시계열 번호 NS를 가져온다(110). `if( QWRSERT(NS) >= 0. )then` (111)은 취수측 IU·JU·KU를 선택한다(113–115). `else` (116)는 방류측 IU·JU·KU를 선택한다(118–120). `QWRABS = ABS(QWRSERT(NS))` (122), `LU = LIJ(IU,JU)` (123), `QMF = WITH_RET(NWR).QWR+QWRABS` (125), `QUMF = QMF*QMF/(H1P(LU)*DZC(LU,KU)*WITH_RET(NWR).BQWRMFU)` (126). 원문 단일행 조건·대입은 `if( WITH_RET(NWR).NQWRMFU == 1 )  FWJET(LU     ,KU) = -QUMF` (127), `if( WITH_RET(NWR).NQWRMFU == 2 )  FWJET(LU     ,KU) = -QUMF` (128), `if( WITH_RET(NWR).NQWRMFU == 3 )  FWJET(LU+1   ,KU) = -QUMF` (129), `if( WITH_RET(NWR).NQWRMFU == 4 )  FWJET(LNC(LU),KU) = -QUMF` (130), `if( WITH_RET(NWR).NQWRMFU == -1 ) FWJET(LU     ,KU) = -QUMF` (131), `if( WITH_RET(NWR).NQWRMFU == -2 ) FWJET(LU     ,KU) = -QUMF` (132), `if( WITH_RET(NWR).NQWRMFU == -3 ) FWJET(LU+1   ,KU) = -QUMF` (133), `if( WITH_RET(NWR).NQWRMFU == -4 ) FWJET(LNC(LU),KU) = -QUMF` (134).108행 조건 종료(135). |
| 136–161 | 시작 시 9행 CALPNHS·107행 NWR 루프 안. `if( WITH_RET(NWR).NQWRMFD > 0 )then` (136)은 방류측 ID·JD·KD를 가져와 `LD = LIJ(ID,JD)` (140)를 계산한다. `ADIFF = ABS(WITH_RET(NWR).ANGWRMFD-90.)` (141). `if( ADIFF < 1.0 )then` (142)이면 `TMPANG = 1.` (143). `else` (144)는 `TMPANG = 0.017453*WITH_RET(NWR).ANGWRMFD` (145), `TMPANG = SIN(TMPANG)` (146). 시계열 번호 선택(148) 뒤 `QMF = WITH_RET(NWR).QWR+QWRSERT(NS)` (149), `QUMF = TMPANG*QMF*QMF/(H1P(LD)*DZC(LD,KD)*WITH_RET(NWR).BQWRMFD)` (150). `if( WITH_RET(NWR).NQWRMFD == 1 )  FWJET(LD     ,KD) = QUMF` (151), `if( WITH_RET(NWR).NQWRMFD == 2 )  FWJET(LD     ,KD) = QUMF` (152), `if( WITH_RET(NWR).NQWRMFD == 3 )  FWJET(LD+1   ,KD) = QUMF` (153), `if( WITH_RET(NWR).NQWRMFD == 4 )  FWJET(LNC(LD),KD) = QUMF` (154), `if( WITH_RET(NWR).NQWRMFD == -1) FWJET(LD     ,KD) = QUMF` (155), `if( WITH_RET(NWR).NQWRMFD == -2) FWJET(LD     ,KD) = QUMF` (156), `if( WITH_RET(NWR).NQWRMFD == -3) FWJET(LD+1   ,KD) = QUMF` (157), `if( WITH_RET(NWR).NQWRMFD == -4) FWJET(LNC(LD),KD) = QUMF` (158). 조건·NWR 루프 종료·빈 줄(159–161). |
| 162–181 | 시작 시 9행 CALPNHS 안. 준 비정수압 계산 주석(162). L=2..LA 루프(163–169)에서 `TMPVAL = 0.5*DZC(L,KC)/DXYP(L)` (166), `PNHYDS(L,KC)= 0.75*TMPVAL*( DELTI*DXYP(L)*(HP(L)*WZ(L,KC)-H1P(L)*WZ1(L,KC)) + FUHU(LE,KC)-FUHU(L,KC)+FVHU(LN,KC)-FVHU(L,KC) )            &` (167); `+ 0.25*TMPVAL*( DELTI*DXYP(L)*(HP(L)*WZ(L,KS)-H1P(L)*WZ1(L,KS)) + FUHU(LE,KS)-FUHU(L,KS)+FVHU(LN,KS)-FVHU(L,KS) ) -FWQQ(L,KC)` (168). K=KS..1을 역순으로 순회하고 LP=1..LLWET(K,0)에서 셀을 선택한다(171–175). `TMPVAL = 0.5*(DZC(L,K+1)+DZC(L,K))/DXYP(L)` (176), `PNHYDS(L,K) = PNHYDS(L,K+1) + FWQQ(L,K+1)-FWQQ(L,K) - FWJET(L,K)   &` (177); `+ TMPVAL*( DELTI*DXYP(L)*(HP(L)*WZ(L,K)-H1P(L)*WZ1(L,K)) + FUHU(LE,K)-FUHU(L,K)+FVHU(LN,K)-FVHU(L,K) )` (178). 루프 종료·빈 줄(179–181). |
| 182–197 | 시작 시 9행 CALPNHS 안. K=0..KC·L=2..LA에서 WZ를 WZ1에 보관한다(182–186). K=1..KC·L=1..LC에서 `PNHYDS(L,K) = 0.5*( PNHYDSS(L,K)+PNHYDS(L,K) )` (190)로 이전 값과 현재 값을 평균한다. 루프 종료·return·END·빈 줄(191–197). 이 파일에는 외부 루틴 call 문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·42·46: DELTD2는 선언되고 두 시간 간격 분기에서 대입된다. 이 파일에는 DELTD2를 읽는 후속 식이 없다.
- 29–38·61–77·182–186: WZ 전체 0 초기화는 최초 할당 조건 안에 있다. 내부 K=1..KS 값의 계산 조건은 KC>2이다. WZ1 복사는 K=0..KC에서 실행된다.
- 108·127–134·136·151–158: NQWRMFU와 NQWRMFD의 음수 비교문은 각각 같은 값이 0보다 큰 바깥 분기 안에 있다.
- 127–134·151–158: FWJET의 구조물 기여는 기존 값에 더하지 않고 대입한다. 같은 배열 위치에 여러 대입이 실행되면 뒤 대입이 앞 값을 바꾼다.
- 141–146: 각도 처리에는 90.·1.0·0.017453이 직접 쓰인다. 90도와 차이가 1.0보다 작으면 TMPANG를 1.로 설정한다.
- 163–180·188–192: 새 압력 계산은 L=2..LA와 LKWET 셀에서 수행한다. 마지막 평균은 L=1..LC에서 수행한다.
