---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_cloglw.f
lines: 61
sha256: 458ab8ba85736b9cfe0bb9e2b5604d8345d9735d3cdef6862372ee8873182fa9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cloglw.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 로그 법칙(log law) 마찰 속도(friction velocity) 계산의 함수·미분 주석과 인수를 선언한다. 원문: `      SUBROUTINE VF_CLOGLW(DL,VA,VT)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CLOGLW:対数則を満たす摩擦速度の計算` (5) (VF_CLOGLW:로그 법칙(log law)을 만족하는 마찰 속도(friction velocity) 계산). 주석: `CD      (1)F (x)=vt/κ*log(dl*vt/ν)+vt*A-Va` (6). 주석: `CD      (2)F'(x)=1/κ*log(dl*vt/ν)+1/κ+A` (7). `C==== 宣言 ===========================================================` (9) (선언). `C     -- 大域型 --` (11) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12). `C     -- 大域変数 --` (14) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (15). `      INCLUDE 'VF_APHYSR.h'` (16). `CD    -- 引数 --` (18) (인수). `CD    DL : IN  : R*8 : 流速の定義位置から壁面までの距離(△x/2)` (19) (DL : IN  : R*8 : 유속 정의 위치에서 벽면까지의 거리(△x/2)). `CD    VA : IN  : R*8 : 接線方向流速の絶対値(VA>=ZERO)` (20) (VA : IN  : R*8 : 접선 방향 유속 절댓값(VA>=ZERO)). `CD    VT : OUT : R*8 : 摩擦速度` (21) (VT : OUT : R*8 : 마찰 속도(friction velocity)). `C==== 実行 ===========================================================` (23) (실행). |
| 25–39 | 시작 시 `      SUBROUTINE VF_CLOGLW(DL,VA,VT)` (1) 블록 안. 속력 또는 분자 점성이 ZERO보다 작으면 VT=0을 유지하고 `      IF (VA.LT.ZERO .OR. ANU0.LT.ZERO) GOTO 9000` (27)에 따라 54행의 레이블 9000으로 이동한다. 뉴턴 방법(Newton method)은 최대 20회,EPS=1D-10이며 초기값은 ANU0/DL이다. 원문: `CD    -- 流速や粘性係数がゼロならば摩擦速度もゼロとする --` (25) (유속이나 점성 계수가 0이면 마찰 속도(friction velocity)도 0으로 설정). `      VT=0.0D0` (26). `      IF (VA.LT.ZERO .OR. ANU0.LT.ZERO) GOTO 9000` (27). `CD    -- 初期設定 --` (29) (초기 설정). `C     * Newton法の最大反復回数` (30) (* 뉴턴 방법(Newton method)의 최대 반복 횟수). `      NI=20` (31). `C     * 収束判定のための微小量` (32) (* 수렴(convergence) 판정을 위한 작은 값). `      EPS=1.0D-10` (33). `C     * 各種逆数` (34) (* 각종 역수). `      AKR=1.0D0/AKK0` (35). `      ANR=1.0D0/ANU0` (36). `C     * Newton法の初期値:logの値がゼロになる` (37) (* 뉴턴 방법(Newton method) 초기값: log 값이 0이 됨). `      XX=ANU0/DL` (38). [11-04 전수 검증 정정] |
| 40–52 | 시작 시 `      SUBROUTINE VF_CLOGLW(DL,VA,VT)` (1) 블록 안. 매 반복에서 로그·함수·도함수와 증분을 계산한다. `        IF (ABS(DX).LT.XX*EPS) GOTO 110` (47)이 참이면 49행의 레이블 110으로 이동한다. 41행 DO는 48행의 레이블 100에서 닫힌다. `      IF (ABS(DX).GE.XX*EPS) CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')` (50)에 따라 오류 루틴을 호출한다. VT에 XX를 넣는다. 원문: `CD    -- Newton法の反復 --` (40) (뉴턴 방법(Newton method) 반복). `      DO 100 I=1,NI` (41). `        W=LOG(DL*XX*ANR)` (42). `        F=XX*AKR*W+XX*AKA0-VA` (43). `        D=AKR*W+AKR+AKA0` (44). `        DX=-F/D` (45). `        XX=XX+DX` (46). `        IF (ABS(DX).LT.XX*EPS) GOTO 110` (47). ` 100  CONTINUE` (48). ` 110  CONTINUE` (49). `      IF (ABS(DX).GE.XX*EPS) CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')` (50). `      VT=XX` (51). [11-04 전수 검증 보완] |
| 53–61 | 시작 시 `      SUBROUTINE VF_CLOGLW(DL,VA,VT)` (1) 블록 안. 공통 반환 경로다. 원문: `C     -- 実行文の終了 --` (53) (실행문 종료). ` 9000 CONTINUE` (54). `      GOTO 9999` (55). `C==== 終了 ===========================================================` (57) (종료). ` 9999 CONTINUE` (59). `      RETURN` (60). `      END` (61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–50: 뉴턴 반복에는 로그 인수의 양수 여부·도함수 D=0·갱신 XX의 양수 여부를 검사하거나 보정하는 문장이 없다.
- 31–33: 최대 반복 횟수 20과 허용오차 1.0D-10은 루틴 내부 상수 대입이다.
