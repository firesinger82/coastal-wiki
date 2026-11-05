---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/rlcorr.f
lines: 46
sha256: 4b7b780e1317c13138ec99aa95883137fea9b7d60a0363a0541858d6095b8b32
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rlcorr.f — 판독 구간 기록

구간은 1행부터 46행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | RLCORR는 POSS와 면(face) 세 절점 좌표를 XYZ에 모으고 AREACD에 RL,E,H,XYZ를 전달한다(7–12). 해석: RL은 면 좌표(area coordinate)이다. DATA EPS=1.D-6과 선언을 포함한다(3–5). 원문: `      SUBROUTINE RLCORR(RLD,POSS,IELC,POS)` (1). `      IMPLICIT REAL*8(A-H,O-Z)` (3). `      DIMENSION XYZ(3,4),POS(3,*),IELC(3),E(3),RL(3),RLD(3),POSS(3)` (4). `      DATA EPS / 1.D-6 /` (5). `      CALL SHIFT1(XYZ(1,4),POSS,3)` (7). `      DO 100 I=1,3` (8). `        CALL SHIFT1(XYZ(1,I),POS(1,IELC(I)),3)` (9). `  100 CONTINUE` (10). `      CALL AREACD(RL,E,H,XYZ)` (12). [11-04 전수 검증 정정] |
| 14–30 | 시작 시 1행 RLCORR 루틴 안. RL(1),RL(2)가 EPS 이상이고 합의 경계 안이면 RL을 RLD로 복사한다(14–16). 두 성분이 작거나 각 꼭짓점 영역 조건이면 EPS와 1-2*EPS로 RLD를 설정하고 세 번째 성분은 합이 1이 되도록 계산한다(17–30). 원문: 연속문(14–15): `      IF( RL(1) .GE. EPS .AND. RL(2) .GE. EPS .AND.` (14); `     &    RL(2) .LE. -RL(1)+1.D0-EPS ) THEN` (15). `        CALL SHIFT1(RLD,RL,3)` (16). `      ELSEIF( RL(1) .LE. EPS .AND. RL(2) .LE. EPS ) THEN` (17). `        RLD(1)=EPS` (18). `        RLD(2)=EPS` (19). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (20). 연속문(21–22): `      ELSEIF( RL(1) .GE. 1.D0-2.D0*EPS .AND.` (21); `     &        RL(2) .LE. RL(1)-1.D0+3.D0*EPS ) THEN` (22). `        RLD(1)=1.D0-2.D0*EPS` (23). `        RLD(2)=EPS` (24). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (25). 연속문(26–27): `      ELSEIF( RL(2) .GE. 1.D0-2.D0*EPS .AND.` (26); `     &        RL(2) .GE. RL(1)+1.D0-3.D0*EPS ) THEN` (27). `        RLD(1)=EPS` (28). `        RLD(2)=1.D0-2.D0*EPS` (29). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (30). |
| 31–46 | 시작 시 1행 RLCORR 루틴·14–15행 `      IF( RL(1) .GE. EPS .AND. RL(2) .GE. EPS .AND.`와 `     &    RL(2) .LE. -RL(1)+1.D0-EPS ) THEN`으로 시작한 분기 사슬 안. 이 IF는 43행 `ENDIF`에서 닫힌다. 31행 이후 분기는 14–15·17·21–22·26–27행 조건이 모두 거짓일 때 평가한다. RL(1) 또는 RL(2)가 EPS보다 작으면 해당 성분을 EPS로 정한다(31–38). 나머지 ELSE는 두 성분 차이를 사용해 합 경계의 좌표를 계산한다(39–42). 조건 종료·RETURN·END를 포함한다. 원문: `      ELSEIF( RL(1) .LT. EPS ) THEN` (31). `        RLD(1)=EPS` (32). `        RLD(2)=RL(2)` (33). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (34). `      ELSEIF( RL(2) .LT. EPS ) THEN` (35). `        RLD(1)=RL(1)` (36). `        RLD(2)=EPS` (37). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (38). `      ELSE` (39). `        RLD(1)=(1.D0-EPS+RL(1)-RL(2))*.5D0` (40). `        RLD(2)=-RLD(1)+1.D0-EPS` (41). `        RLD(3)=1.D0-RLD(1)-RLD(2)` (42). `      ENDIF` (43). `      RETURN` (45). `      END` (46). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5: EPS는 DATA 값 1.D-6으로 고정된다.
- 12: AREACD 출력 E,H는 후속 실행문에서 참조하지 않는다.
