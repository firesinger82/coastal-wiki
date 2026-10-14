---
file: models/SWASH/raw/source_code/swash/src/SwashComputStruc.ftn90
lines: 265
sha256: 75a1f112d4a546da08729e63352dc12db4d4aacbf440896b6f85c96bad6dd5ba
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashComputStruc.ftn90 — 판독 구간 기록

구간은 1행부터 265행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–43 | `SwashComputStruc` 입구(1). 기관·저작권 2010–2026·GPL 3 이상·무보증 주석(3–27), 작성자와 2010년 신설·2022년 이동 강체(moving rigid bodies) 확장 이력(30–38). 구조 격자(structured grid)에서 한 전체 계산 단계를 수행한다는 목적(40–42). |
| 44–87 | 시작 시 1행 루틴 안. ocpcomm4·SwashCommdata3·m_parall·SwashFlowdata·SwashSolvedata의 iamout·SwashRigBoddata 사용(46–51). `integer, save         :: ient = 0 ! number of entries in this subroutine` (57). 반복 수·최대 반복 수·최대 오차의 강체/자유도 인덱스·선형/각변위 허용오차·잔차·최대 변위·STPNOW 선언(58–80). 구조·소스 구분 주석(82–87). |
| 88–106 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwashComputStruc')` (88). `xfotmx    = maxval(abs(xfot0))` (92), `xformx    = maxval(abs(xfor0))` (93), `reps      = pship(8)` (94), `epslin(1) = max(reps,reps*xfotmx)` (95), `epslin(2) = max(reps,reps*xformx)` (96). `maxit   = nint(pship(9))` (100), `j       = 0` (101), `resm(1) = epslin(1) + 1.` (102), `resm(2) = epslin(2) + 1.` (103). 유체·구조 상호작용(fluid-structure interaction; FSI) 반복 시작 주석(105–106). [10-15 전수 검증 보완] |
| 107–147 | 시작 시 1행 루틴 안. `10 if ( ( resm(1) > epslin(1) .or. resm(2) > epslin(2) ) .and. j < maxit ) then` (107)은 `j = j + 1` (109)을 대입한다. 이 조건 안에서 `resm = 0.` (111). `minf = 0` (112). `ninf = 0` (113). 운동학적 경계조건(kinematic boundary conditions): `!TIMG       call SWTSTA(61)` (117), `call SwashUpdKBCrigb` (118), `!TIMG       call SWTSTO(61)` (119), `if (STPNOW()) return` (120). 흐름: `!TIMG       call SWTSTA(51)` (124), `if ( .not.momskip ) call SwashComputFlow` (125), `!TIMG       call SWTSTO(51)` (126), `if (STPNOW()) return` (127). 힘·토크(torque): `!TIMG       call SWTSTA(62)` (131), `call SwashForcesRigidBod` (132), `!TIMG       call SWTSTO(62)` (133), `if (STPNOW()) return` (134). `xfoti = xfot1` (138). `xfori = xfor1` (139). 강체 운동: `!TIMG       call SWTSTA(63)` (143), `call SwashMotionRigidBod` (144), `!TIMG       call SWTSTO(63)` (145), `if (STPNOW()) return` (146). 모든 !TIMG 행은 swash/switch.pl 57행 규칙의 -timg 스위치에서 실행 코드가 된다. [10-15 전수 검증 보완] |
| 148–169 | 시작 시 1행 루틴·107행 `if ( ( resm(1) > epslin(1) .or. resm(2) > epslin(2) ) .and. j < maxit ) then` 안. m=1..mbod·n=1..ndim(150–151)에서 `res = abs(xfot1(m,n) - xfoti(m,n))` (153). `if ( res > resm(1) ) then` (154)은 `resm(1) = res` (155). 같은 분기에서 `minf(1) = m` (156). `ninf(1) = n` (157). `res = abs(xfor1(m,n) - xfori(m,n))` (160). `if ( res > resm(2) ) then` (161)은 `resm(2) = res` (162). 같은 분기에서 `minf(2) = m` (163). `ninf(2) = n` (164). 두 루프 종료(167–168). 154행 조건은 158행에서 닫힌다. 161행 조건은 165행에서 닫힌다. 바깥 107행 조건은 183행에서 닫힌다. [10-15 전수 검증 보완] |
| 170–184 | 시작 시 1행 루틴·107행 `if ( ( resm(1) > epslin(1) .or. resm(2) > epslin(2) ) .and. j < maxit ) then` 안. `if ( iamout == 2 .and. INODE == MASTER .and. maxit > 1 ) then` (170)은 자유도별 반복 로그를 출력한다. 조건 원문: `if ( ninf(1) == 1 )` (172), `if ( ninf(1) == 2 )` (173), `if ( ninf(1) == 3 )` (174), `if ( ninf(2) == 1 )` (175), `if ( ninf(2) == 2 )` (176), `if ( ninf(2) == 3 )` (177). 앞 세 출력은 선형 오차 resm(1), 뒤 세 출력은 `resm(2)*180./pi` (175–177)를 쓴다. 로그 분기 종료(179), `goto 10` (181)으로 조건 재검사. 반복 조건 종료(183). 172–177행은 각각 독립된 단일 행 IF이다. ninf(1)=1·2·3 출력은 각각 surge·sway·heave를 표시한다(172–174). 선형 오차의 출력 단위는 m이다(172–174). ninf(2)=1·2·3 출력은 각각 roll·pitch·yaw를 표시한다(175–177). 각변위 오차의 출력 단위는 deg이다(175–177). `goto 10`의 표적은 107행이다. [10-15 전수 검증 보완] |
| 185–212 | 시작 시 1행 루틴 안. `if ( ifloat == 2 .and. INODE == MASTER ) then` (187) 안 `if ( resm(1) > epslin(1) .and. iamout > 0 ) then` (189)은 선형 변위 비수렴·반복 수·resm(1)·epslin(1) 출력(191–194). `else if ( resm(2) > epslin(2) .and. iamout > 0 ) then` (196)은 각변위 비수렴·반복 수·resm(2)·epslin(2) 출력(198–201). `else if ( iamout == 3 ) then` (203)은 반복 수와 두 최대 오차 출력(205–207). 189행 사슬은 최종 `else` 없이 209행에서 닫힌다. 187행 조건은 211행에서 닫힌다. 193·200행 출력문구는 `2-norm of the residual`이다. 이 출력문은 150–168행에서 구한 최대 절대차를 그대로 출력한다. [10-15 전수 검증 보완] |
| 213–229 | 시작 시 1행 루틴 안. 수심 갱신: `!TIMG    call SWTSTA(52)` (215), `if ( kmax == 1 ) then` (216)은 `call SwashUpdateDepths (   u1,   v1 )` (217), `else` (218)는 `call SwashUpdateDepths ( udep, vdep )` (219), `!TIMG    call SWTSTO(52)` (221), `if (STPNOW()) return` (222). 층 경계면(layer interfaces) 갱신: `!TIMG    call SWTSTA(53)` (226), `if ( kmax > 1 ) call SwashLayerIntfaces` (227), `!TIMG    call SWTSTO(53)` (228). !TIMG 행은 -timg에서 실행 코드가 된다(switch.pl:57). |
| 230–250 | 시작 시 1행 루틴 안. 젖음·마름(wetting and drying): `!TIMG    call SWTSTA(54)` (232), `call SwashDryWet` (233), `!TIMG    call SWTSTO(54)` (234), `if (STPNOW()) return` (235). 자유수면/가압류(free surface/pressurized flow) 마스크: `!TIMG    call SWTSTA(54)` (239), `if ( ifloat /= 0 ) call SwashPresFlow` (240), `!TIMG    call SWTSTO(54)` (241), `if (STPNOW()) return` (242). 쇄파(wave breaking): `!TIMG    call SWTSTA(54)` (246), `if ( isurf /= 0 ) call SwashBreakPoint` (247), `!TIMG    call SWTSTO(54)` (248), `if (STPNOW()) return` (249). !TIMG 행은 -timg에서 실행 코드가 된다(switch.pl:57). |
| 251–265 | 시작 시 1행 루틴 안. 수송(transport): `!TIMG    call SWTSTA(101)` (253), `if ( itrans /= 0 ) call SwashComputTrans` (254), `!TIMG    call SWTSTO(101)` (255), `if (STPNOW()) return` (256). 3차원 난류(turbulence): `!TIMG    call SWTSTA(102)` (260), `if ( iturb /= 0 ) call SwashComputTurb` (261), `!TIMG    call SWTSTO(102)` (262), `if (STPNOW()) return` (263). !TIMG 행은 -timg에서 실행 코드가 된다(switch.pl:57). 루틴 종료(265). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 150–168·193·200: resm은 각 성분의 절대 차이 중 최대값으로 계산한다. 비수렴 출력 문자열은 같은 값을 `2-norm of the residual`이라고 부른다.
- 187–211: 선형 변위와 각변위의 비수렴 출력은 if/else if 관계이다(189·196). 바깥 조건은 `if ( ifloat == 2 .and. INODE == MASTER ) then` (187)이다. 이 조건 안에서 `iamout > 0`이고 두 오차가 모두 허용값을 넘으면 선형 변위 경로만 출력한다(189–201). 조건식상 iamout가 0이면 두 비수렴 출력 조건은 모두 거짓이다(189·196). [10-15 전수 검증 정정]
- 100–107·125·213–263: 최대 반복 수는 nint(pship(9))이다. maxit<=0이면 반복 조건에 들어가지 않으며 그 안의 흐름 계산 호출도 실행하지 않는다. 후속 수심·마스크·수송·난류 처리는 반복 조건 밖에 있다.
- 232–248: 젖음·마름·자유수면/가압류·쇄파 갱신의 세 시간 측정 구간은 같은 타이머 번호 54를 사용한다.
