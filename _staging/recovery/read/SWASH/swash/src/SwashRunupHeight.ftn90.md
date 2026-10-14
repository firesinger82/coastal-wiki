---
file: models/SWASH/raw/source_code/swash/src/SwashRunupHeight.ftn90
lines: 156
sha256: b61d537a42e0e83ccb9526b36a0aa1bac1379745e0e395b13b7140d707d789c9
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashRunupHeight.ftn90 — 판독 구간 기록

구간은 1행부터 156행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | 루틴과 oqproc·nvoqp·voqr·voq 인수 목록을 시작한다(1). 기관·저작권·GPL 3 이상·무보증 머리말(3–27). Tomohiro Suzuki의 2018년 4월 신규 루틴이다(30–36). 출력용 처오름 높이(wave runup height)를 자유수면(free surface)과 바닥 높이에 처오름 임계값을 더한 선의 교차로 계산한다는 주석이다(38–44). 적용은 1차원이고 파 전파는 동향으로 제한한다는 주석이다(46). 교차 대상의 원문 표기는 `!   Based on the intersection between free surface and bottom level + threshold for runup` (44)이다. [10-15 전수 검증 보완] |
| 50–85 | 시작 시 1행 SwashRunupHeight 루틴 안. 출력·시간·격자·병렬·흐름 모듈을 사용한다(50–57). oqproc·voqr의 크기는 nmovar, voq의 크기는 nvoqp이며 voq는 intent(out)이다(63–66). ient·jerr는 save 정수로 0 초기화한다(70–71). 검색 인덱스 m·mr와 격자 포인터, 처오름 높이 rh를 선언한다(72–78). 구조·소스 구분 주석까지 포함한다(80–85). 초기값 선언은 `integer, save :: ient = 0 ! number of entries in this subroutine` (70)과 `integer, save :: jerr = 0 ! actual number of printing error statement` (71)이다. [10-15 전수 검증 보완] |
| 86–118 | 시작 시 1행 루틴 안. ltrace이면 strace를 호출하고 rh를 출력 예외값 ovexcv(115)로 설정한다(86–88). oned일 때만 처오름을 계산한다(90). 서쪽 경계 종류가 2·3·7 모두 아니고 LMXF일 때 jerr<1이면 msgerr로 경고하며 jerr를 증가시킨다(94–101). ml에서 mfu까지 역순 검색한다(103). jerr>0이면 mr=MXCGL+1로 놓고 검색을 끝낸다(105–108). 그렇지 않으면 hs(nm)>delrp인 첫 점을 mr에 저장하고 검색을 끝낸다(110–115). 원문: `if (ltrace) call strace (ient,'SwashRunupHeight')` (86). `rh = ovexcv(115)` (88). `if ( oned ) then` (90). `if ( ibl(1) /= 2 .and. ibl(1) /= 3 .and. ibl(1) /= 7 .and. LMXF ) then` (94). `if ( jerr < 1 ) then` (96). `call msgerr (1, 'wave runup height will not be computed as no waves are imposed on west side')` (97). `jerr = jerr + 1` (98). `mloop: do m = ml, mfu, -1` (103). `if ( jerr > 0 ) then` (105). `mr = MXCGL+1` (106). `nm = kgrpnt(m,1)` (110). `if ( hs(nm) > delrp ) then` (112). `mr = m` (113). |
| 119–145 | 시작 시 1행 루틴·90행 `if ( oned ) then` 참 분기 안. mr를 전역 인덱스로 바꾸고 SWREDUCE의 SWINT·SWMAX로 최댓값을 구한 후 지역 인덱스로 되돌린다(121–125). mf<mr<mlu일 때 mr·mr+1 사이에서 수심 임계값 delrp를 기준으로 수위를 선형보간(linear interpolation)한다(129–134). else는 rh를 출력 예외값으로 설정한다(136–138). SWREAL·SWMAX로 rh의 최댓값을 구한다(142). 90행 IF는 144행의 `endif`에서 닫힌다. 원문: `m = mr + MXF   ! from local to global` (121). `call SWREDUCE ( m, 1, SWINT, SWMAX )` (123). `mr = m - MXF   ! from global to local` (125). `if ( mr > mf .and. mr < mlu ) then` (129). `nmr  = kgrpnt(mr  ,1)` (131). `nmru = kgrpnt(mr+1,1)` (132). `rh = s1(nmr) + ( delrp - hs(nmr) ) * ( s1(nmru) - s1(nmr) ) / ( hs(nmru) - hs(nmr) )` (134). `else` (136). `rh = ovexcv(115)` (138). `call SWREDUCE ( rh, 1, SWREAL, SWMAX )` (142). [10-15 전수 검증 보완] |
| 146–156 | 시작 시 1행 루틴 안이며 oned 분기 밖. oqproc(41)이면 timco에서 outpar(1)을 뺀 경과 시간을 voq에 저장한다(150). voqr(115) 위치에는 rh를 저장한다(154). 루틴을 종료한다(156). 원문: `if ( oqproc(41) ) voq(voqr(41)) = real(timco) - outpar(1)` (150). `voq(voqr(115)) = rh` (154). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 73·103–117·121: mr 선언에는 초기값이 없다. 검색 루프의 mr 대입은 jerr>0 또는 hs(nm)>delrp 분기에만 있고, 이후 121행은 mr를 참조한다.
- 129–134: 처오름 보간의 분모는 hs(nmru)−hs(nmr)이다. 이 블록에는 두 수심의 차가 0인지 검사하는 조건이 없다.
- 71·96–108: jerr는 save이며 선언에서 0으로 초기화한다. 경고 분기에서 증가하고 jerr>0이면 검색을 종료한다. 이 루틴에는 jerr를 다시 0으로 대입하는 문장이 없다.
- 65·150·154: voq는 intent(out)이다. 시간 출력은 oqproc(41) 조건에 따르지만 처오름 저장에는 oqproc(115) 조건이 없다. 다른 voq 성분을 채우는 문장은 이 루틴에 없다.
