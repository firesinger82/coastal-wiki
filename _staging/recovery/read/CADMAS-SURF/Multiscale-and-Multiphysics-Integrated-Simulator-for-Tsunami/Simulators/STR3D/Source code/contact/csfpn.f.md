---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/csfpn.f
lines: 37
sha256: 1becb2c3f09c74f178a6955ff9a653d3a74ef0938fb5ac4b5221cf7be97b5dde
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# csfpn.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 루틴·배열과 6절점의 5개 면 연결표를 DATA로 선언한다(1–4). 면 1:2는 N=3, 3:5는 N=4로 선택한다(6–13). 각 면에서 JG 세 절점의 포함 여부를 검사하고 일치하면 면 번호·N·절점 목록을 ICSF에 저장하고 반환한다(15–30). 끝까지 일치하지 않으면 오류 출력 후 ERRSTP(90,ITO)를 호출한다(34–35). 원문: `      SUBROUTINE CSFPN(ICSF,JG,NP,ITO)` (1); `      DIMENSION II(4,5),ICSF(6),IG(4),NP(6),JG(3)` (3); `      DATA II / 1,2,3,0, 4,6,5,0, 1,4,5,2, 2,5,6,3, 3,6,4,1 /` (4); `      DO I = 1, 5` (6); `        SELECT CASE( I )` (8); `        CASE( 1:2 )` (9); `          N = 3` (10); `        CASE( 3:5 )` (11); `          N = 4` (12); `        IG(1:N) = NP( II(1:N,I) )` (15); `        DO J = 1, 3` (17); `          DO K = 1, N` (19); `            IF( JG(J) == IG(K) ) GOTO 10` (20); `          GOTO 20` (23); `   10   ENDDO` (25); `        ICSF(1) = I` (27); `        ICSF(2) = N` (28); `        ICSF(3:2+N) = IG(1:N)` (29); `   20 ENDDO` (32); `      WRITE(ITO,*) 'STOP IN SUB. CSFPN.'` (34); `      CALL ERRSTP(90,ITO)` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·9–15: 첫 두 면 연결표의 네 번째 값은 0이며 N=3이므로 해당 값은 NP 첨자로 사용하지 않는다.
