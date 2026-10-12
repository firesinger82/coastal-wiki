---
file: models/ShorelineS/raw/source_code/shorelines/functions/make_video.m
lines: 66
sha256: 13f97ef4b2e9e73a8b563c2cd00e3c3bb5ca2685d5ef7c473900b15803851a8d
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# make_video.m — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 함수 시그니처(1). 입력 그림 프레임(frame)을 영상에 쓰는 설명(4). S.video는 0/1 사용 여부, outputdir는 출력 경로, diffraction·xhard·yhard·phiw0는 파일 이름 구성에 쓰는 입력이다(6–14). S 필드 기본값을 설정하는 문장은 이 함수에 없다. 원문: `function make_video(S,vi)` (1). |
| 16–43 | 시작 시 1행 make_video 함수 안. 2020년 저작권·연락처, LGPL 2.1 이상·무보증 안내와 빈 줄(16–43). |
| 44–57 | 시작 시 1행 make_video 함수 안. S.video가 참일 때만 처리한다(44). diffraction==1이면 구조물 좌표와 외해 방향으로 label을 만든다(46–47). 그 외에는 outputdir와 역슬래시 animation을 결합한다(49–50). 프레임률(frame rate) FR은 10이다(52). outputdir가 없으면 mkdir를 호출한다(54–56). 원문: `if S.video` (44), `if  S.diffraction==1` (46), `label=strcat('xhrd_',num2str(S.xhard),'_yhrd_',num2str(S.yhard),'_phi0_',num2str(S.phiw0));` (47), `else` (49), `label=[S.outputdir,'\animation'];` (50), `FR=10;` (52), `if ~exist(S.outputdir,'dir')` (54), `mkdir(S.outputdir);` (55). |
| 58–66 | 시작 시 1행 make_video 함수·44행 S.video 분기 안. Motion JPEG AVI 형식의 VideoWriter를 만들고 FrameRate를 FR로 둔다(58–59). open 후 try 안에서 writeVideo(video,vi)를 호출한다(60–63). close(video)는 try 밖에서 호출한다(64). 분기·함수 종료(65–66). 이 판독에서는 영상 생성 코드를 실행하지 않았다. 원문: `video=VideoWriter(label,'Motion JPEG AVI'); % for surfsara runs` (58), `video.FrameRate=FR;` (59), `open(video)` (60), `try` (61), `writeVideo(video,vi)` (62), `close(video)` (64). [10-12 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50: 비회절 경로의 label은 역슬래시를 포함한 animation 경로를 사용한다.
- 47·54–58: diffraction==1 경로의 label은 S.outputdir를 포함하지 않는다. 디렉터리 존재 검사는 S.outputdir에 대해 수행한다.
- 61–63: writeVideo를 감싼 try에는 catch 절이 없다.
