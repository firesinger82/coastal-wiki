---
file: models/SWASH/raw/source_code/swash/src/SwashCheckGrid.ftn90
lines: 257
sha256: ecd79d6837f3ed18b0c31c0aebd98a4cd3d78876a0acd44deb99299a64e16615
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashCheckGrid.ftn90 — 판독 구간 기록

구간은 1행부터 257행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | `SwashCheckGrid` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자·2023년 신설(30–36). 삼각 격자(triangular mesh)의 꼭짓점 주변 셀 수 4..10·각도 90도 미만·격자 품질(mesh quality)을 검사한다는 목적·방법 주석(38–47). Bank의 PLTMG 1998 및 OceanMesh2D 사용자 안내서를 주석에서 참조한다(49–54). 해당 문헌 내부는 이 파일 판독 범위에 포함하지 않는다. |
| 56–125 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·SwanGriddata·SwanGridobjects 사용(58–61). `integer, save                         :: ient = 0  ! number of entries in this subroutine` (68). 인덱스·면적·변 길이 제곱·각도 코사인·셀 품질 qe·평균 qem·표준편차(standard deviation) qstd·논리변수·자료 포인터 선언(67–106). qe 주석은 0=완전 퇴화 삼각형(degenerated triangle), 1=정삼각형이다(87–89). `if (ltrace) call strace (ient,'SwashCheckGrid')` (114). vert/cell/face를 gridobject 자료에 연결한다(118–120). 내부 꼭짓점의 최소 셀 수와 전체 꼭짓점의 최대 셀 수 검사 주석(122–124). |
| 126–148 | 시작 시 1행 루틴 안. `badvertex = .false.` (126), i=1..nverts(127)에서 `noc = vert(i)%noc` (128). `if ( noc > 0 .and. noc < 4 .and. vmark(i) == 0 ) then` (129) 안 `if ( ITEST >= 30 .and. .not.badvertex ) write(PRINTF,'(a)')` (130), `badvertex = .true.` (131), `if ( ITEST >= 30 ) write(PRINTF,101) noc, i` (132). 별도 `if ( noc > 10 ) then` (134)도 `if ( ITEST >= 30 .and. .not.badvertex ) write(PRINTF,'(a)')` (135), `badvertex = .true.` (136), `if ( ITEST >= 30 ) write(PRINTF,101) noc, i` (137). 루프 후 `if ( badvertex ) call msgerr (1, 'number of cells around vertex is smaller than 4 or larger than 10')` (141). `acute = .true.` (143). `jf = 0` (147). 145행 주석은 90도보다 큰 각도를 검사한다고 적는다. 174·180·186행 실행 조건은 0 이하의 코사인을 검사하므로 90도도 포함한다. [10-15 전수 검증 보완] |
| 149–173 | 시작 시 1행 루틴 안. i=1..ncells(149)에서 `v1 = kvertc(1,i)` (151). 같은 루프에서 `v2 = kvertc(2,i)` (152). `v3 = kvertc(3,i)` (153). `xdif12 = xcugrd(v2) - xcugrd(v1)` (155), `ydif12 = ycugrd(v2) - ycugrd(v1)` (156), `xdif13 = xcugrd(v3) - xcugrd(v1)` (157), `ydif13 = ycugrd(v3) - ycugrd(v1)` (158), `xdif23 = xcugrd(v3) - xcugrd(v2)` (159), `ydif23 = ycugrd(v3) - ycugrd(v2)` (160). `len12 = xdif12*xdif12 + ydif12*ydif12` (162), `len13 = xdif13*xdif13 + ydif13*ydif13` (163), `len23 = xdif23*xdif23 + ydif23*ydif23` (164). `if (acute) acute = (len12+len23>len13) .and. (len23+len13>len12) .and. (len13+len12>len23)` (168). `cosphi1 =( xdif12*xdif13 + ydif12*ydif13)/(sqrt(len12*len13))` (170), `cosphi2 =(-xdif12*xdif23 - ydif12*ydif23)/(sqrt(len12*len23))` (171), `cosphi3 =( xdif13*xdif23 + ydif13*ydif23)/(sqrt(len13*len23))` (172). [10-15 전수 검증 보완] |
| 174–200 | 시작 시 1행 루틴·149행 `do i = 1, ncells` 안. `if ( .not. cosphi1 > 0. .and. ITEST >= 100 ) then` (174), `if ( .not. cosphi2 > 0. .and. ITEST >= 100 ) then` (180), `if ( .not. cosphi3 > 0. .and. ITEST >= 100 ) then` (186)은 각각 `if ( jf == 0 ) write(PRINTF,'(a)')` (175·181·187), `acos(cosphi1)/degrad` (176)·`acos(cosphi2)/degrad` (182)·`acos(cosphi3)/degrad` (188)를 도 단위로 기록한 메시지 생성, `call msgerr (1, trim(msgstr) )` (177·183·189), `jf = 1` (178·184·190). 셀 루프 종료(193). `if (acute) call msgerr (0, 'The grid contains solely acute triangles ')` (195). 정삼각형 기준 품질 검사 주석(197–198), `fac = 4.*sqrt(3.)` (200). 각 IF는 각각 179·185·191행에서 닫힌다. [10-15 전수 검증 보완] |
| 201–231 | 시작 시 1행 루틴 안. qe(ncells) 할당(202), `qem = 0.` (204). i=1..ncells(206)에서 `area = cell(i)%attr(CELLAREA)` (208), `lsq = 0.` (210), jf=1..cell(i)%nof(212)에서 `iface = cell(i)%face(jf)%atti(FACEID)` (216)·`lf = face(iface)%attr(FACELEN)` (218), `lsq = lsq + lf*lf` (220). 면 루프 종료(222), `qe(i) = fac * area / lsq` (224), `qem = qem + qe(i)` (226). 셀 루프 종료(228), `qem = qem / real(ncells)` (230). [10-15 전수 검증 보완] |
| 232–257 | 시작 시 1행 루틴 안. `qstd = 0.` (232), i=1..ncells(234)에서 `qstd = qstd + (qe(i)-qem)**2` (236). `qstd = sqrt(qstd/(real(ncells)-1.))` (240), `mshq = qem - 3.*qstd` (242). `if ( mshq > 0.75 .or. qem > 0.9 ) then` (245)은 높은 품질 msgerr(0)(246), `else` (247)는 낮은 품질 msgerr(1)(248). `write(PRINTF,102) 100.*qem` (250)로 평균 품질을 백분율로 출력한다(255). qe 해제(252), format 101/102(254–255), 루틴 종료(257). 248행 경고는 퇴화 요소가 포함되었을 가능성을 괄호 안에 표시한다. 245행 조건은 249행에서 닫힌다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45·129·134: 방법 주석의 주변 셀 수 하한은 4이다. 실행문은 noc>0이고 noc<4이며 vmark=0인 꼭짓점만 하한 경고 대상으로 삼는다. noc>10 검사는 vmark 조건을 사용하지 않는다.
- 162–172·176·182·188: len12·len13·len23는 변 길이의 제곱이다(162–164). 각도 코사인은 두 변 벡터의 내적을 두 변 길이의 곱으로 나눈 값이다(170–172). 분모의 `sqrt(len12*len13)`·`sqrt(len12*len23)`·`sqrt(len13*len23)`은 변 길이 제곱의 곱에 제곱근을 취한다(170–172). 이 루틴에는 0 길이 변 검사나 acos 입력을 [-1,1]로 제한하는 문장이 없다. [10-15 전수 검증 정정]
- 168·174–195: acute는 직각 삼각형도 거짓으로 만든다. 개별 각도 경고는 ITEST>=100일 때만 실행한다. 전체가 예각일 때의 메시지는 있으며, acute가 거짓일 때의 별도 전체 경고 분기는 없다.
- 224·230·240: 품질식은 lsq, 평균식은 ncells, 표준편차식은 ncells-1을 분모로 사용한다. 이 루틴에는 각 분모가 0인지 확인하는 조건이 없다.
- 242·245: 품질 판단은 평균에서 표준편차의 3배를 뺀 값이 0.75 초과이거나 평균이 0.9 초과라는 고정 기준을 사용한다.
