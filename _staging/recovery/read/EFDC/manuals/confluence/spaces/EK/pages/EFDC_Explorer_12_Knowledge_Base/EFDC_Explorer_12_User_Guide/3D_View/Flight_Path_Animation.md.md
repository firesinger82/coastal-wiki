---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/3D_View/Flight_Path_Animation.md
lines: 26
sha256: fa96a2b18a71b5529ad9e3560a84a76c205fa76e0086c5fbd6f0bf5cc9bd7370
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Flight_Path_Animation.md — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 문서 메타데이터 — 페이지 ID·제목·space·URL·판본·갱신 시각·문서 경로와 frontmatter 구분자를 포함한다(1–9). Flight Path Animation / 실행 버튼 — 3D View의 비행 경로(flight path) 애니메이션 도구와 주 도구 모음 접근 방법을 설명한다(10). Figure 1의 로컬 그림을 열었다(12–14). 그림은 비행 경로 버튼을 붉은 테두리로 표시한 도구 모음이다. 빈 줄·그림 마크업·캡션을 포함한다(11–15). |
| 16–26 | Flight Path Settings — 애니메이션 단계 수와 카메라 피치각(camera pitch angle)을 설정한다(16). 설정 이름·단위 원문: `In the Flight Path Animation form, the user can define *Numbers of Animation Steps* and the *Camera Pitch Angle (deg)* to record the animation.` (16). 2D View에서 폴리라인(polyline)을 그리거나 사용자 파일을 불러오고, 불러온 뒤 점 수·총길이를 자동 계산하며 Edit Height로 Z축 높이를 바꿀 수 있다(18). 적용 절차 원문: `The flight path can be created by [Draw Polyline in 2DView](/wiki/spaces/EK/pages/246546592/Overlays+and+Polyline+Tools) or the user is able to use their own file. Once the file is loaded the number of data point and total length will be calculated automatically ( as shown in [Figure 2](#Figure2)). It is possible to adjust the height of the polyline along Z-axis by clicking *Edit Height* button.` (18). Figure 2의 로컬 그림을 열었다(20–22). 그림은 Flight Path Animation 설정 화면이다. 화면 예시값은 `Number of Animation Steps: 100`, `Camera Pitch Angle (deg.): 10`, `Frame Rate: 24`, `Number of Data Points: 20`, `Total Length: 32959.5 m`이다(20행 그림). `Output to MP4 File`이 선택되고 `Output to AVI File`, `Show Flight Path`, `Smooth Flight Path`는 선택되지 않았다. 출력·경로 파일을 위한 `File Name` 입력란과 `Edit Height` 버튼이 보인다(20행 그림). 본문은 화면 예시값을 기본값으로 정의하지 않는다. 출력 조건 원문: `In addition, EEMS10 also supports the user to export the flight path animation to the AVI or MP4 file by checking the *Output to AVI File* or *Output to MP4 File* box and fill in a name in the *File Name* box ([Figure 2](#Figure2)).` (24). Animate 버튼으로 실행한다(26). 빈 줄·그림 마크업·캡션을 포함한다(17·19–25). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·18·24행의 그림 링크는 `#Figure1`·`#Figure2`를 가리킨다. 이 파일에는 해당 ID 선언이 없고 14·22행은 굵은 글씨 캡션이다.
- 8행의 문서 경로는 `EFDC+ Explorer 12 User Guide`를 포함한다. 24행은 `EEMS10`의 지원이라고 설명한다.
- 16행의 설정 이름은 `Numbers of Animation Steps`이다. 20행 그림의 이름은 `Number of Animation Steps`이다.
- 24행은 출력 형식을 고르는 컨트롤을 `box`라고 적는다. 20행 그림의 AVI/MP4 출력 형식 선택은 라디오 버튼이다.

