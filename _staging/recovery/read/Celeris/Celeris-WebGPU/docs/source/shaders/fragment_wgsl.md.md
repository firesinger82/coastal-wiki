---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/fragment_wgsl.md
lines: 41
sha256: ee0e3151dd8440b6c3c6cf1d0942c44418dc094a8010469579c12aa3e90c97b3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fragment_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/fragment.wgsl`

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 원문 링크와 `2D`·`3D`의 주 과학/실사 표시·합성 역할이다(1–7). `Handler_Render.js` 바인드 그룹(bind group)에서 물 상태·바닥·평균·파고·baseline, 마찰·퇴적물·침식·변위, 설계, 지도·색상 막대, 관측 위치·쇄파, 난류/화살표/설계 PNG 배열, 반정밀도 `txRenderVarsf16`을 읽는다(11–19). |
| 21–28 | `surfaceToPlot`은 수면·속력·속도·와도·쇄파·지형·평균·RMS/유의파고·baseline 차이·마찰·최대 eta·퇴적물 농도/침식/가용 깊이/변위·설계·평균 와도를 고른다(23). waves 색상표는 절차적 단파 거칠기·조명·난류·와도/퇴적물 plume·지도/육지·설계 텍스처(texture)의 실사형 물 모드로 전환한다(27). 실사형 모드는 난류 텍스처로 변조하고 와도/퇴적물 plume으로 색을 입힌다(27). [11-04 전수 검증 보완] |
| 29–41 | overlay는 `showBreaking`별 거품/추적자, 배열 속도 화살표, render uniform의 선형 구조 끝점·선, 시계열 점·윤곽, `txDraw`의 색상 막대·눈금·이름·로고다(31–37). preview 점과 선은 관측점과 같은 종횡비 보정 UV 거리를 쓴다(35). `Copytxf32_txf16.wgsl`, `Handler_Render.js`, UI 이름에 결합하며 표면 모드 번호는 JavaScript와 공유하는 API다(41). 선은 보정된 좌표 공간에서 distance-to-segment 검사를 수행한다(35). `txDraw`는 colorbar 배경도 제공한다(37). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
