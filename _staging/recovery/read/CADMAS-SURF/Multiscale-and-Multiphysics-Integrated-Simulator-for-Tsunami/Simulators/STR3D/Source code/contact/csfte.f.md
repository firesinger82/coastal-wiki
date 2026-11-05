---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/csfte.f
lines: 31
sha256: abe55e875d7c29867b9432728f4dca352d89363ed7f2a15f8a012467b939efc4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# csfte.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 루틴·배열과 4절점의 4개 삼각 면 연결표를 DATA로 선언한다(1–4). ICSF(2)를 3으로 두고 각 면의 세 절점이 JG 세 절점을 포함하는지 검사한다(6–20). 일치하면 면 번호·세 절점을 ICSF에 저장하고 반환한다(22–24). 실패하면 오류 출력 후 ERRSTP(90,ITO)를 호출한다(28–29). 원문: `      SUBROUTINE CSFTE(ICSF,JG,NP,ITO)` (1); `      DIMENSION II(3,4),ICSF(6),IG(3),NP(4),JG(3)` (3); `      DATA II / 2,4,3, 3,4,1, 4,2,1, 1,2,3 /` (4); `      ICSF(2) = 3` (6); `      DO I = 1, 4` (8); `        IG(:) = NP( II(:,I) )` (10); `        DO J = 1, 3` (12); `          DO K = 1, 3` (14); `            IF( JG(J) == IG(K) ) GOTO 10` (15); `          GOTO 20` (18); `   10   ENDDO` (20); `        ICSF(1) = I` (22); `        ICSF(3:5) = IG(:)` (23); `   20 ENDDO` (26); `      WRITE(ITO,*) 'STOP IN SUB. CSFTE.'` (28); `      CALL ERRSTP(90,ITO)` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
