---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Data_Format_B-10__Time_Series_for_atmospheric_forcings.md
lines: 14
sha256: 09ba2a5198a8b55e7df89e8547fa77b8b45bf162109fcde673301b2b60cb3614
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-10__Time_Series_for_atmospheric_forcings.md — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.
그림 경로는 원문과 같은 space 폴더를 기준으로 적었다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 ID·제목·space·URL·버전·갱신 시각·경로와 frontmatter이다(1–9행). |
| 10–11 | `aser.inp`를 대기 강제력(atmospheric forcing) 자료 파일로 설명한다. Noorinastaliq 글꼴·우르두어(Urdu) Nastaliq 문자·페이지 레이아웃 지원에 관한 문장도 원문에 있다(10행). 원문: `aser.inp is the atmospheric data file. It contains text saved in the Noorinastaliq font, which displays Urdu in Nastaliq script. INP files also support standard page layout formatting.` (10). |
| 12–14 | `Example` 표제·빈 줄과 입력 형식 예시 그림이다(12–14행). 그림의 필드·조건·단위·예시 행을 그대로 옮겼다. 그림 직접 확인: `attachments/1588723863/B-12.png` — `aser.inp`를 편집기에서 보여 준다(14행). 그림에 보이는 주석·필드·단위·설정값과 예시 행: `* ASER.INP - TIME SERIES FOR ATMOSPHERIC FORCINGS - Version: 10.3` (그림 1행); `* Project: EFDC+ Demonstration` (그림 2행); `* Use with 28 July 96 and later versions of EFDC` (그림 3행); `*` (그림 4행); `* MASER =Number of time data points` (그림 5행); `* TCASER =Data time unit conversion to seconds` (그림 6행); `* TAASER =additive adjustment of time values same units as input times` (그림 7행); `* IRELH =0 value TWET column value is TWET, =1 value is Relative Humidity` (그림 8행); `* RAINCVT =Converts RAIN to units of m/sec , inch/day=0.0254m/86400s=2.94E-7m/s, inch/h=7.05556E-6m/s` (그림 9행); `* EVAPCVT =Converts EVAP to units of m/sec, if EVAPCVT<0 EVAP is internally computed` (그림 10행); `* SOLRCVT =Converts Solar SW Radiation to joules/sq meter (Watts/m^2)` (그림 11행); `* CLDCVT =Multiplier for adjusting cloud cover` (그림 12행); `* PATM =Atm pressure (millibar)` (그림 13행); `* TDRY/TEQ =Dry atm temp ISOPT(2)=1 or equil temp ISOPT(2)=2 (deg. C)` (그림 14행); `* TWET/RELH =Wet bulb atm temp IRELH=0, relative humidity IRELH=1 (deg. C or dimensionless)` (그림 15행); `* RAIN =Rain fall rate length/time (meters/day)` (그림 16행); `* EVAP =Evaporation rate is EVAPCVT>0 (meters/day)` (그림 17행); `* SOLSWR =Solar Short Wave Radiation at the water surface (energy flux/unit area)` (그림 18행); `* CLOUD =Fractional cloud cover (dimensionless)` (그림 19행); `*` (그림 20행); `EE EFDC_DSI_VER: 7.301` (그림 21행); `*` (그림 22행); `*` (그림 23행); `* MASER TCASER TAASER IRELH RAINCVT EVAPCVT SOLRCVT CLDCVT` (그림 24행); `* IASWRAD REVC RCHC SWRATNF SWRATNS FSWRATF DABEDT TBEDIT HTBED1 HTBED2` (그림 25행); `* TASER(D) PATM(MB) TDRY(C) TWET(C) RAIN(M/D) EVAP(M/D) SOLSWR(W/M2) CLOUD` (그림 26행); `*` (그림 27행); `*Format: F3 F1 F2 F3 F7 F7 F1 F3` (그림 28행); `20138 86400.000 0.000 1 1.15740E-005 1.15741E-005 1.000 1.000 ! SERIES 0` (그림 29행); `-154.000 1001.0 26.10 0.900 0.000000 0.000000 0.0 0.000` (그림 30행); `-153.960 1001.0 25.00 0.900 0.000000 0.000000 0.0 0.000` (그림 31행); `-153.920 1001.0 22.30 0.900 0.000000 0.000000 0.0 0.000` (그림 32행); `-153.870 1001.0 22.20 0.900 0.000000 0.000000 0.0 0.200` (그림 33행); `-153.830 1001.0 21.70 0.930 0.000000 0.000000 0.0 0.200` (그림 34행); `-153.790 1002.0 22.80 0.930 0.000000 0.000000 135.9 0.200` (그림 35행); `-153.750 1002.0 25.60 0.840 0.000000 0.000000 291.3 0.300` (그림 36행); `-153.710 1003.0 27.20 0.760 0.000000 0.000000 446.6 0.300` (그림 37행); `-153.670 1003.0 28.90 0.660 0.000000 0.000000 534.5 0.300` (그림 38행); `-153.620 1003.0 31.10 0.550 0.000000 0.000000 534.5 0.200` (그림 39행); `-153.580 1002.0 32.80 0.490 0.000000 0.000000 534.5 0.200` (그림 40행); `-153.540 1002.0 35.00 0.410 0.000000 0.000000 534.5 0.200` (그림 41행); `-153.500 1001.0 36.10 0.370 0.000000 0.000000 534.5 0.200` (그림 42행); `-153.460 1001.0 37.20 0.370 0.000000 0.000000 446.6 0.200` (그림 43행); `-153.420 1000.0 37.80 0.360 0.000000 0.000000 291.3 0.200` (그림 44행); `-153.380 1000.0 37.80 0.360 0.000000 0.000000 446.6 0.000` (그림 45행); `-153.330 999.0 37.80 0.360 0.000000 0.000000 291.3 0.100` (그림 46행); `-153.290 999.0 37.20 0.380 0.000000 0.000000 135.9 0.100` (그림 47행); `-153.250 999.0 35.60 0.480 0.000000 0.000000 0.0 0.000` (그림 48행); `-153.210 999.0 33.90 0.550 0.000000 0.000000 0.0 0.000` (그림 49행). 단위 환산식의 LaTeX 표기는 `\(\mathrm{inch/day}=0.0254\mathrm{m}/86400\mathrm{s}=2.94\mathrm{E}{-7}\mathrm{m/s}\)`, `\(\mathrm{inch/h}=7.05556\mathrm{E}{-6}\mathrm{m/s}\)`이다(그림 9행). 화면에는 1–49행이 보이고 파일 줄 수는 `20168`이다. |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 본문의 Noorinastaliq·우르두어·페이지 레이아웃 설명과 예시 그림의 영문 주석·숫자 자료 형식 사이의 관계는 설명하지 않는다(10,14행).
- 그림은 파일 전체 `20168`행 중 1–49행만 보여 준다(14행).
- 그림 헤더에 `IASWRAD REVC RCHC SWRATNF SWRATNS FSWRATF DABEDT TBEDIT HTBED1 HTBED2`가 있으나 이 문서의 본문·그림에는 각 필드의 정의가 없다(14행, 그림 25행).

