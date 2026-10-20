---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/SimulationParams.h
lines: 201
sha256: 822a2a77a453ac0ab414f21f156d6509c5b60c0858b86ac6729c2eb7348f2763
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# SimulationParams.h — 판독 구간 기록

구간은 1행부터 201행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | `#pragma once` (1), 좌표·실수형·SolverParams·문자열 키 판독 헤더 포함(3–8). 전처리 조건 분기는 없다. 구조체 기본값은 `real       xmin      = C(0.0);` (12), `real       xmax      = C(0.0);` (13), `real       ymin      = C(0.0);` (14), `real       ymax      = C(0.0);` (15), `Coordinate xsz       = 0;` (16), `Coordinate ysz       = 0;` (17), `real       g         = C(9.80665);` (18), `real       time      = C(0.0);` (19), `real       manning   = C(0.0);` (20), `bool       is_monai  = false;` (21), `bool       is_oregon = false;` (22). |
| 24–62 | 생성자는 시험 번호·입력 파일명·최대 세분화 수준을 받는다(24–29). `int mesh_dim = 1 << max_ref_lvl;` (31). `switch (test_case)` (33)의 `case 0: // raster file based test case` (35)에서 수치표고모형(digital elevation model, DEM) 파일명을 `read_keyword_str`로 읽고 연다(37–40). `if (NULL == fp)` (42)이면 오류 출력 후 `exit(-1)` (44–45). `real cellsize = C(0.0);` (48). `ncols`·`nrows`·`xllcorner`·`yllcorner`·`cellsize`를 키 판독 함수로 읽는다(50–54). `this->xmax      = this->xmin + this->xsz * cellsize;` (55), `this->ymax      = this->ymin + this->ysz * cellsize;` (56). `sim_time`·`fpfric`를 읽는다(57–58). `this->is_monai  = !strncmp("monai.dem", dem_filename_buf, 9);` (59), `this->is_oregon = !strncmp("oregon-seaside-0p02m.dem", dem_filename_buf, 24);` (60). case를 나간다(62). |
| 63–76 | 시작 시 24행 생성자·33행 switch 안. `case 1: // c prop` (63), `case 2:` (64), `case 3:` (65), `case 4:` (66)는 같은 블록을 실행한다. `this->xmin = C(0.0);` (67), `this->xmax = C(50.0);` (68), `this->ymin = C(0.0);` (69), `this->ymax = C(50.0);` (70). xsz·ysz에 mesh_dim을 복사한다(71–72). `this->g    = C(9.80665);` (73), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (74), `this->manning = C(0.0);` (75). break(76). |
| 77–88 | 시작 시 24행 생성자·33행 switch 안. `case 5: // wet dam break` (77), `case 6:` (78). `this->xmin = C(0.0);` (79), `this->xmax = C(50.0);` (80), `this->ymin = C(0.0);` (81), `this->ymax = C(50.0);` (82). xsz·ysz에 mesh_dim을 복사한다(83–84). `this->g    = C(9.80665);` (85), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (86), `this->manning = C(0.0);` (87). break(88). |
| 89–100 | 시작 시 24행 생성자·33행 switch 안. `case 7: // dry dam break` (89), `case 8:` (90). `this->xmin = C(0.0);` (91), `this->xmax = C(50.0);` (92), `this->ymin = C(0.0);` (93), `this->ymax = C(50.0);` (94). xsz·ysz에 mesh_dim을 복사한다(95–96). `this->g    = C(9.80665);` (97), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (98), `this->manning = C(0.0);` (99). break(100). |
| 101–112 | 시작 시 24행 생성자·33행 switch 안. `case 9: // dry dam break w fric` (101), `case 10:` (102). `this->xmin = C(0.0);` (103), `this->xmax = C(50.0);` (104), `this->ymin = C(0.0);` (105), `this->ymax = C(50.0);` (106). xsz·ysz에 mesh_dim을 복사한다(107–108). `this->g    = C(9.80665);` (109), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (110), `this->manning = C(0.02);` (111). break(112). |
| 113–126 | 시작 시 24행 생성자·33행 switch 안. `case 11: // building overtopping` (113), `case 12:` (114), `case 13:` (115), `case 14:` (116). `this->xmin = C(0.0);` (117), `this->xmax = C(50.0);` (118), `this->ymin = C(0.0);` (119), `this->ymax = C(50.0);` (120). xsz·ysz에 mesh_dim을 복사한다(121–122). `this->g    = C(9.80665);` (123), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (124), `this->manning = C(0.02);` (125). break(126). |
| 127–138 | 시작 시 24행 생성자·33행 switch 안. `case 15: // triangle dam break` (127), `case 16:` (128). `this->xmin = C(0.0);` (129), `this->xmax = C(38.0);` (130), `this->ymin = C(0.0);` (131), `this->ymax = C(38.0);` (132). xsz·ysz에 mesh_dim을 복사한다(133–134). `this->g    = C(9.80665);` (135), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (136), `this->manning = C(0.0125);` (137). break(138). |
| 139–150 | 시작 시 24행 생성자·33행 switch 안. `case 17: // parabolic bowl, period "T" = 14.4 s` (139), `case 18:` (140). `this->xmin = C(-50.0);` (141), `this->xmax = C( 50.0);` (142), `this->ymin = C(-50.0);` (143), `this->ymax = C( 50.0);` (144). xsz·ysz에 mesh_dim을 복사한다(145–146). `this->g    = C(9.80665);` (147), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (148), `this->manning = C(0.0);` (149). break(150). |
| 151–161 | 시작 시 24행 생성자·33행 switch 안. `case 19: // three cones c prop` (151). `this->xmin = C( 10.0);` (152), `this->xmax = C( 70.0);` (153), `this->ymin = C(-10.0);` (154), `this->ymax = C( 50.0);` (155). xsz·ysz에 mesh_dim을 복사한다(156–157). `this->g    = C(9.80665);` (158), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (159), `this->manning = C(0.0);` (160). break(161). |
| 162–172 | 시작 시 24행 생성자·33행 switch 안. `case 20: // three cones dam break` (162). `this->xmin = C(0.0);` (163), `this->xmax = C(70.0);` (164), `this->ymin = C(0.0);` (165), `this->ymax = C(30.0);` (166). xsz·ysz에 mesh_dim을 복사한다(167–168). `this->g    = C(9.80665);` (169), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (170), `this->manning = C(0.018);` (171). break(172). |
| 173–184 | 시작 시 24행 생성자·33행 switch 안. `case 21: // diff and non diff topo c prop` (173), `case 22:` (174). `this->xmin = C(0.0);` (175), `this->xmax = C(75.0);` (176), `this->ymin = C(0.0);` (177), `this->ymax = C(75.0);` (178). xsz·ysz에 mesh_dim을 복사한다(179–180). `this->g    = C(9.80665);` (181), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (182), `this->manning = C(0.0);` (183). break(184). |
| 185–201 | 시작 시 24행 생성자·33행 switch 안. `case 23: // radial dam break` (185). `this->xmin = C(-20.0);` (186), `this->xmax = C( 20.0);` (187), `this->ymin = C(-20.0);` (188), `this->ymax = C( 20.0);` (189). xsz·ysz에 mesh_dim을 복사한다(190–191). `this->g    = C(9.80665);` (192), `this->time = read_keyword_real(input_filename, "sim_time", 8);` (193), `this->manning = C(0.0);` (194). break(195)。 `default:` (196)는 break만 한다(197). switch·생성자·구조체를 닫는다(198–201). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 40–62: DEM 파일을 fopen하여 NULL 여부를 검사하지만 이 case 안에는 해당 fp의 fclose 호출이 없다. 헤더 값은 파일명을 받는 별도 키 판독 함수로 읽는다.
- 59–60: 시험 식별은 파일명 문자열의 앞 9자와 앞 24자를 strncmp로 비교한다.
- 196–197: 열거되지 않은 시험 번호는 default에서 break하며 오류를 출력하지 않는다.
