---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enpfaddm.f
lines: 16
sha256: 0ab08059e2eaefa06e1e3789ea6347fc45c7db4df34da6c7cc5dd1dc7cd82f49
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enpfaddm.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | ENPFADDM의 암시적 형과 배열 크기를 선언한다. 해석: FT·FTD·UG는 전역 벡터이고 FC·UE는 요소 벡터이며 EMASS는 질량 배열이다. FC·UE의 두 번째 크기는 20이다. 원문: `      SUBROUTINE ENPFADDM(FT,FTD,EMASS,UG,KN,NDF,ND,CM)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION FT(6,*),FTD(6,*),FC(NDF,20),EMASS(*),UE(NDF,20),UG(6,*)`<br>`     &         ,KN(ND)` (4–5); 주석 원문 `C-----------------------------------------------------------------------` (6). [11-04 전수 검증 정정] |
| 7–16 | 시작 시 1행 ENPFADDM 루틴 안. N=NDF*ND를 계산한다. KN으로 UG를 모아 UE에 넣고 HARFB에 EMASS와 UE를 전달하여 FC를 받는다. FC를 FT에 더하고 CM*FC를 FTD에 더한다. 루틴 끝을 포함한다. 원문: `      N = NDF * ND` (7); `      UE(:,1:ND) = UG(1:NDF,KN(:))` (9); `      CALL HARFB(FC,EMASS,UE,N,N,1)` (11); `      FT(1:NDF,KN(:)) = FT(1:NDF,KN(:)) + FC(:,1:ND)` (13); `      FTD(1:NDF,KN(:)) = FTD(1:NDF,KN(:)) + CM * FC(:,1:ND)` (14); `      END` (16). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4–5·9·13–14: UE·FC의 두 번째 크기는 20이고 UG·FT·FTD의 첫 번째 크기는 6이다. 이 파일에는 ND<=20 또는 NDF<=6 검사가 없다.
