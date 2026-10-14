---
file: models/SWASH/raw/source_code/swash/src/SwashSolvedata.ftn90
lines: 127
sha256: 12021493f9ae3a65abc5bda2f7c7f166400eef1d2760749262e96e95d6af94af
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashSolvedata.ftn90 — 판독 구간 기록

구간은 1행부터 127행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | SwashSolvedata 모듈을 시작한다(1). 기관·저작권·GPL 3 이상·무보증 머리말(3–27). Marcel Zijlema의 2010년 4월 신규 모듈이다(30–36). 선형 해법(linear solver)과 연립방정식 해의 데이터를 보유하며 사용 모듈은 없다는 주석이다(38–48). |
| 50–78 | 시작 시 1행 SwashSolvedata 모듈 안. implicit none과 빈 parameter 절이다(50–55). iamout 주석은 출력 제어값 0=출력 없음, 1=치명적 오류만, 2=반복 과정, 3=추가 반복 정보를 구분한다(58–62). icond 주석은 BiCGSTAB 전처리기(preconditioner)의 1=ILUD 좌우 또는 분할, 2=ILUD 우측, 3=ILU 우측 선택을 적는다(63–66). 압축 희소 행(compressed sparse row, CSR) 형식의 대각 열 인덱스 di/dis, 행 시작 포인터 ia/ias, L·U 항 포인터 iplu/iplu3, 행별 열 순서 irw/irws, 열 인덱스 ja/jas를 save·allocatable 정수 배열로 선언한다(68–77). bicgstab·pcg·pcgu/bicgstabu·bicgstab3의 사용처는 각 선언 주석에 적혀 있다. |
| 79–97 | 시작 시 1행 모듈 안. 중첩 Newton 반복(nested Newton iteration)의 수정 행렬 amata, 삼대각 주대각 ba, 수정 우변 da, 이전·현재 대각 행렬 p0/p1·q0/q1을 real*8로 선언한다(79·83·88·90–91·96–97). CSR 행렬 ax2·axs·axs2, SIP의 ILU 행렬 cmat, CG 스케일링 대각 diag/diag2, BiCGSTAB 스케일링 diagb·방향 벡터 p를 선언한다(80–89). RILU 분해 행렬 prec와 ILU 분해 prec2/3/4의 사용 해법은 선언 주석에 적혀 있다(92–95). prec·prec2·prec4의 자료형 선언은 `real`이다(92–93·95). prec3의 자료형 선언은 `real*8`이다(94). 모두 save·allocatable이다. [10-15 전수 검증 정정] |
| 98–127 | 시작 시 1행 모듈 안. CG 행렬·공액 벡터 곱 r/r2, 잔차(residual) res·resd·resd2, 준잔차(quasi-residual) res0, 수정 우변 rhsa, CG 탐색 방향 s/s2를 선언한다(98–106). Newton 반복 해 sol0/sol1·sola와 bicgstab3 해 sol3를 선언한다(107–110). BiCGSTAB 보조 t/u/v, 임시 vt/vt2/w/w2, 전처리 잔차 z/z3, DAC 보조 z1/z2/z12/z22를 선언한다(111–123). 배열 정밀도는 real 또는 real*8이며 모두 save·allocatable이다. 소스 구분 주석 뒤 모듈을 종료한다(124–127). 이 파일에는 할당·계산·루틴 호출 실행문이 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 107–108: sol0와 sol1의 선언 주석은 모두 previous iteration의 해 벡터라고 적는다. 두 주석은 이전·현재 반복을 구분하지 않는다.
