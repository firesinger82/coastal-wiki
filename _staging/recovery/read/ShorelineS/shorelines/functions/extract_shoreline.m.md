---
file: models/ShorelineS/raw/source_code/shorelines/functions/extract_shoreline.m
lines: 96
sha256: a46501921121287a733793b302a870941c774d5e1aae493ac48d41d303f2da58
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# extract_shoreline.m — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 함수 시그니처 `function extract_shoreline(S,STRUC,COAST,FORMAT)` (1). 지정 시점 해안선(shoreline) 그림과 좌표 내보내기 목적(4–5). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(7–34). S 필드 기본값 대입은 없다. |
| 35–44 | 그림 저장 조건 `if FORMAT.printfig` (35), 회절(diffraction) 조건 `if  S.diffraction==1` (36)이면 구조물 좌표·S.phiw0를 이름에 넣어 PNG 300 dpi로 저장(38). `else` (39)이면 FORMAT.outputdir의 Final에 JPEG 300 dpi 저장(41). 대체 print 문장은 주석 처리(37·40). |
| 45–62 | 해안선 그림 조건 `if ~isempty(FORMAT.slplot)` (45). 경계 자료 조건 `if ~isempty(FORMAT.ldbplot)` (46)은 FORMAT.ldbplot(:,2) 이름 복사(47). `else` (48)는 L2Name(:) 빈 셀 대입·mm=0(49–50). figure 12·hold·hps6 초기화(52–54). 경계 루프 `for mm=1:size(FORMAT.ldbplot,1)` (55), get_landboundary 호출(56), 좌표 오프셋과 선 설정을 포함한 그림 `hps6(mm)=plot(ldbplotval(:,1)-FORMAT.xyoffset(1),ldbplotval(:,2)-FORMAT.xyoffset(2),FORMAT.ldbplot{mm,3},'linewidth',1.5,'MarkerSize',10,'MarkerIndices',1:10:length(COAST.x_mc0));` (57). 해안선 루프 `for sl=1:size(FORMAT.xp_mc,1)` (59), 그림 `hps6(sl+mm)=plot(FORMAT.xp_mc{sl,:},FORMAT.yp_mc{sl,:},FORMAT.slplot{sl,3},'linewidth',1.5);` (60), 이름 추가(61). 자료 선택·계산·호출의 원문은 `ldbplotval = get_landboundary(FORMAT.ldbplot{mm,1});` (56). 추가 원문: `L2Name(end+1)=FORMAT.slplot(sl,2);` (61). [10-12 전수 검증 보완] |
| 63–78 | 시작 시 45행 그림 참 분기·59행 sl 루프 안. 좌표 추출 조건 `if S.extractxy` (63)에서 xp·yp에 셀 내용을 대입(64–65), 출력 행렬 `out=[xp{:}',yp{:}'];` (66). 파일 이름 분기 `if S.da==1 \|\| S.bs==1` (67)의 네 번째 열과 두 번째 열 연결식 `namefl=[cell2mat(FORMAT.slplot(sl,4)) cell2mat(FORMAT.slplot(sl,2))];` (68), `else` (69)의 이름만 선택(70). save ASCII 호출(72). 대체 save는 주석 처리(73–74). 추출하지 않는 `else` (75)는 out 빈 배열(76). sl 루프 종료(78). 추가 원문: `namefl=cell2mat(FORMAT.slplot(sl,2));` (70). [10-12 전수 검증 정정] [10-12 전수 검증 보완] |
| 79–96 | 시작 시 45행 그림 참 분기 안. legend·범례 스타일·구조물·초기 해안선 그림(79–83). xlimits·ylimits 적용(84–85), km 축 눈금 변환 `set(gca,'XtickLabel',num2str(get(gca,'Xtick')'/1000,'%2.1f'));` (86); `set(gca,'YtickLabel',num2str(get(gca,'Ytick')'/1000,'%2.1f'));` (87), 단위 표기(88–89). 저장 조건 `if FORMAT.printfig` (90)에서 Output_without_fill PNG 300 dpi 저장(92). 대체 print·close는 주석 처리(91·93–94). 분기 종료(95–96). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·35–96: 함수 선언 뒤 마지막 end는 45행 if를 닫는다. 별도의 함수 end는 없다.
- 57·81–82: 경계 자료 그림은 FORMAT.xyoffset을 뺀다. 구조물과 초기 해안선 그림은 같은 오프셋 차감을 사용하지 않는다.
- 64–66: xp·yp에 대한 사전 초기화 없이 xp{:}·yp{:} 대입문과 참조가 나온다.
- 67–70: 파일 이름에 FORMAT.slplot의 네 번째 열을 사용할지는 S.da==1 또는 S.bs==1로 정한다.
