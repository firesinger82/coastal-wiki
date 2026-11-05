---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/csfhx.f
lines: 31
sha256: f1cf9e81c1682b9c6999494cea0cfdd2c58bd350563407855ad7b741dfc4a761
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# csfhx.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 루틴과 배열을 선언하고 8절점의 6개 사각 면 연결표 II를 DATA로 지정한다(1–4). ICSF(2)를 4로 둔다(6). 여섯 면의 각 절점 집합 IG에 JG의 세 절점이 모두 포함되는지 중첩 루프·GOTO로 검사한다(8–20). 일치하면 면 번호와 네 절점 번호를 ICSF에 저장하고 반환한다(22–24). 모두 실패하면 메시지를 쓰고 ERRSTP(90,ITO)를 호출한다(28–29). 원문: `      SUBROUTINE CSFHX(ICSF,JG,NP,ITO)` (1); `      DIMENSION II(4,6),ICSF(6),IG(4),NP(8),JG(3)` (3); `      DATA II / 1,2,3,4, 1,5,6,2, 2,6,7,3, 3,7,8,4, 4,8,5,1, 5,8,7,6 /` (4); `      ICSF(2) = 4` (6); `      DO I = 1, 6` (8); `        IG(:) = NP( II(:,I) )` (10); `        DO J = 1, 3` (12); `          DO K = 1, 4` (14); `            IF( JG(J) == IG(K) ) GOTO 10` (15); `          GOTO 20` (18); `   10   ENDDO` (20); `        ICSF(1) = I` (22); `        ICSF(3:6) = IG(:)` (23); `   20 ENDDO` (26); `      WRITE(ITO,*) 'STOP IN SUB. CSFHX.'` (28); `      CALL ERRSTP(90,ITO)` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
