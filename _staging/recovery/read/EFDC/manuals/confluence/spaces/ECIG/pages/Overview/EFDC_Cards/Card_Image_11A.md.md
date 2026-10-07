---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_11A.md
lines: 41
sha256: b512f9335a5686b5ebc4567c68ff2661fe543ba3c147a4daad38425b43fbb838
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_11A.md — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–19 | C11A TWO-LAYER MOMENTUM FLUX AND CURVATURE ACCELERATION CORRECTION FACTORS / 적용 조건·옵션 — 두 층 운동량 플럭스(momentum flux)와 곡률 가속도(curvature acceleration)의 보정 절 제목을 적는다(10). 두 시간 레벨 해법(two time level solution) 및 `ISDRY=0` 조건과 아직 참인지 확인하라는 메모를 함께 적는다(12). `ICK2COR`의 0·1·2 옵션을 설명한다(14–18). 적용 조건과 옵션 원문: `\* (ONLY USED FOR 2 TIME LEVEL SOLUTION & ISDRY=0 PMC-Check to see if still true)` (12); `\* ICK2COR: 0 NO CORRECTION` (14); `\* ICK2COR: 1 CORRECTION USING CK2UUC,CK2VVC,CK2UVC FOR CURVATURE` (16); `\* ICK2COR: 2 CORRECTION USING CK2FCX,CK2FCY FOR CURVATURE` (18). 빈 줄을 포함한다. |
| 20–37 | C11A / 보정 계수 — 운동량 플럭스 보정 계수 세 개, 비활성이라고 적힌 곡률 가속도 보정 계수 세 개와 X·Y 방정식 보정 계수를 설명한다(20–34). 설명에서 `CK2UUM`, `CK2VVM`, `CK2UVM` 모두 `UU MOMENTUM FLUX`로 적힌 표현을 유지했다. 계수·비활성 조건 원문: `\* CK2UUM: CORRECTION FOR UU MOMENTUM FLUX` (20); `\* CK2VVM: CORRECTION FOR UU MOMENTUM FLUX` (22); `\* CK2UVM: CORRECTION FOR UU MOMENTUM FLUX` (24); `\* CK2UUC: CORRECTION FOR UU CURVATURE ACCELERATION (NOT ACTIVE)` (26); `\* CK2VVC: CORRECTION FOR VV CURVATURE ACCELERATION (NOT ACTIVE)` (28); `\* CK2UVC: CORRECTION FOR UV CURVATURE ACCELERATION (NOT ACTIVE)` (30); `\* CK2FCX: CORRECTION FOR X EQUATION CURVATURE ACCELERATION` (32); `\* CK2FCY: CORRECTION FOR Y EQUATION CURVATURE ACCELERATION` (34). 주석용 `\*` 줄과 빈 줄을 포함한다(35–37). |
| 38–41 | C11A / 입력 예시 표 — 빈 표 첫 행, 구분 행, 옵션·계수 헤더 및 입력 예시를 포함한다(38–41). 첫 옵션 값은 0이며 뒤의 여덟 계수 값은 모두 0.0825이다(41). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C11A \| ICK2COR \| CK2UUM \| CK2VVM \| CK2UVM \| CK2UUC \| CK2VVC \| CK2UVC \| CK2FCX \| CK2FCY \|` (40); `\|  \| 0 \| 0.0825 \| 0.0825 \| 0.0825 \| 0.0825 \| 0.0825 \| 0.0825 \| 0.0825 \| 0.0825 \|` (41). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12행: 적용 조건 옆에 `PMC-Check to see if still true`라는 확인 메모가 남아 있다. 이 파일에는 `ISDRY`의 정의가 없다.
- 20·22·24행: `CK2UUM`, `CK2VVM`, `CK2UVM`의 설명이 모두 `CORRECTION FOR UU MOMENTUM FLUX`이다.
- 16·26–30행: `ICK2COR: 1`은 `CK2UUC,CK2VVC,CK2UVC`를 사용하는 보정이라고 적는다. 뒤의 세 계수 설명은 각각 `(NOT ACTIVE)`를 적는다.

