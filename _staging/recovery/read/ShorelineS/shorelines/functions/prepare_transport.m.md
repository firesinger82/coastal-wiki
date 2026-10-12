---
file: models/ShorelineS/raw/source_code/shorelines/functions/prepare_transport.m
lines: 223
sha256: 1faf0604515f70816a2da56e17654742266bde56c2e0c4cd48b855b75a9e0a33
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# prepare_transport.m — 판독 구간 기록

구간은 1행부터 223행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–73 | 함수 시그니처는 `function [TRANSP]=prepare_transport(S)` (1). 입력·출력 주석은 표사 수송(sediment transport) 공식 CERC·KAMP·MILH·VR14, 보정 계수, 입경·공극률(porosity)·경사·조도(roughness)·밀도·중력, 쇄파(breaking) 계수, 너울(swell) 비율, 돌제(groyne) 우회(bypassing), 수송 관성(inertia), 고각 불안정(high-angle instability), 경계조건(boundary condition), 표사 공급 제한(sediment limitation)을 설명한다(2–72). 주석은 porosity의 전형값 0.4(14·48), tanbetasetup 기본 1(16·50), alpha 예시 1.8(22·56), pswell 범위 0부터 100(24·58), 시계열 aw 기본 1.27(25·59), bypasscontrfac 1 이상(26·60)을 적는다. 이 파일에는 S 숫자 기본값 대입이 없다. |
| 74–101 | 저작권·연락처·LGPL 2.1 이상·무보증 주석과 빈 줄이다. |
| 102–131 | 로그 뒤 TRANSP를 만든다(102–103). trform·b·qscal·d50·d90·porosity·tanbeta·tanbetasetup·ks·rhos·rhow·g·cf·n·alpha·gamma·pswell·aw를 같은 이름의 S 필드에서 복사한다(104–121). `if isempty(S.wvcfile)` (122)이면 aw를 S.awfixedhs에서 다시 복사한다(123). relaxationlength·twopoints·critwidth·suppresshighangle·acal·submerged를 같은 이름의 S 필드에서 복사한다(125–130). 각 복사문의 물리 설명 주석과 빈 줄을 포함한다. |
| 132–150 | 경계조건 예시 주석을 포함한다(132–133). `if ischar(S.boundaryconditionstart)` (134)이면 `TRANSP.boundaryconditionstart={S.boundaryconditionstart,nan};` (135). `else` (136)는 입력을 그대로 복사한다(137). `if ischar(S.boundaryconditionend)` (139)이면 `TRANSP.boundaryconditionend={S.boundaryconditionend,nan};` (140). `else` (141)는 입력을 그대로 복사한다(142). xsedlim·ysedlim·widthsedlim을 비우고 sedlim을 S에서 복사한다(146–150). xc_sedlim 초기화는 주석이다(148). |
| 151–175 | `if TRANSP.sedlim` (151) 안에서 `if strcmpi(S.ldbsedlim,'manual') \|\| strcmpi(S.ldbsedlim,'interactive')` (153)이면 그림·안내문 뒤 select_multi_polygon('k')를 호출한다(158). 안내문 위치는 `xl(1)+0.02*diff(xl)`과 `yl(2)-0.01*diff(yl)`이다(157). 좌표를 복사하고 `TRANSP.widthsedlim=repmat(TRANSP.widthsedlim,size(TRANSP.xsedlim));` (162). `elseif ~isempty(S.ldbsedlim)` (165)이면 load(166), `TRANSP.xsedlim=xysedlim(:,1)'-S.xyoffset(1);` (167), `TRANSP.ysedlim=xysedlim(:,2)'-S.xyoffset(2);` (168), `TRANSP.widthsedlim=xysedlim(:,3)';` (169). `elseif ~isempty(S.xsedlim) && ~isempty(S.ysedlim)` (172)이면 `TRANSP.xsedlim=S.xsedlim(:)'-S.xyoffset(1);` (173), `TRANSP.ysedlim=S.ysedlim(:)'-S.xyoffset(2);` (174), `TRANSP.widthsedlim=S.widthsedlim(:)';` (175). [10-12 전수 검증 보완] |
| 176–206 | 시작 시 151행 sedlim 분기·172행 직접 좌표 입력 분기 안. `if length(TRANSP.widthsedlim)<length(TRANSP.xsedlim)` (176)이면 `widthsedlim=TRANSP.widthsedlim(~isnan(TRANSP.widthsedlim));` (177), `idnan=find(isnan(TRANSP.xsedlim));` (179). `if length(widthsedlim)==length(idnan)+1` (180)이면 `ids=[0,idnan(:)',length(TRANSP.xsedlim)+1];` (181), `TRANSP.widthsedlim=nan(size(TRANSP.xsedlim));` (182), jj를 1로 초기화(183). `for ii=1:length(TRANSP.widthsedlim)` (184)에서 `if ~isnan(TRANSP.xsedlim(ii))` (185)이면 widthsedlim(jj)를 복사한다(186). `else` (187)는 `jj=jj+1;` (188). 180행의 `else` (191)는 `TRANSP.widthsedlim=repmat(TRANSP.widthsedlim(1),size(TRANSP.xsedlim));` (193). 입력 선택의 `else` (198)는 `TRANSP.sedlim=0;` (199)과 빈 좌표·폭 대입이다(200–202). `TRANSP.nsedlim=min(sum(isnan(TRANSP.xsedlim))+1,length(TRANSP.xsedlim));` (204)로 개수를 계산한다. sedlim 분기를 닫고 빈 줄을 포함한다. |
| 207–223 | `idnotnan=find(~isnan(TRANSP.xsedlim));` (208). `if ~isempty(TRANSP.xsedlim)` (209)이면 `TRANSP.xsedlim=TRANSP.xsedlim(idnotnan(1):idnotnan(end));` (210), `TRANSP.ysedlim=TRANSP.ysedlim(idnotnan(1):idnotnan(end));` (211), `TRANSP.widthsedlim=TRANSP.widthsedlim(idnotnan(1):idnotnan(end));` (212), `idnan=find(isnan(TRANSP.xsedlim));` (213), `iduse=setdiff([1:length(TRANSP.xsedlim)],idnan(diff(idnan)==1));` (214), `TRANSP.xsedlim=TRANSP.xsedlim(iduse);` (215), `TRANSP.ysedlim=TRANSP.ysedlim(iduse);` (216), `TRANSP.widthsedlim=TRANSP.widthsedlim(iduse);` (217). struct2log 호출은 주석이다(221). 빈 줄과 함수 종료를 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 149·153–162: widthsedlim은 빈 배열로 초기화한다. 대화형 입력 분기는 S.widthsedlim을 읽지 않고 이 빈 배열을 repmat의 첫 인수로 사용한다.
- 181: ids를 계산한다. 이후 실행문은 ids를 참조하지 않는다.
- 151–205: nsedlim 대입은 sedlim 참 분기 안에만 있다.
- 204·207–218: nsedlim은 NaN 정리 전에 계산한다. 정리 뒤 개수를 다시 대입하는 문장은 없다.
- 208–212: 좌표 정리 조건은 xsedlim의 비어 있음만 검사한다. idnotnan의 비어 있음은 검사하지 않고 첫 원소와 마지막 원소를 참조한다.
- 21·55·116: cf는 머리말에서 roughness factor로 설명한다. 복사문 주석은 단위를 m로 적는다.
