---
file: models/SWASH/raw/source_code/swash/src/SwashFlowDP.ftn90
lines: 308
sha256: b96d5352cb286334b9ae943dd8a612828e6a17932517443f9a6dc65009bb0e57
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashFlowDP.ftn90 — 판독 구간 기록

구간은 1행부터 308행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | `SwashFlowDP` 입구(1). 기관·저작권·GPL 3 이상·무보증 주석(2–29). Marcel Zijlema와 2010년 신설 이력(30–37). 수위점(water level point)과 속도점(velocity point)의 바닥 값을 결정한다는 목적 주석(38–41). ocpcomm4·SwashCommdata3·m_genarr·SwashFlowdata를 사용한다(44–47). |
| 49–86 | 시작 시 1행 SwashFlowDP 루틴 안. implicit none(49). 진입 횟수 `integer, save :: ient = 0 ! number of entries in this subroutine` (53). 격자 반복자·인접점과 경계점 포인터·중단 여부 STPNOW를 선언한다(54–75). 구조·소스 머리말 주석(77–82). `if (ltrace) call strace (ient,'SwashFlowDP')` (83). 사용자 입력으로 셀(cell) 바닥 값을 결정한다는 주석(85). |
| 87–128 | 시작 시 1행 루틴 안. `if ( oned ) then` (87)·`do m = mfu, ml` (91)에서 현재점과 m-1점의 kgrpnt 포인터를 구한다(93–96). 바닥 선택은 `if ( dpsopt == 1 ) then` (98)의 `dps(nm) = min( depf(nmd), depf(nm) )` (99), `else if (dpsopt == 2 ) then` (100)의 `dps(nm) = 0.5 * ( depf(nm) + depf(nmd) )` (101), `else if ( dpsopt == 3 ) then` (102)의 `dps(nm) = max( depf(nmd), depf(nm) )` (103), `else if ( dpsopt == 4 ) then` (104)의 `dps(nm) = depf(nm)` (105)이다. `if ( s1(nm) < epsdry - dps(nm) ) then` (108)이면 `s1(nm) = 0.99*epsdry - dps(nm)` (110). 루프 종료(114) 뒤 가상 수위점(virtual water level point) mf·mlu의 바닥과 수위를 mfu·ml 값으로 복사한다(116–127). 이웃 인덱스는 `md = m - 1` (93)이다. 경계 복사식은 `dps(nmf ) = dps(nmfu)` (123), `dps(nmlu) = dps(nml )` (124), `s1(nmf ) = s1(nmfu)` (126), `s1(nmlu) = s1(nml )` (127)이다. 98–106행 분기 사슬에는 `else`가 없다. 87행 조건은 214행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 129–167 | 시작 시 1행 루틴과 87행 `if ( oned ) then` (214행 `endif`) 안. `else` (129)는 2차원 경로이다. `do n = nfu, nl` (133)·`do m = mfu, ml` (135)에서 현재점과 좌측·하측·좌하측 포인터를 구한다(137–143). 영구 건조 인접점의 값 반영 조건은 `if ( nmd  == 1 ) nmd  = nm` (147), `if ( ndm  == 1 ) ndm  = nm` (148), `if ( ndmd == 1 ) ndmd = ndm` (149). 바닥 선택은 `if ( dpsopt == 1 ) then` (151)의 `dps(nm) = min( depf(nmd), depf(nm), depf(ndmd), depf(ndm) )` (152), `else if ( dpsopt == 2 ) then` (153)의 `dps(nm) = 0.25 * ( depf(nm) + depf(nmd) + depf(ndm) + depf(ndmd) )` (154), `else if ( dpsopt == 3 ) then` (155)의 `dps(nm) = max( depf(nmd), depf(nm), depf(ndmd), depf(ndm) )` (156), `else if ( dpsopt == 4 ) then` (157)의 `dps(nm) = depf(nm)` (158)이다. `if ( s1(nm) < epsdry - dps(nm) ) then` (161)이면 `s1(nm) = 0.99*epsdry - dps(nm)` (163). m 루프 종료(167). 이웃 인덱스는 `md = m - 1` (137)과 `nd = n - 1` (138)이다. 151–159행 분기 사슬에는 `else`가 없다. [10-15 전수 검증 보완] |
| 168–214 | 시작 시 1행 루틴과 87행 `if ( oned ) then`의 129행 `else` (214행 `endif`) 및 133행 `do n = nfu, nl` (186행 `enddo`) 안. 좌우 경계 포인터를 구한 뒤 `if ( .not.lreptx ) then` (176)에서 가상점 바닥·수위를 내부 인접점 값으로 복사한다(169–184). n 루프 종료(186) 뒤 `do m = mf, mlu` (188)에서 상하 경계와 모서리 포인터를 구한다(190–193). `if ( .not.lrepty ) then` (197)에서 상하 가상점 바닥·수위를 내부점 값으로 복사한다(199–203). 루프 종료(207) 뒤 영구 건조점 dps(1)·s1(1)을 0으로 설정한다(211–212). oned 조건 종료(214). 좌우 복사식은 `dps(nmf ) = dps(nmfu)` (178), `dps(nmlu) = dps(nml )` (179), `s1(nmf ) = s1(nmfu)` (181), `s1(nmlu) = s1(nml )` (182)이다. 상하 복사식은 `dps(nfm ) = dps(nfum)` (199), `dps(nlum) = dps(nlm )` (200), `s1(nfm ) = s1(nfum)` (202), `s1(nlum) = s1(nlm )` (203)이다. 영구 건조점 초기식은 `dps(1) = 0.` (211)과 `s1 (1) = 0.` (212)이다. [10-15 전수 검증 보완] |
| 215–228 | 시작 시 1행 루틴 안. 인접 부영역(subdomain) 교환은 `call SWEXCHG ( dps, kgrpnt, 1, 1 )` (218), `call SWEXCHG (  s1, kgrpnt, 1, 1 )` (219). `if (STPNOW()) return` (220). 반복 격자(repeating grid) 경계 동기화는 `call periodic ( dps, kgrpnt, 1, 1 )` (224), `call periodic (  s1, kgrpnt, 1, 1 )` (225). 타일 방식(tiled approach)으로 속도점 바닥을 구한다는 주석(227). |
| 229–248 | 시작 시 1행 루틴 안. `if ( oned ) then` (229)·`do m = mf, ml` (233)에서 현재점과 m+1점 포인터를 구한다(235–238). 이웃 인덱스는 `mu = m + 1` (235)이다. 229행 조건은 306행 `endif`에서 닫힌다. `dpu(nm) = min( dps(nm), dps(nmu) )` (240). 루프 종료 뒤 `call SWEXCHG ( dpu, kgrpnt, 1, 1 )` (246), `if (STPNOW()) return` (247). [10-15 전수 검증 보완] |
| 249–269 | 시작 시 1행 루틴과 229행 `if ( oned ) then` (306행 `endif`) 안. `else` (249)는 2차원 속도점 경로이다. `do n = nf, nlu` (253)·`do m = mf, ml` (254)에서 u점과 m+1점 포인터를 구한다(256–259). `if ( nmu == 1 ) nmu = nm` (263)로 영구 건조 인접점을 현재점으로 대체한다. `dpu(nm) = min( dps(nm), dps(nmu) )` (265). 두 루프 종료(267–268). 이웃 인덱스는 `mu = m + 1` (256)이다. [10-15 전수 검증 보완] |
| 270–308 | 시작 시 1행 루틴과 229행 `if ( oned ) then`의 249행 `else` (306행 `endif`) 안. `do m = mf, mlu` (272)·`do n = nf, nl` (273)에서 v점과 n+1점 포인터를 구한다(275–278). `if ( num == 1 ) num = nm` (282), `dpv(nm) = min( dps(nm), dps(num) )` (284). 이웃 인덱스는 `nu = n + 1` (275)이다. 루프 종료 뒤 `dpu(1) = 0.` (291)과 `dpv(1) = 0.` (292)를 설정한다. `call SWEXCHG ( dpu, kgrpnt, 1, 1 )` (296), `if (STPNOW()) return` (297), `call SWEXCHG ( dpv, kgrpnt, 1, 1 )` (298), `if (STPNOW()) return` (299). `call periodic ( dpu, kgrpnt, 1, 1 )` (303), `call periodic ( dpv, kgrpnt, 1, 1 )` (304). 조건·루틴 종료와 주석(305–308). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 98–106·151–159: dpsopt 분기는 1·2·3·4만 처리한다. 두 분기 모두 그 밖의 값을 처리하는 else가 없다.
- 229–247·249–304: 1차원 속도점 경로는 dpu 교환만 호출한다. 2차원 속도점 경로는 dpu·dpv 교환과 periodic 호출을 포함한다.
