---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csedtaus.f90
lines: 113
sha256: 3c76c33535bc69603c636f9f300f540ed6d0b106e01cbce72e9e4a1f9f6e307f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedtaus.f90 — 판독 구간 기록

구간은 1행부터 113행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | EFDC+·저작권·GPLv2 머리말(1–8). CSEDTAUS 함수 입구(9). 점착성 퇴적물(cohesive sediment)의 표면 침식(surface erosion) 임계전단응력(critical shear stress)을 m²/s²로 반환한다는 주석(11). DENBULK는 kg/m³, TAUCO는 입력·참조 임계전단응력, VDRO·VDR·VDRC는 무차원 공극비(void ratio)로 설명한다(13–17). implicit none과 L·IOPT·실수 인수를 선언한다(19–23). |
| 25–54 | 시작 시 9행 CSEDTAUS 안. 옵션 1은 Hwang–Mehta 1989의 벌크밀도(bulk density) 식이다(25–35). DENBULK를 0.001배한 BULKDEN<=1.065이면 1.0E-12를 반환한다(30–32). else는 0.2승과 선형 계수를 사용한다(33–36). 옵션 2·3은 TAUCO에 참조 공극비와 현재 공극비의 비를 곱한다(38–46). 옵션 4·5는 TAUCO를 그대로 반환한다(48–53). 44행 주석은 VDR=VDRC이므로 2·3이 동일하다고 적는다. 조건·계산·호출 원문: `if( IOPT == 1 )then` (29); `BULKDEN = 0.001*DENBULK  ! *** TO PREVENT CORRUPTING THE DENBULK VARIABLE` (30); `if( BULKDEN <= 1.065 )then` (31); `CSEDTAUS = 1.0E-12` (32); `else` (33); `TMP = (BULKDEN - 1.065)**0.2` (34); `CSEDTAUS = 0.001*(0.883*TMP + 0.05)` (35); `elseif( IOPT == 2 )then` (41); `CSEDTAUS = TAUCO*(1. + VDRO)/(1. + VDR)` (42); `elseif( IOPT == 3 )then` (45); `CSEDTAUS = TAUCO*(1. + VDRO)/(1. + VDRC)` (46); `elseif( IOPT == 4 )then` (49); `elseif( IOPT == 5 )then` (52). |
| 55–74 | 시작 시 9행 CSEDTAUS·29행 옵션 선택 블록 안. IOPT=99의 병렬 elseif와 변경 이력 주석(55–65). L<=265이면 0.2/1000., else이면 0.4/1000.을 반환한다(66–70). 외부 else는 잘못된 재부유(resuspension) 옵션 문자열로 STOPP를 호출한다(71–72). 선택 블록 종료·주석을 포함한다(73–74). 조건·계산·호출 원문: `elseif( IOPT == 99 )then` (55); `if( L <= 265 )then` (66); `CSEDTAUS = 0.2/1000.` (67); `else` (68); `CSEDTAUS = 0.4/1000.` (69); `else` (71); `call STOPP('CSEDTAUS: BAD SEDIMENT RESUSPENSION OPTION! STOPPING!')` (72). |
| 75–113 | 시작 시 9행 CSEDTAUS 안. D90·D50·phi 표준편차(standard deviation) 계산과 변경 이력을 설명하는 주석 블록이다(75–110). 입경 변환, phi의 거듭제곱, D50 합·정규화, 90백분위 Z 점수, 점착농도, D90/D50 응력식은 모두 주석 처리되어 있다(80–108). return·END·마지막 빈 줄을 포함한다(111–113). 조건·계산·호출 원문: `!      SEDDIA(1) = 22.0*1.E-6 !CONVERT MICRON TO METER` (80); `!      SEDDIA(1) = 22.0*1.E-6 !CONVERT MICRON TO METER` (87); `!      RSIGPHI = 2.**(RSIGPHI)` (94); `!       !D50SIG = D50SIG+SNDB(L,KTOP,NX)*(SEDDIA(NS))` (98); `!      !D50SIG = D50SIG+SEDB(L,KTOP,1)*(SEDDIA(1))` (99); `!      !D50SIG = D50SIG/RSNDBT` (100); `!      Z90 = 1.281551  !(Z-SCORE FOR THE 90TH PERCENTILE)` (103); `!      COHCON= (SEDB(L,KTOP,1)*1E-6)/HBED(L,KTOP)` (105); `!      CSEDTAUS = (0.36*((D90SIG/D50SIG)**0.948803))` (106); `!        CSEDTAUS = 2./10000.` (107). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–46: 주석은 VDR와 VDRC가 같다고 적는다. 함수는 두 값을 별도 인수로 받으며 동일성을 검사하거나 대입하는 실행문은 없다.
- 49–53: IOPT=4와 IOPT=5의 실행 반환값은 모두 TAUCO이다.
- 55–70: IOPT=99는 셀 번호 L의 고정 경계 265를 사용한다. 이 분기의 실행식에는 DENBULK·TAUCO·공극비 인수가 없다.
- 75–108: D90·D50 관련 계산과 STOPP 호출은 모두 주석 처리되어 있다.

