---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/maxmin63.rst
lines: 62
sha256: d11610f3a8ed7545a6f538f8a9a81719ad4d5d848788b32c3502b84cc6bc569f
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# maxmin63.rst — 판독 구간 기록

구간은 1행부터 62행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | Maximum and Minimum Value Files (max*.63, min*.63) — orphan 지시문·앵커·제목·빈 줄을 포함한다(1–9·15·17). 목록은 절점(node)별 최대 수위(water surface elevation), 최대 유속 크기(water velocity magnitude), 최대 풍속 크기(wind velocity magnitude), 최대 파랑 복사응력(wave radiation stress), 최소 기압(barometric pressure)의 파일을 제시한다(10–14). 파랑 복사응력 파일의 적용 조건은 해당 목록에 명시되어 있다(13). 문서는 높은 빈도의 시계열 출력 없이 극값(extreme values)을 효율적으로 기록하려고 이 파일들을 개발했다고 적는다(16). ADCIRC는 시간 단계마다 극값을 수집한다(16). 파일은 모의가 끝난 뒤 쓴다(16). 원문: ` :orphan: ` (1); ` * **maxele.63**: Maximum water surface elevation at each node ` (10); ` * **maxvel.63**: Maximum water velocity magnitude at each node ` (11); ` * **maxwvel.63**: Maximum wind velocity magnitude at each node ` (12); ` * **maxrs.63**: Maximum wave radiation stress at each node (if wave forcing is enabled) ` (13); ` * **minpr.63**: Minimum barometric pressure at each node ` (14); ` These files were developed to efficiently record extreme values at each node in the domain without requiring high-frequency time series output. ADCIRC collects these extreme values at every time step and writes them after the simulation completes. ` (16). |
| 18–22 | Hotstart Considerations — 재시작(hotstart) 때 ADCIRC는 실행 디렉터리에서 기존 극값 파일을 읽으려고 시도한다(21). 파일을 찾으면 해당 값을 재시작 실행의 초기 조건으로 사용한다(21). 문서는 이를 여러 모의 구간 사이의 극값 추적 연속성을 위한 처리로 설명한다(21). 제목과 빈 줄을 포함한다(18–22). 원문: ` When using hotstart files to restart a simulation, ADCIRC will attempt to load existing extreme value files from the run directory at startup. If found, these values are used as initial conditions for the hotstarted run, ensuring continuity of extreme value tracking across multiple simulation segments. ` (21). |
| 23–49 | File Structure — 문서는 ADCIRC version 51부터 전체 영역 자료 집합(datasets)을 둘 포함한다고 적는다(26). 첫째 자료는 절점별 극값이다(27). 둘째 자료는 초기 시작(cold start) 이후 초 단위로 적은 극값 발생 시각이다(28). 예제는 헤더의 자료 집합 수를 2로 적는다(36). 예제는 극값 블록과 발생 시각 블록을 각각 제시한다(38–48). 지시문과 중간 빈 줄을 포함한다(23–49). 원문: ` Since ADCIRC version 51, these files contain two full domain datasets: ` (26); ` 1. The extreme value at each node ` (27); ` 2. The time (in seconds since cold start) when each extreme value occurred ` (28); ` .. parsed-literal:: ` (32); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (34); ``     2, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`NSPOOLGE <NSPOOLGE>`, :ref:`IRTYPE <IRTYPE>` `` (36); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (38); ``     for k=1, :ref:`NP <NP>` `` (40); `         k, extreme_value(k) ` (41); `     end k loop ` (42); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (44); ``     for k=1, :ref:`NP <NP>` `` (46); `         k, time_of_extreme(k) ` (47); `     end k loop ` (48). |
| 50–62 | Notes — 문서는 출력 형식 설정과 이진(binary) 출력의 절점 번호 생략을 설명한다(53–54). version 51 이전에는 발생 시각 없이 극값만 포함했다고 적는다(55). 파일은 모의 종료에만 쓴다(56). 극값은 모의 중 매 시간 단계에서 계속 추적한다(57). 재시작 때는 이전 실행의 극값도 고려한다(58). 문서는 이 파일들이 전체 시계열의 큰 파일 크기, 지점 출력의 제한된 공간 범위, 출력 빈도 제한에 따른 첨두값 누락 문제를 피하는 데 도움이 된다고 적는다(59–62). 원문: `` * Output format (ASCII/binary) is determined by :ref:`NOUTGE <NOUTGE>` in the fort.15 file `` (53); ` * For binary output, the node number (k) is not included in the output ` (54); ` * Prior to ADCIRC version 51, only the extreme values were included (without timing information) ` (55); ` * Files are written only at the end of the simulation ` (56); ` * Values are tracked continuously throughout the simulation at every time step ` (57); ` * Extreme values from previous runs are considered when using hotstart ` (58). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
