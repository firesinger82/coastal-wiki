---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/crh2set.f
lines: 39
sha256: 1a91473e224446d4b8855050e8ed8b4835e35561906cde8295c89ebf9f11a36c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# crh2set.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | 루틴·암시적 자료형·배열을 선언한다(1–6). IS를 1로 초기화하고 접촉점 1..NINDC를 순회한다(8–10). 상태 1·2·3·4·5에 따라 CRH2VRTX·CRH2EDGE·CRH2FACE·CRH2STKE·CRH2STKF를 호출한다(14–34). 각 상태는 기본 길이 3·14·11·6·9만큼 IS를 늘리고 IVRQ·IEDQ·IFCQ가 양수이면 각각 9·12·3·6·3을 더한다. 루프·루틴을 닫는다(35–39). 원문: `      SUBROUTINE CRH2SET(CRH,NINDC,ISLV,INDC,IEDG,IELC,IVRQ,IEDQ,IFCQ` `     &                  ,POS,IRH)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION ISLV(2,NINDC),POS(3,*),IELC(3,*),INDC(NINDC),IEDG(6,*)` `     &         ,CRH(*),IRH(2,*),IVRQ(*),IEDQ(*),IFCQ(*)` (5–6, 하나의 고정형식 연속문); `      IS=1` (8); `      DO 100 I=1,NINDC` (10); `        NS =INDC(I)` (11); `        IST=ISLV(1,I)` (12); `        MA =ISLV(2,I)` (13); `        IF( IST .EQ. 1 ) THEN` (14); `          CALL CRH2VRTX(CRH(IS),IVRQ(MA))` (15); `          IS=IS+3` (16); `          IF( IVRQ(MA) .GT. 0 ) IS=IS+9` (17); `        ELSEIF( IST .EQ. 2 ) THEN` (18); `          CALL CRH2EDGE(CRH(IS),NS,IRH(2,IS),IEDG(1,MA),IEDQ(MA),POS)` (19); `          IS=IS+14` (20); `          IF( IEDQ(MA) .GT. 0 ) IS=IS+12` (21); `        ELSEIF( IST .EQ. 3 ) THEN` (22); `          CALL CRH2FACE(CRH(IS),NS,IRH(2,IS),IRH(2,IS+1),IELC(1,MA)` `     &                 ,IFCQ(MA),POS)` (23–24, 하나의 고정형식 연속문); `          IS=IS+11` (25); `          IF( IFCQ(MA) .GT. 0 ) IS=IS+3` (26); `        ELSEIF( IST .EQ. 4 ) THEN` (27); `          CALL CRH2STKE(CRH(IS),NS,IEDG(1,MA),IEDQ(MA),POS)` (28); `          IS=IS+6` (29); `          IF( IEDQ(MA) .GT. 0 ) IS=IS+6` (30); `        ELSEIF( IST .EQ. 5 ) THEN` (31); `          CALL CRH2STKF(CRH(IS),NS,IELC(1,MA),IFCQ(MA),POS)` (32); `          IS=IS+9` (33); `          IF( IFCQ(MA) .GT. 0 ) IS=IS+3` (34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–35: 상태 1..5 이외를 처리하는 ELSE는 없으며 그 경우 IS를 증가시키지 않는다.
