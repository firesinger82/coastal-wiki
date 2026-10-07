---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/caldiff.f90
lines: 45
sha256: dadd333f0e02c44f86a14d5d2751f77b88385cd1a7c520e94b56e2b916b565d0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# caldiff.f90 — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | CALDIFF(CON1,IW)의 GPLv2 머리말과 수평 확산(horizontal diffusion) 수송 목적·변경 기록을 포함한다(1–20). GLOBAL을 사용한다(22). IW는 입력 정수이며 CON1(LCM,KCM)은 입력 실수 배열이다(25–26). ND·K·LP·L·LS·LW를 지역 정수로 선언한다(27). |
| 29–45 | 시작 시 9행 CALDIFF 루틴 안이다. ND=1..NDM, K=1..KC, LP=1..LLHDMF(K,ND)를 순회한다(30–32). LKHDMF에서 현재 셀을 얻고 LWC·LSC에서 서·남 셀을 얻는다(33–37). 현재·인접 셀 AH의 합에 0.5, 면 개방 계수(face mask), 면 폭·수심·지층 비율·농도 차·역거리를 곱한 확산 플럭스(diffusive flux)를 기존 FUHUD·FVHUD에 더한다(36·38). 주석은 단위를 g/s로 적는다(35). 루프·반환·루틴 종료와 마지막 빈 줄을 포함한다(39–45). 원문: `do ND = 1,NDM` (30); `do K = 1,KC` (31); `do LP = 1,LLHDMF(K,ND)` (32); `L = LKHDMF(LP,K,ND)` (33); `LW = LWC(L)` (34); `FUHUD(L,K,IW) = FUHUD(L,K,IW) + 0.5*SUB3D(L,K)*DYU(L)*HU(L)*DZC(L,K)*(AH(L,K)+AH(LW,K))*(CON1(LW,K)-CON1(L,K))*DXIU(L)` (36); `LS = LSC(L)` (37); `FVHUD(L,K,IW) = FVHUD(L,K,IW) + 0.5*SVB3D(L,K)*DXV(L)*HV(L)*DZC(L,K)*(AH(L,K)+AH(LS,K))*(CON1(LS,K)-CON1(L,K))*DYIV(L)` (38). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26·36·38: CON1은 INTENT(IN) 배열이다. 이 루틴은 CON1을 갱신하지 않고 기존 FUHUD·FVHUD에 확산 플럭스를 더한다. 이 루틴에는 두 플럭스 배열을 0으로 초기화하는 문장이 없다.

