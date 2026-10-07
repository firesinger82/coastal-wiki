---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-20__SEDZLJ_Input_Files_BED.md
lines: 62
sha256: 35ff4fcc9265b3c468797c79714d05633ae6dd8063aabdfd29414a737fe3a04d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-20__SEDZLJ_Input_Files_BED.md — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–23 | BED.SDF 제어 필드 — 제목, 제어 매개변수 줄, 배열 매개변수 줄과 예시 값을 제시한다(10–18). 표면 거칠기(surface roughness)와 일정 전단응력(constant shear stress) 설정의 조건·단위는 원문 헤더에 있다(20). 해당 예시 데이터 줄도 포함한다(22). 원문: `**Data Format B-20  SEDZLJ Input Files: BED.SDF**` (10); `# VAR\_BED Bedload  Nequil LAYMAX  ISEDTIME  IMORPH IFWAVE MAXDEPLIM#` (12); `     1                    1            0             7               1                 0               0             1.0` (14); `# ITBM NSICM  Array Parameters #` (16); `    8     8` (18); `# ZBSKIN (>0 sets Zo in [um]) TAUCONST [dynes/cm^2] (> 0 to set constant)  ISSLOPE #` (20); `    10.0  0.0   0` (22). |
| 24–43 | BED.SDF 입경과 임계 전단응력 — 입경 등급(size class)의 D50, 침식(erosion)과 부유(suspension)의 임계 전단응력(critical shear stress), 하상 입경 표 및 하상 표면 침식의 임계 전단응력 예시를 제시한다(24–42). 각 헤더의 단위와 값은 다음과 같다. 원문: `# D50 of Size Class D50(K) [um] #` (24); ` 10.0  22.0  222.0  375.0  750.0  4000.0  22.0  222.0` (26); ` # Critical Shear for Erosion TAUCRS(K) [dynes/cm^2] #` (28); ` 1.0   2.2   1.6    2.4    3.8    30.8    2.2   1.6` (30); `# Critical Shear for Suspension TCRDPS(K) [dynes/cm^2] #` (32); ` 1.0   2.2   2.4    3.5    12.5   98.8    2.2   2.4` (34); `# Sediment Bed Size (um) Tables #` (36); ` 2.0  222.0  432.0  1020.0  2400.0  2600.0  3360.0  6000.0  8520.0` (38); `# Critical Shear for Erosion of Bed Surface [dynes/cm^2]  #` (40); ` 0.50  2.27   2.96    4.17    5.88    6.07    6.72    8.48    9.75` (42). |
| 44–62 | BED.SDF 침식률 — 활성층(active layer)과 퇴적층(deposited layer)의 침식률(erosion rate) 단위를 적는다(44). 입경 주석이 붙은 각 데이터 줄과 사이의 빈 줄을 포함한다(46–62). 원문: `#  Erosion rates for active and deposited Layers [cm/s] #` (44); ` 1.00E-09 5.97E-05 5.97E-04 5.96E-03 5.95E-02 5.94E-01 5.94E+00 5.93E+01 !    2 Micron` (46); ` 1.00E-09 5.97E-05 5.97E-04 5.96E-03 5.95E-02 5.94E-01 5.94E+00 5.93E+01 !  222 Micron` (48); ` 1.00E-09 3.65E-04 2.16E-03 1.27E-02 7.49E-02 4.42E-01 2.61E+00 1.54E+01 !  432 Micron` (50); ` 1.00E-09 2.01E-04 1.14E-03 6.51E-03 3.71E-02 2.11E-01 1.20E+00 6.85E+00 ! 1020 Micron` (52); ` 1.00E-09 1.12E-05 8.40E-05 6.28E-04 4.70E-03 3.51E-02 2.63E-01 1.96E+00 ! 2400 Micron` (54); ` 1.00E-09 7.94E-06 6.01E-05 4.55E-04 3.45E-03 2.61E-02 1.98E-01 1.50E+00 ! 2600 Micron` (56); ` 1.00E-09 2.11E-06 1.67E-05 1.31E-04 1.04E-03 8.17E-03 6.44E-02 5.08E-01 ! 3360 Micron` (58); ` 1.00E-09 2.03E-08 1.67E-07 1.44E-06 1.24E-05 1.07E-04 9.28E-04 8.02E-03 ! 6000 Micron` (60); `1.00E-09 1.19E-09 2.75E-09 1.69E-08 1.47E-07 1.33E-06 1.22E-05 1.11E-04 ! 8250 micron` (62). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 38·62: 하상 입경 표의 마지막 값은 `8520.0`이고 마지막 침식률 줄의 주석은 `8250 micron`이다.
- 12–22: `VAR_BED`, `Bedload`, `Nequil`, `LAYMAX`, `ISEDTIME`, `IMORPH`, `IFWAVE`, `MAXDEPLIM`, `ITBM`, `NSICM`, `ISSLOPE`의 의미와 허용 범위는 이 파일에 별도로 정의되어 있지 않다.
