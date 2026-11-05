---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/input/Set_table/St_SPC1.f
lines: 35
sha256: 671196fefe504e3a83496d8c16e0a04771102a174c5da5112f9d536f57eabaef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# St_SPC1.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | ST_SPC1은 세트 일치 시 입력 절점 범위 IS:IE를 전개한다(8–31). INDGR(K)>0인 절점만 등록하며 입력 4:9 성분을 NSP1의 2:7로 복사한다(17–23). ISP1 두 번째 성분에 누적 끝을 저장하고 최종 절점 번호를 INDGR로 변환한다(29·33). 배열 크기와 주석·루틴 끝을 포함한다(1–35). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ST_SPC1( ISP1, NSP1, NISP1, NNSP1, J_SPC1, N_SPC1,` (1) <br> `     &                    INDGR )` (2) <br> `      DIMENSION ISP1(2,NISP1), NSP1(7,NNSP1), J_SPC1(9,N_SPC1), INDGR(*)` (4) <br> `      IP = 0` (6) <br> `      DO I = 1, NISP1` (8) <br> `        DO J = 1, N_SPC1` (10) <br> `          IF( J_SPC1(1,J) == ISP1(1,I) ) THEN` (12) <br> `            IS = J_SPC1(2,J)` (14) <br> `            IE = J_SPC1(3,J)` (15) <br> `            DO K = IS, IE` (17) <br> `              IF( INDGR(K) > 0 ) THEN` (18) <br> `                IP = IP + 1` (19) <br> `                NSP1(1,IP) = K` (20) <br> `                NSP1(2:7,IP) = J_SPC1(4:9,J)` (21) <br> `              ENDIF` (22) <br> `            ENDDO ` (23) <br> `          ENDIF` (25) <br> `        ENDDO` (27) <br> `        ISP1(2,I) = IP` (29) <br> `      ENDDO` (31) <br> `      NSP1(1,:) = INDGR( NSP1(1,:) )` (33) <br> `      END` (35) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
