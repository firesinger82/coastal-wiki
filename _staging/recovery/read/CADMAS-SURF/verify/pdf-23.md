# CADMAS-AGENT Manual p.19–30 전수 대조

대조일은 2026-11-04이다.
대조 대상은 `CADMAS-AGENT_Manual_English.pdf`의 PDF 쪽 번호 p.19–30이다.
이 범위의 인쇄 쪽 번호는 18–29이다.
기록 파일은 [p019-030.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/AGENT/Manual/CADMAS-AGENT_Manual_English.pdf/p019-030.md)이다.
대조한 쪽 수는 12쪽이다.
고친 쪽 수는 7쪽이다.
정정한 쪽은 p.25, p.26, p.28이다.
보완한 쪽은 p.22, p.23, p.29, p.30이다.
일치한 쪽은 p.19, p.20, p.21, p.24, p.27이다.
마지막 집계의 단위는 쪽이다.

사용자가 지정한 `cad-agent-manual-019.png`부터 `cad-agent-manual-030.png`까지 모두 이미지 보기 도구로 직접 열었다.
PNG 경로의 공통 디렉터리는 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/cadpages/`이다.
p.27–30은 원래 해상도로 확대해서 확인했다.
p.27–29의 수식 첨자와 부호를 확인했다.
p.30의 일본어 문구와 흐름도 연결선을 확인했다.
텍스트 추출본과 Marker 초안은 철자와 기존 OCR 차이 기록을 확인하는 데만 사용했다.

| 쪽 | 이전 | 새 | 근거 |
|---|---|---|---|
| p.22 | 시간 적분(time integration)의 단계 수와 시각을 설명한다. | [보완] 시간 적분(time integration)의 단계 수와 시각을 설명한다.<br>본문 인용: `Table 6-5 shows the modules varibles about time integration defined in m_timectl.`<br>본문은 `m_timectl`에 정의한 시간 적분 변수를 `Table 6-5`에 제시한다고 설명한다. | p.22 §6.1.4 첫 문장에 표 참조와 모듈 정의가 있다. `varibles`는 인쇄 철자이다. |
| p.23 | 쓰나미 침수(tsunami inundation)를 회피하는 경로 탐색용 자료 경로를 설명한다. | [보완] 쓰나미 침수(tsunami inundation)를 회피하는 경로 탐색용 자료 경로를 설명한다.<br>§6.1.7 본문 인용: `Table 6-6 shows module variables about tsunami inundation aboiding route searching method defined in m_danger.` | p.23 §6.1.7 본문의 `aboiding` 철자와 `m_danger` 정의 문장을 추가했다. |
| p.23 | §6.1.8의 제목은 `m_prob`를 쓰지만 본문은 `m_output`을 쓴다. | [보완] §6.1.8의 제목은 `m_prob`를 쓰지만 본문은 `m_output`을 쓴다.<br>§6.1.8 본문 인용: `Table 6-6 shows module variables about tsunami inundation avoiding route searching method defined in m_output.` | p.23 §6.1.8 본문 전체를 인쇄대로 추가했다. |
| p.25 | §6.2의 처리 흐름도 앞부분이다. | [정정] 앞 쪽에서 이어지는 절 §6.2 `Subroutine description and process flow`의 처리 흐름도 앞부분이다.<br>이 쪽에는 절 제목이 인쇄되어 있지 않다. | p.25에는 흐름도만 있다. §6.2 제목은 p.24에 있다. |
| p.26 | §6.2의 처리 흐름도 뒷부분이다. | [정정] 앞 쪽에서 이어지는 절 §6.2 `Subroutine description and process flow`의 처리 흐름도 뒷부분이다.<br>이 쪽에는 절 제목이 인쇄되어 있지 않다. | p.26에는 흐름도 뒷부분과 Figure 6-1 캡션이 있다. §6.2 제목은 p.24에 있다. |
| p.28 | $u_{shelter}(i,j)=\frac{-1}{r(i,j)}\tag{7-3}$ | [정정] $u_{shelter}(i,j)=-1/r(i,j)\tag{7-3}$ | p.28 식 (7-3)은 가로 분수선이 아닌 사선 분수이다. 음수 부호와 식 번호는 유지했다. |
| p.29 | §7.2 `Signpost model`. | [보완] §7.2 `Signpost model`.<br>본문은 도로 표지의 효과를 도입했다고 설명한다. | p.29 §7.2 첫 문장 `We have introduced the effect of road signs.`의 한국어 요지를 추가했다. |
| p.29 | 그림 출처로 `Sakata, Y., | [보완] 그림 출처로 `2. Sakata, Y., | p.29 §7.4 그림 출처의 저자명 앞에는 `2.`가 인쇄되어 있다. |
| p.30 | §7.4에서 이어지는 그림 캡션: | [보완] 앞 쪽에서 이어지는 절 §7.4 `Model of searching route avoiding tsunami inundation`의 그림이다.<br>이 쪽에는 §7.4 제목이 인쇄되어 있지 않다.<br>그림 캡션: | p.30 맨 위 그림은 p.29 §7.4에서 이어진다. 해당 절 제목은 p.30에 없다. |
| p.30 | `予想津波到達時間読み込み`는 “예상 쓰나미 도달 시각 읽기”라는 뜻이다. | [보완] `予想津波到達時間読み込み`는 “예상 쓰나미 도달 시각 읽기”라는 뜻이다.<br>포텐셜장 생성에서 피난자 위치 읽기로 내려가는 화살표가 있다.<br>피난자 위치 읽기에서 예상 쓰나미 도달 시각 읽기로 내려가는 화살표가 있다.<br>예상 쓰나미 도달 시각 읽기에서 쓰나미를 만나지 않는 경우와 만나는 경우로 화살표가 갈라진다. | p.30 Figure 7-1 상단 생성 단계부터 두 경우로 갈라지는 연결선이 있다. |
| p.30 | 그림의 마지막 `津波に遭遇しない避難経路の決定`은 “쓰나미를 만나지 않는 피난 경로 결정”이라는 뜻이다. | [보완] 그림의 마지막 `津波に遭遇しない避難経路の決定`은 “쓰나미를 만나지 않는 피난 경로 결정”이라는 뜻이다.<br>`避難所に到達`에서 마지막 피난 경로 결정 상자로 내려가는 화살표가 있다. | p.30 Figure 7-1의 피난소 도달 상자에서 최종 결정 상자로 연결된다. |
| p.30 | 본문 인용: `A model of searching route with low tsunami arrived probability was introduced.`(p.30) | [보완] 본문 인용: `A model of searching route with low tsunami arrived probability was introduced.`(p.30)<br>본문은 쓰나미 도달 확률이 낮은 경로를 탐색하는 모델을 도입했다고 설명한다.<br>본문은 `Figure 7-2 shows model flow`라고 설명한다. | p.30 §7.5 본문의 모델 도입 요지와 Figure 7-2 참조 문장을 추가했다. |

일치한 p.19–21의 표는 각 행의 변수 이름, 자료형, 차원, 설명과 명시된 단위를 대조했다.
일치한 p.24의 표는 서브루틴 이름과 설명을 대조했다.
일치한 p.27은 모든 본문 문단, 식 (7-1)과 식 (7-2), 기호 정의를 대조했다.
보완한 p.22–23의 표 값은 원래 기록을 유지했다.
p.23의 일본어 설명은 원문 인용과 한국어 뜻을 대조했다.
p.25–26의 흐름도 루틴 이름과 열 위치는 원래 기록을 유지했다.
p.28의 식 (7-4)는 합 상한이 없는 인쇄를 유지했다.
p.29의 식 (7-5)와 정규분포의 평균·표준편차 기호는 원래 기록을 유지했다.
p.30의 일본어 블록 이름과 영어 블록 이름은 원래 기록을 유지했다.
원문의 표 참조 불일치와 철자 차이는 기록 끝의 “판독 중 확인된 사실”에 적었다.
열지 못한 이미지는 없다.
기록 표의 쪽 행 수는 수정 전후 모두 12개이다.
기존 frontmatter는 보존했다.
frontmatter에는 요청한 `verified_by` 한 줄만 추가했다.
지정한 두 파일만 썼다.
git 명령은 실행하지 않았다.

정정 3, 보완 4, 일치 5
