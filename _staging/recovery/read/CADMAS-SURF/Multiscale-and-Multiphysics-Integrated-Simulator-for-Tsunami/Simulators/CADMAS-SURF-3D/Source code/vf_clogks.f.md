---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_clogks.f
lines: 40
sha256: e58e32160504d3aba8d0e8978023d742667eeffd40b01abe4f18461db5d2dd86
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_clogks.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 완전 거친 면(fully rough wall)의 마찰 속도(friction velocity) 계산 목적과 거리·속력·거칠기 인수를 선언한다. 원문: `      SUBROUTINE VF_CLOGKS(DL,VA,BKS,VT)` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_CLOGKS:完全粗面の摩擦速度の計算` (5) (VF_CLOGKS:완전 거친 면(fully rough wall)의 마찰 속도(friction velocity) 계산). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C     -- 大域変数 --` (12) (전역 변수). `      INCLUDE 'VF_A0PRM.h'` (13). `      INCLUDE 'VF_APHYSR.h'` (14). `CD    -- 引数 --` (16) (인수). `CD    DL  : IN  : R*8 : 流速の定義位置から壁面までの距離(△x/2)` (17) (DL  : IN  : R*8 : 유속 정의 위치에서 벽면까지의 거리(△x/2)). `CD    VA  : IN  : R*8 : 接線方向流速の絶対値(VA>=ZERO)` (18) (VA  : IN  : R*8 : 접선 방향 유속 절댓값(VA>=ZERO)). `CD    BKS : IN  : R*8 : 壁面の粗さ` (19) (BKS : IN  : R*8 : 벽면 거칠기(wall roughness)). `CD    VT  : OUT : R*8 : 摩擦速度` (20) (VT  : OUT : R*8 : 마찰 속도(friction velocity)). `C==== 実行 ===========================================================` (22) (실행). |
| 24–31 | 시작 시 `      SUBROUTINE VF_CLOGKS(DL,VA,BKS,VT)` (1) 블록 안. VT=0으로 시작한다. VA 또는 ANU0가 ZERO보다 작으면 `      IF (VA.LT.ZERO .OR. ANU0.LT.ZERO) GOTO 9000` (26)에 따라 33행의 레이블 9000으로 이동하여 계산을 건너뛴다. 그 외에는 로그 법칙(log law)의 분모를 구하고 VA를 나누어 VT를 설정한다. 원문: `CD    -- 流速や粘性係数がゼロならば摩擦速度もゼロとする --` (24) (유속이나 점성 계수가 0이면 마찰 속도(friction velocity)도 0으로 설정). `      VT=0.0D0` (25). `      IF (VA.LT.ZERO .OR. ANU0.LT.ZERO) GOTO 9000` (26). `CD    -- 摩擦速度の計算 --` (28) (마찰 속도(friction velocity) 계산). `      XX=LOG(DL/BKS)/AKK0+AKA0+3.0D0` (29). `      VT=VA/XX` (30). [11-04 전수 검증 보완] |
| 32–40 | 시작 시 `      SUBROUTINE VF_CLOGKS(DL,VA,BKS,VT)` (1) 블록 안. 조기 종료와 일반 종료가 공통 반환으로 이어진다. 원문: `C     -- 実行文の終了 --` (32) (실행문 종료). ` 9000 CONTINUE` (33). `      GOTO 9999` (34). `C==== 終了 ===========================================================` (36) (종료). ` 9999 CONTINUE` (38). `      RETURN` (39). `      END` (40). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26: 완전 거친 면 마찰 속도 계산도 ANU0.LT.ZERO 조건에서 건너뛴다.
- 29–30: LOG(DL/BKS),AKK0의 역수 및 VA/XX를 사용하며 해당 인수의 양수·0 여부 검사문은 이 루틴에 없다.
