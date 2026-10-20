---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/friction.cpp
lines: 104
sha256: 670c6dfd962981bd4eeaca9a22bc3737725636cbdbd75f6c85fce08d1efd02ac
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# friction.cpp — 판독 구간 기록

구간은 1행부터 104행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | friction.h·modifiedvars.h를 포함한다(1–2). dg2::apply_friction에서 `if (Arrptr->Manningsn == nullptr && Parptr->FPn <= C(0.0)) return;` (11)이면 반환한다. OpenMP 지시는 `#pragma omp parallel for` (13)이며 `for (int j=0; j<Parptr->ysz; j++)` (14)·`for(int i=0; i<Parptr->xsz; i++)` (16)에서 셀 평균 H와 HU·HV 참조를 가져온다(18–20). Manning 조도(Manning roughness) 선택의 여러 줄 삼항식은 `NUMERIC_TYPE n = (Arrptr->Manningsn == nullptr)` (22), `? Parptr->FPn : Arrptr->Manningsn[j*Parptr->xsz + i];` (23)이다. `if (H <= Solverptr->DepthThresh) continue;` (25)이면 셀을 건너뛰고 friction을 호출한다(27). 이 파일에는 전처리 분기가 없다. |
| 29–53 | 시작 시 4행 apply_friction·14행 j 루프·16행 i 루프 안. x·y방향 각 하·상 Gauss 지점(Gauss point)의 H·HU·HV를 gauss_lower·gauss_upper로 복원한다. 여러 줄 호출·대입의 원문은 `NUMERIC_TYPE H_x_lower = gauss_lower(Arrptr->H, Arrptr->H1x,` (29), `Parptr, i, j);` (30), `NUMERIC_TYPE H_x_upper = gauss_upper(Arrptr->H, Arrptr->H1x,` (31), `Parptr, i, j);` (32), `NUMERIC_TYPE HU_x_lower = gauss_lower(Arrptr->HU, Arrptr->HU1x,` (33), `Parptr, i, j);` (34), `NUMERIC_TYPE HU_x_upper = gauss_upper(Arrptr->HU, Arrptr->HU1x,` (35), `Parptr, i, j);` (36), `NUMERIC_TYPE HV_x_lower = gauss_lower(Arrptr->HV, Arrptr->HV1x,` (37), `Parptr, i, j);` (38), `NUMERIC_TYPE HV_x_upper = gauss_upper(Arrptr->HV, Arrptr->HV1x,` (39), `Parptr, i, j);` (40), `NUMERIC_TYPE H_y_lower = gauss_lower(Arrptr->H, Arrptr->H1y,` (41), `Parptr, i, j);` (42), `NUMERIC_TYPE H_y_upper = gauss_upper(Arrptr->H, Arrptr->H1y,` (43), `Parptr, i, j);` (44), `NUMERIC_TYPE HU_y_lower = gauss_lower(Arrptr->HU, Arrptr->HU1y,` (45), `Parptr, i, j);` (46), `NUMERIC_TYPE HU_y_upper = gauss_upper(Arrptr->HU, Arrptr->HU1y,` (47), `Parptr, i, j);` (48), `NUMERIC_TYPE HV_y_lower = gauss_lower(Arrptr->HV, Arrptr->HV1y,` (49), `Parptr, i, j);` (50), `NUMERIC_TYPE HV_y_upper = gauss_upper(Arrptr->HV, Arrptr->HV1y,` (51), `Parptr, i, j);` (52)이다. |
| 54–71 | 시작 시 4행 apply_friction·14행 j 루프·16행 i 루프 안. HU1x·HU1y·HV1x·HV1y 참조를 가져온다(54–57). friction을 x하·x상·y하·y상의 H·HU·HV에 각각 호출한다(59–62). `HU1x = C(0.5)*(HU_x_upper - HU_x_lower);` (64), `HU1y = C(0.5)*(HU_y_upper - HU_y_lower);` (65), `HV1x = C(0.5)*(HV_x_upper - HV_x_lower);` (66), `HV1y = C(0.5)*(HV_y_upper - HV_y_lower);` (67)로 두 점 차이의 반을 기울기 계수로 재구성한다. 루프·함수를 닫는다(68–70). |
| 72–104 | dg2::friction은 수심 H와 조도 n을 값으로, HU·HV를 참조로 받는다(72–79). `if (H <= Solverptr->DepthThresh)` (81)이면 HU·HV를 0으로 하고 반환한다(83–85). `NUMERIC_TYPE U = HU/H;` (88), `NUMERIC_TYPE V = HV/H;` (89)로 속도를 구하고 `if (FABS(U) <= Solverptr->SpeedThresh && FABS(V) <= Solverptr->SpeedThresh)` (91)이면 그대로 반환한다(93). `NUMERIC_TYPE speed = SQRT(U*U+V*V);` (96), `NUMERIC_TYPE Cf = Solverptr->g*n*n / pow(H, C(1.0)/C(3.0));` (97), `NUMERIC_TYPE Sfx = -Cf*U*speed;` (98), `NUMERIC_TYPE Sfy = -Cf*V*speed;` (99), `NUMERIC_TYPE Dx = C(1.0) + Solverptr->Tstep*Cf/H * (C(2.0)*U*U + V*V)/speed;` (100), `NUMERIC_TYPE Dy = C(1.0) + Solverptr->Tstep*Cf/H * (U*U + C(2.0)*V*V)/speed;` (101)로 속력·Manning 마찰계수·생성항·갱신 분모를 구한다. `HU += Solverptr->Tstep * Sfx / Dx;` (102), `HV += Solverptr->Tstep * Sfy / Dy;` (103)으로 시간 간격을 적용해 두 유량 계수를 더한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25·81–85: apply_friction은 얕은 셀에서 friction 호출을 건너뛴다. friction을 직접 호출한 경우에는 얕은 수심에서 HU·HV를 0으로 설정한다.
- 27·29–52: 평균 HU·HV에 대한 friction 호출이 Gauss 지점 복원보다 먼저 실행된다. 복원 호출은 갱신된 평균 배열과 기존 기울기 배열을 전달받는다.
