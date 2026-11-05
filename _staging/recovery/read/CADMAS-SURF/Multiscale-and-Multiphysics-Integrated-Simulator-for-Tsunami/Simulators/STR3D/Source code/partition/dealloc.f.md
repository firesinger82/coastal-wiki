---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/partition/dealloc.f
lines: 105
sha256: 6fbc3554eb064c4f1522074cf1e5819b60bb5d8cd577093ac5aa3b1414c10d12
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dealloc.f — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | DEALLOC는 MPI_PARAM/M_VAL/M_PART와 INTEGER*8 MUSED, KK(*)를 사용한다(1–9). MUSED()*4.D-6을 메모리 MB 로그로 출력한다(11–12). ISUB/RTIM/IGCD를 해제한다(14–18). ISTM==0 .AND. ICHK==0일 때만 GRID를, ICHK==0일 때만 IELM을 해제한다(19–21). RODA/MAT/AMAT와 ISPD/NSPD/SPCD 및 LOAD/SLOD/SILD/LILD를 해제한다(23–35). 해석: 뒤의 두 배열 묶음은 지정 변위와 하중 관련 배열로 읽힌다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE DEALLOC(KK,ITO,ICHK)` (1); `      USE MPI_PARAM` (3); `      USE M_VAL` (4); `      USE M_PART` (5); `      INTEGER*8 MUSED` (7); `      DIMENSION KK(*)` (9); `      WRITE(ITO,'(/X,A,F8.1,A)')` (11); `     &  'SUB. DEALLOC    : ', MUSED()*4.D-6, '(MB) USED.'` (12); `      DEALLOCATE( ISUB )` (14); `      DEALLOCATE( RTIM )` (16); `      DEALLOCATE( IGCD )` (18); `      IF( ISTM == 0 .AND. ICHK == 0 ) DEALLOCATE( GRID )` (19); `      IF( ICHK == 0 ) DEALLOCATE( IELM )` (21); `      DEALLOCATE( RODA )` (23); `      DEALLOCATE( MAT )` (25); `      DEALLOCATE( AMAT )` (26); `      DEALLOCATE( ISPD )` (28); `      DEALLOCATE( NSPD )` (29); `      DEALLOCATE( SPCD )` (30); `      DEALLOCATE( LOAD )` (32); `      DEALLOCATE( SLOD )` (33); `      DEALLOCATE( SILD )` (34); `      DEALLOCATE( LILD )` (35) [11-04 전수 검증 정정] |
| 36–81 | 시작 시 1행 DEALLOC 루틴 안. IFC/NFC/FC, IPL4/NPL4/PLD4, IGRV/GRAV, ISPA/NSPA, ISP1/NSP1, ISPC/NSPC/SPC, IDLD/SDLD/SIDL/LIDL, ITD1/TBD1, ISTP/NSTP/DELT, ITL1을 해제한다(37–70). M_PART의 NPEW/NIMPW/NEXPW와 IPEW/IDXIMPW/NODIMPW/IDXEXPW/NODEXPW를 해제한다(72–80). M_PART 소속의 근거는 `module/m_part.f90:16–22`이다. 해석: 앞의 배열 묶음들은 동하중·시계열·단계 자료이고 M_PART의 배열들은 작업 통신 자료로 읽힌다. 원문(연속행은 앞 문장에 이어짐): `      DEALLOCATE( IFC )` (37); `      DEALLOCATE( NFC )` (38); `      DEALLOCATE( FC )` (39); `      DEALLOCATE( IPL4 )` (41); `      DEALLOCATE( NPL4 )` (42); `      DEALLOCATE( PLD4 )` (43); `      DEALLOCATE( IGRV )` (45); `      DEALLOCATE( GRAV )` (46); `      DEALLOCATE( ISPA )` (48); `      DEALLOCATE( NSPA )` (49); `      DEALLOCATE( ISP1 )` (51); `      DEALLOCATE( NSP1 )` (52); `      DEALLOCATE( ISPC )` (54); `      DEALLOCATE( NSPC )` (55); `      DEALLOCATE( SPC )` (56); `      DEALLOCATE( IDLD )` (58); `      DEALLOCATE( SDLD )` (59); `      DEALLOCATE( SIDL )` (60); `      DEALLOCATE( LIDL )` (61); `      DEALLOCATE( ITD1 )` (63); `      DEALLOCATE( TBD1 )` (64); `      DEALLOCATE( ISTP )` (66); `      DEALLOCATE( NSTP )` (67); `      DEALLOCATE( DELT )` (68); `      DEALLOCATE( ITL1 )` (70); `      DEALLOCATE( NPEW )` (72); `      DEALLOCATE( NIMPW )` (73); `      DEALLOCATE( NEXPW )` (74); `      DEALLOCATE( IPEW )` (76); `      DEALLOCATE( IDXIMPW )` (77); `      DEALLOCATE( NODIMPW )` (78); `      DEALLOCATE( IDXEXPW )` (79); `      DEALLOCATE( NODEXPW )` (80) [11-04 전수 검증 정정] |
| 82–105 | 시작 시 1행 DEALLOC 루틴 안. KK(92)==0이면 반환한다(82). 남은 경로에서 ICPA/NCPA/ICPR/NCPR/CPR/NCRG를 해제한다(84–92). ICHK<2일 때 IBEL을 해제한다(94). IBTE/IELG/NIBT/IEQ/IBT를 해제하고 종료한다(96–105). 원문(연속행은 앞 문장에 이어짐): `      IF( KK(92) == 0 ) RETURN` (82); `      DEALLOCATE( ICPA )` (84); `      DEALLOCATE( NCPA )` (85); `      DEALLOCATE( ICPR )` (87); `      DEALLOCATE( NCPR )` (88); `      DEALLOCATE( CPR )` (90); `      DEALLOCATE( NCRG )` (92); `      IF( ICHK < 2 ) DEALLOCATE( IBEL )` (94); `      DEALLOCATE( IBTE )` (96); `      DEALLOCATE( IELG )` (98); `      DEALLOCATE( NIBT )` (100); `      DEALLOCATE( IEQ )` (102); `      DEALLOCATE( IBT )` (103); `      END` (105) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–103: 이 파일의 DEALLOCATE에는 ALLOCATED 검사와 STAT 인수가 없다. GRID/IELM/IBEL에는 별도 조건이 있다. 82행에는 `IF( KK(92) == 0 ) RETURN` 조기 반환이 있다. 해석: 이 조기 반환 뒤의 해제 대상은 접촉 관련 배열로 읽힌다. [11-04 전수 검증 정정]
