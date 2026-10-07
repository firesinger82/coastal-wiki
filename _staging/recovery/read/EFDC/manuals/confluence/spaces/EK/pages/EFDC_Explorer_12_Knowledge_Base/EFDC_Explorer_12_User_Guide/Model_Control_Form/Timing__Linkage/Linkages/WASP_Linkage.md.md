---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Timing__Linkage/Linkages/WASP_Linkage.md
lines: 16
sha256: 21a0fae0fbd444fc6a040cb516556aeb0b2f321c627caf5e00a808f7ec275bf7
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# WASP_Linkage.md — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — WASP Linkage의 페이지 ID, URL, 버전, 갱신 시각, 계층을 수록한다(1–9). |
| 10–14 | WASP 연계 — Water Quality Analysis Simulation Program의 목적을 소개한다(10). EEMS10.4부터 생성하는 `*.HYD` 유체역학 연계(hydrodynamic linkage) 파일에 체적·수심·속도 등 수송 정보가 들어가며 WASP의 입력으로 쓰인다고 적는다(10). WASP 7/8과 평균 구간의 적용·예시·단위 원문: `From the *Model Control* form, go to the *Timing/Linkage* tab, as shown in [Figure 1](#Figure1). RMC on *Linkages* sub-tab, the *EFDC Model Linkages* form will be displayed as shown in [Figure 2](#Figure2). Go to the *WASP Linkage* tab, select the *WASP 7/8* radial button under *Linkage to Water Quality Models* frame. Type in a value, in this case 10, for *Number of Minutes to Average per Linkage Step* box to set the output frequency of the linkage file. The WASP linkage output will be saved per 10 minutes. Click *OK* button to save the setting.` (12) Building a WASP Model의 외부 space 안내 링크를 포함한다(14). |
| 15–16 | Figure 1·2 — 로컬 그림 두 개를 모두 직접 열었다(16). 첫 그림은 EE 연계 사용, `Linkage Output Frequency (minutes): 0.5`, NetCDF 미사용, WASP 파일 생성 상태를 보여 주는 보고서이다(16 첫 그림). 두 번째는 `WASP 7/8` 선택 화면이며 `Number of Minutes to Average per Linkage Step: 0`을 표시한다(16 두 번째 그림). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12·16행 두 번째 그림: 본문은 Number of Minutes to Average per Linkage Step의 예시 값 `10`과 10분 출력 간격을 적는다. 그림의 해당 입력 상자에는 `0`이 보인다.

