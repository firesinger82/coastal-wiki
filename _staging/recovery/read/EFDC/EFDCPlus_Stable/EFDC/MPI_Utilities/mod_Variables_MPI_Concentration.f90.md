---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/mod_Variables_MPI_Concentration.f90
lines: 54
sha256: d70377cf5004d8b67a38dec102577d8bddca5455fcb08f872d2798260e2859df
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI_Concentration.f90 — 판독 구간 기록

구간은 1행부터 54행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | EFDC+ 표제·저작권 2021–2022·GPLv2 안내(1–8). 전역(global) 농도(concentration) 출력 배열이라는 주석(9). Variables_MPI_Concentration 모듈 시작·implicit none·빈 줄(10–14). |
| 15–35 | 시작 시 11행 Variables_MPI_Concentration 선언부 안. 모두 allocatable인 S/W/E/N 접미사 그룹을 선언한다. S 그룹은 ICBS_GL/JCBS_GL/NTSCRS_GL 1차원 정수, NCSERS_GL 2차원 정수, CBS_GL 3차원 기본 REAL이다(16–20). W 그룹은 ICBW_GL/JCBW_GL/NTSCRW_GL·NCSERW_GL·CBW_GL을 같은 차원·자료형으로 선언한다(21–25). E 그룹은 ICBE_GL/JCBE_GL/NTSCRE_GL·NCSERE_GL·CBE_GL(26–30), N 그룹은 ICBN_GL/JCBN_GL/NTSCRN_GL·NCSERN_GL·CBN_GL(31–35)이다. 선언 크기는 모두 콜론으로 남겨 둔다. |
| 36–49 | 시작 시 11행 Variables_MPI_Concentration 선언부 안. ILTMSR_GL/JLTMSR_GL/NTSSSS_GL/MTMSRP_GL/MTMSRC_GL/MTMSRA_GL/MTMSRUE_GL/MTMSRUT_GL/MTMSRU_GL/MTMSRQE_GL/MTMSRQ_GL/MLTM_GL을 1차원 allocatable 정수 배열로 선언한다(37–48). 앞뒤 빈 줄을 포함한다(36·49). |
| 50–54 | 시작 시 11행 Variables_MPI_Concentration 선언부 안. 전역 매핑(mapping) 변수 끝 주석(50). CLTMSR_GL은 요소 길이 20의 1차원 allocatable 문자 배열이다(52). 빈 줄·모듈 종료(51·53–54). 이 파일에는 contains·실행 루틴·할당·초기화 문장이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음

