---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/welcome.f90
lines: 50
sha256: c564b06637d70d59f9edda91faf10ee5f0f417b3fff114dc215ea2f0ac94ecd9
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# welcome.f90 — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | EFDC+·저작권·GPLv2 머리말과 빈 줄(1–9), `SUBROUTINE WELCOME` (10). 2006 Fortran 90 갱신 주석(12–14). GLOBAL에서 EFDC_VER만 가져온다(15). 주석은 EFDC_VER를 aaefdc.f90에서 설정한다고 적는다(17). write(6,1) EFDC_VER로 배너(banner)를 출력한다(18). |
| 20–33 | 시작 시 10행 WELCOME 안. FORMAT 1의 문자열과 연속행(20–33). 별표 테두리·빈 행·EFDC+ 문자 그림을 출력한다(20–30). ENVIRONMENTAL FLUID DYNAMICS CODE (PLUS)와 원개발자 JOHN M. HAMRICK 문구를 출력한다(31–32). |
| 34–50 | 시작 시 10행 WELCOME·20행 FORMAT 문장 안. DSI, LLC 소재지와 포함 기능을 배너 문자열로 열거한다(34–42). 기능 문구는 GOTM, SIGMA-STRETCHED/SIGMA-ZED 수직 층화(vertical layering), 프로펠러 세척류(propeller wash), 라그랑주 입자 추적(Lagrangian particle tracking), 동물플랑크톤(zooplankton)·RPEM, SEDZLJ·수류 에너지 장치(hydrokinetic device), OpenMP·OpenMPI이다. DSI의 EFDC+ EXPLORER 12.5 문구는 고정 문자열이다(44). VERSION DATE: MPI 뒤 A10으로 EFDC_VER를 출력한다(46). 테두리와 FORMAT 종료(48), return·END(49–50). 조건 분기·값 계산식·다른 루틴 호출은 없다. 이 구간은 출력 문자열을 판독한 기록이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44·46: 배너의 EXPLORER 12.5는 고정 문자열이다. VERSION DATE 항목은 EFDC_VER를 A10 형식으로 출력한다. 외부 프로그램의 현재 판본은 이 파일에서 확인하지 않았다.
