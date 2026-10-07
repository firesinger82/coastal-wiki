---
file: models/EFDC/raw/source_code/EFDC-GVC/solvsmbe.for
lines: 44
sha256: 55e28f1a5f7c6b89069ec3ff2dbf1cd291e7c36fde36e35d05acd431c0d7891f
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# solvsmbe.for — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 구분 주석과 `SUBROUTINE SOLVSMBE(SMV1,SMV2,SMA11,SMA22,SMA1,SMA2,SMB11,SMB22)` 입구(1–8). 2×2 행렬(matrix) 해법이라는 목적 주석(10). EFDC-FULL 1.0a·2001년 수정일·변경 기록과 구분 주석(12–29). |
| 30–38 | 시작 시 6행 SOLVSMBE 루틴 안. 비대각 계수는 `SMA12 = -SMA2` (30), `SMA21 = -SMA1` (31). 행렬식(determinant)은 `SMDET = SMA11*SMA22 - SMA12*SMA21` (32). `IF(SMDET.EQ.0.0)THEN` (33)이면 특이 행렬(singular matrix) 안내와 계수 SMA11·SMA12·SMA21·SMA22·SMB11·SMB22를 출력하고 STOP(34–36). 분기 종료·끝 주석(37–38). |
| 39–44 | 시작 시 6행 SOLVSMBE 루틴 안이며 33행 조건문 밖. `SMDET = 1.0 / SMDET` (39)로 행렬식의 역수를 계산한다. 해는 `SMV1 = (SMB11*SMA22 - SMB22*SMA12) * SMDET` (40), `SMV2 = (SMB22*SMA11 - SMB11*SMA21) * SMDET` (41). 끝 주석·RETURN·END(42–44). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 32–39: 특이 행렬 검사는 행렬식과 0.0의 EQ 비교이다. 이 루틴에는 행렬식의 크기에 대한 허용오차 검사가 없다.
