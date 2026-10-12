---
file: models/SWAN/raw/source_code/swan/src/SwanCheckGrid.ftn90
lines: 176
sha256: b8267c694b88bf36871cd19e8a1511dcadfe9bcbc9b4c5dd6b09a493305f4d2e
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanCheckGrid.ftn90 — 판독 구간 기록

구간은 1행부터 176행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–56 | SwanCheckGrid 선언·기관·GPL·작성자·2007년 도입 이력을 포함한다(1–36). 삼각망(triangular mesh)의 계산 적합성 검사 목적을 적는다(38–40). 검사 방법 주석은 꼭짓점(vertex) 주변 셀(cell) 수 4..10과 삼각형 각도 143도 미만을 제시한다(44–46). 공통·격자 모듈과 implicit none을 포함한다(48–55). |
| 57–92 | 시작 시 1행 SwanCheckGrid 루틴 안. 꼭짓점·셀 인덱스와 IENT=0 SAVE 선언을 포함한다(57–65). 세 각의 코사인·변 길이 제곱·좌표차를 선언한다(67–78). acute·badvertex·메시지 문자열과 격자 꼭짓점 포인터를 선언한다(80–85). 구조·원문 안내 주석을 포함한다(87–92). 원문: `integer, save                         :: ient = 0  ! number of entries in this subroutine` (60). |
| 93–119 | 시작 시 1행 SwanCheckGrid 루틴 안. LTRACE이면 STRACE를 호출하고 vert를 격자 객체에 연결한다(93–97). badvertex를 거짓으로 초기화한다(103). 각 꼭짓점에서 noc>0이며 noc<4이며 vmark=0인 조건을 검사한다(104–110). 별도로 noc>10도 검사한다(111–115). 해당 점이 있으면 badvertex를 참으로 설정하며 ITEST>=30 조건에서 진단을 출력한다(107–114). 루프 뒤 badvertex이면 MSGERR(1)를 호출한다(118). 원문: `if (ltrace) call strace (ient,'SwanCheckGrid')` (93); `vert => gridobject%vert_grid` (97); `badvertex = .false.` (103); `do i = 1, nverts` (104); `noc = vert(i)%noc` (105); `if ( noc > 0 .and. noc < 4 .and. vmark(i) == 0 ) then` (106); `if ( ITEST >= 30 .and. .not.badvertex ) write(PRINTF,'(a)')` (107); `badvertex = .true.` (108); `if ( ITEST >= 30 ) write(PRINTF,101) noc, i` (109); `if ( noc > 10 ) then` (111); `if ( ITEST >= 30 .and. .not.badvertex ) write(PRINTF,'(a)')` (112); `badvertex = .true.` (113); `if ( ITEST >= 30 ) write(PRINTF,101) noc, i` (114); `if ( badvertex ) call msgerr (1, 'number of cells around vertex is smaller than 4 or larger than 10')` (118). |
| 120–146 | 시작 시 1행 SwanCheckGrid 루틴 안. acute를 참, 진단 줄 출력 표시 j를 0으로 초기화한다(120–124). 각 셀의 세 꼭짓점을 가져오고 세 변의 좌표차·길이 제곱을 계산한다(126–141). acute가 아직 참이면 세 변 제곱의 엄격한 합 비교로 예각 삼각형(acute triangle) 여부를 갱신한다(143–145). 원문: `acute = .true.` (120); `j = 0` (124); `do i = 1, ncells` (126); `v1 = kvertc(1,i)` (128); `v2 = kvertc(2,i)` (129); `v3 = kvertc(3,i)` (130); `xdif12 = xcugrd(v2) - xcugrd(v1)` (132); `ydif12 = ycugrd(v2) - ycugrd(v1)` (133); `xdif13 = xcugrd(v3) - xcugrd(v1)` (134); `ydif13 = ycugrd(v3) - ycugrd(v1)` (135); `xdif23 = xcugrd(v3) - xcugrd(v2)` (136); `ydif23 = ycugrd(v3) - ycugrd(v2)` (137); `len12 = xdif12*xdif12 + ydif12*ydif12` (139); `len13 = xdif13*xdif13 + ydif13*ydif13` (140); `len23 = xdif23*xdif23 + ydif23*ydif23` (141); `if (acute) acute = (len12+len23>len13) .and. (len23+len13>len12) .and. (len13+len12>len23)` (145). |
| 147–170 | 시작 시 1행 SwanCheckGrid 루틴·126행 i 루프 안. 벡터 내적(vector dot product)과 변 길이로 세 각의 코사인을 계산한다(147–149). 각 cosphi가 -0.8보다 크지 않으며 ITEST>=100일 때 메시지를 작성하고 MSGERR(1)를 호출한다(151–168). 메시지의 각도는 acos(cosphi)/degrad이다(153·159·165). 첫 메시지에서 빈 줄을 출력하고 j=1을 설정한다(152–155·158–161·164–167). 셀 루프를 닫는다(170). 원문: `cosphi1 =( xdif12*xdif13 + ydif12*ydif13)/(sqrt(len12*len13))` (147); `cosphi2 =(-xdif12*xdif23 - ydif12*ydif23)/(sqrt(len12*len23))` (148); `cosphi3 =( xdif13*xdif23 + ydif13*ydif23)/(sqrt(len13*len23))` (149); `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then` (151); `if ( j == 0 ) write(PRINTF,'(a)')` (152); `write (msgstr,'(a,i6,a,f12.5,a)') 'angle of cell no. ',i,' is ',acos(cosphi1)/degrad,' degrees'` (153); `call msgerr (1, trim(msgstr) )` (154); `j = 1` (155); `if ( .not. cosphi2 > -0.8 .and. ITEST >= 100 ) then` (157); `if ( j == 0 ) write(PRINTF,'(a)')` (158); `write (msgstr,'(a,i6,a,f12.5,a)') 'angle of cell no. ',i,' is ',acos(cosphi2)/degrad,' degrees'` (159); `call msgerr (1, trim(msgstr) )` (160); `j = 1` (161); `if ( .not. cosphi3 > -0.8 .and. ITEST >= 100 ) then` (163); `if ( j == 0 ) write(PRINTF,'(a)')` (164); `write (msgstr,'(a,i6,a,f12.5,a)') 'angle of cell no. ',i,' is ',acos(cosphi3)/degrad,' degrees'` (165); `call msgerr (1, trim(msgstr) )` (166); `j = 1` (167). |
| 171–176 | 시작 시 1행 SwanCheckGrid 루틴 안. 모든 셀이 예각이면 MSGERR(0)으로 안내한다(172). 주변 셀 수의 FORMAT·빈 주석과 루틴 종료를 포함한다(174–176). 원문: `if (acute) call msgerr (0, 'The grid contains solely acute triangles ')` (172). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 45·99–106·118: 주변 셀 수 하한 주석은 최소 4이다. 실제 하한 경고 조건은 noc>0, noc<4, vmark=0을 함께 요구하며 noc=0은 이 조건에 포함되지 않는다.
- 46·122·151–168: 주석은 삼각형 각도 143도 미만을 적는다. 실제 경고 조건은 cosphi>-0.8의 부정과 ITEST>=100을 함께 사용한다.
- 139–149·153·159·165: 코사인 식의 분모는 변 길이 제곱의 곱에 대한 제곱근이다. 0 분모 검사와 acos 입력을 [-1,1]로 제한하는 문장은 해당 계산 앞에 없다.
