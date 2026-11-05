---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/efpte1.f
lines: 14
sha256: ec6a13e11afc189af76ba36bcc3bf4d2f79bfdabaf9cbbadc0945dfc80461c87
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# efpte1.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | EFPTE1의 암시적 형과 RN·DNDX·X·PB·FP 배열의 크기를 선언한다. 해석: 이 배열들은 4절점 요소의 형상함수·공간 미분·좌표·압력·힘 자료에 해당한다. 원문: `      SUBROUTINE EFPTE1(FP,X,PB,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION RN(4),DNDX(3,4),X(3,4),PB(4),FP(3,4)` (4). [11-04 전수 검증 정정] |
| 6–14 | 시작 시 1행 EFPTE1 루틴 안. RN을 모두 .25D0으로 두고 DERXTE1을 호출한다. VECML1(PG,RN,PB,4)를 호출한다. DNDX에 PG와 DET/6을 곱하여 FP를 계산한다. 해석: VECML1이 내적을 계산한다면 RN=.25D0에 의해 PG는 네 PB 값의 평균이다. DERXTE1의 DNDX·체적 6배 출력 설명은 `derxte1.f:3–4`에 있다. 루틴 끝을 포함한다. 원문: `      RN(:) = .25D0` (6); `      CALL DERXTE1(DNDX,DET,X,ITO)` (8); `      CALL VECML1(PG,RN,PB,4)` (10); `      FP(:,:) = DNDX(:,:) * PG * DET / 6.D0` (12); `      END` (14). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6·10·12: RN의 대입값은 .25D0이다. VECML1의 마지막 인수는 4이다. FP 대입식의 분모는 6.D0이다. 체적 6배 출력의 근거는 `derxte1.f:4`이다. 해석: RN은 보간 계수에 해당한다. [11-04 전수 검증 정정]
