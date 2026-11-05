---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/spcdsetdu.f
lines: 27
sha256: bb0fd827a3f771a848c5a550a038a3c207f9edf29962b8f43cbf2ff57e3783b1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdsetdu.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | SPCDSETDU 입구와 배열 선언이다(1–6). ISID와 일치하는 첫 ISPD 집합을 ADDSET으로 펼친다(8–12). 절점과 여섯 성분을 순회하며 NSPD 플래그가 1이면 ENFDISP를 호출한다(13–21). 처리 뒤 레이블 500으로 이동해 반환한다(22–27). 원문: `      SUBROUTINE SPCDSETDU(ISID,DUG,KK,ISPD,NSPD,SPCD,F,ITYP,UG1,UG2`<br>`     &                    ,DT1,DT2)` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION KK(*),ISPD(2,*),NSPD(7,*),SPCD(6,*),UG1(6,*),UG2(6,*)`<br>`     &         ,DUG(6,*)` (5–6); `      NISPD = KK(38)` (8); `      DO 410 J=1,NISPD` (10); `        IF(ISPD(1,J) .EQ. ISID) THEN` (11); `          CALL ADDSET(J,ISPD,IS,NN)` (12); `          DO 411 K=1,NN` (13); `            IAD=IS-1+K` (14); `            NODFIX=NSPD(1,IAD)` (15); `            DO 412 L=1,6` (16); `              IF(NSPD(L+1,IAD) .EQ. 1) `<br>`     &          CALL ENFDISP(DUG(L,NODFIX),SPCD(L,IAD),F,ITYP`<br>`     &                      ,UG1(L,NODFIX),UG2(L,NODFIX),DT1,DT2)` (17–19); `  412       CONTINUE` (20); `  411     CONTINUE` (21); `          GOTO 500` (22); `        ENDIF` (23); `  410 CONTINUE` (24); `  500 RETURN` (26); `      END` (27) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
