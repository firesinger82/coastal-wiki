---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/StagePoints.h
lines: 142
sha256: 5f1b2874e9ab62700d7e60f6f1ddfd98b8cd70c4670227479c6e2116dd603921
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# StagePoints.h — 판독 구간 기록

구간은 1행부터 142행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | `#pragma once` (1), SimulationParams·모턴 코드(Morton code) 생성 헤더 포함(3–5). 전처리 조건 분기는 없다. codes 포인터·num_points·`bool        is_copy_cuda = false;` (9–11). 생성자에서 `read_num_stage_points`를 호출한다(21). `codes      = (num_points > 0) ? new MortonCode[num_points] : nullptr;` (22). `read_stage_points`에 파일명·셀 크기·모의 매개변수를 전달한다(24–29). 복사 생성자는 멤버 복사 후 is_copy_cuda=true(32). 소멸자 원문은 `~StagePoints() { if (!is_copy_cuda && codes != nullptr) delete[] codes; }` (34). |
| 36–78 | `read_num_stage_points`는 개수를 0으로, 문자 버퍼를 널 문자로 초기화한다(36–42). 입력 파일을 연 뒤(44), `if (NULL == fp)` (46)이면 오류 출력·exit(-1)(48–49). `while ( strncmp(buf, "stagefile", 9) )` (52) 안에서 `if ( NULL == fgets(str, sizeof(str), fp) )` (54)이면 로그·fclose·return 0(56–58). 그 외에는 `sscanf`로 키와 파일명을 읽는다(61). 입력 파일을 닫고 관측 파일을 연다(64–66). `if (NULL == fp)` (68)이면 오류 출력·exit(-1)(70–71). `fscanf`로 개수를 읽고 반환한다(74–76). |
| 79–125 | `read_stage_points`는 파일명·셀 크기·SimulationParams 참조를 받는다(79–84). `if (num_points == 0) return;` (86). 지역 개수·문자 버퍼 초기화 뒤 입력 파일을 연다(88–94). `if (NULL == fp)` (96)이면 오류 출력·exit(-1)(98–99). `while ( strncmp(buf, "stagefile", 9) )` (102) 안에서 `if ( NULL == fgets(str, sizeof(str), fp) )` (104)이면 로그·fclose·return(106–108). `sscanf`로 파일명을 읽는다(111). 입력 파일을 닫고 관측 파일을 연다(114–116). `if (NULL == fp)` (118)이면 오류 출력·exit(-1)(120–121). 파일의 개수를 지역 num_stage_points에 읽는다(124). |
| 126–142 | 시작 시 79행 read_stage_points 안. `real x_stage = C(0.0);` (126), `real y_stage = C(0.0);` (127). `for (int i = 0; i < num_points; i++)` (129) 안에서 `fscanf(fp, "%" NUM_FRMT " %" NUM_FRMT, &x_stage, &y_stage);` (131)로 좌표를 읽는다. `Coordinate x = (x_stage - sim_params.xmin) / cell_size;` (133), `Coordinate y = (y_stage - sim_params.ymin) / cell_size;` (134), `codes[i] = generate_morton_code(x, y);` (136). 루프 뒤 fclose하고 메서드·구조체를 닫는다(137–142). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 66–76: read_num_stage_points는 관측 파일의 개수를 읽은 뒤 fclose 없이 반환한다.
- 124·129: read_stage_points는 파일의 개수를 지역 num_stage_points에 읽지만 반복 한계에는 멤버 num_points를 쓴다.
- 61·74·111·124·131: sscanf/fscanf의 반환값을 검사하는 문장은 없다. 좌표의 영역 검사와 cell_size의 0 여부 검사도 133–136행에 없다.
