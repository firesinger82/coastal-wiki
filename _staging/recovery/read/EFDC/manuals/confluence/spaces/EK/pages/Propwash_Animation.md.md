---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/Propwash_Animation.md
lines: 34
sha256: ebf4313c361fafa121e87cf1b8720a73d406f4ddd899de537c657b676156a61e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Propwash_Animation.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 ID, 제목, space, 원문 URL, 판본, 갱신 시각과 경로를 담은 frontmatter를 읽었다(1–9). |
| 10–17 | Ship Track / 애니메이션 레이어 — 움직이는 선박의 항적(ship track)과 선미 뒤 제트(jet) 영향을 집중해서 관찰하는 기능을 소개한다(10). 2DH View의 prop wash 그룹에 항적 레이어를 추가한다(12). 14행 그림 URL은 `unknown-attachment`이며 제목은 `Ship1.png`이다. 원문의 페이지 ID를 사용해 로컬 `attachments/2002223105/Ship1.png`를 열었다(14). 그림은 `Primary Group: PropWash`, `Parameter: Ship Track`, `Ship: C-TRACTOR 13`, `All` 선택, `Time Setting: 1.0000`, `Fixed` 해제와 `Add`를 보여 준다(14 그림). 뒤의 길고 얇은 직사각형 격자는 흰 셀 경계와 녹색 바닥 표고를 보여 준다. 범례는 `2020-01-02 00:00`, `Bottom Elevation (m)`, 양 끝 값 `-10`, `-10`을 표시한다(14 그림). |
| 18–23 | Set Focusing Objet / 선박 선택 — 항적 레이어를 활성화하고 선박을 우클릭하면 선박 정보와 빨간 항적을 표시한다고 적는다(18). 옵션 이름 원문: `Please select and turn the active mode of the ship track layer. RMC on the ship so the ship information will present and the track of the ship will be highlighted with the red line. Moreover, the option of Set Focusing Objet is available ( as shown in figure 2).` (18). 20행의 URL 제목은 `Ship2(1).png`이다. 규칙명 `attachments/2002223105/Ship2(1).png`는 없어서 해당 폴더를 `ls`로 확인했다. `ls`에서 확인한 파일 `Ship21.png`를 열었다(20). 그림은 수평 빨간 항적, 노란 `C-TRACTOR 13` 선박 표시와 노란 선박 정보 상자 및 `Ship Properties`, `Set Focusing Object`, `Unset Focusing Object` 메뉴를 보여 준다(20 그림). 선박 모양의 뾰족한 끝은 화면 왼쪽을 향한다. 좌표축·수식·축척 막대는 없다(20 그림). |
| 24–29 | 집중 항적 애니메이션 — 집중 대상으로 설정한 뒤 도구 모음의 `Animate`를 누르는 절차를 설명한다(24). 설정 적용 조건 원문: `Select the feature “ Set Focusing Objet” and click the Animate button in the main toolbar. Now the animation of the current ship track will be focused in the window, and the user can easily observe the shipping path and the jet impact behind the ship.` (24). 26행의 URL 제목을 사용해 로컬 `Ship3.png`를 열었다(26). `2020-01-02 00:30`에서 선박을 화면 중앙 가까이에 두고 오른쪽으로 넓어지는 부채꼴의 제트 점 격자를 보여 준다. 선박 바로 뒤 점은 붉고 바깥쪽 점은 청색 계열이다. 범례는 `Velocity (C-TRACTOR 13) (m/s)`, 하한 `0.000`, 상한 `0.863`을 표시한다(26 그림). 점 격자에는 방향 화살표와 수식이 없다. 본문은 이 범례 값을 모델 매개변수의 기본값으로 지정하지 않는다. |
| 30–34 | Unset Focusing Object / 집중 해제 — 해제 절차 원문: `After the animation, RMC and select “Unset Focusing Object“ to stop focusing.` (30). 32행은 20행과 같은 `Ship2(1).png` 제목의 placeholder URL을 사용한다. 로컬 `Ship21.png`를 다시 열었다(32). 이 그림은 선박 우클릭 메뉴의 `Unset Focusing Object`를 포함하며 `Set Focusing Object`도 함께 표시한다(32 그림). 마지막 `Unset Focusing Objet` 캡션까지 읽었다(34). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·20·26·32: 그림 URL은 모두 `/plugins/servlet/confluence/placeholder/unknown-attachment`이다. URL에는 `/download/attachments/<페이지ID>/<파일명>` 부분이 없어 지정된 URL 치환 규칙을 적용할 수 없다. 원문 frontmatter의 페이지 ID와 그림 제목으로 로컬 폴더를 확인했다.
- 20·32: 그림 제목은 `Ship2(1).png`이지만 첨부 폴더에 이 파일명은 없다. `ls`에서 확인한 로컬 파일명은 `Ship21.png`이며 두 참조 위치에서 이 파일을 열었다.
- 18·22·24·34: 본문과 일부 캡션은 `Objet`로 적는다. 로컬 그림 20·32행의 메뉴는 `Object`로 적는다.
