---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/stats.cpp
lines: 169
sha256: 2eef43e9a936ca510d9643b8f46b255f4febf9230a03dca8c6f5195d612d1ea1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# stats.cpp — 판독 구간 기록

구간은 1행부터 169행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 헤더 포함(1) 뒤 `update_mass_stats`가 `flood_area`·`DomainVol`로 침수 면적과 체적을 구한다. 질량 수지(mass balance)의 체적·유량 오차를 계산한다. 유입·유출 누계를 0으로 초기화하고 현재 체적을 이전 체적에 복사하며 MassTotal을 한 주기 증가시킨다. 이 구간은 조건부 전처리 분기 밖이다. 원문: `Solverptr->FArea = flood_area(Parptr, Arrptr);` (12); `Solverptr->vol2 = DomainVol(Statesptr, Parptr, nullptr, Arrptr, nullptr);` (13); `Solverptr->Verror = BCptr->VolInMT - BCptr->VolOutMT -` (14); `(Solverptr->vol2 - Solverptr->vol1);` (15); `Solverptr->Qerror = Solverptr->Verror / Parptr->MassInt;` (16); `BCptr->VolInMT = C(0.0);` (18); `BCptr->VolOutMT = C(0.0);` (19); `Solverptr->vol1 = Solverptr->vol2;` (20); `Parptr->MassTotal += Parptr->MassInt;` (21). |
| 24–47 | `flood_area`는 면적을 0으로 시작하고 OpenMP 합 축약(reduction) 셀 루프에서 H가 0.01보다 큰 셀의 dA를 더한다. 면적을 반환한다(39). `zero_flux_stats`는 Qin·Qout을 0으로 설정한다(44–45). 원문: `NUMERIC_TYPE FloodArea = C(0.0);` (30); `#pragma omp parallel for reduction(+:FloodArea)` (31); `for (int j=0; j<Parptr->ysz; j++)` (32); `{` (33); `for (int i=0; i<Parptr->xsz; i++)` (34); `{` (35); `if (Arrptr->H[j*Parptr->xsz + i] > C(0.01)) FloodArea += Parptr->dA;` (36). |
| 48–65 | `accumulate_point_flux_stats`는 점원(point source) 유량 Q가 양수이면 Qin에 더하고 else는 Qout에서 Q를 뺀다. Qpoint_pos·Qpoint_neg 대신 Qin·Qout에 직접 누적한다는 주석이 있다(54–55). 원문: `if (Q > 0)` (56); `{` (57); `BCptr->Qin += Q;` (58); `}` (59); `else` (60); `{` (61); `BCptr->Qout -= Q;` (62); `}` (63). |
| 66–94 | `accumulate_boundary_flux_stats`는 지역 Qin·Qout을 0으로 초기화한다(74–75). 북쪽 y플럭스가 음수이면 유입, else면 유출이다. 남쪽은 양수이면 유입, else면 유출이다. 각 경우 dx를 곱하며 별도 OpenMP 합 축약 루프를 쓴다. 원문: `#pragma omp parallel for reduction(+:Qin, Qout)` (78); `for (int i=0; i<Parptr->xsz; i++)` (79); `{` (80); `const int j = 0;` (81); `NUMERIC_TYPE FHy = Arrptr->FHy[j*(Parptr->xsz+1) + i];` (82); `if (FHy	< 0) Qin += -FHy*Parptr->dx; else Qout += FHy*Parptr->dx;` (83); `#pragma omp parallel for reduction(+:Qin, Qout)` (87); `for (int i=0; i<Parptr->xsz; i++)` (88); `{` (89); `const int j = Parptr->ysz;` (90); `NUMERIC_TYPE FHy = Arrptr->FHy[j*(Parptr->xsz+1) + i];` (91); `if (FHy	> 0) Qin += FHy*Parptr->dx; else Qout += -FHy*Parptr->dx;` (92). |
| 95–118 | 시작 시 66행 `accumulate_boundary_flux_stats` 안이다. 서쪽 x플럭스가 양수이면 유입, 동쪽은 음수이면 유입이다. 각 플럭스에 dy를 곱한다. 네 경계의 지역 유량을 BCptr 누계에 더한 뒤 현재 Qin·Qout에 Tstep을 곱하여 체적을 누적한다. 원문: `#pragma omp parallel for reduction(+:Qin, Qout)` (96); `for (int j=0; j<Parptr->ysz; j++)` (97); `{` (98); `const int i = 0;` (99); `NUMERIC_TYPE FHx = Arrptr->FHx[j*(Parptr->xsz+1) + i];` (100); `if (FHx	> 0) Qin += FHx*Parptr->dy; else Qout += -FHx*Parptr->dy;` (101); `#pragma omp parallel for reduction(+:Qin, Qout)` (105); `for (int j=0; j<Parptr->ysz; j++)` (106); `{` (107); `const int i = Parptr->xsz;` (108); `NUMERIC_TYPE FHx = Arrptr->FHx[j*(Parptr->xsz+1) + i];` (109); `if (FHx	< 0) Qin += -FHx*Parptr->dy; else Qout += FHx*Parptr->dy;` (110); `}` (111); `BCptr->Qin += Qin;` (113); `BCptr->Qout += Qout;` (114); `BCptr->VolInMT += BCptr->Qin*Solverptr->Tstep;` (115); `BCptr->VolOutMT += BCptr->Qout*Solverptr->Tstep;` (116). |
| 119–150 | `update_velocity`는 OpenMP 전체 셀 루프에서 H·HU·HV를 읽는다. 수심이 DepthThresh보다 크면 성분 유량을 H로 나누어 Vx·Vy를 만들고 else는 둘 다 0으로 설정한다. 원문: `#pragma omp parallel for` (126); `for (int j=0; j<Parptr->ysz; j++)` (127); `{` (128); `for(int i=0; i<Parptr->xsz; i++)` (129); `{` (130); `NUMERIC_TYPE H = Arrptr->H[j*Parptr->xsz + i];` (131); `NUMERIC_TYPE HU = Arrptr->HU[j*Parptr->xsz + i];` (132); `NUMERIC_TYPE HV = Arrptr->HV[j*Parptr->xsz + i];` (133); `NUMERIC_TYPE& Vx = Arrptr->Vx[j*Parptr->xsz + i];` (134); `NUMERIC_TYPE& Vy = Arrptr->Vy[j*Parptr->xsz + i];` (135); `if (H > Solverptr->DepthThresh)` (137); `{` (138); `Vx = HU / H;` (139); `Vy = HV / H;` (140); `}` (141); `else` (142); `{` (143); `Vx = C(0.0);` (144); `Vy = C(0.0);` (145); `}` (146). |
| 151–169 | `update_max_field`는 전체 셀에서 maxH와 현재 H의 FMAX를 저장한다. `_MSC_VER` 미정의일 때만 OpenMP 지시를 포함하며 정의일 때는 지시를 제외한다(157–159). 두 경우 모두 같은 셀 루프를 포함한다. 이 파일에는 매크로 값 정의가 없다. 끝의 빈 줄도 포함한다. 원문: `#ifndef _MSC_VER` (157); `#pragma omp parallel for` (158); `#endif` (159); `for (int j=0; j<Parptr->ysz; j++)` (160); `{` (161); `for(int i=0; i<Parptr->xsz; i++)` (162); `{` (163); `NUMERIC_TYPE& maxH = Arrptr->maxH[j*Parptr->xsz + i];` (164); `maxH = FMAX(maxH, Arrptr->H[j*Parptr->xsz + i]);` (165); `}` (166); `}` (167). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 36: 침수 면적 계산의 수심 기준은 `C(0.01)`로 고정되어 있다. 이 함수에는 Solver 인수가 없다.
- 56–62: 점원 통계 함수는 BCptr->Qin·Qout에 직접 가감한다. 함수 안에는 OpenMP atomic·critical 지시가 없다.
- 115–116: 경계 통계의 체적 적분은 경계 지역 Qin·Qout만이 아니라 점원 유량이 포함될 수 있는 BCptr->Qin·Qout을 사용한다.
- 16: Qerror는 MassInt로 나눈다. 이 함수 안에는 MassInt 영값 검사가 없다.
