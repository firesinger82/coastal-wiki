---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/enpfrcd.f
lines: 12
sha256: 3b276755f155dd258488cc1a12805fa436887c798e44b30cc737749f5c4650ba
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfrcd.f — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 루틴·암시적 자료형과 NDF×NNP 배열을 선언한다(1–4). NP 절점 목록에서 DUG의 1:NDF 성분을 모아 DU를 만든다(6). N=NDF*NNP를 계산하고 MATML에 ESTF·DU·DF와 차원·배치 인수를 전달한다(8–10). 루틴을 끝낸다(12). 원문: `      SUBROUTINE ENPFRCD(DF,ESTF,DUG,NP,NDF,NNP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION DU(NDF,NNP),NP(NNP),DUG(6,*),DF(NDF,NNP),ESTF(*)` (4); `      DU(:,:) = DUG(1:NDF,NP(:))` (6); `      N = NDF * NNP` (8); `      CALL MATML(DF,2,ESTF,1,DU,2,N,1,N)` (10). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
