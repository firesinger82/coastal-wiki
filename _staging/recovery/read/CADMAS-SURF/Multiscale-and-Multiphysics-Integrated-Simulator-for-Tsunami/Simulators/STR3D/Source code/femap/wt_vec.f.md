---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/wt_vec.f
lines: 21
sha256: 9a51b9b52228d94a05fd832e68bef389e4f5d4b3347be06c6226145edc267285
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wt_vec.f — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | WT_VEC은 실수 IMPLICIT 선언과 ID(N)·X(NDF,N)를 사용한다. 고정 헤더, 성분 식별자 IDX·IDY·IDZ와 17개 정수 영값, 유형 ITYP를 기록한다. 9행 WRITE의 implied-DO 범위도 아래에 그대로 적었다. 원문: `      SUBROUTINE WT_VEC(IDX,IDY,IDZ,ITYP,ID,X,IDF,NDF,N,IFL)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      CHARACTER*1 C /','/` (4); `      DIMENSION ID(N),X(NDF,N)` (5); `      WRITE(IFL,'(A)') '1.,-1.,0.,'` (7); `      WRITE(IFL,'(10(I0,A))') IDX,C,IDY,C,IDZ,C,(0,C,I=1,17)` (9); `      WRITE(IFL,'(4(I0,A))') 0,C,0,C,0,C,ITYP,C` (11); `      WRITE(IFL,'(A)') '0,1,1,'` (13) |
| 15–21 | 1–N 루프에서 각 ID(I)와 X(IDF,I)를 쉼표 구분으로 출력한다. 이후 종료 레코드 -1,0.,를 기록하고 끝낸다. 원문: `      DO I = 1, N` (15); `        WRITE(IFL,'(I0,A,1PE11.4,A)') ID(I),C,X(IDF,I),C` (16); `      ENDDO` (17); `      WRITE(IFL,'(A)') '-1,0.,'` (19); `      END` (21) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·16: 성분 선택 인수 IDF를 X의 첫 첨자에 사용한다. 이 파일에는 IDF의 범위 검사문이 없다.
