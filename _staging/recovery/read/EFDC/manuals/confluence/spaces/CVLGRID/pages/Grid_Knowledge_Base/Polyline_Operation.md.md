---
file: models/EFDC/raw/manuals/confluence/spaces/CVLGRID/pages/Grid_Knowledge_Base/Polyline_Operation.md
lines: 68
sha256: 9c5630aff25e7f35ed566117fd1caf6e2cde0e7d318b50dc287c6c32f3b3b780
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Polyline_Operation.md — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 제목 `Polyline Operation`, space `CVLGRID`, 원문 URL, 버전과 갱신 시각을 담는다(2–8). |
| 10–29 | 폴리라인(polyline) RMC 기능 — Overlay 레이어와 선을 선택하면 빨간색으로 강조하며 RMC에서 명령을 연다(10). Properties는 속성 창을 연다(12). Translate는 각 점의 X·Y에 값을 더해 이동한다(14). 입력 예제·단위 원문: `enter two values in meters in the form (e.g -100,50) then click the *OK* button, the polyline will be shifted.` (14). Rotate는 회전한다(16). 조건 원문: `enter a rotation angle in degree in the form then click the *OK* button, the polyline will be rotated. The rotation angle can be a positive or negative value.` (16). Copy to a Spline Layer는 `<New Layer>` 또는 기존 스플라인(spline) 레이어를 선택하여 복사한다(18). Break Polyline은 두 선으로 분리하고, Delete Segment는 한 구간을, Delete Polyline은 전체 선을 지운다(20–24). Delete Grid Elevations는 선 내부 절점의 고도를 제거하며 Interpolate Grid Elevations는 그 고도를 보간한다(26–28). |
| 30–49 | 폴리라인 속성·변환 화면 — 그림 1–5를 모두 열었다(30·34·38·42·46). 그림 1은 빨간 선택 선과 RMC 메뉴를 보여 준다(30). 그림 2에는 `Name`, `Show Line`, `Style: Solid`, `Color`, `Width: 1.0`, `Close Polygon`, `Smooth` 및 Data Points·Labels·Distance Labeling 탭이 보인다(34). 그림 3은 `Enter Translation Distances (m):` 입력 `0.000, 0.000`, 그림 4는 `Enter Rotation Angle (°):` 입력 `30`을 보여 준다(38·42). 그림 5의 `Select Layer`에는 `<New Layer>`와 `Spline 001`이 보인다(46). 이 값들은 화면 표시값이며 본문은 기본값으로 정의하지 않는다. |
| 50–57 | Delete Grid Elevations 절차 — Show Labels/Bottom Elevation으로 절점 고도를 표시한다(52). 격자 위에 선을 그리고 선을 LMC로 선택한 뒤 격자 레이어도 LMC로 선택하고 선 근처에서 RMC 메뉴를 연다(54). 표시를 갱신하면 선 내부 절점 고도가 삭제되어 `NaN` 레이블로 보인다고 적는다(56). |
| 58–68 | 고도 삭제 전후 격자 — 그림 6–8을 열었다(58·62·66). 그림 6의 곡선 격자에는 `15.000`, `10.000`, `14.000` 고도 레이블이 행을 따라 반복된다(58). 그림 7은 위쪽이 열린 빨간 선과 Delete Grid Elevations 메뉴를 보여 준다(62). 그림 8은 선 내부의 여러 레이블이 `NaN`으로 바뀌고 바깥의 `15.000`, `10.000`, `14.000`이 남은 화면과 Bottom Elevation 표시 메뉴를 보여 준다(66). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·12·14·16·18·52·54·56행: `#PolylineOperation-Figure1` 등의 fragment를 참조하지만, 이 Markdown에는 같은 이름의 명시적 앵커가 없다.
- 30·32행: 그림 1은 폴리라인 RMC 메뉴를 보여 주지만 캡션은 `Draw splines procedure`이다.
- 24행: 삭제 명령 표기의 강조 마크업이 `*Delete *Polyline**`로 적혀 있다.

