---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/emasstrs.f
lines: 19
sha256: f8b9d45b43d0d07a9dbcb59ae9210a10108fa62ba84718e50d4d3d8892a65250
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# emasstrs.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | EMASSTRS의 암시적 형과 배열 크기를 선언한다. 해석: EMASS는 두 절점의 질량행렬이다. 원문: `      SUBROUTINE EMASSTRS(EMASS,AMAT,S,GRID,KN,LUMP,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GRID(3,*),KN(2),AMAT(*),EMASS(2,2)` (4); 주석 원문 `C----&------------------------------------------------------------------` (5). [11-04 전수 검증 정정] |
| 6–19 | 시작 시 1행 EMASSTRS 루틴 안. LENGTH에 GRID(1,KN(1))·GRID(1,KN(2))와 3을 전달한다. `EM=AMAT(3)*S*RL`을 계산한다. 해석: RL이 두 절점 사이 길이이고 AMAT(3)·S가 밀도·단면적이면 EM은 전체 질량이다. LUMP=0이면 첫 열에 절반씩 저장한다. ELSE에서는 대각에 EM/3, 비대각에 EM/6을 둔다. 반환문과 루틴 끝을 포함한다. 원문: `      CALL LENGTH(RL,GRID(1,KN(1)),GRID(1,KN(2)),3)` (6); `      EM=AMAT(3)*S*RL` (7); `      IF( LUMP .EQ. 0 ) THEN` (8); `        EMASS(1,1) = EM*.5` (9); `        EMASS(2,1) = EM*.5` (10); `      ELSE` (11); `        EMASS(1,1) = EM/3.D0` (12); `        EMASS(1,2) = EM/6.D0` (13); `        EMASS(2,1) = EM/6.D0` (14); `        EMASS(2,2) = EM/3.D0` (15); `      ENDIF` (16); `      RETURN` (18); `      END` (19). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–16: LUMP=0 분기는 EMASS의 첫 열만 대입한다. 두 번째 열 초기화는 이 파일에 없다.
- 1·3–19: ITO는 인수에 있지만 본문에서 참조하지 않는다.
