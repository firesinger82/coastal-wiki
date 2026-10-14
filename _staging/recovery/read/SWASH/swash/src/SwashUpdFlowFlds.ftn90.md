---
file: models/SWASH/raw/source_code/swash/src/SwashUpdFlowFlds.ftn90
lines: 307
sha256: 2aa56303a45aa0114a95d1bd53d83af27f5890dc4fac1530636e77330bcdf2da
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashUpdFlowFlds.ftn90 — 판독 구간 기록

구간은 1행부터 307행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–41 | `SwashUpdFlowFlds` 시작(1). 기관·개발팀·SWASH·2010–2026 저작권·GPL 3 이상·무보증 머리말(3–27). 저자·2010년 3월 신규 이력(30–36). 공간 가변 입력장(space varying input field)으로 흐름 변수를 초기화·갱신하는 목적(40). |
| 42–74 | 시작 시 1행 `SwashUpdFlowFlds` 안. 통신·일반 배열·흐름 모듈 사용(44–48). `integer, save :: ient = 0` (54)으로 초기화한다. 수직/수평 반복 인덱스·이웃 격자 포인터·logical STPNOW를 선언한다(54–65). 구조·소스 구분 주석(67–72). `if (ltrace) call strace (ient,'SwashUpdFlowFlds')` (73). [10-15 전수 검증 보완] |
| 75–95 | 시작 시 1행 루틴 안. `if ( initsf .or. ifldyn(7) == 1 ) then` (75)은 수위점(water level point) 수위를 갱신한다. `if ( oned ) then` (79)의 `do m = mfu, ml` (83)에서 `md = m - 1` (85), `nm  = kgrpnt(m ,1)` (87), `nmd = kgrpnt(md,1)` (88), `s1(nm) = 0.5 * ( wlevf(nm,2) + wlevf(nmd,2) )` (90). 루프 종료(92), oned의 `else` 시작(94). [10-15 전수 검증 보완]  |
| 96–140 | 시작 시 1행 루틴·75행 `if ( initsf .or. ifldyn(7) == 1 ) then` 참 분기·79행 `if ( oned ) then`의 94행 `else` 안. `do n = nfu, nl` (98)·`do m = mfu, ml` (100)에서 `md = m - 1` (102), `nd = n - 1` (103), `nm   = kgrpnt(m ,n )` (105), `nmd  = kgrpnt(md,n )` (106), `ndm  = kgrpnt(m ,nd)` (107), `ndmd = kgrpnt(md,nd)` (108). 영구 건조 이웃(permanently dry neighbour)의 값 반사(mirroring) 주석(110). `if ( nmd  == 1 ) nmd  = nm` (112), `if ( ndm  == 1 ) ndm  = nm` (113), `if ( ndmd == 1 ) ndmd = ndm` (114). `s1(nm) = 0.25 * ( wlevf(nm,2) + wlevf(nmd,2) + wlevf(ndm,2) + wlevf(ndmd,2) )` (116). m/n 루프 종료(118·120). `s1(1) = 0.` (124), oned 종료(126). 수위 갱신 참 분기 안에서 `call SWEXCHG ( s1, kgrpnt, 1, 1 )` (130), `if (STPNOW()) return` (131), `call periodic ( s1, kgrpnt, 1, 1 )` (135), `initsf = .false.` (137). 수위 조건 종료(139). [10-15 전수 검증 보완] |
| 141–160 | 시작 시 1행 루틴 안. `if ( inituf .or. ifldyn(2) == 1 ) then` (141)은 u속도 갱신 경로다. `if ( oned ) then` (145)의 `do m = mf, ml` (149)에서 `nm = kgrpnt(m,1)` (151), `u1(nm,1) = uxf(nm,2)` (153). 149행 루프는 155행에서 닫힌다. oned의 `else` (157)는 2차원 경로다. [10-15 전수 검증 보완] |
| 161–205 | 시작 시 1행 루틴·141행 `if ( inituf .or. ifldyn(2) == 1 ) then` 참 분기·145행 `if ( oned ) then`의 157행 `else` 안. `if ( lstag(2) ) then` (161)은 `uxf`를 `u1`에 직접 복사하는 경로다(169). `do n = nfu, nl` (163)·`do m = mf, ml` (165)에서 `nm = kgrpnt(m,n)` (167), `u1(nm,1) = uxf(nm,2)` (169)를 대입한다. m/n 루프는 171·173행에서 닫힌다. `else` (175)의 `do n = nfu, nl` (177)·`do m = mf, ml` (179)는 `nd = n - 1` (181), `nm  = kgrpnt(m,n )` (183), `ndm = kgrpnt(m,nd)` (184), `if ( ndm == 1 ) ndm = nm` (188). 속도 투영(projection)은 `u1(nm,1) = 0.5 * ( uxf(nm,2) + uxf(ndm,2) ) * ( ycgrid(m,n) - ycgrid(m,n-1) ) - 0.5 * ( uyf(nm,2) + uyf(ndm,2) ) * ( xcgrid(m,n) - xcgrid(m,n-1) )` (190), `u1(nm,1) = u1(nm,1) / guu(nm)` (191), `if ( .not.cvleft ) u1(nm,1) = -u1(nm,1)` (192). 두 루프·lstag 조건 종료(194–198). `u1(1,1) = 0.` (202), oned 조건 종료(204). [10-15 전수 검증 보완] [10-15 전수 검증 정정] |
| 206–232 | 시작 시 1행 루틴·141행 `if ( inituf .or. ifldyn(2) == 1 ) then` 참 분기 안. `call SWEXCHG ( u1(1,1), kgrpnt, 1, 1 )` (208), `if (STPNOW()) return` (209), 반복 격자(repeating grid) 경계 동기화 `call periodic ( u1(1,1), kgrpnt, 1, 1 )` (213). `if ( kmax > 1 ) then` (215)은 `udep(:) = u1(:,1)` 복사(217), 수직 균일 속도 가정 주석(219). `do k = 2, kmax` (221)에서 `u1(:,k) = udep(:)`를 복사한다(223). k 루프는 225행에서 닫힌다. 다층 조건 종료(227), `inituf = .false.` (229), u 갱신 조건 종료(231). [10-15 전수 검증 보완] |
| 233–250 | 시작 시 1행 루틴 안. `if ( .not.oned .and. (initvf .or. ifldyn(3) == 1) ) then` (233)은 2차원 v속도 갱신 경로다. `if ( lstag(3) ) then` (237)의 `do n = nf, nl` (239), `do m = mfu, ml` (241)에서 `nm = kgrpnt(m,n)` (243)을 대입한다. `v1(nm,1) = uyf(nm,2)` (245)를 복사한다. 두 루프 종료(247–249). [10-15 전수 검증 보완] |
| 251–275 | 시작 시 1행 루틴·233행 `if ( .not.oned .and. (initvf .or. ifldyn(3) == 1) ) then` 참 분기·237행 `if ( lstag(3) ) then` 블록 안. `else` (251)의 `do n = nf, nl` (253)·`do m = mfu, ml` (255)에서 `md = m - 1` (257), `nm  = kgrpnt(m ,n)` (259), `nmd = kgrpnt(md,n)` (260), `if ( nmd == 1 ) nmd = nm` (264). `v1(nm,1) = 0.5 * ( uyf(nm,2) + uyf(nmd,2) ) * ( xcgrid(m,n) - xcgrid(m-1,n) ) - 0.5 * ( uxf(nm,2) + uxf(nmd,2) ) * ( ycgrid(m,n) - ycgrid(m-1,n) )` (266), `v1(nm,1) = v1(nm,1) / gvv(nm)` (267), `if ( .not.cvleft ) v1(nm,1) = -v1(nm,1)` (268). 두 루프·lstag 조건 종료(270–274). [10-15 전수 검증 보완] |
| 276–307 | 시작 시 1행 루틴·233행 `if ( .not.oned .and. (initvf .or. ifldyn(3) == 1) ) then` 참 분기 안. 237행 `if ( lstag(3) ) then` 블록은 274행에서 이미 닫혔다. `v1(1,1) = 0.` (278), `call SWEXCHG ( v1(1,1), kgrpnt, 1, 1 )` (282), `if (STPNOW()) return` (283), `call periodic ( v1(1,1), kgrpnt, 1, 1 )` (287). `if ( kmax > 1 ) then` (289)은 `vdep(:) = v1(:,1)` 복사(291), 수직 균일 속도 가정 주석(293). `do k = 2, kmax` (295)에서 `v1(:,k) = vdep(:)` 복사(297). k 루프는 299행에서 닫힌다. 다층 조건 종료(301), `initvf = .false.` (303), v 갱신 조건·루틴 종료(305–307). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 161–169·190–192·237–245·266–268: lstag(2)/lstag(3) 참 경로는 입력 uxf/uyf를 속도 배열에 직접 복사한다. 거짓 경로만 격자 좌표 차·guu/gvv·cvleft로 속도를 변환한다.
- 191·267: 속도 투영은 guu(nm) 또는 gvv(nm)로 나눈다. 이 루틴에는 두 분모의 0 여부를 검사하는 조건이 없다.
- 215–227·289–301: udep/vdep 대입은 kmax>1 조건 안에만 있다. 이 루틴은 같은 조건에서 첫 층 속도를 나머지 모든 층에 복사한다.
