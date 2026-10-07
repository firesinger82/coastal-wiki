---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_71.md
lines: 50
sha256: e2979c19cea73cfab1d51293e28894643e1667e3cd43c081aecb2016996a98e5
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_71.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 원문 메타데이터(frontmatter) — 문서 ID·제목·space·URL·버전·갱신 시각·계층 경로를 적는다(1–9). |
| 10–34 | C71 CONTROLS FOR HORIZONTAL PLANE SCALAR FIELD CONTOURING - RESIDUAL ONLY — 잔차(residual) 전용 수평면 스칼라장 등치선(scalar field contouring) 출력을 설명한다(10). 두 매개변수는 미사용이라고 적는다(14·18). 잔차 스칼라 변수 파일의 출력 조건과 파일에 기록할 I·J·X·Y 좌표의 옵션을 제시한다(20·24–28). 일곱 변수에 대해 데이터 행을 일곱 번 반복한다고 적는다(32). 주석 표식과 빈 줄을 포함한다(11–34). 원문: `C71 CONTROLS FOR HORIZONTAL PLANE SCALAR FIELD CONTOURING - RESIDUAL ONLY` (10); `\* ISSPH: NOT USED` (14); `\* NPSPH: NOT USED` (18); `\* ISRSPH: 1 TO WRITE FILE FOR RESIDUAL SCALAR VARIABLE IN HORIZONTAL PLANE` (20); `\* ISPHXY: 0 DOES NOT WRITE I,J,X,Y IN \*\*\*CNH.OUT AND R\*\*\*CNH.OUT FILES (RESIDUAL ONLY)` (24); `\*              1 WRITES I,J ONLY IN \*\*\*CNH.OUT AND R\*\*\*CNH.OUT FILES (RESIDUAL ONLY)` (26); `\*              2 WRITES I,J,X,Y IN \*\*\*CNH.OUT AND R\*\*\*CNH.OUT FILES (RESIDUAL ONLY)` (28); `\* DATA LINE REPEATS 7 TIMES FOR SAL,TEM,DYE,SFL,TOX,SED,SND` (32). |
| 35–50 | C71 입력 예시 — 입력 열 제목과 염분(salinity)·수온(temperature)·염료(dye)·패류 유생(shellfish larvae)·독성 오염물질(toxic contaminant)·점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(non-cohesive sediment)의 데이터 행을 제시한다(36–50). 값 행은 원문 예시이며 기본값이라는 표시는 없다. 빈 줄을 포함한다(35–49). 원문: `C71 ISSPH NPSPH ISRSPH ISPHXY` (36); `           0         8          0           3        !SAL` (38); `           0         8          0           3        !TEM` (40); `           0         8          0           3        !DYE` (42); `           1         8          0           3        !SFL` (44); `           0         8          0           3        !TOX` (46); `           0         8          0           3        !SED` (48); `           0         8          0           3        !SND` (50). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 24–28·38–50행: `ISPHXY` 설명은 `0`·`1`·`2`만 제시하지만 모든 예시 데이터 행의 `ISPHXY` 값은 `3`이다. 이 파일에는 `3`의 의미가 없다.

