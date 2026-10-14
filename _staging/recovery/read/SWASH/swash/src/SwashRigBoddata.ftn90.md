---
file: models/SWASH/raw/source_code/swash/src/SwashRigBoddata.ftn90
lines: 153
sha256: 149ca24eca16dee4c39758b857c7cd029e894e60cdbe12958baaccb4424b2d53
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashRigBoddata.ftn90 — 판독 구간 기록

구간은 1행부터 153행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 모듈 SwashRigBoddata를 시작한다(1). 기관·저작권·GPL 3 이상·무보증 머리말(3–27). Marcel Zijlema의 2022년 10월 신규 모듈이라는 갱신 기록이다(30–36). 강체(rigid body) 계산의 속성 데이터를 보유하며 사용 모듈은 없다는 주석이다(38–48). |
| 50–74 | 시작 시 1행 SwashRigBoddata 모듈 안. implicit none을 적용한다(50). 강체 운동 차원 ndim의 고정값은 3이다(54). 강체 수 mbod, 시간적분법(time integration) mfoti, 최대 방현재(fender) 수 mxfen, 최대 계류선(mooring line) 수 mxmli를 선언한다(58–65). mfoti 주석의 선택값은 1=Newmark, 2=Chung–Hulbert, 3=Hilber–Hughes–Taylor, 4=Wood–Bossak–Zienkiewicz이다(59–63). 힘·관성에 대한 generalized-alpha 계수 alfaf·alfam은 내부에서 결정한다는 주석이다(67–70). 강체별 방현재·계류선 수 배열 nfeb·nmlb는 save·allocatable이다(72–73). 원문: `integer, parameter                           :: ndim = 3 ! number of dimensions related to body motions` (54). alfaf와 alfam은 고주파 모드의 증폭을 제어하는 암시성 계수이다(67–70). [10-15 전수 검증 보완] |
| 75–104 | 시작 시 1행 모듈 안. 수선면적(water plane area) barea, 부심(center of buoyancy) bcob, 무게중심(center of gravity) bcog, 질량 bmass, 단면 이차모멘트(second moment of area) bmoax·bmoay, 관성모멘트(moment of inertia) bmoi, 잠긴 체적 bvol을 선언한다(75–98). bfen의 세 번째 첨자는 1=스프링 계수, 2..4=무게중심 기준 부착점 x·y·z라는 주석이다(78–82). bmli의 세 번째 첨자는 1=스프링, 2=감쇠, 3..5=바닥 부착점, 6..8=강체 부착점, 9=평형 길이, 10=초기장력(pretension) 계수이다(84–94). 이전·현재 계류선 신장량 extml0·extml1과 동력인출장치(power take-off, PTO)의 출력 ptop을 선언한다(100–103). 모든 배열은 save·allocatable이며 이 구간에는 할당·초기화 실행문이 없다. bcob는 평형 위치에 대한 부심이다(76). bcog는 문제 좌표계에 대한 무게중심이다(77). bmli의 바닥 부착점 3..5와 강체 부착점 6..8은 모두 무게중심 기준이다(87–92). bmoax와 bmoay의 기준축은 각각 x축과 y축이다(95–96). bmoi는 회전축 기준이다(97). [10-15 전수 검증 보완] |
| 105–127 | 시작 시 1행 모듈 안. 이전·현재 시간의 각가속도 afor0/1, 선형가속도 afot0/1, 스프링·감쇠력 fbod0/1, 유체력(hydrodynamic force) fhyd0/1, 스프링·감쇠 토크 tbod0/1, 유체 토크 thyd0/1, 각속도 vfor0/1, 선형속도 vfot0/1, 각변위 xfor0/1, 선형변위 xfot0/1을 save·allocatable 2차원 배열로 선언한다(105–125). 유체·구조 상호작용(fluid-structure interaction) 반복 과정의 중간 각변위 xfori와 선형변위 xfoti도 선언한다(123·126). |
| 128–153 | 시작 시 1행 모듈 안. 자유도(degree of freedom) 사용 여부 bdof는 논리형 save·allocatable 3차원 배열이다(128). 주석은 bdof(:,1..3,1)=surge·sway·heave, bdof(:,1..3,2)=roll·pitch·yaw로 대응시킨다(129–135). 계류선 초기장력 사용 여부 cpto를 선언한다(136). ribdat 형식은 label, nfen/nmli, parm(7), pret, dof(6), fen/mli 배열 포인터와 연결목록 포인터 nextrib을 보유한다(138–147). save·target frigbod를 선언하고 모듈을 종료한다(149–153). 루틴·조건·계산 실행문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 138–149: ribdat의 fen·mli·nextrib 포인터 선언에는 => null() 초기화가 없다. 이 파일에는 해당 포인터를 초기화하는 실행문도 없다.
