---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_ens_geom.f
lines: 42
sha256: d77d8c89343f5ed9078b35bb704d54d5b7bd0e80296c5e4ee29cbc14bfe5ae78
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_ens_geom.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–42 | SF_ENS_GEOM 선언, INCLUDE 세 개와 격자 배열·문자열 범위(1–12). NPROCS=1이면 cadmas_out, 그 밖에는 한 자리 MYRANK를 포함한 cadmas_<IP>_out을 고른다(14–21). 23행 MK_DIR 호출은 주석 처리된 코드다. data.geom을 열어 EnSight Gold 직교 격자(rectilinear grid)의 머리말·크기·세 축 좌표를 기록하고 닫는다(25–40). 원문: `      SUBROUTINE SF_ENS_GEOM(XX,YY,ZZ)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'VF_APARAI.h'` (7)<br>`      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (9)<br>`      CHARACTER*1 IP` (11)<br>`      CHARACTER*12 FLD` (12)<br>`      IF( NPROCS == 1 ) THEN` (14)<br>`        FLD = 'cadmas_out'` (15)<br>`        N = 10` (16)<br>`      ELSE` (17)<br>`        WRITE(IP,'(I1)') MYRANK` (18)<br>`        FLD = 'cadmas_'//IP//'_out'` (19)<br>`        N = 12` (20)<br>`      ENDIF` (21)<br>` !    CALL MK_DIR(FLD)` (23)<br>`      OPEN(40, FILE = FLD(1:N)//'/data.geom' )` (25)<br>`      WRITE(40,'(A)') 'CADMAS-SURF/3D-2F'` (27)<br>`      WRITE(40,'(A)') 'EnSight Gold geometry file'` (28)<br>`      WRITE(40,'(A)') 'part'` (30)<br>`      WRITE(40,'(I10)') 1` (31)<br>`      WRITE(40,'(A)') '3D strucured mesh'` (32)<br>`      WRITE(40,'(A)') 'block rectilinear'` (33)<br>`      WRITE(40,'(3I10)') MYIE-MYIS+2, MYJE-MYJS+2, NUMK-1` (35)<br>`      WRITE(40,'(1PE12.5)') XX(1,MYIS:MYIE+1)` (36)<br>`      WRITE(40,'(1PE12.5)') YY(1,MYJS:MYJE+1)` (37)<br>`      WRITE(40,'(1PE12.5)') ZZ(1,2:NUMK)` (38)<br>`      CLOSE(40)` (40)<br>`      END` (42) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·18–20: 랭크 문자열 IP는 CHARACTER*1이며 변환 형식은 I1이다.
- 23–25: 출력 디렉터리를 만드는 MK_DIR 호출은 주석 처리되어 있다. OPEN 전에 별도의 디렉터리 생성 실행문은 이 파일에 없다.
