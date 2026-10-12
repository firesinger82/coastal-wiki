---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_waveconditions.m
lines: 123
sha256: c0bd7e56b7ebb081d9b2cdbcbfb53690cd90e8d2bfdd532871f7de34797fd38c
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_waveconditions.m — 판독 구간 기록

구간은 1행부터 123행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | 함수 시그니처는 `function [WAVE]=prepare_waveconditions(S,TIME)` (1). 출력 주석은 외해·근해 수심, 쇄파(breaking), 조석·파랑 상호작용, 회절(diffraction), 보간(interpolation), 파랑 입력 파일·시공간 변화·기후 보정·자료 동화(data assimilation)를 설명한다(2–33). dirspr는 시점별 2차원 스펙트럼의 방향 퍼짐(directional spreading), spread는 시간에 따른 방향 퍼짐으로 구분한다(26–27). spread의 주석상 파향 범위식은 `S.phiw0 +/- 0.5*S.spread`이다(16). 저작권·연락처·LGPL 2.1 이상·무보증 주석과 공백 줄을 포함한다(34–61). [10-12 전수 검증 보완] |
| 62–85 | 로그 뒤 WAVE를 만든다(62–63). ddeep·dnearshore·alpha·gamma·waveinteraction·tideinteraction·wavefile·surfwidth·spread·wvcfile·diffraction·diffsmooth·sphimax·interpolationmethod·mergeconditions를 같은 이름의 S 필드에서 복사한다(64–78). ccslr·ccdir·cchs를 같은 이름의 S 필드에서 복사한다(81–83). `try WAVE.DA=S.da;end` (84)로 da를 선택적으로 읽는다. 이 파일에는 S 필드 기본값 대입이 없다. |
| 86–100 | `if ~isfield(S,'dirspr')` (87)이면 `WAVE.dirspr=12;` (88). `elseif isempty(S.dirspr)` (89)이면 `WAVE.dirspr=12;` (90). `else` (91)는 S.dirspr를 복사한다(92). iwc를 빈 배열로 초기화한다(96). `if isempty(WAVE.wvcfile) && isfield(S,'waveclimfile')` (97)이면 이전 입력 S.waveclimfile을 wvcfile에 복사한다(98). 방향 퍼짐과 이전 키워드 호환 주석·빈 줄을 포함한다. |
| 101–123 | WVC를 비운다(102). `if ~isempty(WAVE.wvcfile)` (103)이면 `[WVC]=get_inputfiledata(WAVE.wvcfile,TIME);` (106), `[WVC]=get_aggregatedtimeseries(WVC,TIME);` (110)로 입력을 읽고 시간 간격별 평균 조건으로 집계한다는 주석을 포함한다(108–109). WVC 전체와 WVC(1).spacevaryingwave를 복사한다(113–114). `else` (115)는 Hso·phiw0·spread·tper를 S.hso·S.phiw0·S.spread·S.tper에서 복사한다(116–119). `WAVE.dtrewind=zeros(1,max(length(WAVE.WVC),1));` (121). 빈 줄과 함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 87–92: dirspr 입력 필드가 없거나 비어 있으면 WAVE.dirspr에 12를 대입한다.
- 103–120: spacevaryingwave는 파일 입력 분기에서만 대입한다. Hso·phiw0·tper는 정적 입력 분기에서만 대입한다.
- 106–114: 집계 루틴 반환값을 WVC(1)로 바로 참조한다. 해당 참조 앞에 WVC가 비어 있는지 검사하는 조건은 없다.
