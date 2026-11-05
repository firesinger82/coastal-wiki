---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_BSURFS.f
lines: 36
sha256: a772ad83ce8e9e4cd536e7fad4d7ce230c4691263a10308ff75e3607656a710c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_BSURFS.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | ST_BSURFS는 J_BSRF(1,J)와 ICRG(1,I)가 같은 항목을 NCRG에 모은다. 배열 ICRG(2,NICRG)·NCRG(4,NNCRG)·J_BSRF(5,N_BSRF)를 선언한다(1–5). I와 J의 전 범위를 순회하고 식별자가 일치하면 IP를 늘려 J_BSRF의 2:5 성분을 복사한다(9–20). ICRG(2,I)는 해당 영역의 누적 끝 위치다(22). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_BSURFS( ICRG, NCRG, ICRGR, NICRG, NNCRG, J_BSRF,` (1) <br> `     &                      N_BSRF, IELR, INDGR )` (2) <br> `      DIMENSION ICRG(2,NICRG), NCRG(4,NNCRG), J_BSRF(5,N_BSRF),` (4) <br> `     &          IELR(*), INDGR(*), ICRGR(*)` (5) <br> `      IP = 0` (7) <br> `      DO I = 1, NICRG` (9) <br> `        DO J = 1, N_BSRF` (11) <br> `          IF( J_BSRF(1,J) == ICRG(1,I) ) THEN` (13) <br> `            IP = IP + 1` (15) <br> `            NCRG(:,IP) = J_BSRF(2:5,J)` (16) <br> `          ENDIF` (18) <br> `        ENDDO` (20) <br> `        ICRG(2,I) = IP` (22) <br> `      ENDDO` (24) [11-04 전수 검증 정정] |
| 25–36 | 시작 시 1행 ST_BSURFS 루틴 안이며 앞 영역 구성 루프 밖이다. 영역 구성 루프 밖이다. NCRG 첫 성분의 요소 번호는 IELR로 변환한다(26). 2:4 성분의 절점 번호는 INDGR로 변환한다(28–30). ICRGR는 영역 외부 번호에서 내부 번호로의 역표를 받는다(32–34). 루틴을 종료한다(36). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      NCRG(1,:) = IELR( NCRG(1,:) )` (26) <br> `      DO I = 2, 4` (28) <br> `        NCRG(I,:) = INDGR( NCRG(I,:) )` (29) <br> `      ENDDO` (30) <br> `      DO I = 1, NICRG` (32) <br> `        ICRGR( ICRG(1,I) ) = I` (33) <br> `      ENDDO` (34) <br> `      END` (36) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
