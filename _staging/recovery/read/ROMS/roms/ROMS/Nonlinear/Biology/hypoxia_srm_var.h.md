---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/hypoxia_srm_var.h
lines: 59
sha256: d62a5ff1f7ac6c6953de49b95c7b3d23c3ab4e9fac7f5c854a3daceecc0a35bc
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# hypoxia_srm_var.h — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 저작권·MIT/X 라이선스·메타데이터(metadata) 인덱스 설명(1–18). varinfo.yaml 정보를 사용하며 mod_ncparam.F의 initialize_ncparm에 포함된다는 주석이다(9–15). 외부 SELECT CASE에 들어가는 조각이며 여는 SELECT는 이 파일에 없다. 모델 상태 CASE에서 idResR와 용존 산소(dissolved oxygen) idTvar(iOxyg)에 varid를 대입한다(24–27). 원문 조건·루프·대입·전처리: `CASE ('idResR')` (24) / `idResR=varid` (25) / `CASE ('idTvar(iOxyg)')` (26) / `idTvar(iOxyg)=varid` (27). |
| 29–39 | 외부 SELECT CASE 조각이 이어진다. AD_SENSITIVITY/I4DVAR_ANA_SENSITIVITY/OPT_OBSERVATIONS/SENSITIVITY_4DVAR/SO_SEMI 전처리 조건에서 수반 민감도(adjoint sensitivity) idTads(iOxyg)에 varid를 대입한다(29–39). 원문 조건·루프·대입·전처리: `#if defined AD_SENSITIVITY   \|\| defined I4DVAR_ANA_SENSITIVITY \|\| \` (29); `defined OPT_OBSERVATIONS \|\| defined SENSITIVITY_4DVAR      \|\| \` (30); `defined SO_SEMI` (31) / `CASE ('idTads(iOxyg)')` (37) / `idTads(iOxyg)=varid` (38) / `#endif` (39). |
| 40–59 | 외부 SELECT CASE 조각이 이어진다. 개방 경계(open boundary) 주석 뒤 서·동·남·북 idTbry의 용존 산소 식별자를 연결한다(41–52). 하천 유출 점 공급/소멸(point source/sink) 주석 뒤 idRtrc(iOxyg)에 varid를 대입한다(54–59). 원문 조건·루프·대입·전처리: `CASE ('idTbry(iwest,iOxyg)')` (45) / `idTbry(iwest,iOxyg)=varid` (46) / `CASE ('idTbry(ieast,iOxyg)')` (47) / `idTbry(ieast,iOxyg)=varid` (48) / `CASE ('idTbry(isouth,iOxyg)')` (49) / `idTbry(isouth,iOxyg)=varid` (50) / `CASE ('idTbry(inorth,iOxyg)')` (51) / `idTbry(inorth,iOxyg)=varid` (52) / `CASE ('idRtrc(iOxyg)')` (58) / `idRtrc(iOxyg)=varid` (59). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
