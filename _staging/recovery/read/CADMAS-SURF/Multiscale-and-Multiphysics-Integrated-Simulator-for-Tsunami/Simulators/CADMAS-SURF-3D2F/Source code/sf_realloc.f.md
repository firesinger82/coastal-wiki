---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_realloc.f
lines: 42
sha256: b94b330f4600ce941f9fed63ef2011b61b22b5122a397677683dffd08460ef30
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_realloc.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SF_REALLOC의 선언과 기존 배열 해제다. VF_A2ARRAY·SF_ARRAY를 사용한다(3–4). IELM부터 SPC까지 기존 배열을 해제한다(8–23). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_REALLOC(NELM,NNOD,NPFC)` (1); `      USE VF_A2ARRAY` (3); `      USE SF_ARRAY` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DEALLOCATE( IELM )` (8); `      DEALLOCATE( IENO )` (9); `      DEALLOCATE( INDG )` (10); `      DEALLOCATE( IGFC )` (11); `      DEALLOCATE( GRDL )` (12); `      DEALLOCATE( IGNO )` (13); `      DEALLOCATE( IPFACE )` (14); `      DEALLOCATE( IPFNO )` (15); `      DEALLOCATE( IPGRID )` (16); `      DEALLOCATE( POS )` (17); `      DEALLOCATE( POS1 )` (18); `      DEALLOCATE( POS2 )` (19); `      DEALLOCATE( DVEL )` (20); `      DEALLOCATE( DVEL1 )` (21); `      DEALLOCATE( DVEL2 )` (22); `      DEALLOCATE( SPC )` (23). |
| 25–42 | 시작 시 1행 SF_REALLOC 루틴 안. SF_REALLOC 안. NELM·NNOD·NPFC에 맞춰 25–40행에 나열된 배열을 다시 할당한다. IELM 첫 차원은 24다. IPFACE 첫 차원은 12다. IPGRID 첫 차원은 2다. POS·POS1·POS2·DVEL·DVEL1·DVEL2 첫 차원은 3이다. 원문(연속 표시는 앞 문장에 이어짐): `      ALLOCATE( IELM(24,NELM) )` (25); `      ALLOCATE( IENO(NELM) )` (26); `      ALLOCATE( INDG(NNOD) )` (27); `      ALLOCATE( IGFC(NNOD) )` (28); `      ALLOCATE( GRDL(NNOD) )` (29); `      ALLOCATE( IGNO(NNOD) )` (30); `      ALLOCATE( IPFACE(12,NPFC) )` (31); `      ALLOCATE( IPFNO(NPFC) )` (32); `      ALLOCATE( IPGRID(2,NNOD) )` (33); `      ALLOCATE( POS(3,NNOD) )` (34); `      ALLOCATE( POS1(3,NNOD) )` (35); `      ALLOCATE( POS2(3,NNOD) )` (36); `      ALLOCATE( DVEL(3,NELM) )` (37); `      ALLOCATE( DVEL1(3,NELM) )` (38); `      ALLOCATE( DVEL2(3,NELM) )` (39); `      ALLOCATE( SPC(NELM) )` (40); `      END` (42). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–23: DEALLOCATE 앞에 연관·할당 여부를 검사하는 조건문이 없다.
- 25–40: 새 배열은 할당만 하며 이 루틴에는 값 초기화가 없다.
