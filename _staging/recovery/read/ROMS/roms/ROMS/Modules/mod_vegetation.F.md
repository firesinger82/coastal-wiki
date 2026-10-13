---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_vegetation.F
lines: 90
sha256: 139983dc909aee40e61e1e78de5dc77db7526626b1a3e8d18a204f8fed65db8e
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_vegetation.F — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)로 `cppdefs.h`를 끼워 넣고 `mod_vegetation` 모듈을 연다(2). 빈 줄과 C 형식 주석 시작(3–4). 저작권·MIT/X 라이선스 주석(5–10). 침수 수생 식생(submerged aquatic vegetation) 모델의 상태 변수(state variable)와 내부 매개변수를 선언한다는 설명(12–14). 매개변수 일부는 입력 스크립트에서 읽으며, 사용자 확장이 가능하다는 주석(14–17). 끝 주석행 포함(18). |
| 19–59 | 시작 시 열린 전처리 조건 없음·2행 모듈 안이며 4행 C 형식 주석 안. 구성 파일의 역할을 설명한다. vegetation_drag.F는 3차원 우변(right-hand side, rhs3d)을 수정한다(21–23). vegetation_turb.F는 난류(turbulence) 항을 수정한다(25–27). vegetation_stream.F는 파랑 유도 흐름(streaming) 항을 수정한다(29–31). vegetation_biomass.F는 생물량(biomass)을 계산한다(33–35). vegetation_output.F는 식생 변수를 NetCDF 파일에 출력한다(37–39). marsh_dynamics.F는 염습지 동역학(marsh dynamics)의 주 호출 루틴이다(41–43). marsh_wave_thrust.F는 염습지 파랑 추력(wave thrust)을 계산한다(45–47). marsh_sed_erosion.F는 퇴적물 침식(sediment erosion)을 계산한다(49–51). marsh_tidal_range.F는 평균 고조위(mean high water)·조석 계산을 담당한다는 주석이다(53–55). marsh_vert_growth.F는 수직 성장을 계산한다(57–59). 이 구간은 파일 목록 주석이며 실행 호출문이 없다. |
| 60–85 | 시작 시 열린 전처리 조건 없음·2행 모듈 안이며 4행 C 형식 주석 안. vegetation_mod.h는 내부 매개변수 선언(61–63), vegetation.in은 표준 입력 스크립트(65–67), vegetation_inp.h는 매개변수 판독 코드(69–71), vegetation_var.h는 varinfo.yaml 메타데이터(metadata) 판독 때 모델 변수 인덱스를 정하는 코드로 설명한다(73–76). 파일 위치는 ROMS/Nonlinear/Vegetation이라는 주석이다(78). `<...>` 형식의 포함은 배포 코드를 유지하면서 프로젝트 디렉터리에서 사용자 정의 파일을 선택하게 한다는 주석이다(79–81). 주석 끝과 빈 줄 포함(82–85). 목록에 적힌 파일 내부는 이 대상 파일에서 판독하지 않았다. |
| 86–90 | 시작 시 열린 전처리 조건 없음·2행 모듈 안. `#if defined VEGETATION` (86) 안에서 `# include <vegetation_mod.h>` (87)로 `vegetation_mod.h`를 끼워 넣는다. `#endif` (88)로 닫는다. 빈 줄·모듈 종료(89–90). 이 파일에 직접 적힌 계산식·기본값 대입·실행 호출문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
