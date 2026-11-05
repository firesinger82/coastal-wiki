---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fmp_sol0.f
lines: 67
sha256: 1756ec02e6a94d7076bd26ca135c26c4b4dce9c82df6aeed5df2c28cdeec3b6d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_sol0.f — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | 절점 번호와 응력 포인터를 선언한다(3–5). SIGP(6,NNOD)를 수집하고 항목 30·31·32로 X·Y·Z 수직응력(normal stress)을 출력한다(7–27). 원문: `      SUBROUTINE FMP_SOL0(IOUT,INDG,NNOD,IFL)` (1); `      CHARACTER*1 C /','/` (3); `      DIMENSION INDG(NNOD)` (4); `      REAL(8), POINTER :: SIGP(:,:),PRNSIGP(:,:)` (5); `      ALLOCATE( SIGP(6,NNOD) )` (7); `      CALL GATHER_NODAL_D(SIGP,6)` (9); `      WRITE(IFL,'(3(I0,A))') IOUT,C,30,C,1,C` (11); `      WRITE(IFL,'(A)') 'X Normal Stress'` (13); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,1,6,NNOD,IFL)` (15); `      WRITE(IFL,'(3(I0,A))') IOUT,C,31,C,1,C` (17); `      WRITE(IFL,'(A)') 'Y Normal Stress'` (19); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,2,6,NNOD,IFL)` (21); `      WRITE(IFL,'(3(I0,A))') IOUT,C,32,C,1,C` (23); `      WRITE(IFL,'(A)') 'Z Normal Stress'` (25); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,3,6,NNOD,IFL)` (27). |
| 29–48 | 시작 시 1행 fmp_sol0 루틴 안. SIGP의 성분 4·5·6을 항목 33·34·35의 XY·YZ·ZX 전단응력(shear stress)으로 출력하고 배열을 해제한다(29–47). 원문: `      WRITE(IFL,'(3(I0,A))') IOUT,C,33,C,1,C` (29); `      WRITE(IFL,'(A)') 'XY Shear Stress'` (31); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,4,6,NNOD,IFL)` (33); `      WRITE(IFL,'(3(I0,A))') IOUT,C,34,C,1,C` (35); `      WRITE(IFL,'(A)') 'YZ Shear Stress'` (37); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,5,6,NNOD,IFL)` (39); `      WRITE(IFL,'(3(I0,A))') IOUT,C,35,C,1,C` (41); `      WRITE(IFL,'(A)') 'ZX Shear Stress'` (43); `      CALL WT_VEC(0,0,0,7,INDG,SIGP,6,6,NNOD,IFL)` (45); `      DEALLOCATE( SIGP )` (47). |
| 49–67 | 시작 시 1행 fmp_sol0 루틴 안. PRNSIGP(3,NNOD)를 수집한다(49–51). 성분 1을 항목 36의 최대 주응력(principal stress), 성분 3을 항목 37의 최소 주응력으로 출력한다(53–63). 배열을 해제하고 종료한다(65–67). 원문: `      ALLOCATE( PRNSIGP(3,NNOD) )` (49); `      CALL GATHER_NODAL_D(PRNSIGP,3)` (51); `      WRITE(IFL,'(3(I0,A))') IOUT,C,36,C,1,C` (53); `      WRITE(IFL,'(A)') 'Max Prin Stress'` (55); `      CALL WT_VEC(0,0,0,7,INDG,PRNSIGP,1,3,NNOD,IFL)` (57); `      WRITE(IFL,'(3(I0,A))') IOUT,C,37,C,1,C` (59); `      WRITE(IFL,'(A)') 'Min Prin Stress'` (61); `      CALL WT_VEC(0,0,0,7,INDG,PRNSIGP,3,3,NNOD,IFL)` (63); `      DEALLOCATE( PRNSIGP )` (65); `      END` (67). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49–63: 주응력 배열의 첫 차원은 3이며 이 루틴은 성분 1·3만 출력한다.
