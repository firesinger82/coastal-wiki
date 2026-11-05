---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mstnod.f
lines: 33
sha256: 2f4de734b91553f9faff31a42d99b7837e74c0c99b40ee1d10c79deedb6ef88a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mstnod.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | MSTNOD는 IST에 따라 주절점(master node) 목록 IG와 수 N을 반환한다. IST=1 또는 11이면 IVRQ>0일 때 사각형 네 절점, 그 밖에는 MA 한 절점을 선택한다(6–14). 배열 선언과 빈 줄을 포함한다. 원문: `      SUBROUTINE MSTNOD(N,IG,IST,MA,IELC,IEDG,IELQ,IFCQ,IEDQ,IVRQ)` (1). 연속문(3–4): `      DIMENSION IG(*),IEDG(6,*),IELC(3,*),IELQ(4,*),IVRQ(*),IEDQ(*)` (3); `     &         ,IFCQ(*)` (4). `      SELECT CASE( IST )` (6). `      CASE( 1, 11 )` (7). `        IF( IVRQ(MA) > 0 ) THEN` (8). `          N = 4` (9). `          IG(1:4) = IELQ(:,IVRQ(MA))` (10). `        ELSE` (11). `          N = 1` (12). `          IG(1) = MA` (13). `        ENDIF` (14). |
| 15–33 | 시작 시 1행 MSTNOD 루틴·6행 `SELECT CASE( IST )` 안. 이 블록은 31행 `END SELECT`에서 닫힌다. IST=2,12,14이면 IEDQ로 사각형 네 절점 또는 변 두 절점을 선택한다(15–22). IST=3,13,15이면 IFCQ로 사각형 네 절점 또는 면 세 절점을 선택한다(23–30). SELECT 종료와 END를 포함한다. 원문: `      CASE( 2, 12, 14 )` (15). `        IF( IEDQ(MA) > 0 ) THEN` (16). `          N = 4` (17). `          IG(1:4) = IELQ(:,IEDQ(MA))` (18). `        ELSE` (19). `          N = 2` (20). `          IG(1:2) = IEDG(1:2,MA)` (21). `        ENDIF` (22). `      CASE( 3, 13, 15 )` (23). `        IF( IFCQ(MA) > 0 ) THEN` (24). `          N = 4` (25). `          IG(1:4) = IELQ(:,IFCQ(MA))` (26). `        ELSE` (27). `          N = 3` (28). `          IG(1:3) = IELC(:,MA)` (29). `        ENDIF` (30). `      END SELECT` (31). `      END` (33). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–31: IST=4,5에 대한 CASE와 CASE DEFAULT가 없다.
