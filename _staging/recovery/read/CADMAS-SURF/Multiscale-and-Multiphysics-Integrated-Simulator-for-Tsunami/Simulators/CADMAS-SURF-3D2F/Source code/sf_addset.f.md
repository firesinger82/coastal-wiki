---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_addset.f
lines: 13
sha256: ac6a02347ec8bd44dee3bdd801c7f9fda17fd4a9b559411103aa6e33887323de
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_addset.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | INDEX(*)를 사용하여 IS와 IE를 설정한다. 해석: INDEX를 누적 끝 인덱스로 보면 IS와 IE는 I번째 구간의 시작과 끝이다. I==1이면 시작 IS=1이고 ELSE에서는 이전 끝+1이다. 끝 IE는 INDEX(I)를 복사한다. 별도 IMPLICIT 선언은 없다. 원문: `      SUBROUTINE SF_ADDSET(IS,IE,INDEX,I)` (1); `      DIMENSION INDEX(*)` (3); `      IF( I == 1 ) THEN` (5); `        IS = 1` (6); `      ELSE` (7); `        IS = INDEX(I-1) + 1` (8); `      ENDIF` (9); `      IE = INDEX(I)` (11); `      END` (13) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3·8·11: INDEX는 가정 크기(assumed-size) 배열이다. 이 루틴에는 I의 범위나 INDEX의 단조성 검사문이 없다.
