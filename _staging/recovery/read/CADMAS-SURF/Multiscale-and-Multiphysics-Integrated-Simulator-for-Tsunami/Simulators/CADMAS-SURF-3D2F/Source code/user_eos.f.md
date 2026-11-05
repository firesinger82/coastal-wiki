---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/user_eos.f
lines: 44
sha256: baaf334592013b3566ec55a53b7c0b5d11a80cf7f33b9b69e4405328047d0525
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# user_eos.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 기체 상태방정식(equation of state) 루틴. 일본어 주석은 3행 개요, 5행 상태방정식 rho=rho(p), 7행 선언, 9행 전역형, 12행 인수, 13행 상태방정식 번호, 14행 상태방정식 매개변수, 15행 압력 p, 16행 기상 밀도 ρ, 17행 압력에 대한 밀도 미분계수 (dρ/dp)/ρ, 21행 실행을 뜻한다. IMPLICIT와 SPARAM(*)을 원문으로 적는다(10·19). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      SUBROUTINE USER_EOS(ISTATE,SPARAM,PP,RHOG,DRHODP)` (1)<br>`CD=== 概要 ===========================================================` (3)<br>`CDT   USER_EOS:状態方程式 rho=rho(p)` (5)<br>`C==== 宣言 ===========================================================` (7)<br>`C     -- 大域型 --` (9)<br>`      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)<br>`CD    -- 引数 --` (12)<br>`CD    ISTATE    : IN  : I*4 : 状態方程式番号` (13)<br>`CD    SPARAM    : IN  : R*8 : 状態方程式のパラメータ` (14)<br>`CD    PP        : IN  : R*8 : 圧力 p ` (15)<br>`CD    RHOG      : OUT : R*8 : 気相密度 ρ` (16)<br>`CD    DRHODP    : OUT : R*8 : 気相密度の圧力による微係数 (dρ/dp)/ρ` (17)<br>`      DIMENSION SPARAM(*)` (19)<br>`C==== 実行 ===========================================================` (21) |
| 23–44 | 시작 시 1행 루틴 안. ISTATE=1이면 SPARAM(1:3)에서 P0·RCONS·TCONS를 읽고 밀도와 정규화 압력 미분을 계산한다(23–34). 일본어 주석 25행은 기준 압력[Pa], 26행은 기체 상수[J/kg/K], 27행은 온도[K]를 뜻한다. ELSE는 VF_A2ERR이며 40행은 종료를 뜻한다(36–44). 원문(연속행은 아래 행 번호 순서로 이어지는 한 문장): `      IF(ISTATE.EQ.1) THEN` (23)<br>`C` (24)<br>`C P0    : 基準圧力[Pa]` (25)<br>`C RCONS : 気体定数[J/kg/K]` (26)<br>`C TCONS : 温度[K]` (27)<br>`C` (28)<br>`        P0    = SPARAM(1)` (29)<br>`        RCONS = SPARAM(2)` (30)<br>`        TCONS = SPARAM(3)` (31)<br>`        RHOG   = (PP + P0)/(RCONS*TCONS)` (33)<br>`        DRHODP = 1.0D0/(PP + P0)` (34)<br>`      ELSE` (36)<br>`        CALL VF_A2ERR('USER_EOS','ISTATE ERROR.')` (37)<br>`      END IF` (38)<br>`C==== 終了 ===========================================================` (40)<br>` 9999 CONTINUE` (42)<br>`      RETURN` (43)<br>`      END` (44) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–38: 구현한 상태방정식 번호는 1이다. 나머지는 VF_A2ERR를 호출한다.
- 33–34: RCONS*TCONS와 PP+P0를 분모로 사용한다. 이 식 앞에 분모 0을 검사하는 문장은 없다.
