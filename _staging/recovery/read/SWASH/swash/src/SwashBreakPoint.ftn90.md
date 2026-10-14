---
file: models/SWASH/raw/source_code/swash/src/SwashBreakPoint.ftn90
lines: 244
sha256: f4d74c2a12bb654a9d511ae12114a820d4ef2015c9727d4ad5f5fb57c283f62d
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashBreakPoint.ftn90 — 판독 구간 기록

구간은 1행부터 244행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | `SwashBreakPoint` 입구(1).기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27). 작성자와 2011년 신설·2012년 에너지 소산·2019년 내부 조파(internal wave generation) 확장 이력(30–39). 쇄파(wave breaking) 전면을 찾고 수면 상승속도가 파속의 일부를 넘으면 정수압(hydrostatic pressure)을 적용한다는 목적·방법 주석(41–53). 주석의 소산·파형 보존 설명은 이 파일의 실행 검증 결과가 아니다. 49행 주석은 쇄파 전면에서 정수압 가정을 유지한다고 설명한다. 51–52행 주석은 적절한 운동량 보존과의 결합을 에너지 소산 설명의 조건으로 둔다. 53행 주석은 비대칭성과 왜도 보존을 언급한다. [10-15 전수 검증 보완] |
| 55–101 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·SwashTimecomm·m_genarr·SwashFlowdata 사용(57–61). `integer, save :: ient = 0 ! number of entries in this subroutine` (67), 격자 인덱스·임계계수 alpha/beta·수면 상승속도 dsdt·천수 파속(shallow water celerity) rootgh·STPNOW 선언(68–85). `if (ltrace) call strace (ient,'SwashBreakPoint')` (93). `alpha = psurf(1)` (95), `beta  = psurf(2)` (96). 이전 쇄파 마스크(mask)를 `iwrk(:,1) = brks(:)` (100)에 복사한다. |
| 102–148 | 시작 시 1행 루틴 안. `if ( oned ) then` (102), m=mfu..ml(104). `md = m - 1` (106), `mu = m + 1` (107), `nm  = kgrpnt(m ,1)` (109). `nmd = kgrpnt(md,1)` (110). `nmu = kgrpnt(mu,1)` (111). `if ( wets(nm) == 1 .and. presp(nm) == 0 ) then` (113)은 `rootgh = sqrt( grav * hs(nm) )` (115), `dsdt = ( s1(nm) - s0(nm) ) / dt` (117). `if ( dsdt > alpha * rootgh ) then` (119)은 `brks(nm) = 1` (121)·`q(nm,:) = 0.` (123). `else if ( dsdt > beta * rootgh .and. (iwrk(nmd,1) == 1 .or. iwrk(nmu,1) == 1) ) then` (125)도 `brks(nm) = 1` (127)·`q(nm,:) = 0.` (129). `else if ( dsdt > 0. .and. brks(nm) == 1 ) then` (131)은 `q(nm,:) = 0.` (133). `else` (135)는 `brks(nm) = 0` (137). 젖음/압력 조건의 `else` (141)는 `brks(nm) = 0` (143). m 루프 종료(147). 119행 사슬은 139행에서 닫힌다. 113행 조건은 145행에서 닫힌다. [10-15 전수 검증 보완] |
| 149–173 | 시작 시 1행 루틴·102행 `if ( oned ) then` 안에서 `else` (149)로 2차원 경로. n=nfu..nl·m=mfu..ml(151–152)에서 `md = m - 1` (154), `mu = m + 1` (155), `nd = n - 1` (156), `nu = n + 1` (157). `nm  = kgrpnt(m ,n )` (159). `nmd = kgrpnt(md,n )` (160). `nmu = kgrpnt(mu,n )` (161). `ndm = kgrpnt(m ,nd)` (162). `num = kgrpnt(m ,nu)` (163). 영구 건조 이웃의 대칭 처리: `if ( nmd == 1 ) nmd = nm` (167), `if ( nmu == 1 ) nmu = nm` (168), `if ( ndm == 1 ) ndm = nm` (169), `if ( num == 1 ) num = nm` (170). `if ( wets(nm) == 1 .and. presp(nm) == 0 ) then` (172)의 계산은 다음 구간에 이어진다. [10-15 전수 검증 보완] |
| 174–214 | 시작 시 1행 루틴·102행 `if ( oned ) then`의 `else` (149)·151행 `do n = nfu, nl`·152행 `do m = mfu, ml`·172행 `if ( wets(nm) == 1 .and. presp(nm) == 0 ) then` 안. `rootgh = sqrt( grav * hs(nm) )` (174), `dsdt = ( s1(nm) - s0(nm) ) / dt` (176). `if ( dsdt > alpha * rootgh ) then` (178)은 `brks(nm) = 1` (180)·`q(nm,:) = 0.` (182). `else if ( dsdt > beta * rootgh .and. (iwrk(nmd,1) == 1 .or. iwrk(nmu,1) == 1 .or. iwrk(ndm,1) == 1 .or. iwrk(num,1) == 1) ) then` (184)도 `brks(nm) = 1` (186)·`q(nm,:) = 0.` (188). `else if ( dsdt > 0. .and. brks(nm) == 1 ) then` (190)은 `q(nm,:) = 0.` (192). `else` (194)는 `brks(nm) = 0` (196). 젖음/압력 조건의 `else` (200)는 `brks(nm) = 0` (202). 루프 종료(206–207), 2차원 경로 안에서 `brks(1) = 0` (211), 차원 분기 종료(213). 178행 사슬은 198행에서 닫힌다. 172행 조건은 204행에서 닫힌다. [10-15 전수 검증 보완] |
| 215–244 | 시작 시 1행 루틴 안. `if ( iwvgen /= 0 ) then` (217)은 nm=2..mcgrd(219)에서 `if ( srcm(nm) /= 0. ) brks(nm) = 0` (221)으로 조파 원천 영역(source region)의 쇄파 표시를 지운다. `call SWEXCHGI ( brks, kgrpnt, 1, 1 )` (229), `if (STPNOW()) return` (230). `call periodici ( brks, kgrpnt, 1, 1 )` (234)로 주기 격자 경계를 동기화한다. nm=1..mcgrd(238)에서 `if ( wets(nm) == 1 .and. brks(nm) == 1 ) wets(nm) = 0` (240). 루틴 종료(244). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 100·125·184: 이웃의 쇄파 여부는 갱신 전 brks를 복사한 iwrk(:,1)에서 읽는다. 셀 자신의 지속 조건은 brks(nm)를 읽는다(131·190).
- 106–111·154–170·211: 영구 건조 이웃 인덱스 1을 현재점으로 바꾸는 네 문장과 brks(1)=0 대입은 2차원 경로에만 있다. 1차원 경로에는 대응 문장이 없다.
- 115–117·174–176: rootgh는 sqrt(grav*hs(nm)), dsdt는 수면 차이를 dt로 나눈 값이다. 이 루틴에는 hs의 하한 제한이나 dt=0 검사가 없다.
- 123·129·133·182·188·192·217–225: q를 0으로 만드는 쇄파 분기 뒤에 조파 원천 영역의 brks를 0으로 지운다. 이 후처리 블록에는 q를 되돌리는 대입이 없다.
