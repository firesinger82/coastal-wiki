---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cgrid.f
lines: 80
sha256: 5825399e9efab274ae2caeb46f8cf0aa33a52d7ed7d1dd9526d736df0fdc7a92
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cgrid.f — 판독 구간 기록

구간은 1행부터 80행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 격자 좌표 파생 자료 설정 목적과 방향·오른쪽 끝 좌표·격자 크기를 선언한다. 원문: `      SUBROUTINE VF_CGRID(ISW,XYZ,XBUF,NUML)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CGRID:x,yまたはz方向格子関連データを設定` (5) (VF_CGRID:x,y 또는 z 방향 격자 관련 자료 설정). `CD      (1)仮想セルの幅は内側と等しいと仮定` (6) ((1)가상 셀(ghost cell)의 폭은 내부와 같다고 가정). `C==== 宣言 ===========================================================` (8) (선언). `C     -- 大域型 --` (10) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11). `C     -- 大域変数 --` (13) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (14). `      INCLUDE 'VF_APARAI.h'` (15). `CD    -- 引数 --` (17) (인수). `CD    ISW             : IN  : I*4 : 方向(X:=1,Y:=2,Z:=3)` (18) (ISW             : IN  : I*4 : 방향(X:=1,Y:=2,Z:=3)). `CD    XYZ(MAXG1,NUML) : I/O : R*8 : x,yまたはz方向格子座標等` (19) (XYZ(MAXG1,NUML) : I/O : R*8 : x,y 또는 z 방향 격자 좌표 등). `CD    XBUF            : IN  : R*8 : 右端の座標値(通信をしないため)` (20) (XBUF            : IN  : R*8 : 오른쪽 끝 좌표값(통신하지 않기 때문)). `CD    NUML            : IN  : I*4 : 格子数+1` (21) (NUML            : IN  : I*4 : 격자 수+1). `      DIMENSION XYZ(MAXG1,NUML)` (22). `C==== 実行 ===========================================================` (24) (실행). |
| 26–41 | 시작 시 `      SUBROUTINE VF_CGRID(ISW,XYZ,XBUF,NUML)` (1) 블록 안. x,y 방향은 전역 격자 수와 병렬 영역을 선택하고 그 외는 전체 방향으로 설정한다. 시작 전역 번호 1은 2로 바꾼다. 원문: `CD    -- 初期設定 --` (26) (초기 설정). `      IF     (ISW.EQ.1) THEN` (27). `        NUML0=NUMI0` (28). `        LG1=MYGIS` (29). `        LG2=MYGIE` (30). `      ELSEIF (ISW.EQ.2) THEN` (31). `        NUML0=NUMJ0` (32). `        LG1=MYGJS` (33). `        LG2=MYGJE` (34). `      ELSE` (35). `        NUML0=NUML` (36). `        LG1=1` (37). `        LG2=NUML0` (38). `      ENDIF` (39). `      IF (LG1.EQ.1) LG1=2` (40). |
| 42–62 | 시작 시 `      SUBROUTINE VF_CGRID(ISW,XYZ,XBUF,NUML)` (1) 블록 안. 내부 격자폭과 역수를 구한다. 물리 경계의 가상 셀(ghost cell) 폭은 내부 폭을 복사하고 분할 영역 끝은 입력 좌표 또는 XBUF를 사용한다. 원문: `CD    -- dx=X(I+1)-X(I)と1/dxの計算 --` (42) (dx=X(I+1)-X(I)와 1/dx 계산). `      DO 100 I=2,NUML-1` (43). `        XYZ(2,I)=XYZ(1,I+1)-XYZ(1,I)` (44). `        XYZ(4,I)=1.0D0/XYZ(2,I)` (45). ` 100  CONTINUE` (46). `      IF (LG1.EQ.2) THEN` (47). `        XYZ(2,1)=XYZ(2,2)` (48). `        XYZ(4,1)=1.0D0/XYZ(2,1)` (49). `        XYZ(1,1)=XYZ(1,2)-XYZ(2,1)` (50). `      ELSE` (51). `        XYZ(2,1)=XYZ(1,2)-XYZ(1,1)` (52). `        XYZ(4,1)=1.0D0/XYZ(2,1)` (53). `      ENDIF` (54). `      IF (LG2.EQ.NUML0) THEN` (55). `        XYZ(2,NUML)=XYZ(2,NUML-1)` (56). `        XYZ(4,NUML)=1.0D0/XYZ(2,NUML)` (57). `      ELSE` (58). `        XYZ(2,NUML)=XBUF-XYZ(1,NUML)` (59). `        XYZ(4,NUML)=1.0D0/XYZ(2,NUML)` (60). `      ENDIF` (61). |
| 63–80 | 시작 시 `      SUBROUTINE VF_CGRID(ISW,XYZ,XBUF,NUML)` (1) 블록 안. 인접 두 폭의 평균과 그 역수·두 폭 합의 역수를 계산한다. 첫 원소의 세 값은 0으로 설정하고 반환한다. 원문: `CD    -- cx=(dx(I)+dx(I-1))/2.0、1/cxと1/(dx+dx)の計算 --` (63) (cx=(dx(I)+dx(I-1))/2.0,1/cx와 1/(dx+dx) 계산). `      DO 200 I=2,NUML` (64). `        XYZ(3,I)=(XYZ(2,I)+XYZ(2,I-1))/2.0D0` (65). `        XYZ(5,I)=1.0D0/XYZ(3,I)` (66). `        XYZ(6,I)=1.0D0/(XYZ(2,I)+XYZ(2,I-1))` (67). ` 200  CONTINUE` (68). `      XYZ(3,1)=0.0D0` (69). `      XYZ(5,1)=0.0D0` (70). `      XYZ(6,1)=0.0D0` (71). `C     -- 実行文の終了 --` (73) (실행문 종료). `      GOTO 9999` (74). `C==== 終了 ===========================================================` (76) (종료). ` 9999 CONTINUE` (78). `      RETURN` (79). `      END` (80). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 44–67: 좌표 차와 평균 폭의 역수를 계산하며 좌표 단조성·0 폭을 검사하는 문장은 이 루틴에 없다.
