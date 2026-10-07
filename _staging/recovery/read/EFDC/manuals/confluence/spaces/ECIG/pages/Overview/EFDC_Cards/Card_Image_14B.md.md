---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_14B.md
lines: 38
sha256: 6d1c406e7d6c079c5872f58d7982affd34525fd9564dbfbc0b8065e93393d845
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_14B.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–23 | C14B WIND WAVE PARAMETERS (ISWAVE=1/2/4) / 응력·소산·길이 규모 — 바람 파랑(wind wave) 매개변수의 적용 조건을 제목에 적는다(10). 응력의 회전 성분(rotational component)·비회전 성분(irrotational component) 포함, 연직 TKE 폐쇄에 공급하는 파랑 소산(wave dissipation) 비율, 수심과 `SQRT(dxdy)`를 수평 SSG 와점성 길이 규모(eddy viscosity length scale)에 쓰는 가중치(weight)를 설명한다(14–22). 매개변수·조건·표현 원문: `C14B WIND WAVE PARAMETERS (ISWAVE=1/2/4)` (10); `\* ISWRSR = 1 Activates inclusion of Rotational component of rad stress` (14); `\* ISWRSI = 1 Activates inclusion of Irrotational component of rad stress` (16); `\* WVDISV = Fraction of Wave Dissipation as source in vertical TKE closure` (18); `\* WVLSH = Weight for depth as the horiz SSG eddy viscosity length scale` (20); `\* WVLSX = Weight for SQRT(dxdy) as the horiz SSG eddy vis length scale` (22). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 24–35 | C14B / 수송·파장·점진 도입·이동 저면·진단 — 질량 수송(mass transport)의 비발산(nondivergent) 파랑 스토크스 표류(Stokes drift), 파장(wave length) 계산 선택, 파랑 강제력의 점진 도입 시간 단계(time steps) 수, 이동 저면(moving bed) 효과와 유효 파랑 변수 진단 출력을 설명한다(24–32). 각 항목의 `ISWAVE` 적용 조건을 유지했다. 매개변수·조건 원문: `\* ISWVSD = 1 Include nondiverg wave stokes drift in mass transport` (24); `\* WVLCAL = 1 Calucate wave length; 0: No calculation (ISWAVE=1/2)` (26); `\* NTSWV = Number of time steps for gradual introduction of wave forcing (ISWAVE=2/4)` (28); `\* ISWCBL = 2 taking moving bed effect; 0 No effect (ISWAVE=2/4)` (30); `\* ISDZBR = Write diagnostics for variable of effective waves(ISWAVE=1)` (32). 주석용 `\*` 줄과 빈 줄을 포함한다(33–35). |
| 36–38 | C14B / 입력 예시 — 열 개 필드의 입력 헤더와 수치 예시를 적는다(36·38). 예시를 기본값으로 표시하지 않았다. 입력 줄 원문: `C14B      ISWRSR     ISWRSI      WVDISV      WVLSH      WVLSX     ISWVSD      WVLCAL     NTSWV      ISWCBL     ISDZBR` (36); `                    1               1                 1                 .1              .1               0                0               200             0                0` (38). 빈 줄을 포함한다(37). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 10·18–22·26–32행: 이 파일에는 조건·설명에 쓰인 `ISWAVE`, `TKE`, `SSG`, `dxdy`의 정의가 없다.

