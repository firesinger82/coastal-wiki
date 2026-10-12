---
file: models/ShorelineS/raw/source_code/shorelines/functions/extract_berm.m
lines: 79
sha256: 2552eade283284baedf55e72e0731a1caeef2c127a0bd1f4e002757387a38633
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# extract_berm.m — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | 함수 시그니처 `function extract_berm(S,step,qwind,qwave,time,bermW,WBplot2,ds_cl,csplot2,ntrans)` (1). 바람·파랑·버름(berm) 폭 자료 저장 목적 주석(4). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(6–33). S 필드 기본값 대입은 없다. |
| 34–59 | 출력 조건 `if S.extractbermplot` (34). step·qwind·qwave·time을 ASCII로 저장(35–38), figure 11·13을 plan.fig·trans.fig로 저장(39–40). 버름 시계열 조건 `if ~isempty(WBplot2)` (41), 단면(transect) 루프 `for i =1:ntrans` (43). figure 14의 subplot(ntrans,1,i)에 WBplot2·bermW(i,:)를 표시(44–47). 월·연도 축, 첫·끝 시간 범위, 제목·단위 설정(48–52), `print(gcf,'berm_width.jpg','-dpng','-r300')` (53)으로 이미지 저장, 격자 표시(54). 반복 뒤 bermW·WBplot2 ASCII 저장(57–58). plot_wb 호출은 주석 처리(42). |
| 60–79 | 시작 시 34행 출력 참 분기 안. 해안선 변화 자료 조건 `if ~isempty(csplot2)` (60). figure 14·hold 설정(62–63). 단면 루프 `for i =1:ntrans` (64), subplot·csplot2와 ds_cl 표시(65–66), 축·제목·단위·격자 설정(67–72). 반복 뒤 `print(gcf,'berm_width.jpg','-dpng','-r300')` (74)로 이미지 저장, ds_cl·csplot2 ASCII 저장(75–76). plot_cl 호출은 주석 처리(61). 두 분기·함수 종료(77–79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 53·74: 이미지 이름은 berm_width.jpg이지만 print 장치 옵션은 -dpng이다.
- 44·53·62·74: 두 자료 분기는 figure 14를 사용하며 같은 이미지 이름으로 저장한다.
- 66·69–71: 두 번째 분기는 ds_cl을 표시하지만 제목과 y축은 Berm width로 적는다.
