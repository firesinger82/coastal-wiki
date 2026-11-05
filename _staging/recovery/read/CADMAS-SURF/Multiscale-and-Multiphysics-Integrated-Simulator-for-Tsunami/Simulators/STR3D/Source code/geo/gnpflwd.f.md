---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/gnpflwd.f
lines: 12
sha256: 7d20c840c8d0f3000d580889d943ea9af53cd892d3f66a29b37f777c22766275
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# gnpflwd.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | GNPFLWD는 실수 IMPLICIT 선언을 사용한다. NP(:)를 첨자로 사용하여 DPG 값을 DP에 모은다. AXB에 DF·ELHM·DP와 크기 3*N·N·1을 전달한다. 해석: DPG는 압력 증분(pressure increment)으로 보인다. 해석: AXB는 ELHM과 DP를 곱하여 DF를 구하는 호출로 보인다. 해당 절점의 FT 첫 세 성분에 DF를 더한다. 원문: `      SUBROUTINE GNPFLWD(FT,ELHM,DPG,NP,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION FT(6,*),ELHM(3*N,N),DPG(*),NP(N),DP(N),DF(3,N)` (4); `      DP(:) = DPG(NP(:))` (6); `      CALL AXB(DF,ELHM,DP,3*N,N,1)` (8); `      FT(1:3,NP(:)) = FT(1:3,NP(:)) + DF(:,:)` (10); `      END` (12) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
