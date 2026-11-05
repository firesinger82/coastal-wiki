---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/fmp_elem.f
lines: 89
sha256: 91c07c64bc4cde096940a0bded1df6abfa69bddc821629efff95dc8779e9f36a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_elem.f — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | FMP_ELEM은 IP0(NP)를 IG의 첨자로 사용하여 IP(NP)에 값을 대입하고 JP(20)를 0으로 초기화한다. ITYPE의 SELECT CASE에서 CASE(2,6)은 IDP=IDM을 사용한다. 그 안 NP=4·10은 각각 유형 25·26, 위상(topology) 6·10과 절점 위치 재배열을 지정한다. 원문: `      SUBROUTINE FMP_ELEM(NMAT,NRODA,ID,ITYPE,IDM,IDS,NP,IP0,IG,IFL)` (1); `      CHARACTER*200 CHAR` (3); `      CHARACTER*1 C /','/` (4); `      DIMENSION IP0(NP),IP(NP),JP(20),IG(*)` (5); `      IP(:) = IG( IP0(:) )` (7); `      JP(:) = 0` (9); `      SELECT CASE( ITYPE )` (11); `      CASE( 2, 6 )` (12); `        IDP = IDM` (14); `        SELECT CASE( NP )` (16); `        CASE( 4 )` (17); `          ITYP = 25` (18); `          ITOP = 6` (19); `          JP(1:3)   = IP(1:3)` (20); `          JP(5)     = IP(4)` (21); `        CASE( 10 )` (22); `          ITYP = 26` (23); `          ITOP = 10` (24); `          JP(1:3)   = IP(1:3)` (25); `          JP(5)     = IP(4)` (26); `          JP(9:11)  = IP(5:7)` (27); `          JP(13:15) = IP(8:10)` (28) [11-04 전수 검증 정정] |
| 29–51 | 시작 시 11행 `SELECT CASE( ITYPE )`의 12행 `CASE( 2, 6 )` 안이다. 이 선택문은 66행 `END SELECT`에서 닫힌다. 안쪽 16행 `SELECT CASE( NP )`는 50행 `END SELECT`에서 닫힌다. CASE(6)·CASE(15)·CASE(8)·CASE(20)은 유형·위상과 JP의 대응 위치를 정한다. 각 배열 첨자 범위와 상수는 아래 원문과 같다. NP 선택을 닫는다. 원문: `        CASE( 6 )` (29); `          ITYP = 25` (30); `          ITOP = 7` (31); `          JP(1:3)   = IP(1:3)` (32); `          JP(5:7)   = IP(4:6)` (33); `        CASE( 15 )` (34); `          ITYP = 26` (35); `          ITOP = 11` (36); `          JP(1:3)   = IP(1:3)` (37); `          JP(5:7)   = IP(4:6)` (38); `          JP(9:11)  = IP(7:9)` (39); `          JP(13:15) = IP(10:12)` (40); `          JP(17:19) = IP(13:15)` (41); `        CASE( 8 )` (42); `          ITYP = 25` (43); `          ITOP = 8` (44); `          JP(1:8)   = IP(1:8)` (45); `        CASE( 20 )` (46); `          ITYP = 26` (47); `          ITOP = 12` (48); `          JP(1:20)  = IP(1:20)` (49); `        END SELECT` (50) [11-04 전수 검증 보완] |
| 52–67 | 시작 시 11행 `SELECT CASE( ITYPE )` 안이다. 이 선택문은 66행 `END SELECT`에서 닫힌다. CASE(3)는 IDP에 NMAT+IDS를 쓴다. CASE(4)는 NMAT+NRODA+IDS를 쓴다. 두 경우 유형 1·위상 0·절점 두 개를 설정한다. ITYPE 선택을 닫는다. 원문: `      CASE( 3 )` (52); `        IDP = NMAT + IDS` (54); `        ITYP = 1` (55); `        ITOP = 0` (56); `        JP(1:2) = IP(1:2)` (57); `      CASE( 4 )` (59); `        IDP = NMAT + NRODA + IDS` (61); `        ITYP = 1` (62); `        ITOP = 0` (63); `        JP(1:2) = IP(1:2)` (64); `      END SELECT` (66) [11-04 전수 검증 보완] |
| 68–89 | 요소 헤더를 내부 문자열 CHAR에 포맷하여 WT_DATA에 넘긴다. JP(1:10)·JP(11:20)를 두 번에 나누어 쓴다. 이후 고정 영값 레코드와 16개의 정수 0을 출력한다. 68–69행은 하나의 WRITE 연속문이다. 원문: `      WRITE(CHAR,'(I10,12I4)') ` (68); `     &  ID,124,IDP,ITYP,ITOP,1,0,0,0,0,0,0,0` (69); `      CALL WT_DATA(CHAR,IFL)` (71); `      WRITE(CHAR,'(10I10)') JP(1:10)` (73); `      CALL WT_DATA(CHAR,IFL)` (75); `      WRITE(CHAR,'(10I10)') JP(11:20)` (77); `      CALL WT_DATA(CHAR,IFL)` (79); `      WRITE(IFL,'(A)') '0.,0.,0.,0,0,0,0,0,0,'` (81); `      WRITE(IFL,'(A)') '0.,0.,0.,'` (83); `      WRITE(IFL,'(A)') '0.,0.,0.,'` (85); `      WRITE(IFL,'(16(I1,A))') (0,C,I=1,16)` (87); `      END` (89) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–66: ITYPE 선택과 NP 선택에는 CASE DEFAULT가 없다. ITYP·ITOP는 이 선택 전 초기화하지 않는다.
- 5·9·73–79: 출력 절점 슬롯은 JP(20)으로 고정하고 선택한 절점만 채운다.
