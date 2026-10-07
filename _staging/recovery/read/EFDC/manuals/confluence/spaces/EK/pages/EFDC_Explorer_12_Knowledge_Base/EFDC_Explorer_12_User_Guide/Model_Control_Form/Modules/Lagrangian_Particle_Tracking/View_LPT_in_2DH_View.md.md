---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Lagrangian_Particle_Tracking/View_LPT_in_2DH_View.md
lines: 95
sha256: de7118cfa82f1a79bdae971449f48d1abf9d9ea9d3d65ee28a2ee6b475a2b3be
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# View_LPT_in_2DH_View.md — 판독 구간 기록

구간은 1행부터 95행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID는 `246579597`이다(2). 제목은 `View LPT in 2DH View`이다(3). space, URL, version, 갱신 시각, 문서 계층과 frontmatter 구분자를 포함한다(1–9). |
| 10–20 | LPT 레이어 추가와 예제 격자 — 2차원 수평 보기(2DH View)에 라그랑주 입자 추적(Lagrangian Particle Tracking, LPT) 레이어를 추가하는 절차를 설명한다(10). 예제는 평탄한 저면과 동쪽 개방경계(open boundary), 남서쪽 유량경계(flow boundary), U 성분 마스크(U component masks)를 가진 직사각형 영역이다(12). 그림 1은 `Primary Group: LPT / Oilspill`, `Parameter: Particles` 선택 화면이다(14). 그림 2는 위아래 끝에서 번갈아 시작하는 검은 수직 마스크 사이에 왼쪽의 붉은 입자 다섯 개를 표시한다(18). 그림의 저면고(bottom elevation) 범례 양 끝은 `-4.960`이며 단위는 `m`이다(18). 오른쪽 경계의 곡선에는 축 눈금이 없다(18). 그림 URL, 캡션과 빈 줄을 포함한다(14–20). |
| 21–32 | 단일 층 예제의 입자 궤적 — 적용 조건 원문: `The model represents the vertical component as a depth-averaged system with one sigma layer. The depths of the five drifters are initialized at specified depths.` (21). 다섯 표류자(drifters)의 12시간 궤적을 제시한다(23). 원문: `Even though there was no vertical component, the tidal range is seen to result in changing particle elevations.` (25). 그림 3은 무작위 보행(random walk)이 없는 궤적이고 그림 4는 무작위 보행을 적용한 궤적이다(27–31). 두 그림의 `Day: 0.5000`에서 입자들은 마스크 끝을 돌아가는 궤적을 그린다(27, 30). 고도(elevation) 색 범례는 그림 3의 `-3.490`부터 `0.530`까지, 그림 4의 `-3.860`부터 `0.780`까지이다(27, 30). 격자 좌표 축과 궤적 진행 화살표는 표시하지 않는다(27, 30). |
| 33–54 | Options from RMC on the LPT layer / Properties·Zoom to Layer — 그림 5는 LPT 레이어의 오른쪽 클릭 메뉴를 표시한다(35–39). Properties는 입자의 색, 모양, 표시 시작·종료 시각을 설정한다(41). 그림 6은 General Options의 초기·최종 위치, 색 기준, 색 범위, 배경과 외곽선 설정 화면이다(45). 그림 7은 Particle Group Options의 그룹·초기/현재/영역 밖 위치, 가시성, 심벌 설정 화면이다(49). 화면에 표시된 값은 `Style: Circle` (49행 그림)과 `Size: 10.0 Pixels` (49행 그림)이다. Zoom to Layer는 선택 레이어에 맞춰 보기를 확대한다(53). 제목, 캡션과 빈 줄을 포함한다(33–54). |
| 55–64 | Export to / 특정 시각의 표류자 위치 — 특정 스냅숏(snapshot)의 위치를 텍스트 파일로 내보낸다(55). 원문: `file extension is \*.txt` (55); `By default, the file will be saved in the *#analysis* folder.` (55). 그림 8은 `Particles` 파일 저장 화면이다(57). 그림 9는 좌표 파일을 보여 준다(61). 그림의 열 이름은 `XLA YLA ZLA REL_Time END_Time GROUP L` (61행 그림)이다. 붉은 화살표는 `XLA`를 X 좌표, `YLA`를 Y 좌표, `ZLA`를 Z 고도, `REL_Time`과 `END_Time`을 방출·종료 시각, `GROUP`을 입자 그룹, `L`을 격자 셀 L 번호로 가리킨다(61). 스냅숏 시각은 `Julian time(Day): 0.199746581183464` (61행 그림)이다. 첫 완전한 데이터 행은 `153.120 239.580 -0.680 0.0420 1.0000 1 3598` (61행 그림)이다. 화면의 마지막 데이터 행 일부는 아래쪽에서 잘려 있다(61). |
| 65–74 | Export All Drifters to / 전체 출력 시각의 위치 — 모델 출력의 모든 시각에서 모든 표류자의 위치를 내보낸다(65). 원문: `file extension is \*.txt` (65); `By default, the file will be saved in the *#analysis* folder.` (65); `Julian time (Day) is the time column; X1 and Y1 are the coordinates of drifter 1, and Z1 is the depth of drifter 1, and so on.` (65). 그림 10은 `All drifters.txt` 저장 화면이다(67). 그림 11의 보이는 헤더는 `* Julian time(Day) X1 Y1 Z1 X2 Y2 Z2` (71행 그림)이다. 첫 데이터 행의 보이는 값은 `357.1036 526975.138 5036721.237 1.970 526970.098 5036724.987 2.880` (71행 그림)이다. 화면 마지막 행의 보이는 값은 `357.1834 527078.068 5037168.547 -2.880 526484.678 5037964.067 -2.980` (71행 그림)이다. 숫자 사이 간격은 그림의 열 구분을 공백으로 옮겼다(61, 71). |
| 75–82 | Edit·Remove — Edit는 2DH View Option을 연다(75). 그림 12는 시간과 궤적 표시 설정 화면이다(77). 선택 가능한 표시 항목은 `Display Entire Track to Current Time` (77행 그림); `Display Entire Track` (77행 그림); `Display Recent History` (77행 그림); `Current Position of Particle Only` (77행 그림)이다. Remove는 Layer Control에서 LPT 레이어를 삭제한다(81). 캡션과 빈 줄을 포함한다(79–82). |
| 83–95 | 선택한 표류자 내보내기 — Particles 레이어에서 커서를 켠 후 표류자를 선택하고 Export Selected Drifter를 사용한다(83). 저장 확장자와 기본 폴더 원문은 `file extension is \*.txt` (83); `By default, the file will be saved in the *#analysis* folder.` (83)이다. 이 파일은 표류자 하나의 기록이라는 점만 그림 11의 형식과 다르다(83). 그림 13은 `Particle ID: 24`와 내보내기 메뉴를 보여 준다(85). 그림 14는 `Export_Particle ID24.txt` 저장 화면이다(89). 그림 15의 헤더는 `* Julian time(Day) X1 Y1 Z1` (93행 그림)이다. 첫 완전한 데이터 행은 `357.1036 526679.678 5037606.497 2.800` (93행 그림)이고 마지막 완전한 데이터 행은 `357.1765 526436.648 5038486.717 1.070` (93행 그림)이다. 그림의 열 구분은 공백으로 옮겼다(93). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 65행·71행 그림: 본문은 `Z1`을 표류자 1의 깊이(depth)라고 부른다. 61행 그림의 주석은 `ZLA`를 `Z elevation`이라고 부른다. 이 문서는 두 Z 표기의 기준과 부호 관계를 정의하지 않는다.
- 83행·87행: 본문은 선택 표류자 내보내기 메뉴를 설명한다. 그림 13의 캡션은 `2DH View Option.`이다.
- 83행·91행: 본문은 선택 표류자 하나를 내보내는 절차를 설명한다. 그림 14의 캡션은 `Export all drifters.`이다.

