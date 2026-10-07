---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Input_Files/Time_Series_Files/Time_Series_Input_File_Formats/aser.md
lines: 110
sha256: 2e98302dcd0928c4c018efdd72392e66ebc20ad07e02e92c8bce94ea75395bc9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# aser.md — 판독 구간 기록

구간은 1행부터 110행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 aser.inp이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–16 | aser.inp / 파일 용도·적용 버전 — 자유 형식(free format)의 대기 강제력(atmospheric forcing) 파일이며 lake okeechobee 예와 naser=1 반복을 적는다(10). EFDC의 1996년 7월 28일 및 이후 버전에 사용하도록 적는다(14). 주석과 빈 줄을 포함한다. 원문: `C aser.inp file, in free format across line, repeats naser=1 times, lake okeechobee` (10); `C ATMOSPHERIC FORCING FILE, USE WITH 28 JULY 96 AND LATER VERSIONS OF EFDC` (14). |
| 17–52 | 대기·열 교환 매개변수 — 시간 데이터 수, 시간 단위의 초 변환, 입력 시각과 같은 단위의 가산 조정, 습구 온도(wet-bulb temperature)·상대 습도(relative humidity) 선택을 설명한다(18–24). 강우·증발·단파 복사(shortwave radiation)·운량(cloud cover) 변환을 설명한다(26–34). 증발·대류 열 전달, 빠른·느린 감쇠(attenuation), 빠른 감쇠 분율, 활성 하상 온도층의 깊이·두께, 초기 하상 온도, 하상과 최하층 물 사이 열 교환을 설명한다(36–52). 수식처럼 적힌 변환 관계, 조건, 이름·범위·단위는 각 행을 그대로 옮긴다. 기본값은 별도로 제시하지 않는다. 원문: `C MASER =NUMBER OF TIME DATA POINTS` (18); `C TCASER =DATA TIME UNIT CONVERSION TO SECONDS` (20); `C TAASER =ADDITIVE ADJUSTMENT OF TIME VALUES SAME UNITS AS INPUT TIMES` (22); `C IRELH =0 VALUE TWET COLUMN VALUE IS TWET, =1 VALUE IS RELATIVE HUMIDITY` (24); `C RAINCVT =CONVERTS RAIN TO UNITS OF M/SEC,inch/hour=0.0254 m/3600 s=7.0556E-6m/s` (26); `C EVAPCVT =CONVERTS EVAP TO UNITS OF M/SEC, IF EVAPCVT<0 EVAP IS INTERNALLY COMPUTED, \*abs(evapcvt) in calqvs.for for TestWQ, Ji, 9/22/02` (28); `C SOLRCVT =CONVERTS SOLAR SW RADIATION TO JOULES/SQ METER` (30); `C CLDCVT =MULTIPLIER FOR ADJUSTING CLOUD COVER` (32); `C IASWRAD =O DISTRIBUTE SW SOL RAD OVER WATER COL AND INTO BED, =1 ALL TO SURF LAYER` (34); `C REVC =1000\*EVAPORATIVE TRANSFER COEF, REVC<0 USE WIND SPD DEPD DRAG COEF` (36); `C RCHC =1000\*CONVECTIVE HEAT TRANSFER COEF, REVC<0 USE WIND SPD DEPD DRAG COEF` (38); `C SWRATNF =FAST SCALE SOLAR SW RADIATION ATTENUATION COEFFCIENT 1./METERS` (40); `C SWRATNS =SLOW SCALE SOLAR SW RADIATION ATTENUATION COEFFCIENT 1./METERS` (42); `C FSWRATF =FRACTION OF SOLSR SW RADIATION ATTENUATED FAST 0<FSWRATF<1` (44); `C DABEDT =DEPTH OR THICKNESS OF ACTIVE BED TEMPERATURE LAYER, METERS` (46); `C TBEDIT =INITIAL BED TEMPERATURE` (48); `C HTBED1 =CONVECTIVE HT COEFFCIENT BETWEEN BED AND BOTTOM WATER LAYER NO DIM` (50); `C HTBED2 =HEAT TRANS COEFFCIENT BETWEEN BED AND BOTTOM WATER LAYER M/SEC` (52). |
| 53–73 | 시계열 열 정의 — 대기압(atmospheric pressure), ISOPT(2)에 따른 건구 온도(dry-bulb temperature) 또는 평형 온도(equilibrium temperature), IRELH에 따른 습구 온도 또는 상대 습도, 강우율·증발율, 수면 단파 복사와 운량을 설명한다(54–66). 주석과 빈 줄을 포함한다(68–73). 원문: `C PATM =ATM PRESS MILLIBAR` (54); `C TDRY/TEQ =DRY ATM TEMP ISOPT(2)=1 OR EQUIL TEMP ISOPT(2)=2` (56); `C TWET/RELH =WET BULB ATM TEMP IRELH=0, RELATIVE HUMIDITY IRELH=1` (58); `C RAIN =RAIN FALL RATE LENGTH/TIME` (60); `C EVAP =EVAPORATION RATE IS EVAPCVT>0.` (62); `C SOLSWR =SOLAR SHORT WAVE RADIATION AT WATER SURFACE ENERGY FLUX/UNIT AREA` (64); `C CLOUD =FRATIONAL CLOUD COVER` (66). |
| 74–85 | 버전 표기 / 열 이름·단위 / 입력 헤더 예시 — EFDC_DSI_VER 값 7.301을 적는다(74). TASER(D), PATM(MB), TDRY(C), TWET(C), RAIN(M/D), EVAP(M/D), SOLSWR(W/M2), CLOUD의 순서와 단위를 제시한다(78). MASER부터 CLDCVT까지 헤더 필드와 예시값을 그대로 옮긴다(82–84). 예시값을 기본값으로 정의하지 않는다. 원문: `EE EFDC\_DSI\_VER: 7.301` (74); `C \*\* TASER(D) PATM(MB) TDRY(C) TWET(C) RAIN(M/D) EVAP(M/D) SOLSWR(W/M2) CLOUD` (78); `C \*\* MASER TCASER TAASER IRELH RAINCVT EVAPCVT SOLRCVT CLDCVT ! \*\*\* ID` (82); `9547 86400.0 0.0 1 1.1574E-05 1.1574E-05 1.0 1.0 ! ASER\_1` (84). |
| 86–110 | 대기 시계열 입력 예시 — 86–110행의 비어 있지 않은 13개 데이터 행을 순서대로 그대로 옮긴다. 시각과 대기압·온도 또는 상대 습도·강우·증발·단파 복사·운량 열의 예시이다. 빈 줄을 포함한다(87–109). 원문: `0.000 1012.0000 22.2720 0.8550 0.0000 0.0000 0.0000 0.1000` (86); `0.062 1012.0000 21.8340 0.8550 0.0000 0.0000 0.0000 0.1000` (88); `0.104 1012.0000 21.6670 0.8480 0.0000 0.0000 0.0000 0.1000` (90); `0.140 1012.0000 21.5670 0.8490 0.0000 0.0000 0.0000 0.1000` (92); `0.188 1012.0000 21.4980 0.8460 0.0000 0.0000 0.0000 0.1000` (94); `0.229 1012.0000 21.4970 0.8540 0.0000 0.0000 0.0000 0.1000` (96); `0.266 1012.0000 21.3850 0.8560 0.0000 0.0000 15.6000 0.1000` (98); `0.312 1012.0000 21.6400 0.8180 0.0000 0.0000 160.2000 0.1000` (100); `0.354 1012.0000 21.6970 0.7980 0.0000 0.0000 259.8000 0.1000` (102); `0.391 1012.0000 21.9650 0.8000 0.0000 0.0000 375.6000 0.1000` (104); `0.438 1012.0000 22.6700 0.7850 0.0000 0.0000 478.8000 0.1000` (106); `0.479 1012.0000 23.6500 0.7480 0.0000 0.0000 516.6000 0.1000` (108); `0.516 1012.0000 24.2000 0.7120 0.0000 0.0000 529.2000 0.1000` (110). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 34행: IASWRAD의 첫 옵션 문자는 숫자 0이 아니라 대문자 `O`로 적혀 있다.
- 36·38행: REVC 설명과 RCHC 설명 모두 풍속 의존 계수를 사용하는 조건을 `REVC<0`으로 적는다.
- 30·78행: SOLRCVT 설명은 태양 단파 복사의 단위를 `JOULES/SQ METER`로 적고 데이터 열 표기는 `SOLSWR(W/M2)`로 적는다.
- 18·84·86–110행: MASER를 시간 데이터 수로 정의한다. 예시 헤더의 MASER는 9547이다. 이 파일에 실린 뒤쪽 데이터 행은 13개이다.

