# 기대 I/O · 검증 포인트

> 본 시나리오는 **재현 절차 템플릿**이며 정량 run 결과는 미수록. 아래는 실행 시 산출물과 검증해야 할 항목.

## 산출물

| 단계 | 파일 | 내용 |
|---|---|---|
| SWAN coarse | `swan_spec.dat` | SWAN-포맷 2D 스펙트럼 시간열 (nest 경계점 × 주파수 × 방향) |
| SWAN coarse | `PRINT` | iteration 수렴(curvature stopping)·경고 |
| SWASH fine | `runup.tbl` | 정점별 수위·runup 시계열 |
| SWASH fine | `hsig.mat` | 니어쇼어 H_sig·wave setup 장 |

## 검증 포인트

1. **경계 연속성**: SWASH 외해 경계의 H_sig 가 SWAN nest 출력 H_sig 와 일치(±수 %)해야 함. 불일치 시 격자 정합·좌표계·방향관례(nautical/cartesian) 점검.
2. **스펙트럼 파싱**: SWASH PRINT 에서 `swan_spec.dat` 의 SWAN 헤더 인식 확인 (`SwashBCspecfile` SWAN 분기). 헤더 불일치 시 SWAN `NESTOUT` 포맷 확인.
3. **분산 표현**: SWASH `VERTICAL` 층수가 충분한지 — 상대수심 kd 가 클수록 층 필요(swash-tech §dispersion). 처오름대는 천수라 적은 층으로 충분.
4. **wetting-drying**: 처오름대 moving shoreline 이 안정적인지 (`SwashDryWet` 마스크). 진동·불안정 시 dt(CFL)·friction 조정.

## 관련 검수 노트

- SWAN nest writer: [`swan-nesting-io-implementation`](../../../models/SWAN/source-analysis/swan-nesting-io-implementation.md)
- SWASH spectral reader: [`swash-boundary-spectral-transfer`](../../../models/SWASH/source-analysis/swash-boundary-spectral-transfer.md)
- SWASH runup/wetting-drying: [`swash-wetting-drying-runup`](../../../models/SWASH/source-analysis/swash-wetting-drying-runup.md)
- 비정수압 분산: [`swash-nonhydrostatic-pressure-solver`](../../../models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md)
