ShorelineS 판독 기록 전수 검증 — 2026-10-12

사용자가 지정한 기록 24개를 원문과 대조했다. 각 원문 경로는 기록의 frontmatter `file:`에서 읽었다. 각 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. ISO-8859-1 문자는 출력 단계에서 UTF-8로 변환했다.

기록 전체 행 수는 frontmatter, 제목, 표 머리말, 빈 줄을 포함한 물리 행 수다. 구간 행은 구간 표의 본문 행이다. 사실 행은 「판독 중 확인된 코드 사실」 목록의 항목 행이다. 정정·보완·이상 없음은 구간 행과 사실 행을 합친 본문 대조 항목 수다. 같은 행의 변경은 한 항목으로 집계했다. 이상 없음은 대조 후 수정하지 않은 항목이다.

모든 구간의 실행 조건, 계산식, 입력 필드 대입, 기본값, 부정, 수량, 분기, 단위, 순서를 대조했다. 배열 용도의 근거, 삭제 대상, 점 개수, 구간 시작의 바깥 블록도 대조했다. 표 아래 사실 목록의 각 문장도 대조했다.

| 기록 | 기록 전체 행 | 구간 행 | 사실 행 | 원문 대조 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|
| [prepare_channel.m.md](shorelines/functions/prepare_channel.m.md) | 25 | 4 | 4 | 137 | 0 | 1 | 7 |
| [prepare_climatechange.m.md](shorelines/functions/prepare_climatechange.m.md) | 25 | 5 | 3 | 154 | 1 | 0 | 7 |
| [prepare_coastline.m.md](shorelines/functions/prepare_coastline.m.md) | 26 | 5 | 4 | 174 | 0 | 1 | 8 |
| [prepare_delta.m.md](shorelines/functions/prepare_delta.m.md) | 23 | 3 | 3 | 88 | 0 | 0 | 6 |
| [prepare_dunes.m.md](shorelines/functions/prepare_dunes.m.md) | 24 | 3 | 4 | 147 | 0 | 1 | 6 |
| [prepare_fnourishment.m.md](shorelines/functions/prepare_fnourishment.m.md) | 26 | 5 | 4 | 132 | 0 | 0 | 9 |
| [prepare_grid_groyne.m.md](shorelines/functions/prepare_grid_groyne.m.md) | 36 | 11 | 8 | 409 | 0 | 0 | 19 |
| [prepare_mudcoast.m.md](shorelines/functions/prepare_mudcoast.m.md) | 24 | 4 | 3 | 136 | 0 | 0 | 7 |
| [prepare_nourishment.m.md](shorelines/functions/prepare_nourishment.m.md) | 27 | 5 | 5 | 172 | 0 | 1 | 9 |
| [prepare_runupconditions.m.md](shorelines/functions/prepare_runupconditions.m.md) | 27 | 6 | 4 | 176 | 1 | 0 | 9 |
| [prepare_spit.m.md](shorelines/functions/prepare_spit.m.md) | 23 | 3 | 3 | 90 | 0 | 0 | 6 |
| [prepare_structures.m.md](shorelines/functions/prepare_structures.m.md) | 37 | 11 | 9 | 368 | 0 | 3 | 17 |
| [prepare_tide.m.md](shorelines/functions/prepare_tide.m.md) | 23 | 3 | 3 | 83 | 0 | 0 | 6 |
| [prepare_transport.m.md](shorelines/functions/prepare_transport.m.md) | 30 | 7 | 6 | 223 | 0 | 1 | 12 |
| [prepare_waveconditions.m.md](shorelines/functions/prepare_waveconditions.m.md) | 24 | 4 | 3 | 123 | 0 | 1 | 6 |
| [prepare_windconditions.m.md](shorelines/functions/prepare_windconditions.m.md) | 23 | 3 | 3 | 96 | 0 | 0 | 6 |
| [readkeys.m.md](shorelines/functions/readkeys.m.md) | 26 | 4 | 5 | 75 | 0 | 0 | 9 |
| [runShorelineS.m.md](shorelines/functions/runShorelineS.m.md) | 21 | 2 | 2 | 48 | 0 | 0 | 4 |
| [save_shorelines.m.md](shorelines/functions/save_shorelines.m.md) | 42 | 17 | 8 | 512 | 1 | 0 | 24 |
| [save_shorelines_netcdf.m.md](shorelines/functions/save_shorelines_netcdf.m.md) | 44 | 17 | 10 | 436 | 0 | 0 | 27 |
| [select_multi_polygon.m.md](shorelines/functions/select_multi_polygon.m.md) | 24 | 4 | 3 | 99 | 0 | 0 | 7 |
| [snap_coastline_to_data.m.md](shorelines/functions/snap_coastline_to_data.m.md) | 24 | 4 | 3 | 45 | 0 | 0 | 7 |
| [struct2log.m.md](shorelines/functions/struct2log.m.md) | 29 | 7 | 5 | 157 | 1 | 0 | 11 |
| [tide_1d_ana_anycomp.m.md](shorelines/functions/tide_1d_ana_anycomp.m.md) | 27 | 4 | 6 | 92 | 0 | 0 | 10 |
| 합계 | 660 | 141 | 111 | 4172 | 4 | 9 | 239 |

수치는 위 대상 기록과 각 `file:` 원문의 행을 집계한 값이다. 각 원문은 1행부터 마지막 행까지 대조했다.

정정 내역은 다음과 같다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [prepare_climatechange.m.md](shorelines/functions/prepare_climatechange.m.md):사실 18·55·58·125·148 | 55·58행 초기값을 도 단위 변화율로 묶어 설명. | DIR의 °/yr과 PHIcor의 °를 구별한다. | [prepare_climatechange.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_climatechange.m):55·58·125 |
| [prepare_runupconditions.m.md](shorelines/functions/prepare_runupconditions.m.md):사실 157–169 | 위치 개수 불일치를 경고 출력으로만 설명. | 경고에는 157행과 158행 조건이 모두 필요함을 명시한다. | [prepare_runupconditions.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_runupconditions.m):157–159 |
| [save_shorelines.m.md](shorelines/functions/save_shorelines.m.md):사실 495–497 | 파일 저장 전후에 경고를 항상 끄고 켠다고 설명. | 경고 상태 변경의 ~isoctave 조건을 명시한다. | [save_shorelines.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/save_shorelines.m):495–497 |
| [struct2log.m.md](shorelines/functions/struct2log.m.md):81–106 | 수치 분기를 닫은 뒤 대괄호와 줄 끝을 출력한다고 설명. | mm 루프 종료, 대괄호 출력, 길이 조건 종료의 순서를 구별한다. | [struct2log.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/struct2log.m):96–105 |

보완 내역은 다음과 같다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [prepare_channel.m.md](shorelines/functions/prepare_channel.m.md):55–97 | 안내문 위치 계산식 생략. | 안내문 x·y 위치 계산식을 인용한다. | [prepare_channel.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_channel.m):72 |
| [prepare_coastline.m.md](shorelines/functions/prepare_coastline.m.md):98–141 | 안내문 위치 계산식 생략. | 안내문 x·y 위치 계산식을 인용한다. | [prepare_coastline.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_coastline.m):135 |
| [prepare_dunes.m.md](shorelines/functions/prepare_dunes.m.md):1–72 | perctill 범위만 설명하고 모래 백분율 식 생략. | 주석의 모래 백분율 식을 인용한다. | [prepare_dunes.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_dunes.m):33 |
| [prepare_nourishment.m.md](shorelines/functions/prepare_nourishment.m.md):118–154 | 안내문 위치 계산식 생략. | 안내문 x·y 위치 계산식을 인용한다. | [prepare_nourishment.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_nourishment.m):151 |
| [prepare_structures.m.md](shorelines/functions/prepare_structures.m.md):131–170 | 안내문 위치 계산식과 132행 조건 종료 위치 생략. | 안내문 위치 식을 인용한다. nhard 계산이 132행 조건 밖임을 명시한다. | [prepare_structures.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_structures.m):138·160–162 |
| [prepare_structures.m.md](shorelines/functions/prepare_structures.m.md):237–269 | 안내문 위치 계산식 생략. | 안내문 x·y 위치 계산식을 인용한다. | [prepare_structures.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_structures.m):244 |
| [prepare_structures.m.md](shorelines/functions/prepare_structures.m.md):270–313 | 안내문 위치 계산식과 272행 조건 종료 위치 생략. | 안내문 위치 식을 인용한다. 302행 조건이 272행 조건 밖임을 명시한다. | [prepare_structures.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_structures.m):278·301–302 |
| [prepare_transport.m.md](shorelines/functions/prepare_transport.m.md):151–175 | 안내문 위치 계산식 생략. | 안내문 x·y 위치 계산식을 인용한다. | [prepare_transport.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_transport.m):157 |
| [prepare_waveconditions.m.md](shorelines/functions/prepare_waveconditions.m.md):1–61 | 주석의 파향 범위식을 산문으로만 설명. | 주석의 파향 범위식을 원문 그대로 인용한다. | [prepare_waveconditions.m](../../../../models/ShorelineS/raw/source_code/shorelines/functions/prepare_waveconditions.m):16 |

각 변경 행 끝에 요청한 정정 또는 보완 표식을 붙였다. 원문 해시는 각 기록의 frontmatter 해시와 일치했다. 구간 경계와 frontmatter는 변경하지 않았다. 정적 문자열 검사에서 본문의 백틱 인용은 해당 원문 구간과 일치했다. 단일 행 번호가 붙은 인용은 해당 원문 행과도 일치했다.

쓰기 대상은 지정된 판독 기록과 이 보고서로 제한했다. 원문과 노트는 수정하지 않았다. git 명령은 실행하지 않았다. 모델은 실행하지 않았다.

정정 4, 보완 9, 이상 없음 239
