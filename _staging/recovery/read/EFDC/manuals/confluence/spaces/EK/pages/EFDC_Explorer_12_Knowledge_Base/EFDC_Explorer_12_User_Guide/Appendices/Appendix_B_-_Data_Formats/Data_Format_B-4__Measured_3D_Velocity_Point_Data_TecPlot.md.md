---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-4__Measured_3D_Velocity_Point_Data_TecPlot.md
lines: 31
sha256: 476e57e799b9980ee85b4093c45946b016e12bf54b61eeaabf35b662a8234fa2
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-4__Measured_3D_Velocity_Point_Data_TecPlot.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–16 | Measured 3D Velocity Point Data (TecPlot) / 헤더 — 실측 3D 유속 점 자료(measured 3D velocity point data)의 예시 제목, 변수 열 목록과 ZONE 필드를 제시한다(10–15). 원문: `**Data Format B-4**  **Measured 3D Velocity Point Data (TecPlot).**   ` (10); `TITLE = "ADCP IJK Data"` (11); `VARIABLES = "X", "Y", "Z", "V\_E\_W", "V\_N\_S", "V\_U\_D"` (13); `ZONE I= 257, J=1, K=1,F=POINT, T="Avg Vel"` (15). |
| 17–31 | TecPlot 점 데이터 예시 — 여섯 열의 수치 데이터 줄과 생략 표시 및 빈 줄을 포함한다(17–31). 원문: `56730.14 906511.90 288.38 -0.0443 -0.1582 -0.0001` (17); `56731.96 906530.90 288.42 -0.0570 -0.1482 -0.0001` (19); `56730.98 906533.00 288.45 -0.0599 -0.1219 -0.0001` (21); `56731.46 906535.70 288.49 -0.0578 -0.1042 -0.0001` (23); `56733.52 906512.90 288.39 -0.0548 -0.1524 -0.0001` (25); `...` (27); `...` (29); `...` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13·17–25: 좌표와 유속 열의 단위 및 `V_E_W`, `V_N_S`, `V_U_D`의 양의 방향은 이 파일에 정의되어 있지 않다.
