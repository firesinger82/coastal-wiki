# SWAN 판독 기록 전수 대조 — doc-2

검증일은 2026-10-13이다.
기록 경로의 기준은 `_staging/recovery/read/SWAN/manuals/website/`이다.
원문 경로는 각 기록의 frontmatter `file:`을 따랐다.

각 기록의 구간 행마다 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문 구간은 200행 이하였다.
각 구간에서 인용 내용과 행 번호를 대조했다.
각 구간에서 요약의 부정·수량·조건·단위·순서를 대조했다.
표 밖의 확인 사실도 해당 원문과 로컬 파일 상태에 대조했다.

아래 표의 기록 행 수는 판독 표의 구간 행을 센 값이다.
원문 행 수는 빈 줄을 포함한 대조 구간의 행 수이다.
정정·보완·이상 없음의 집계 단위도 판독 표의 구간 행이다.
이상 없음은 정정이나 보완이 필요하지 않은 구간 행을 뜻한다.

| 기록 | 대조한 기록 행 수 | 원문 범위 | 대조한 원문 행 수 | 정정 | 보완 | 이상 없음 |
|---|---:|---|---:|---:|---:|---:|
| [research_and_development/jpgbook/pictures.htm.md](../manuals/website/research_and_development/jpgbook/pictures.htm.md) | 11 | 1–200 | 200 | 0 | 0 | 11 |
| [research_and_development/research_and_development.htm.md](../manuals/website/research_and_development/research_and_development.htm.md) | 3 | 1–42 | 42 | 0 | 0 | 3 |
| [settings/basin.swn.md](../manuals/website/settings/basin.swn.md) | 3 | 1–9 | 9 | 0 | 0 | 3 |
| [settings/booij99.swn.md](../manuals/website/settings/booij99.swn.md) | 3 | 1–7 | 7 | 0 | 0 | 3 |
| [settings/fort.26.v41.10.md](../manuals/website/settings/fort.26.v41.10.md) | 3 | 1–7 | 7 | 0 | 0 | 3 |
| [settings/fort.26.v41.31.md](../manuals/website/settings/fort.26.v41.31.md) | 3 | 1–7 | 7 | 0 | 0 | 3 |
| [settings/settings.htm.md](../manuals/website/settings/settings.htm.md) | 10 | 1–194 | 194 | 0 | 0 | 10 |
| [settings/tud.swn.md](../manuals/website/settings/tud.swn.md) | 3 | 1–9 | 9 | 0 | 0 | 3 |
| [settings/tud2.swn.md](../manuals/website/settings/tud2.swn.md) | 3 | 1–9 | 9 | 0 | 0 | 3 |
| [support/license.htm.md](../manuals/website/support/license.htm.md) | 4 | 1–70 | 70 | 0 | 1 | 3 |
| [support/support.htm.md](../manuals/website/support/support.htm.md) | 4 | 1–62 | 62 | 0 | 0 | 4 |
| 합계 | 50 | 전체 대상 구간 | 616 | 0 | 1 | 49 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [support/license.htm.md:27–44](../manuals/website/support/license.htm.md) | GPL 적용 조건과 SWAN의 풀어쓴 이름, 저작권 연도를 요약했다. 이 구간에는 원문 인용이 없었다. | GPL 적용 조건과 문구 부착 범위의 원문을 추가했다. SWAN의 풀어쓴 이름을 원문으로 추가했다. 저작권 연도 `1993-2024`와 저작권 주체를 원문으로 추가했다. [10-13 전수 검증 보완] | `models/SWAN/raw/manuals/website/support/license.htm` 27–35, 38–40, 42–43 |

최종 기록에서 행 번호가 붙은 원문 인용 372개를 문자열로도 대조했다.
이 인용은 모두 표시된 원문 행과 일치했다.
대상 원문에는 Fortran 분기·반복 블록이 없다.
대상 원문에는 `models/SWAN/raw/source_code/swan/switch.pl` 82–105행이 처리하는 행 첫머리 전처리 표시가 없다.
설정 명령 뒤의 `! note:` 문구는 인라인 주석으로 대조했다.

기록의 frontmatter는 변경하지 않았다.
기록의 구간 경계는 변경하지 않았다.
대상 원문의 SHA-256은 검증 전후에 같았다.
원문과 노트는 수정하지 않았다.
git은 조작하지 않았다.
모델은 실행하지 않았다.
HTML이 참조하는 그림의 내부 내용은 확인하지 않았다.

정정 0, 보완 1, 이상 없음 49
