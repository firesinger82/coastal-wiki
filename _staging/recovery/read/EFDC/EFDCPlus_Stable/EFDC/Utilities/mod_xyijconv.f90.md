---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_xyijconv.f90
lines: 491
sha256: 9d1f4facd799eaea005d01c86520c2c3acd89266bf2db4bccb004ee32aca5cd8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_xyijconv.f90 — 판독 구간 기록

구간은 1행부터 491행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | EFDC+·GPLv2 머리말(1–8). XYIJCONV·작성자·GLOBAL·INFOMOD·MPI 변수·MPI 매핑(mapping)·Broadcast_Routines 사용과 implicit none·contains·빈 줄(9–21). |
| 22–40 | XY2IJ의 CELL형 CEL과 선택 인수 VALID·지역 정수 선언(22–25). `if( PRESENT(VALID) )then` (27)은 `ISVALID = 1` (28), `else` (29)는 `ISVALID = 0` (30). `NPMAX = SIZE(CEL.XCEL)` (33). `do N = 1,NPMAX` (35)에서 `call CONTAINERIJ_GL(N, CEL.XCEL(N), CEL.YCEL(N), CEL.ICEL(N), CEL.JCEL(N), ISVALID)` (36). 루프·루틴 종료·빈 줄(37–40). |
| 41–84 | CONTAINERIJ 인수·지역 선언(41–48). 최근접 거리 원문은 `RADLA(2:LA) = SQRT((XCLL-XCOR(2:LA,5))**2+(YCLL-YCOR(2:LA,5))**2)` (51; 뒤 주석은 비효율성과 개선 TODO를 적는다). `LMILOC = MINLOC(RADLA(2:LA))` (52), `ILN = IL(LMILOC(1)+1)    !I OF THE NEAREST CELL FOR DRIFTER` (53), `JLN = JL(LMILOC(1)+1)    !J OF THE NEAREST CELL FOR DRIFTER` (54). `I1 = max(1,ILN-1)` (57), `I2 = min(ILN+1,ICM)` (58), `J1 = max(1,JLN-1)` (59), `J2 = min(JLN+1,JCM)` (60). J/I 루프(61–62)에서 LIJ를 조회(63), `if( L < 2 ) CYCLE` (64). `if( INSIDECELL(L, XCLL, YCLL) )then` (65)은 ICLL/JCLL 복사 후 return(66–68). 검색 실패 뒤 `if( ISVALID > 0 )then` (74)은 `ICLL = -999` (76), `JCLL = -999` (77). `else` (78)는 메시지 출력과 `call STOPP('Invalid XY in SUBSET.INP')` (80). 종료·빈 줄(81–84). |
| 85–128 | CONTAINERIJ_GL은 전역 배열을 쓰는 대응 루틴이다(85–92). `RADLA(2:LA_GLOBAL) = SQRT((XCLL-XCOR_Global(2:LA_GLOBAL,5))**2+(YCLL-YCOR_Global(2:LA_GLOBAL,5))**2)` (95; 뒤 개선 TODO 주석), `LMILOC = MINLOC(RADLA(2:LA_GLOBAL))` (96), `ILN = IL_GL(LMILOC(1)+1)    !I OF THE NEAREST CELL FOR DRIFTER` (97), `JLN = JL_GL(LMILOC(1)+1)    !J OF THE NEAREST CELL FOR DRIFTER` (98). `I1 = max(1,ILN-1)` (101), `I2 = min(ILN+1,ICM_Global)` (102), `J1 = max(1,JLN-1)` (103), `J2 = min(JLN+1,JCM_Global)` (104). J/I 루프(105–106)에서 LIJ_Global 조회(107), `if( L < 2 ) CYCLE` (108). `if( INSIDECELL_GL(L, XCLL, YCLL) )then` (109)은 인덱스 복사 후 return(110–112). 실패 시 `if( ISVALID > 0 )then` (118)은 `ICLL = -999` (120), `JCLL = -999` (121). `else` (122)는 출력과 STOPP 호출(123–124). 종료·빈 줄(125–128). |
| 129–164 | 다각형(polygon) 면적 AREACAL 안내·작성자·날짜(129–138), 인수와 XVEC/YVEC·NPOL/K 선언(139–148). `NPOL = SIZE(XC)` (151), AREA=0 초기화(152). `XVEC(1) = XC(2) - XC(1)` (154), `YVEC(1) = YC(2) - YC(1)` (155). `do K = 3,NPOL` (156)에서 `XVEC(2) = XC(K) - XC(1)` (157), `YVEC(2) = YC(K) - YC(1)` (158), `AREA    = AREA + 0.5*ABS( XVEC(1)*YVEC(2) - XVEC(2)*YVEC(1) )` (159). 이전 벡터에 현재 벡터를 복사(160–161), 루프·루틴 종료·빈 줄(162–164). |
| 165–205 | INSIDECELL 안내·선언(165–187). 검사점과 셀 네 꼭짓점을 XC/YC(1:5)에 넣고 여섯째 원소에 둘째 원소를 복사한다(189–194). `call AREACAL(XC,YC,AREA2)` (196). `if( ABS(AREA2-AREA(L)) <= 1D-6 )then` (198)은 INSIDE=.TRUE.(199), `else` (200)는 .FALSE.(201). 조건·함수 종료·구분 주석(202–205). |
| 206–235 | INSIDECELL_GL 선언과 XC/YC(6) 작업 배열(206–216). 검사점과 전역 꼭짓점을 넣고 끝점을 닫는다(218–223). `call AREACAL(XC,YC,AREA2)` (225), `if( ABS(AREA2-AREA_Global(L)) <= 1D-6 )then` (227)은 .TRUE.(228), `else` (229)는 .FALSE.(230). 조건·함수 종료·구분 주석·빈 줄(231–235). |
| 236–285 | AREA_CENTRD 선언·셀 중심과 면적 설명·지역 변수(236–245). `if( process_id == master_id )then` (248)은 corners.inp를 읽기 모드로 열고 `call SKIPCOM(UCOR, '*')` (251). 조건 밖에서 전역·지역 좌표와 면적 배열을 할당하고 0으로 초기화한다(256–265). `do Q = 1,LA_Global-1` (266) 안의 `if( process_id == master_id )then` (267)은 IIN/JIN·네 꼭짓점을 읽고 err=998을 지정한다(268). 독립 조건 `if(process_id == master_id )then` (272)은 전역 셀 번호와 네 꼭짓점 복사(273–276), `call AREACAL(xc,yc,area2)` (278), 면적 복사(280). 중심식은 `XCOR_Global(l_global, 5) = 0.25*SUM(XC)` (282), `YCOR_Global(l_global, 5) = 0.25*SUM(YC)` (283). 이 내부 조건 종료(284)·빈 줄(285). |
| 286–326 | 시작 시 236행 AREA_CENTRD·266행 Q 루프 안이며 master 조건 밖. Broadcast_Scalar로 IIN/JIN을 전파한다(287–288). `I = IG2IL(IIN)` (290), `J = JG2JL(JIN)` (291). 전역 XCOR·YCOR의 1–5번 원소를 각각 Broadcast_Scalar로 전파한다(293–303). `if( I >0 .and. I <= IC )then` (307) 안의 `if( J > 0 .and. J <= JC )then` (308)에서 전역·지역 셀 번호 조회, 지역 네 꼭짓점 복사(309–316), `call AREACAL(XC,YC,AREA2)` (317), 지역 면적 복사(318). `XCOR(l_local,5) = 0.25*SUM(XC)` (320), `YCOR(l_local,5) = 0.25*SUM(YC)` (321). 두 조건·Q 루프 종료와 빈 줄(322–326). |
| 327–343 | 시작 시 236행 AREA_CENTRD 안이며 Q 루프 밖. 로그·전체 좌표 Broadcast_Array 호출은 주석이다(327–334). `if( process_id == master_id )then` (336)은 레이블 100에서 UCOR를 닫는다(337). 조건 종료·return, 998 레이블의 `STOP 'CORNERS.INP READING ERROR!'`, 루틴 종료·빈 줄(338–343). |
| 344–382 | DIST2LINE의 점과 선분(line segment) 거리·교점 설명, 꼭짓점·면 번호 그림, 인수·지역 선언(344–361). `if( IP == 4 )then` (363)은 I1=4·I2=1(364–365), `else` (366)는 I1=IP(367), `I2 = IP+1` (368). `XDEL = XCOR(L,I2) - XCOR(L,I1)` (370), `YDEL = YCOR(L,I2) - YCOR(L,I1)` (371), `D = YDEL*X0 - XDEL*Y0 + XCOR(L,I2)*YCOR(L,I1) - YCOR(L,I2)*XCOR(L,I1)` (373), `H = SQRT(XDEL*XDEL + YDEL*YDEL)` (374). `if( H < 1E-6 )then` (375)은 D=0 후 return(376–377). 조건 밖에서 `D = D/H` (381). 부호는 선 왼쪽 음수·오른쪽 양수라는 주석이다(380). |
| 383–419 | 시작 시 344행 DIST2LINE 안. `if( IPOINT > 0 )then` (383)에서 이전 기울기 코드는 주석이다(384–390). `ANG = ATAN2(YDEL,XDEL)` (391), `ANG = ANG + 0.5*PI` (392), `X3 = X0 + COS(ANG)*D  !*DS` (395), `Y3 = Y0 + SIN(ANG)*D  !*DS` (396), `EPSILON = 1E-12*X3` (399). `if( (X3 + EPSILON) < min(XCOR(L,I1),XCOR(L,I2)) .or. (X3 - EPSILON) > max(XCOR(L,I1),XCOR(L,I2)) )then` (400)은 `D = 1E32` (402) 후 return(403). `elseif( (Y3 + EPSILON) < min(YCOR(L,I1),YCOR(L,I2)) .or. (Y3 - EPSILON) > max(YCOR(L,I1),YCOR(L,I2)) )then` (404)도 `D = 1E32` (406) 후 return(407). 두 검사 통과 뒤 `X3 = X0 + COS(ANG)*(D-OFFSET)  !*DS` (411), `Y3 = Y0 + SIN(ANG)*(D-OFFSET)  !*DS` (412). 조건·루틴 종료·return·빈 줄(414–419). |
| 420–466 | BLOCKED는 선과 셀 마스크(mask)의 교차를 검사한다는 안내·선언(420–438). intersect=.false.(440). `imin = max(icell - 1,1)` (443), `imax = min(icell + 1,IC)` (444), `jmin = max(jcell - 1,1)` (445), `jmax = min(jcell + 1,JC)` (446). J/I 루프(447–448)에서 LIJ 조회(449). `if( UMASK(L)  ==  1 )then` (450) 안의 `if( L > 0 )then` (451)은 `intersect = isintersect(X1, Y1, X2, Y2, XCOR(L,1), YCOR(L,1), XCOR(L,2), YCOR(L,2))` (452), `if( intersect) return` (453). 독립 `if( VMASK(L)  ==  1 )then` (456) 안의 `if( L > 0 )then` (457)은 `intersect = isintersect(X1, Y1, X2, Y2, XCOR(L,1), YCOR(L,1), XCOR(L,4), YCOR(L,4))` (458), `if( intersect) return` (459). 조건·루프·함수 종료·빈 줄(460–466). |
| 467–483 | ISINTERSECT 인수·논리 선언(467–471). `L134 = ISCCW(X1,Y1,X3,Y3,X4,Y4)` (473), `L234 = ISCCW(X2,Y2,X3,Y3,X4,Y4)` (474), `L123 = ISCCW(X1,Y1,X2,Y2,X3,Y3)` (475), `L124 = ISCCW(X1,Y1,X2,Y2,X4,Y4)` (476). `#ifdef GNU` (477)에서는 `XSECT = (L134 .NEQV. L234) .AND. (L123 .NEQV. L124)` (478), `#else` (479)에서는 `XSECT = (L134 /= L234) .AND. (L123 /= L124)` (480). 전처리·함수 종료·빈 줄(481–483). |
| 484–491 | ISCCW는 반시계 방향(counterclockwise) 여부를 반환한다(484–487). 원문은 `CCW = (Y3-Y1)*(X2-X1) > (Y2-Y1)*(X3-X1)` (488). 함수·모듈 종료·빈 줄(489–491). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24·27–30: XY2IJ는 VALID의 값이 아니라 인수 존재 여부만으로 ISVALID를 1 또는 0으로 설정한다.
- 151–159: AREACAL은 SIZE(XC)를 NPOL로 쓰고 XC(2)·YC(2)를 바로 읽는다. 꼭짓점 수나 XC/YC 크기의 일치 여부를 확인하는 조건은 이 루틴에 없다.
- 159·282–283·320–321: 면적은 첫 꼭짓점을 기준으로 한 삼각형 면적의 절댓값을 누적한다. 셀 중심의 원문 식은 네 꼭짓점의 산술평균이다.
- 272–284·293–303: AREA_Global 계산은 master 조건 안에 있다. 이 파일에서 개별 전파하는 원소는 XCOR_Global·YCOR_Global이며 AREA_Global 전파 호출은 없다.
- 358·375–377·383–414: DIST2LINE의 출력 X3/Y3는 H<1E-6 조기 반환 경로와 IPOINT<=0 경로에서 대입하지 않는다.
- 399–404: 거리 범위 검사의 EPSILON은 1E-12*X3이다. 같은 EPSILON을 x·y 두 범위 검사에 사용한다.
- 449–457: BLOCKED는 LIJ에서 얻은 L로 UMASK/VMASK를 먼저 조회한 다음 내부 조건에서 L>0을 검사한다.
- 473–480·488: ISINTERSECT는 네 방향 검사 결과의 차이를 조합한다. ISCCW 원문 비교는 엄격한 >이며, 이 두 함수에는 공선(collinear) 구간의 별도 범위 검사가 없다.
