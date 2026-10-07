---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/2DH_View/Menu_and_Toolbar_Items/Harmonic_Analysis.md
lines: 28
sha256: 46afb75be26663527769d0fe436af8228228d0613cabda50c7c4bbc552964176
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Harmonic_Analysis.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 메타데이터 — 문서 ID, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(1–9). |
| 10–17 | 조화 분석(Harmonic Analysis) / 분조 선택 — 10행은 CSS 색상 규칙 마크업 뒤에 본문이 이어진다. 모델 출력 수위의 후처리(post-processing)로 분조(harmonic constituent)를 평가하며 메뉴 선택으로 CoTidal Chart를 연다(10). `Available Constituents`에서 오른쪽 화살표로 `Analyzing Constituents`에 추가하거나 `Search` 입력과 검색·추가 아이콘을 사용하며 주요 `4`, `8`, `11`개 분조의 바로가기 버튼도 제공한다(12). 추가를 끝내면 OK를 누른다(12). 12행의 오른쪽 화살표·검색 추가 아이콘과 그림 1을 직접 열었다(14–16). 그림 1의 시간 필드는 `From: 2009-03-06 00:00:00`, `To: 2009-06-04 00:00:00`이다. 사용 가능한 분조 목록에 보이는 이름·주기 원문은 `SL4 6.048 hrs`, `S4 6.000 hrs`, `SK4 5.992 hrs`, `2SMN4 5.946 hrs`, `3SM4 5.900 hrs`, `2SKM4 5.892 hrs`, `MNO5 5.044 hrs`, `3MK5 5.006 hrs`, `3MP5 5.000 hrs`, `M5 4.968 hrs`, `MNK5 4.968 hrs`, `2MP5 4.936 hrs`, `MSO5 4.936 hrs`, `3MO5 4.931 hrs`이다(14행 그림). 그림의 분석 목록은 비어 있으며 기간은 화면 예시 값이다. |
| 18–23 | 자료 길이 부족 — 모델 실행 기간 때문에 출력 수위의 자료 길이가 필요한 표준 길이에 미치지 못할 수 있으며 이 경우 오류가 나타난다고 적는다(18). 그림 2를 직접 열었다(20–22). 오류는 `Data length is not enough for the separation between P1`와 `and K1`을 표시하며 OK로 닫는다. 본문이나 그림은 필요한 길이의 수치를 제시하지 않는다. |
| 24–28 | 분조 제거와 분석 결과 — 반드시 창을 다시 열고 오류에 언급된 분조를 왼쪽 화살표로 제거한 뒤 OK를 눌러 진행해야 한다(24). 예시 이름 원문은 `P1 and K1 in this case`이다(24). 분석 후 Mean Level 레이어를 추가하며 오른쪽 클릭으로 평균 수위, 모델 출력 대비 분석 수위의 평균 제곱근 오차(Root Mean Square Error, RMSE), 각 분조의 위상(phase)·진폭(amplitude)을 선택한다(24). 24행 왼쪽 화살표와 그림 3을 직접 열었다(26–28). 그림 메뉴는 `Mean Level`, `RMSE`, `O1 Amplitude`, `O1 Phase`, `K1 Amplitude`, `K1 Phase`, `M2 Amplitude`, `M2 Phase`, `S2 Amplitude`, `S2 Phase`를 보여 준다. 평균 수위 범례는 `-1.240`부터 `6.305`, 단위 `(m)`이다(26행 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18–20: 자료 길이 부족을 설명하지만 분조 분리에 필요한 표준 길이의 수치와 계산식은 이 문서에 없다.
- 10·18·24: `#HarmonicAnalysis-Figure1`부터 `#HarmonicAnalysis-Figure3`까지의 링크가 있지만 이 Markdown 파일에는 해당 앵커 정의가 없다.
