---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ztimec.f
lines: 59
sha256: e6a8520e4e68589f1114012b2642c8388d064f4086d88086a2cebf0f50705f8e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_ztimec.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 경과시간(elapsed time) 측정 루틴이다. 주석은 사용자 시간과 시스템 시간의 합을 경과시간이라고 설명하고 기종 의존성을 적는다. IMPLICIT과 단정밀도 E·T(2)·ETIME을 선언한다. 원문: `      SUBROUTINE VF_ZTIMEC(TALL,TUSER,TSYS)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZTIMEC:経過時間を計測` (5) (경과시간을 측정한다)。 `CD      (1)ユーザ時間とシステム時間の和が経過時間` (6) (사용자 시간과 시스템 시간의 합이 경과시간)。 `CD      (2)機種依存性有り` (7) (기종 의존성이 있다)。 `C==== 宣言 ===========================================================` (9) (선언)。 `C     -- 大域型 --` (11) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (12)。 `CD    -- 引数 --` (14) (인수)。 `CD    TALL  : OUT : R*8 : 経過時間` (15) (경과시간)。 `CD    TUSER : OUT : R*8 : ユーザ時間` (16) (사용자 시간)。 `CD    TSYS  : OUT : R*8 : システム時間` (17) (시스템 시간)。 `CD    -- 局所変数 --` (19) (지역 변수)。 `      REAL E,T(2),ETIME` (20)。 `C==== 実行 ===========================================================` (22) (실행)。 |
| 24–40 | 시작 시 1행 SUBROUTINE VF_ZTIMEC 루틴 안. 오류 검사기를 피하기 위한 T(1)·T(2)=0 초기화다. Compaq용 ETIME 호출과 DBLE 변환, Intel/Linux용 CPU_TIME 호출 및 출력 대입은 전부 주석 처리된 코드다. 원문: `CD    -- エラーチェッカーをごまかすため --` (24) (오류 검사기를 속이기 위해)。 `      T(1)=0.0E0` (25)。 `      T(2)=0.0E0` (26)。 `CD    -- 経過時間を計測 --` (28) (경과시간 측정)。 `C     * for Compaq Tru64 UNIX V5.1` (29)。 `C     E=ETIME(T)` (30)。 `C     TALL =DBLE(E   )` (31)。 `C     TUSER=DBLE(T(1))` (32)。 `C     TSYS =DBLE(T(2))` (33)。 `C     * for Intel/LINUX` (35)。 `C     CALL CPU_TIME(E)` (36)。 `C     TALL =0.0D0` (37)。 `C     TUSER=DBLE(E)` (38)。 `C     TSYS =0.0D0` (39)。 |
| 41–51 | 시작 시 1행 SUBROUTINE VF_ZTIMEC 루틴 안. 활성 경로는 VF_P0TIME(PT)를 호출하고 TALL=0, TUSER=PT, TSYS=0으로 반환값을 정한다. 더미(dummy) 시간 대입 세 개는 주석 처리된 코드다. 원문: `C     * for MPI` (41)。 `      CALL VF_P0TIME(PT)` (42)。 `      TALL =0.0D0` (43)。 `      TUSER=PT` (44)。 `      TSYS =0.0D0` (45)。 `C     * ダミーの場合` (47) (더미인 경우)。 `C     TALL =0.0D0` (48)。 `C     TUSER=0.0D0` (49)。 `C     TSYS =0.0D0` (50)。 |
| 52–59 | 시작 시 1행 SUBROUTINE VF_ZTIMEC 루틴 안. 9999 종료 표지로 이동하고 반환한다. 원문: `C     -- 実行文の終了 --` (52) (실행문 종료)。 `      GOTO 9999` (53)。 `C==== 終了 ===========================================================` (55) (종료)。 ` 9999 CONTINUE` (57)。 `      RETURN` (58)。 `      END` (59)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5–7·42–45: 개요 주석은 사용자 시간과 시스템 시간의 합을 경과시간으로 설명한다. 활성 경로는 VF_P0TIME 결과를 TUSER에 넣고 TALL·TSYS를 0으로 설정한다.
- 20·25–39: ETIME·CPU_TIME 경로는 주석 처리되어 있다. 활성 실행문에서 T(1)·T(2)는 0 대입 이후 참조하지 않는다.
