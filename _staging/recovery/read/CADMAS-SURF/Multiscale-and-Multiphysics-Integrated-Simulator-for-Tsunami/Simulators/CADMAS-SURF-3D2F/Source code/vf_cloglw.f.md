---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_cloglw.f
lines: 62
sha256: 5ad8291f891d27bd16f9c4447e2b14fd39c5c1d7e3a2f930af5672668eb96ca4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_cloglw.f — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | 로그법칙(log law) 마찰속도(friction velocity) 루틴이다. 주석은 함수와 도함수를 제시한다(5–7). 인수와 INCLUDE 선언을 둔다(12–22).<br>`      SUBROUTINE VF_CLOGLW(DL,VA,ANU1,VT)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CLOGLW:対数則を満たす摩擦速度の計算` (5) (VF_CLOGLW:로그법칙(log law)을 만족하는 마찰속도 계산).<br>주석 원문(실행하지 않음): `CD      (1)F (x)=vt/κ*log(dl*vt/ν)+vt*A-Va` (6).<br>주석 원문(실행하지 않음): `CD      (2)F'(x)=1/κ*log(dl*vt/ν)+1/κ+A` (7).<br>`C==== 宣言 ===========================================================` (9) (선언).<br>`C     -- 大域型 --` (11) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12).<br>`C     -- 大域変数 --` (14) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (15).<br>`      INCLUDE 'VF_APHYSR.h'` (16).<br>`CD    -- 引数 --` (18) (인수).<br>`CD    DL   : IN  : R*8 : 流速の定義位置から壁面までの距離(△x/2)` (19) (DL   : IN  : R*8 : 유속 정의 위치에서 벽면까지의 거리(△x/2)).<br>`CD    VA   : IN  : R*8 : 接線方向流速の絶対値(VA>=ZERO)` (20) (VA   : IN  : R*8 : 접선방향 유속의 절댓값(VA>=ZERO)).<br>`CD    ANU1 : IN  : R*8 : 分子動粘性係数（２相混合）` (21) (ANU1 : IN  : R*8 : 분자 동점성계수(2상 혼합)).<br>`CD    VT   : OUT : R*8 : 摩擦速度` (22) (VT   : OUT : R*8 : 마찰속도(friction velocity)).<br>`C==== 実行 ===========================================================` (24) (실행). |
| 26–40 | 시작 시 1행 SUBROUTINE VF_CLOGLW 루틴 안. 유속·점성이 작으면 0으로 반환한다(27–28). 뉴턴법(Newton method)의 최대 반복 횟수 20, 상대 판정값 1.0D-10, 역수와 초깃값을 설정한다(32–39).<br>`CD    -- 流速や粘性係数がゼロならば摩擦速度もゼロとする --` (26) (유속이나 점성계수가 0이면 마찰속도도 0으로 한다).<br>`      VT=0.0D0` (27).<br>`      IF (VA.LT.ZERO .OR. ANU1.LT.ZERO) GOTO 9000` (28).<br>`CD    -- 初期設定 --` (30) (초기 설정).<br>`C     * Newton法の最大反復回数` (31) (* 뉴턴법(Newton method) 최대 반복 횟수).<br>`      NI=20` (32).<br>`C     * 収束判定のための微小量` (33) (* 수렴 판정용 작은 값).<br>`      EPS=1.0D-10` (34).<br>`C     * 各種逆数` (35) (* 각종 역수).<br>`      AKR=1.0D0/AKK0` (36).<br>`      ANR=1.0D0/ANU1` (37).<br>`C     * Newton法の初期値:logの値がゼロになる` (38) (* 뉴턴법 초깃값: log 값이 0이 된다).<br>`      XX=ANU1/DL` (39).<br>28행의 정확한 조건은 `IF (VA.LT.ZERO .OR. ANU1.LT.ZERO) GOTO 9000`이다. 대상은 55행 `9000 CONTINUE`이다. [11-04 전수 검증 보완] |
| 41–62 | 시작 시 1행 SUBROUTINE VF_CLOGLW 루틴 안. 뉴턴 반복에서 함수·미분·보정량을 계산하고 상대 보정량 조건으로 탈출한다(42–50). 51행은 `ABS(DX).GE.XX*EPS`이면 `CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')`를 실행한다. 다음 실행문은 52행 `VT=XX`이다. VF_A2ERR 내부의 반환 여부는 이 구간에서 확인하지 않는다.<br>`CD    -- Newton法の反復 --` (41) (뉴턴법 반복).<br>`      DO 100 I=1,NI` (42).<br>`        W=LOG(DL*XX*ANR)` (43).<br>`        F=XX*AKR*W+XX*AKA0-VA` (44).<br>`        D=AKR*W+AKR+AKA0` (45).<br>`        DX=-F/D` (46).<br>`        XX=XX+DX` (47).<br>`        IF (ABS(DX).LT.XX*EPS) GOTO 110` (48).<br>` 100  CONTINUE` (49).<br>` 110  CONTINUE` (50).<br>`      IF (ABS(DX).GE.XX*EPS) CALL VF_A2ERR('VF_CLOGLW','NOT CONVERGED.')` (51).<br>`      VT=XX` (52).<br>`C     -- 実行文の終了 --` (54) (실행문 종료).<br>` 9000 CONTINUE` (55).<br>`      GOTO 9999` (56).<br>`C==== 終了 ===========================================================` (58) (종료).<br>` 9999 CONTINUE` (60).<br>`      RETURN` (61).<br>`      END` (62).<br>42행 `DO 100 I=1,NI`는 49행에서 닫힌다. 48행 `GOTO 110`은 루프 밖의 50행으로 이동한다. 56행 `GOTO 9999`는 60행으로 이동한다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32·34: 최대 반복 횟수는 20이고 EPS는 1.0D-10으로 고정된다.
- 43–47: 반복식은 log(DL*XX*ANR) 및 -F/D를 사용한다. 이 루프에는 로그 인수 양수 또는 D=0 여부를 따로 검사하는 문장이 없다.
