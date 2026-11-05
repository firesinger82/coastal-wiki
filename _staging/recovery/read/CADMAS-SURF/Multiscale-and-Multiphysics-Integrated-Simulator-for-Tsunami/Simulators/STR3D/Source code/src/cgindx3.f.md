---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cgindx3.f
lines: 36
sha256: 332d61783f336e579a31c407fd50bbad19a9b2116ff6af4674eeb2476b5d1854
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgindx3.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | CGINDX3의 희소 인덱스(sparse index) 배열을 선언하고 NCG를 0으로 초기화한다. 원문: `      SUBROUTINE CGINDX3(IDSK,IDCG,IDCGWK,NCGMAX,N,NEXT,NEQ,ISLV)` (1); `      DIMENSION IDSK(NEQ+1),IDCG(*),IDCGWK(NCGMAX,*),NEXT(*),N(*)` (3); `      NCG = 0` (5). |
| 7–18 | 시작 시 1행 CGINDX3 루틴 안. 각 행에서 ISLV가 11 이하이면 대각 인덱스를 별도로 저장한다. 나머지는 현재 저장 위치 다음을 IDSK(I)로 둔다. 연결 목록(linked list)의 시작 IP를 I로 설정한다. 원문: `      DO I = 1, NEQ` (7); `        IF( ISLV <= 11 ) THEN` (9); `          NCG = NCG + 1` (10); `          IDSK(I) = NCG` (11); `          IDCG(NCG) = I` (12); `        ELSE` (13); `          IDSK(I) = NCG + 1` (14); `        ENDIF` (15); `        IP = I` (17). |
| 19–36 | 시작 시 7행 `      DO I = 1, NEQ` 안이다. 이 루프는 32행 `      ENDDO`에서 닫힌다. 무한 DO에서 현재 IP의 N개 인덱스를 IDCG에 복사하고 NEXT를 따라간다. IP가 0이면 종료한다. I 루프 종료 후 IDSK(NEQ+1)에 마지막 위치 다음을 저장한다. 루틴 끝을 포함한다. 원문: `        DO` (19); `          NN = N(IP)` (21); `          IDCG(NCG+1:NCG+NN) = IDCGWK(1:NN,IP)` (23); `          NCG = NCG + NN` (25); `          IP = NEXT(IP)` (27); `          IF( IP == 0 ) EXIT` (28); `        ENDDO` (30); `      ENDDO` (32); `      IDSK(NEQ+1) = NCG + 1` (34); `      END` (36). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
