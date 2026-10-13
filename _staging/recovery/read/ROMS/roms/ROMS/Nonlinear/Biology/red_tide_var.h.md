---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/red_tide_var.h
lines: 63
sha256: 84b67e0d4787654b22c33cd53ccb864d47ae40307e87c83691dcd81e1fc8ed62
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# red_tide_var.h — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 전처리 조건 밖. C 형식 머리말과 빈 줄이다. 주석은 `varinfo.yaml`에서 읽은 적조 생물모델 NetCDF 메타데이터(metadata) ID를 배정한다고 설명한다(9–12). 주석은 이 파일을 `mod_ncparam.F`의 `initialize_ncparm`에 포함한다고 적는다(14–15). SELECT 입구와 포함하는 쪽의 전처리 조건은 이 파일에 없다. |
| 24–43 | 전처리 조건 밖에서 시작한다. CASE로 idAsrf·idCyst·idODIN·idTvar(iDino)에 varid를 배정한다(24–31). 33–35행의 감도(sensitivity) 관련 전처리 조건 안에서 idTads(iDino)를 배정하고 조건을 닫는다(41–43). 원문: `CASE ('idAsrf')` (24); `idAsrf=varid` (25); `CASE ('idCyst')` (26); `idCyst=varid` (27); `CASE ('idODIN')` (28); `idODIN=varid` (29); `CASE ('idTvar(iDino)')` (30); `idTvar(iDino)=varid` (31); `#if defined AD_SENSITIVITY   \|\| defined I4DVAR_ANA_SENSITIVITY \|\| \` (33); `defined OPT_OBSERVATIONS \|\| defined SENSITIVITY_4DVAR      \|\| \` (34); `defined SO_SEMI` (35); `CASE ('idTads(iDino)')` (41); `idTads(iDino)=varid` (42); `#endif` (43). |
| 44–63 | 전처리 조건 밖. 개방 경계(open boundary) 주석 뒤 서·동·남·북 idTbry의 iDino 메타데이터 ID를 배정한다(45–56). 하천 유출(river runoff) 점원/흡수원 주석 뒤 idRtrc(iDino)에 varid를 배정한다(58–63). CASE가 속한 바깥 SELECT의 입구는 이 파일 범위 밖이다. 원문: `CASE ('idTbry(iwest,iDino)')` (49); `idTbry(iwest,iDino)=varid` (50); `CASE ('idTbry(ieast,iDino)')` (51); `idTbry(ieast,iDino)=varid` (52); `CASE ('idTbry(isouth,iDino)')` (53); `idTbry(isouth,iDino)=varid` (54); `CASE ('idTbry(inorth,iDino)')` (55); `idTbry(inorth,iDino)=varid` (56); `CASE ('idRtrc(iDino)')` (62); `idRtrc(iDino)=varid` (63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
