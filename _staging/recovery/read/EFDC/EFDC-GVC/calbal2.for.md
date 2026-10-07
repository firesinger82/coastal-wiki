---
file: models/EFDC/raw/source_code/EFDC-GVC/calbal2.for
lines: 143
sha256: ab49d7cf59dc10489c9bc812b7e76ac34a5b8bdb6751cbbb1661f6fb1eafa727
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# calbal2.for — 판독 구간 기록

구간은 1행부터 143행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 `SUBROUTINE CALBAL2` (6) 입구. 버전·수정일·변경 이력 머리말을 포함한다(8–17). 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지 목적 주석이다(19–20). `INCLUDE 'EFDC.PAR'` (24); `INCLUDE 'EFDC.CMN'` (25)로 공통 선언을 포함한다. 개방 경계(open boundary) 유량(flux) 누적 주석이다(29). |
| 33–60 | 시작 시 6행 CALBAL2 루틴 안. K=1..KC·LL=1..NCBS(33–34)에서 남쪽 경계 L=LCBS(LL)·LN=LNC(L)를 얻는다(35–36). 체적은 `VOLOUT=VOLOUT-VHDX2(LN,K)*DZC(K)` (38). 염 질량(salt mass)·염료 질량(dye mass)의 부호별 상류값(upwind value)은 `SALOUT=SALOUT-MIN(VHDX2(LN,K),0.)*SAL1(LN,K)*DZC(K)` (39); `&             -MAX(VHDX2(LN,K),0.)*SAL1(L,K)*DZC(K)` (40); `DYEOUT=DYEOUT-MIN(VHDX2(LN,K),0.)*DYE1(LN,K)*DZC(K)` (41); `&             -MAX(VHDX2(LN,K),0.)*DYE1(L,K)*DZC(K)` (42). 위치에너지(potential energy) 유량은 `PPEOUT=PPEOUT-VHDX2(LN,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(LN))` (43); `&       +0.125*(HP(L)+H2P(L)+HP(LN)+H2P(LN))*(Z(K)+Z(K-1)) )` (44); `BBEOUT=BBEOUT-MIN(VHDX2(LN,K),0.)*DZC(K)*GP*( BELV(LN)` (45); `&                  +0.5*HP(LN)*(Z(K)+Z(K-1)) )*B1(LN,K)` (46); `&             -MAX(VHDX2(LN,K),0.)*DZC(K)*GP*( BELV(L)` (47); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (48). 두 루프를 닫는다(50–51). 53–57행 VHDX2E 체적 대체 누적은 주석이다. |
| 61–86 | 시작 시 6행 CALBAL2 루틴 안. K=1..KC·LL=1..NCBW(61–62)에서 서쪽 경계 L=LCBW(LL)를 얻는다(63). 체적은 `VOLOUT=VOLOUT-UHDY2(L+1,K)*DZC(K)` (65). 염·염료의 부호별 상류값은 `SALOUT=SALOUT-MIN(UHDY2(L+1,K),0.)*SAL1(L+1,K)*DZC(K)` (66); `&             -MAX(UHDY2(L+1,K),0.)*SAL1(L,K)*DZC(K)` (67); `DYEOUT=DYEOUT-MIN(UHDY2(L+1,K),0.)*DYE1(L+1,K)*DZC(K)` (68); `&             -MAX(UHDY2(L+1,K),0.)*DYE1(L,K)*DZC(K)` (69). 위치에너지 유량은 `PPEOUT=PPEOUT-UHDY2(L+1,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(L+1))` (70); `&       +0.125*(HP(L)+H2P(L)+HP(L+1)+H2P(L+1))*(Z(K)+Z(K-1)) )` (71); `BBEOUT=BBEOUT-MIN(UHDY2(L+1,K),0.)*DZC(K)*GP*( BELV(L+1)` (72); `&                  +0.5*HP(L+1)*(Z(K)+Z(K-1)) )*B1(L+1,K)` (73); `&             -MAX(UHDY2(L+1,K),0.)*DZC(K)*GP*( BELV(L)` (74); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (75). 두 루프를 닫는다(77–78). 80–83행 UHDY2E 체적 대체 누적은 주석이다. |
| 87–113 | 시작 시 6행 CALBAL2 루틴 안. K=1..KC·LL=1..NCBE(87–88)에서 동쪽 경계 L=LCBE(LL)를 얻는다(89). 체적은 `VOLOUT=VOLOUT+UHDY2(L,K)*DZC(K)` (91). 염·염료의 부호별 상류값은 `SALOUT=SALOUT+MIN(UHDY2(L,K),0.)*SAL1(L,K)*DZC(K)` (92); `&             +MAX(UHDY2(L,K),0.)*SAL1(L-1,K)*DZC(K)` (93); `DYEOUT=DYEOUT+MIN(UHDY2(L,K),0.)*DYE1(L,K)*DZC(K)` (94); `&             +MAX(UHDY2(L,K),0.)*DYE1(L-1,K)*DZC(K)` (95). 위치에너지 유량은 `PPEOUT=PPEOUT+UHDY2(L,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(L-1))` (96); `&       +0.125*(HP(L)+H2P(L)+HP(L-1)+H2P(L-1))*(Z(K)+Z(K-1)) )` (97); `BBEOUT=BBEOUT+MIN(UHDY2(L,K),0.)*DZC(K)*GP*(BELV(L)` (98); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (99); `&             +MAX(UHDY2(L,K),0.)*DZC(K)*GP*(BELV(L-1)` (100); `&                  +0.5*HP(L-1)*(Z(K)+Z(K-1)) )*B1(L-1,K)` (101). 두 루프를 닫는다(103–104). 107–110행 UHDY2E 체적 대체 누적은 주석이다. |
| 114–143 | 시작 시 6행 CALBAL2 루틴 안. K=1..KC·LL=1..NCBN(114–115)에서 북쪽 경계 L=LCBN(LL)·LS=LSC(L)를 얻는다(116–117). 체적은 `VOLOUT=VOLOUT+VHDX2(L,K)*DZC(K)` (119). 염·염료의 부호별 상류값은 `SALOUT=SALOUT+MIN(VHDX2(L,K),0.)*SAL1(L,K)*DZC(K)` (120); `&             +MAX(VHDX2(L,K),0.)*SAL1(LS,K)*DZC(K)` (121); `DYEOUT=DYEOUT+MIN(VHDX2(L,K),0.)*DYE1(L,K)*DZC(K)` (122); `&             +MAX(VHDX2(L,K),0.)*DYE1(LS,K)*DZC(K)` (123). 위치에너지 유량은 `PPEOUT=PPEOUT+VHDX2(L,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(LS))` (124); `&       +0.125*(HP(L)+H2P(L)+HP(LS)+H2P(LS))*(Z(K)+Z(K-1)) )` (125); `BBEOUT=BBEOUT+MIN(VHDX2(L,K),0.)*DZC(K)*GP*( BELV(L)` (126); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (127); `&             +MAX(VHDX2(L,K),0.)*DZC(K)*GP*( BELV(LS)` (128); `&                  +0.5*HP(LS)*(Z(K)+Z(K-1)) )*B1(LS,K)` (129). 두 루프를 닫는다(131–132). 134–138행 VHDX2E 체적 대체 누적은 주석이다. RETURN·END로 종료한다(142–143). 실행 IF·CALL 문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 38–48·65–75·91–101·119–129: 누적식에는 DZC(K)를 곱하지만 시간 간격을 곱하는 항은 없다. 이 파일에는 누적량을 0으로 초기화하는 문장도 없다.
- 19–20·38–129: 머리말은 운동량·에너지 수지를 함께 적는다. 실행 누적 대상은 VOLOUT·SALOUT·DYEOUT·PPEOUT·BBEOUT이다. 이 파일에는 UMOOUT·VMOOUT·UUEOUT·VVEOUT 대입이 없다.
- 43–44·70–71·96–97·124–125: PPEOUT의 각 경계식은 0.125와 HP·H2P의 합을 사용한다. BBEOUT의 부호별 높이 항은 HP와 0.5를 사용한다(45–48·72–75·98–101·126–129).
