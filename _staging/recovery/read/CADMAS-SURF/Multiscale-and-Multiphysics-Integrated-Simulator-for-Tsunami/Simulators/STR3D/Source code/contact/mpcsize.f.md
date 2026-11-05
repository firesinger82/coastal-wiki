---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/mpcsize.f
lines: 39
sha256: f5681096d0f9988d26c9e009681f87372efffa0c608ff31a7b0e7fcd0017e53f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mpcsize.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | MPCSIZE는 NIDEP와 NIRH를 0으로 초기화하고 NINDC 접촉을 순회한다(5–10). ISLV,IVRQ,IEDQ,IFCQ의 배열 선언을 포함한다. 원문: `      SUBROUTINE MPCSIZE(NIDEP,NIRH,NINDC,ISLV,IVRQ,IEDQ,IFCQ)` (1). `      DIMENSION ISLV(2,*),IVRQ(*),IEDQ(*),IFCQ(*)` (3). `      NIDEP=0` (5). `      NIRH=0` (6). `      DO 100 K=1,NINDC` (8). `        IST=ISLV(1,K)` (9). `        MA =ISLV(2,K)` (10). |
| 11–39 | 시작 시 1행 MPCSIZE 루틴·8행 `DO 100 K=1,NINDC` 안. 이 루프는 37행 `100 CONTINUE`에서 닫힌다. IST=1/11은 I=3,J=3을 설정한다(11–13). IVRQ(MA)>0이면 J에 9를 추가한다(14). IST=2/12는 I=2,J=14를 설정한다(15–17). IEDQ(MA)>0이면 J에 12를 추가한다(18). IST=3/13은 I=1,J=11을 설정한다(19–21). IFCQ(MA)>0이면 J에 3을 추가한다(22). IST=4/14는 I=3,J=6을 설정한다(23–25). IEDQ(MA)>0이면 J에 6을 추가한다(26). IST=5/15는 I=3,J=9를 설정한다(27–29). IFCQ(MA)>0이면 J에 3을 추가한다(30). 그 밖에는 I,J를 0으로 한다(31–34). 각 값을 NIDEP,NIRH에 누적한다(35–37). END를 포함한다. 원문: `        IF( IST .EQ. 1 .OR. IST .EQ. 11 ) THEN` (11). `          I=3` (12). `          J=3` (13). `          IF( IVRQ(MA) .GT. 0 ) J=J+9` (14). `        ELSEIF( IST .EQ. 2 .OR. IST .EQ. 12 ) THEN` (15). `          I=2` (16). `          J=14` (17). `          IF( IEDQ(MA) .GT. 0 ) J=J+12` (18). `        ELSEIF( IST .EQ. 3 .OR. IST .EQ. 13 ) THEN` (19). `          I=1` (20). `          J=11` (21). `          IF( IFCQ(MA) .GT. 0 ) J=J+3` (22). `        ELSEIF( IST .EQ. 4 .OR. IST .EQ. 14 ) THEN` (23). `          I=3` (24). `          J=6` (25). `          IF( IEDQ(MA) .GT. 0 ) J=J+6` (26). `        ELSEIF( IST .EQ. 5 .OR. IST .EQ. 15 ) THEN` (27). `          I=3` (28). `          J=9` (29). `          IF( IFCQ(MA) .GT. 0 ) J=J+3` (30). `        ELSE` (31). `          I=0` (32). `          J=0` (33). `        ENDIF` (34). `        NIDEP=NIDEP+I` (35). `        NIRH=NIRH+J` (36). `  100 CONTINUE` (37). `      END` (39). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
