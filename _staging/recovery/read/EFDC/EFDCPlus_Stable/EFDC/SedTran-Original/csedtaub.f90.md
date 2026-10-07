---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-Original/csedtaub.f90
lines: 50
sha256: 21f98b2d881e05b58e96ca94c9b44a4e4182bce431829a80926d61f27a08b0f3
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# csedtaub.f90 — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | EFDC+·저작권·GPLv2 머리말(1–8). CSEDTAUB(DENBULK,IOPT) 입구(9). 점착성 퇴적물(cohesive sediment)의 벌크·질량 침식(bulk or mass erosion) 임계응력(critical stress)을 바닥 벌크밀도(bulk density)로 계산한다는 주석(11–12). IOPT=1과 2 모두 Hwang–Mehta 1989를 출처로 적는다(14–22). 변경 이력·implicit none·IOPT·실수 선언을 포함한다(24–29). |
| 31–44 | 시작 시 9행 CSEDTAUB 안. IOPT=1은 BULKDEN=0.001*DENBULK를 설정한다(31–32). BULKDEN<=1.013이면 반환값은 0이다(33–34). else는 0.001*(9.808*BULKDEN-9.934)를 계산한다(35–37). 병렬 elseif의 IOPT=2는 같은 변환·조건·식을 반복한다(38–44). 조건·계산·호출 원문: `if( IOPT == 1 )then` (31); `BULKDEN = 0.001*DENBULK  ! *** PMC Changed to prevent` (32); `if( BULKDEN <= 1.013 )then` (33); `else` (35); `CSEDTAUB = 0.001*(9.808*BULKDEN-9.934)` (36); `elseif( IOPT == 2 )then` (38); `BULKDEN = 0.001*DENBULK  ! *** PMC Changed to prevent` (39); `if( BULKDEN <= 1.013 )then` (40); `else` (42); `CSEDTAUB = 0.001*(9.808*BULKDEN-9.934)` (43). |
| 45–50 | 시작 시 9행 CSEDTAUB·31행 옵션 선택 블록 안. else는 잘못된 임계응력 옵션이라는 문자열로 STOPP를 호출한다(45–46). 선택 블록·함수 종료와 마지막 빈 줄을 포함한다(47–50). 조건·계산·호출 원문: `else` (45); `call STOPP('CSEDTAUB: BAD SEDIMENT CRITICAL STRESS OPTION! STOPPING!')` (46). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 31–44: IOPT=1과 IOPT=2의 밀도 변환, 1.013 경계조건, 반환식이 동일하다.

