---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_clogks.f
lines: 41
sha256: 50be4321ad41b919fb3364252f7b5ac43777b5be6b37818ef3cc69136441154d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_clogks.f — 판독 구간 기록

구간은 1행부터 41행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 완전 거친 면의 마찰속도(friction velocity) 계산 루틴이다. DL·VA·BKS·ANU1·VT 인수를 설명한다(17–21).<br>`      SUBROUTINE VF_CLOGKS(DL,VA,BKS,ANU1,VT)` (1).<br>`CD=== 概要 ===========================================================` (3) (개요).<br>`CDT   VF_CLOGKS:完全粗面の摩擦速度の計算` (5) (VF_CLOGKS:완전 거친 면의 마찰속도(friction velocity) 계산).<br>`C==== 宣言 ===========================================================` (7) (선언).<br>`C     -- 大域型 --` (9) (전역 형).<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10).<br>`C     -- 大域変数 --` (12) (전역 변수).<br>`      INCLUDE 'VF_A0PRM.h'` (13).<br>`      INCLUDE 'VF_APHYSR.h'` (14).<br>`CD    -- 引数 --` (16) (인수).<br>`CD    DL   : IN  : R*8 : 流速の定義位置から壁面までの距離(△x/2)` (17) (DL   : IN  : R*8 : 유속 정의 위치에서 벽면까지의 거리(△x/2)).<br>`CD    VA   : IN  : R*8 : 接線方向流速の絶対値(VA>=ZERO)` (18) (VA   : IN  : R*8 : 접선방향 유속의 절댓값(VA>=ZERO)).<br>`CD    BKS  : IN  : R*8 : 壁面の粗さ` (19) (BKS  : IN  : R*8 : 벽면 거칠기).<br>`CD    ANU1 : IN  : R*8 : 分子動粘性係数（２相混合）` (20) (ANU1 : IN  : R*8 : 분자 동점성계수(2상 혼합)).<br>`CD    VT   : OUT : R*8 : 摩擦速度` (21) (VT   : OUT : R*8 : 마찰속도(friction velocity)).<br>`C==== 実行 ===========================================================` (23) (실행). |
| 25–41 | 시작 시 1행 SUBROUTINE VF_CLOGKS 루틴 안. VA 또는 ANU1이 ZERO보다 작으면 VT=0으로 반환한다(26–27). 그 외에는 거칠기 로그식과 VA/XX로 VT를 계산한다(30–31).<br>`CD    -- 流速や粘性係数がゼロならば摩擦速度もゼロとする --` (25) (유속이나 점성계수가 0이면 마찰속도도 0으로 한다).<br>`      VT=0.0D0` (26).<br>`      IF (VA.LT.ZERO .OR. ANU1.LT.ZERO) GOTO 9000` (27).<br>`CD    -- 摩擦速度の計算 --` (29) (마찰속도 계산).<br>`      XX=LOG(DL/BKS)/AKK0+AKA0+3.0D0` (30).<br>`      VT=VA/XX` (31).<br>`C     -- 実行文の終了 --` (33) (실행문 종료).<br>` 9000 CONTINUE` (34).<br>`      GOTO 9999` (35).<br>`C==== 終了 ===========================================================` (37) (종료).<br>` 9999 CONTINUE` (39).<br>`      RETURN` (40).<br>`      END` (41).<br>27행 `GOTO 9000`은 34행 `9000 CONTINUE`로 이동한다. 35행 `GOTO 9999`는 39행으로 이동한다. 40행 RETURN으로 복귀한다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·30–31: VA·ANU1의 작은 값 검사는 있으나 DL/BKS의 양수 여부와 XX=0 여부 검사는 이 파일에 없다.
- 20·27·30–31: ANU1은 조기 반환 조건에만 쓰인다. 마찰속도 계산식 자체에는 ANU1이 없다.
