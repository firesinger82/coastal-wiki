---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_BCTSET.f
lines: 30
sha256: bdbc5340ce8613c05a72625fa16c99a0d188250a0722c5678419370add680d0a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_BCTSET.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | ST_BCTSET의 인수 선언은 1–2행 연속문이다. IMPLICIT와 배열 범위를 선언한다(4–5). IP=0에서 시작한다(7). 9행 바깥 루프(loop)와 11행 내부 루프는 13행 ID 일치 조건을 검사한다. 일치할 때마다 IP를 늘려 J_BCTS(2:3,J)를 NCPR(:,IP)에 복사한다(15–16). 내부 루프 종료 후 ICPR(2,I)에 누적 끝 위치 IP를 기록한다(22). 원문: `      SUBROUTINE ST_BCTSET( ICPR, NCPR, NICPR, NNCPR, J_BCTS, N_BCTS,` / `     &                      ICRGR )` (1–2; 하나의 고정형식 연속문); `      IMPLICIT REAL*8 (A-H,O-Z)` (4); `      DIMENSION ICPR(2,NICPR), NCPR(2,NNCPR), J_BCTS(3,N_BCTS), ICRGR(*)` (5); `      IP = 0` (7); `      DO I = 1, NICPR` (9); `        DO J = 1, N_BCTS` (11); `          IF( J_BCTS(1,J) == ICPR(1,I) ) THEN` (13); `            IP = IP + 1` (15); `            NCPR(:,IP) = J_BCTS(2:3,J)` (16); `          ENDIF` (18); `        ENDDO` (20); `        ICPR(2,I) = IP` (22); `      ENDDO` (24). [11-04 전수 검증 정정] |
| 26–30 | 시작 시 1행 ST_BCTSET 안이며 9행 루프 밖. 26행 루프가 1–NNCPR 전체를 순회한다. 27행 벡터 첨자(vector subscript) 식은 NCPR(:,I)의 각 값을 ICRGR의 첨자로 사용하여 해당 배열값으로 대체한다. 루프 종료·주석·END를 포함한다(28–30). 원문: `      DO I = 1, NNCPR` (26); `        NCPR(:,I) = ICRGR( NCPR(:,I) )` (27); `      ENDDO` (28); `      END` (30). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–16·26–27: 매칭으로 채운 개수는 IP로 누적한다. 번호 변환 루프의 상한은 최종 IP가 아니라 인수 NNCPR이다.
