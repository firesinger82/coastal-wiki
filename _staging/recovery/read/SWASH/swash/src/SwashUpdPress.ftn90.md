---
file: models/SWASH/raw/source_code/swash/src/SwashUpdPress.ftn90
lines: 262
sha256: 72de9d0f132e9c416db142c565df4f99eeb9f24d3c8b80c66d9fe53863a71c17
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUpdPress.ftn90 — 판독 구간 기록

구간은 1행부터 262행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–81 | `SwashUpdPress` 시작(1). 기관·저작권·GPL 3 이상·무보증 머리말(2–29), 작성자·2013년 신규 작성 이력(30–36). 공간 입력장으로 대기압(atmospheric pressure)을 초기화·갱신하고 필요하면 개방 경계(open boundary) 수위를 보정한다는 목적 주석(38–41). ocpcomm4·SwashCommdata2/3·m_genarr·m_parall·SwashFlowdata 사용(45–50), implicit none(52). `integer, save :: ient = 0` (56)으로 초기화한다. 격자·경계 포인터와 정지 판정 STPNOW를 선언한다(57–74). 구조·소스 시작 주석도 포함한다(76–81). [10-15 전수 검증 보완] |
| 82–118 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashUpdPress')` (82). `if ( ifldyn(13) == 1 ) then` (84)의 입력장 갱신 안에서 `if ( oned ) then` (88). `do m = mfu, ml` (92), `md = m - 1` (94), `nm  = kgrpnt(m ,1)` (96), `nmd = kgrpnt(md,1)` (97), `patm(nm) = 0.5 * ( presf(nm,2) + presf(nmd,2) )` (99)로 수위점(wl-point) 압력을 평균한다. 101행 `enddo` 뒤 `call SWEXCHG ( patm, kgrpnt, 1, 1 )` (105), `if (STPNOW()) return` (106). `nmf  = kgrpnt(mf ,1)` (110), `nmfu = kgrpnt(mfu,1)` (111), `nml  = kgrpnt(ml ,1)` (112), `nmlu = kgrpnt(mlu,1)` (113)를 대입한다. `if ( LMXF ) patm(nmf ) = patm(nmfu)` (115), `if ( LMXL ) patm(nmlu) = patm(nml )` (116). `else` (118)는 2차원 경로를 연다. [10-15 전수 검증 보완] |
| 119–156 | 시작 시 1행 루틴·84행 `if ( ifldyn(13) == 1 ) then` 참 분기·88행 `if ( oned ) then`의 118행 `else` 안. `do n = nfu, nl` (122), `do m = mfu, ml` (124), `md = m - 1` (126), `nd = n - 1` (127). `nm   = kgrpnt(m ,n )` (129), `nmd  = kgrpnt(md,n )` (130), `ndm  = kgrpnt(m ,nd)` (131), `ndmd = kgrpnt(md,nd)` (132). 영구 건조 이웃의 대칭 복사(mirroring): `if ( nmd  == 1 ) nmd  = nm` (136), `if ( ndm  == 1 ) ndm  = nm` (137), `if ( ndmd == 1 ) ndmd = ndm` (138). `patm(nm) = 0.25 * ( presf(nm,2) + presf(nmd,2) + presf(ndm,2) + presf(ndmd,2) )` (140). m/n 루프 종료(142·144) 후 `patm(1) = 0.` 초기화(148), `call SWEXCHG ( patm, kgrpnt, 1, 1 )` (152), `if (STPNOW()) return` (153). [10-15 전수 검증 보완] |
| 157–185 | 시작 시 1행 루틴·84행 `if ( ifldyn(13) == 1 ) then` 참 분기(217행 `endif`)·88행 `if ( oned ) then`의 118행 `else` 안(215행 `endif`). `if ( .not.lreptx ) then` (157). 비주기 x경계는 `do n = nfu, nl` (159)에서 `nmf  = kgrpnt(mf ,n)` (161), `nmfu = kgrpnt(mfu,n)` (162), `nml  = kgrpnt(ml ,n)` (163), `nmlu = kgrpnt(mlu,n)` (164)를 대입한다., `if ( LMXF ) then` (166)에서 `patm(nmf) = patm(nmfu)` (168), `if ( LMXL ) then` (172)에서 `patm(nmlu) = patm(nml)` (174)로 내부 압력을 복사한다. `else` (180)의 주기 경계(periodic boundary)는 `call periodic ( patm, kgrpnt, 1, 1 )` (182). 조건 종료(184). 166·172행 조건은 각각 170·176행 `endif`에서 닫힌다. 159행 루프는 178행 `enddo`에서 닫힌다. [10-15 전수 검증 보완] |
| 186–218 | 시작 시 1행 루틴·84행 `if ( ifldyn(13) == 1 ) then` 참 분기(217행 `endif`)·88행 `if ( oned ) then`의 118행 `else` 안(215행 `endif`). `if ( .not.lrepty ) then` (186). `do m = mfu, ml` (188)에서 `nfm  = kgrpnt(m,nf )` (190), `nfum = kgrpnt(m,nfu)` (191), `nlm  = kgrpnt(m,nl )` (192), `nlum = kgrpnt(m,nlu)` (193), `if ( LMYF ) then` (195)에서 `patm(nfm) = patm(nfum)` (197), `if ( LMYL ) then` (201)에서 `patm(nlum) = patm(nlm)` (203). `else` (209)는 `call periodic ( patm, kgrpnt, 1, 1 )` (211). y주기 조건·oned 조건·입력장 조건 종료(213·215·217). 195·201행 조건은 각각 199·205행 `endif`에서 닫힌다. 188행 루프는 207행 `enddo`에서 닫힌다. 157행 `if ( .not.lreptx ) then` 블록은 184행에서 이미 닫혔다. [10-15 전수 검증 보완] |
| 219–243 | 시작 시 1행 루틴 안이며 217행에서 닫힌 84행 `if ( ifldyn(13) == 1 ) then` 블록 밖. 국소 대기압에 의한 경계 수위 보정: `if ( prmean > 0. ) then` (221), `if ( oned ) then` (223). 1차원은 `if ( ibl(1) == 2 ) s1(nmf ) = s1(nmf ) + ( prmean - patm(nmf ) ) / (rhow*grav)` (225), `if ( ibr(1) == 2 ) s1(nmlu) = s1(nmlu) + ( prmean - patm(nmlu) ) / (rhow*grav)` (226). `else` (228)의 2차원은 `if ( .not.lreptx ) then` (230) 안의 `do n = nfu, nl` (232)에서 `nmf  = kgrpnt(mf ,n)` (234), `nmlu = kgrpnt(mlu,n)` (235)를 대입한다. `if ( ibl(n) == 2 ) s1(nmf ) = s1(nmf ) + ( prmean - patm(nmf ) ) / (rhow*grav)` (237), `if ( ibr(n) == 2 ) s1(nmlu) = s1(nmlu) + ( prmean - patm(nmlu) ) / (rhow*grav)` (238). 232행 루프는 240행 `enddo`에서 닫힌다. 230행 조건은 242행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 244–262 | 시작 시 1행 루틴·221행 `if ( prmean > 0. ) then` 참 분기·223행 `if ( oned ) then`의 228행 `else` 안. `if ( .not.lrepty ) then` (244), `do m = mfu, ml` (246)에서 `nfm  = kgrpnt(m,nf )` (248), `nlum = kgrpnt(m,nlu)` (249). `if ( ibb(m) == 2 ) s1(nfm ) = s1(nfm ) + ( prmean - patm(nfm ) ) / (rhow*grav)` (251), `if ( ibt(m) == 2 ) s1(nlum) = s1(nlum) + ( prmean - patm(nlum) ) / (rhow*grav)` (252). 246행 루프는 254행 `enddo`에서 닫힌다. 244·223·221행 조건은 각각 256·258·260행 `endif`에서 닫힌다. 루틴은 262행에서 끝난다. 이 파일에는 switch.pl 대상 표지나 !DIFF·!MUD·!TEST·!VEGE 표지 행이 없다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 84·110–113·221–226: 1차원 nmf/nmlu의 대입은 ifldyn(13)==1 분기 안에 있다. 1차원 수위 보정은 그 분기 밖에서 nmf/nmlu를 참조한다. 지역 선언에는 이 포인터들의 초기값이 없다(69–72).
- 94–99·134–148: 1차원 압력 평균에는 영구 건조 이웃 포인터 1의 대칭 복사나 patm(1)=0 대입이 없다. 두 처리는 2차원 경로에 있다.
- 157–213: x주기 else와 y주기 else는 동일 인수의 periodic 호출을 각각 갖는다. 이 파일에는 두 호출을 하나로 합치는 조건이 없다.
