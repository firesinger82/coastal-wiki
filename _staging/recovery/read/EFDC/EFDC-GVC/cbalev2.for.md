---
file: models/EFDC/raw/source_code/EFDC-GVC/cbalev2.for
lines: 120
sha256: 2b9a3c569b2b47a3f67cec070bab42b528d79a872380c1f0780e8b09f2307201
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# cbalev2.for — 판독 구간 기록

구간은 1행부터 120행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | 구분 주석과 CBALEV2 선언을 포함한다(1–6). 머리말은 EFDC-FULL 1.0a와 2001-11-01 수정일을 적는다(8–10). CBALEV 루틴들이 전체 체적(volume)·질량(mass)·운동량(momentum)·에너지(energy) 수지(balance)를 계산한다는 주석이 있다(19–20). EFDC.PAR와 EFDC.CMN을 포함한다(24–25). 포함 파일 내부는 이 기록의 판독 대상이 아니다. 개방 경계(open boundary)를 지나는 유량 누적을 안내한다(29–31). |
| 33–54 | 시작 시 6행 CBALEV2 루틴 안. K=1..KC와 남쪽 경계 LL=1..NCBS를 순회한다(33–36). VOLOUTE에는 북쪽 면의 VHDX2*DZC를 차감한다(38). SALOUTE와 DYEOUTE는 VHDX2의 MIN/MAX 부호별로 LN 또는 L의 이전 농도를 사용한다(39–42). PPEOUTE는 두 셀의 BELV와 HP·H2P 및 평균 층 높이를 사용한다(43–44). BBEOUTE는 부호별로 각 셀의 HP와 B1을 사용한다(45–48). 두 루프와 구분 주석을 포함한다(50–54). 원문 실행문: `DO K=1,KC` (33); `DO LL=1,NCBS` (34); `L=LCBS(LL)` (35); `LN=LNC(L)` (36); `VOLOUTE=VOLOUTE-VHDX2(LN,K)*DZC(K)` (38); `SALOUTE=SALOUTE-MIN(VHDX2(LN,K),0.)*SAL1(LN,K)*DZC(K)` (39); `&             -MAX(VHDX2(LN,K),0.)*SAL1(L,K)*DZC(K)` (40); `DYEOUTE=DYEOUTE-MIN(VHDX2(LN,K),0.)*DYE1(LN,K)*DZC(K)` (41); `&             -MAX(VHDX2(LN,K),0.)*DYE1(L,K)*DZC(K)` (42); `PPEOUTE=PPEOUTE-VHDX2(LN,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(LN))` (43); `&       +0.125*(HP(L)+H2P(L)+HP(LN)+H2P(LN))*(Z(K)+Z(K-1)) )` (44); `BBEOUTE=BBEOUTE-MIN(VHDX2(LN,K),0.)*DZC(K)*GP*( BELV(LN)` (45); `&                  +0.5*HP(LN)*(Z(K)+Z(K-1)) )*B1(LN,K)` (46); `&             -MAX(VHDX2(LN,K),0.)*DZC(K)*GP*( BELV(L)` (47); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (48). |
| 55–75 | 시작 시 6행 CBALEV2 루틴 안. K=1..KC와 서쪽 경계 LL=1..NCBW를 순회한다(55–57). 동쪽 면 UHDY2(L+1,K)의 수송량을 VOLOUTE에서 뺀다(59). MIN/MAX 부호별로 L+1 또는 L의 SAL1·DYE1을 사용한다(60–63). PPEOUTE와 BBEOUTE에는 L과 L+1의 위치 및 농도 자료를 사용한다(64–69). 두 루프와 구분 주석을 포함한다(71–75). 원문 실행문: `DO K=1,KC` (55); `DO LL=1,NCBW` (56); `L=LCBW(LL)` (57); `VOLOUTE=VOLOUTE-UHDY2(L+1,K)*DZC(K)` (59); `SALOUTE=SALOUTE-MIN(UHDY2(L+1,K),0.)*SAL1(L+1,K)*DZC(K)` (60); `&             -MAX(UHDY2(L+1,K),0.)*SAL1(L,K)*DZC(K)` (61); `DYEOUTE=DYEOUTE-MIN(UHDY2(L+1,K),0.)*DYE1(L+1,K)*DZC(K)` (62); `&             -MAX(UHDY2(L+1,K),0.)*DYE1(L,K)*DZC(K)` (63); `PPEOUTE=PPEOUTE-UHDY2(L+1,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(L+1))` (64); `&       +0.125*(HP(L)+H2P(L)+HP(L+1)+H2P(L+1))*(Z(K)+Z(K-1)) )` (65); `BBEOUTE=BBEOUTE-MIN(UHDY2(L+1,K),0.)*DZC(K)*GP*( BELV(L+1)` (66); `&                  +0.5*HP(L+1)*(Z(K)+Z(K-1)) )*B1(L+1,K)` (67); `&             -MAX(UHDY2(L+1,K),0.)*DZC(K)*GP*( BELV(L)` (68); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (69). |
| 76–96 | 시작 시 6행 CBALEV2 루틴 안. K=1..KC와 동쪽 경계 LL=1..NCBE를 순회한다(76–78). UHDY2(L,K)의 수송량을 VOLOUTE에 더한다(80). MIN/MAX 부호별로 L 또는 L-1의 SAL1·DYE1을 사용한다(81–84). PPEOUTE와 BBEOUTE에는 L과 L-1의 자료를 사용한다(85–90). 두 루프와 구분 주석을 포함한다(92–96). 원문 실행문: `DO K=1,KC` (76); `DO LL=1,NCBE` (77); `L=LCBE(LL)` (78); `VOLOUTE=VOLOUTE+UHDY2(L,K)*DZC(K)` (80); `SALOUTE=SALOUTE+MIN(UHDY2(L,K),0.)*SAL1(L,K)*DZC(K)` (81); `&             +MAX(UHDY2(L,K),0.)*SAL1(L-1,K)*DZC(K)` (82); `DYEOUTE=DYEOUTE+MIN(UHDY2(L,K),0.)*DYE1(L,K)*DZC(K)` (83); `&             +MAX(UHDY2(L,K),0.)*DYE1(L-1,K)*DZC(K)` (84); `PPEOUTE=PPEOUTE+UHDY2(L,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(L-1))` (85); `&       +0.125*(HP(L)+H2P(L)+HP(L-1)+H2P(L-1))*(Z(K)+Z(K-1)) )` (86); `BBEOUTE=BBEOUTE+MIN(UHDY2(L,K),0.)*DZC(K)*GP*(BELV(L)` (87); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (88); `&             +MAX(UHDY2(L,K),0.)*DZC(K)*GP*(BELV(L-1)` (89); `&                  +0.5*HP(L-1)*(Z(K)+Z(K-1)) )*B1(L-1,K)` (90). |
| 97–116 | 시작 시 6행 CBALEV2 루틴 안. K=1..KC와 북쪽 경계 LL=1..NCBN을 순회한다(97–100). VHDX2(L,K)의 수송량을 VOLOUTE에 더한다(102). MIN/MAX 부호별로 L 또는 남쪽 이웃 LS의 SAL1·DYE1을 사용한다(103–106). PPEOUTE와 BBEOUTE에는 L과 LS의 자료를 사용한다(107–112). 두 루프를 닫는다(114–115). 원문 실행문: `DO K=1,KC` (97); `DO LL=1,NCBN` (98); `L=LCBN(LL)` (99); `LS=LSC(L)` (100); `VOLOUTE=VOLOUTE+VHDX2(L,K)*DZC(K)` (102); `SALOUTE=SALOUTE+MIN(VHDX2(L,K),0.)*SAL1(L,K)*DZC(K)` (103); `&             +MAX(VHDX2(L,K),0.)*SAL1(LS,K)*DZC(K)` (104); `DYEOUTE=DYEOUTE+MIN(VHDX2(L,K),0.)*DYE1(L,K)*DZC(K)` (105); `&             +MAX(VHDX2(L,K),0.)*DYE1(LS,K)*DZC(K)` (106); `PPEOUTE=PPEOUTE+VHDX2(L,K)*G*DZC(K)*( 0.5*(BELV(L)+BELV(LS))` (107); `&       +0.125*(HP(L)+H2P(L)+HP(LS)+H2P(LS))*(Z(K)+Z(K-1)) )` (108); `BBEOUTE=BBEOUTE+MIN(VHDX2(L,K),0.)*DZC(K)*GP*( BELV(L)` (109); `&                  +0.5*HP(L)*(Z(K)+Z(K-1)) )*B1(L,K)` (110); `&             +MAX(VHDX2(L,K),0.)*DZC(K)*GP*( BELV(LS)` (111); `&                  +0.5*HP(LS)*(Z(K)+Z(K-1)) )*B1(LS,K)` (112). |
| 117–120 | 시작 시 6행 CBALEV2 루틴 안. 구분 주석과 RETURN·END를 포함한다(117–120). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–115: 이 파일의 경계 누적 식은 DZC를 곱하지만 DT 또는 DT2를 곱하지 않는다. 이 파일에는 누적값 초기화나 시간 간격 선택 조건이 없다.
- 43–48·64–69·85–90·107–112: PPEOUTE는 HP와 H2P를 함께 사용한다. BBEOUTE의 높이 항은 HP만 사용한다.
