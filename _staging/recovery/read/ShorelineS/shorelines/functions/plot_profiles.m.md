---
file: models/ShorelineS/raw/source_code/shorelines/functions/plot_profiles.m
lines: 86
sha256: 148d405ff8772d1928887e99e160ffcf6b2a399f1e1c9d0fc6a0ace8287ece81
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# plot_profiles.m — 판독 구간 기록

구간은 1행부터 86행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 함수 시그니처(1). 지정 횡단선(transect)에서 해안선·사구 기부(dune foot)의 시간 변화를 그린다는 설명(4–5). 입력은 그림 간격·그림 핸들(handle), 사구 사용 여부, 시간 단계, 위치·시간별 해안 및 사구 위치이다(7–21). 출력은 축·선 핸들과 프로파일 그림 핸들이다(23–26). 원문: `function [FORMAT]=plot_profiles(FORMAT,TIME,DUNE,O)` (1). |
| 28–55 | 시작 시 1행 plot_profiles 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(28–55). |
| 56–67 | 시작 시 1행 plot_profiles 함수 안. profilefighandle을 22로 둔다(56). 시간 단계가 plotinterval 배수이고 xyprofiles가 있으면 그린다(57). 프로파일 수에서 round(sqrt(np))와 ceil(np/nm)로 패널 행·열 수를 만든다(58–60). 현재 그림을 가져오고 22번 그림에 plot_figureproperties(900,900,32,800,50)를 적용한다(61–63). it_profile==0이면 clf한다(64–66). hs·hp를 clear한다(67). 원문: `FORMAT.profilefighandle=22;` (56), `if mod(TIME.it,FORMAT.plotinterval)==0 && ~isempty(O.xyprofiles)` (57), `np=size(O.c_profile,1);` (58), `nm=round(sqrt(np));` (59), `nn=ceil(np./nm);` (60), `hf=gcf;` (61), `figure(FORMAT.profilefighandle);` (62), `plot_figureproperties(FORMAT.profilefighandle,900,900,32,800,50);` (63), `if O.it_profile==0` (64), `clf;` (65), `clear hs hp` (67). |
| 68–77 | 시작 시 1행 plot_profiles 함수·57행 그림 조건 분기 안. 프로파일 루프에서 subplot을 만들고 시간별 해안 위치를 파란 점으로 그린다(68–71). DUNE.used이면 사구 위치를 빨간 점으로 그린다(72–74). 날짜 눈금과 프로파일 번호 제목을 붙인다(75–76). 원문: `for pp=1:np` (68), `hs(pp)=subplot(nm,nn,pp);` (69), `hp(pp,1)=plot(O.timenum_profile,O.c_profile(pp,:),'b.');` (70), `hold on;` (71), `if DUNE.used` (72), `hp(pp,2)=plot(O.timenum_profile,O.d_profile(pp,:),'r.');` (73), `datetick('x','dd-mm-yyyy');` (75), `ht=title(['profile ',num2str(pp)]);` (76). |
| 78–86 | 시작 시 1행 plot_profiles 함수·57행 그림 조건 분기 안. 마지막 축 위치를 보관하고 Coast·Dune 범례를 만든 뒤 위치를 복원한다(78–80). FORMAT.plotprofiles에 축·선 핸들을 저장한다(81). mainfighandle로 돌아간다(83). 분기·함수 종료(85–86). 원문: `pos0=get(gca,'Position');` (78), `hleg=legend([hp(pp,1),hp(pp,2)],{'Coast','Dune'},'Location','SouthOutside','Orientation','Horizontal');` (79), `set(gca,'Position',pos0);` (80), `FORMAT.plotprofiles={hs,hp};` (81), `figure(FORMAT.mainfighandle);` (83). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56: 입력 FORMAT.profilefighandle 값과 관계없이 22를 대입한다.
- 61: hf는 gcf 결과를 받지만 이후 이 함수에서 참조하지 않는다.
- 64: 초기 그림 지우기 조건은 O.it_profile==0이며 비교 결과를 모으는 별도 all·any 호출은 없다.
- 72–79: hp의 둘째 열은 DUNE.used 분기에서만 대입한다. 범례는 분기 밖에서 hp(pp,2)를 참조한다.
