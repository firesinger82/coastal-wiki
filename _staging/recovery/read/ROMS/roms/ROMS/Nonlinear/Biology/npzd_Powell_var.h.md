---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Powell_var.h
lines: 102
sha256: 9d196123b372299d70a18c0af46c10b20b8dca24b97f13a8d8b7a2b895b3fa13
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Powell_var.h — 판독 구간 기록

구간은 1행부터 102행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 저작권·MIT/X 사용허가·License_ROMS.md 안내(1–7). Powell 등(2006)의 입출력 NetCDF 변수에 메타데이터(metadata) 인덱스를 부여하며 정보는 varinfo.yaml에서 읽는다는 주석(9–11). mod_ncparam.F의 initialize_ncparm에 삽입된다는 설명(13–14). 이 파일에는 SELECT CASE를 여는 행이 없고 삽입할 CASE 본문만 있다. C 주석·빈 줄·모델 상태 추적자 안내(16–22). |
| 23–31 | 포함한 파일의 SELECT CASE 안. `CASE ('idTvar(iNO3_)')` (23), `CASE ('idTvar(iPhyt)')` (25), `CASE ('idTvar(iZoop)')` (27), `CASE ('idTvar(iSDet)')` (29)는 각각 idTvar(iNO3_/iPhyt/iZoop/iSDet)에 varid를 복사(24·26·28·30). 빈 줄 포함(31). |
| 32–49 | 포함한 파일의 SELECT CASE 안. 수반 민감도(adjoint sensitivity) 전처리 조건은 `#if defined AD_SENSITIVITY   \|\| defined I4DVAR_ANA_SENSITIVITY \|\| \` (32), `defined OPT_OBSERVATIONS \|\| defined SENSITIVITY_4DVAR      \|\| \` (33), `defined SO_SEMI` (34)의 세 물리 행이다. 설명 주석·빈 줄(35–39). `CASE ('idTads(iNO3_)')` (40), `CASE ('idTads(iPhyt)')` (42), `CASE ('idTads(iZoop)')` (44), `CASE ('idTads(iSDet)')` (46)는 idTads(iNO3_/iPhyt/iZoop/iSDet)에 varid를 복사(41·43·45·47). `#endif` (48)와 빈 줄(49). |
| 50–89 | 포함한 파일의 SELECT CASE 안. 개방경계(open boundary) 메타데이터 설명(50–53). 질산염의 `CASE ('idTbry(iwest,iNO3_)')` (54), `CASE ('idTbry(ieast,iNO3_)')` (56), `CASE ('idTbry(isouth,iNO3_)')` (58), `CASE ('idTbry(inorth,iNO3_)')` (60)는 서/동/남/북 idTbry에 varid 복사(55·57·59·61). 식물플랑크톤의 `CASE ('idTbry(iwest,iPhyt)')` (63), `CASE ('idTbry(ieast,iPhyt)')` (65), `CASE ('idTbry(isouth,iPhyt)')` (67), `CASE ('idTbry(inorth,iPhyt)')` (69)는 같은 네 방향에 복사(64·66·68·70). 동물플랑크톤의 `CASE ('idTbry(iwest,iZoop)')` (72), `CASE ('idTbry(ieast,iZoop)')` (74), `CASE ('idTbry(isouth,iZoop)')` (76), `CASE ('idTbry(inorth,iZoop)')` (78)는 같은 네 방향에 복사(73·75·77·79). 쇄설물의 `CASE ('idTbry(iwest,iSDet)')` (81), `CASE ('idTbry(ieast,iSDet)')` (83), `CASE ('idTbry(isouth,iSDet)')` (85), `CASE ('idTbry(inorth,iSDet)')` (87)는 같은 네 방향에 복사(82·84·86·88). 빈 줄 포함(89). |
| 90–102 | 포함한 파일의 SELECT CASE 안. 점 공급원·소멸항(point source/sink)과 하천 유출(river runoff) 설명·빈 줄(90–94). `CASE ('idRtrc(iNO3_)')` (95), `CASE ('idRtrc(iPhyt)')` (97), `CASE ('idRtrc(iZoop)')` (99), `CASE ('idRtrc(iSDet)')` (101)는 각각 idRtrc(iNO3_)·idRtrc(iPhyt)·idRtrc(iZoop)·idRtrc(iSDet)에 varid를 복사(96·98·100·102). 마지막 행은 쇄설물 식별자 복사이다(102). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
