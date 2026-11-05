---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/ens_geom_p.f
lines: 47
sha256: 7cd6475003cd9438756b8314c5e8f949cf367a0744122d3577642913032999ca
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# ens_geom_p.f — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | ENS_GEOM_P는 M_VAL, KK(*)/IEP(*) 및 정수 포인터 작업 배열 IE/NUG/IG/LG를 선언한다(1–6). KK(8)/KK(10)에서 NNOD/NSOL을 읽는다(8–9). str_p.case를 열고 EnSight Gold 형식과 part.geom 모델 파일명을 써서 닫는다(11–21). part.geom을 열고 IE(NSOL*6), NUG/IG/LG(NNOD)를 할당한다(23–28). C로 시작하는 구분 주석도 이 구간에 포함한다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE ENS_GEOM_P(KK,NPART,IEP,IFCAS,IFG)` (1); `      USE M_VAL` (3); `      DIMENSION KK(*),IEP(*)` (5); `      INTEGER, POINTER :: IE(:), NUG(:), IG(:), LG(:)` (6); `      NNOD = KK(8)` (8); `      NSOL = KK(10)` (9); `      OPEN( IFCAS, FILE = 'str_p.case')` (11); `      WRITE(IFCAS,'(A)') 'FORMAT'` (13); `      WRITE(IFCAS,'(A)') 'type: ensight gold'` (15); `      WRITE(IFCAS,'(A)') 'GEOMETRY'` (17); `      WRITE(IFCAS,'(2A)') 'model: ', 'part.geom'` (19); `      CLOSE( IFCAS )` (21); `      OPEN( IFG , FILE = 'part.geom' )` (23); `      ALLOCATE( IE(NSOL*6) )` (25); `      ALLOCATE( NUG(NNOD) )` (26); `      ALLOCATE( IG(NNOD) )` (27); `      ALLOCATE( LG(NNOD) )` (28) |
| 29–47 | 시작 시 1행 ENS_GEOM_P 루틴 안. 기하 파일 머리말과 절점·요소 ID를 명시하는 줄을 출력한다(30–33). IPART=1:NPART에서 PART_GEOM에 INDG/GRID/IELM/KK(37)/NNOD/NSOL 및 IE/NUG/IG/LG, 출력 장치 IFG, IEP, IPART를 넘긴다(35–38). 해석: IEP는 분할표이고 IPART는 현재 분할 번호로 읽힌다. 작업 배열 네 개를 해제하고 기하 파일을 닫는다(40–45). C 구분 주석과 종료문까지 포함한다(39–47). 원문(연속행은 앞 문장에 이어짐): `      WRITE(IFG,'(A)') 'ASTEA MECHANICAL'` (30); `      WRITE(IFG,'(A)') 'EnSight Gold geometry file'` (31); `      WRITE(IFG,'(A)') 'node id given'` (32); `      WRITE(IFG,'(A)') 'element id given'` (33); `      DO IPART = 1, NPART` (35); `        CALL PART_GEOM( INDG, GRID, IELM, KK(37), NNOD, NSOL, IE,` (36); `     &                  NUG, IG, LG, IFG, IEP, IPART )` (37); `      ENDDO` (38); `      DEALLOCATE( IE )` (40); `      DEALLOCATE( NUG )` (41); `      DEALLOCATE( IG )` (42); `      DEALLOCATE( LG )` (43); `      CLOSE( IFG )` (45); `      END` (47) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·19·23: 출력 파일명은 str_p.case와 part.geom으로 고정되어 있다.
- 25: IE 작업 배열의 크기는 NSOL*6으로 지정한다.
