---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fmp_soil0.f
lines: 43
sha256: 1e6c520f5b5aa6a0600b3ab80b22550bf788dd3cab85f094d0ce95cd8d191bef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fmp_soil0.f — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | INDG(NNOD)와 결과 포인터를 선언한다(3–5). TVELP(NNOD)를 수집하고 항목 71의 총간극수 유량(pore water flux)을 WT_VEC으로 출력한 뒤 해제한다(7–17). 원문: `      SUBROUTINE FMP_SOIL0(IOUT,INDG,NNOD,IFL)` (1); `      CHARACTER*1 C /','/` (3); `      DIMENSION INDG(NNOD)` (4); `      REAL(8), POINTER :: TVELP(:),VELP(:,:)` (5); `      ALLOCATE( TVELP(NNOD) )` (7); `      CALL GATHER_NODAL_D(TVELP,1)` (9); `      WRITE(IFL,'(3(I0,A))') IOUT,C,71,C,1,C` (11); `      WRITE(IFL,'(A)') 'Total Pore Water Flux'` (13); `      CALL WT_VEC(72,73,74,7,INDG,TVELP,1,1,NNOD,IFL)` (15); `      DEALLOCATE( TVELP )` (17). |
| 19–43 | 시작 시 1행 fmp_soil0 루틴 안. VELP(3,NNOD)를 수집한다(19–21). 항목 72·73·74로 X·Y·Z 간극수 유량을 출력한다(23–39). 배열 해제 후 종료한다(41–43). 원문: `      ALLOCATE( VELP(3,NNOD) )` (19); `      CALL GATHER_NODAL_D(VELP,3)` (21); `      WRITE(IFL,'(3(I0,A))') IOUT,C,72,C,1,C` (23); `      WRITE(IFL,'(A)') 'X Pore Water Flux'` (25); `      CALL WT_VEC(72,0,0,7,INDG,VELP,1,3,NNOD,IFL)` (27); `      WRITE(IFL,'(3(I0,A))') IOUT,C,73,C,1,C` (29); `      WRITE(IFL,'(A)') 'Y Pore Water Flux'` (31); `      CALL WT_VEC(0,73,0,7,INDG,VELP,2,3,NNOD,IFL)` (33); `      WRITE(IFL,'(3(I0,A))') IOUT,C,74,C,1,C` (35); `      WRITE(IFL,'(A)') 'Z Pore Water Flux'` (37); `      CALL WT_VEC(0,0,74,7,INDG,VELP,3,3,NNOD,IFL)` (39); `      DEALLOCATE( VELP )` (41); `      END` (43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
