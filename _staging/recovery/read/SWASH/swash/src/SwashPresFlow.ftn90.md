---
file: models/SWASH/raw/source_code/swash/src/SwashPresFlow.ftn90
lines: 232
sha256: 4ecfa0589e3b2abd6298a9e0a2c4ad3121fbeebfb48464afe0637f6a60f97914
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashPresFlow.ftn90 — 판독 구간 기록

구간은 1행부터 232행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–51 | `SwashPresFlow` 시작(1). 기관·SWASH 비정수압(non-hydrostatic) 파랑·흐름 모델·2010–2026 저작권·GPL 3 이상·무보증 주석(3–27). 저자·2014년 신설 이력(30–36). 수위점(water-level point)·유속점에서 가압 흐름(pressurized flow) 마스크 배열을 갱신하는 목적(38–40). ocpcomm4·SwashCommdata3·m_genarr·SwashFlowdata 사용(44–47), implicit none·지역변수 절 머리말(49–51). |
| 52–71 | 시작 시 1행 SwashPresFlow 루틴 안. `integer, save :: ient = 0` (53), m/n·오른쪽/위쪽 이웃 인덱스 mu/nu·현재/이웃 격자점 주소 nm/nmu/num·STPNOW 선언(53–62). 구조·의사코드·Source text 주석(64–69). `if (ltrace) call strace (ient,'SwashPresFlow')` (70), 구분 주석(71). [10-15 전수 검증 보완] |
| 72–98 | 시작 시 1행 루틴 안. `if ( oned ) then` (72) 안의 수위점 `do m = mfu, ml` (76)에서 `nm = kgrpnt(m,1)` (78). `if ( s1(nm) < -flos(nm) ) then` (80)은 `presp(nm) = 0` (82), `else` (84)는 `presp(nm) = 1` (86)로 설정한다. 조건·루프 종료(88–90). 이웃 부분영역(subdomain)과 마스크 교환을 위해 `call SWEXCHGI ( presp, kgrpnt, 1, 1 )` (94), `if (STPNOW()) return` (95). u점 머리말·빈 줄(97–98). [10-15 전수 검증 보완] |
| 99–122 | 시작 시 1행 루틴·`if ( oned ) then` (72)의 참 분기 안. `do m = mf, ml` (99), `mu = m + 1` (101), `nm  = kgrpnt(m ,1)` (103), `nmu = kgrpnt(mu,1)` (104). `if ( presp(nm) == 0 .and. presp(nmu) == 0 ) then` (106)은 `presu(nm) = 0` (108), `else` (110)는 `presu(nm) = 1` (112). 조건·루프 종료(114–116). `call SWEXCHGI ( presu, kgrpnt, 1, 1 )` (120), `if (STPNOW()) return` (121), 구분 주석(122). [10-15 전수 검증 보완] |
| 123–157 | 시작 시 1행 루틴·`if ( oned ) then` (72) 안. `else` (123)는 비일차원 분기이다. 수위점 `do n = nfu, nl` (127)·`do m = mfu, ml` (128)에서 `nm = kgrpnt(m,n)` (130). `if ( s1(nm) < -flos(nm) ) then` (132)은 `presp(nm) = 0` (134), `else` (136)는 `presp(nm) = 1` (138). 조건·두 루프 종료(140–143). 영구 건조점은 `presp(1) = 0` (147). `call SWEXCHGI ( presp, kgrpnt, 1, 1 )` (151), `if (STPNOW()) return` (152). 주기 격자(repeating grid) 경계 동기화 `call periodici ( presp, kgrpnt, 1, 1 )` (156), 구분 주석(157). [10-15 전수 검증 보완] |
| 158–193 | 시작 시 1행 루틴·`if ( oned ) then` (72)의 `else` (123) 안. u점 `do n = nfu, nl` (160)·`do m = mf, ml` (161), `mu = m + 1` (163), `nm  = kgrpnt(m ,n)` (165), `nmu = kgrpnt(mu,n)` (166). `if ( presp(nm) == 0 .and. presp(nmu) == 0 ) then` (168)은 `presu(nm) = 0` (170), `else` (172)는 `presu(nm) = 1` (174). 조건·두 루프 종료(176–179). 영구 건조점은 `presu(1) = 0` (183). `call SWEXCHGI ( presu, kgrpnt, 1, 1 )` (187), `if (STPNOW()) return` (188), `call periodici ( presu, kgrpnt, 1, 1 )` (192), 구분 주석(193). [10-15 전수 검증 보완] |
| 194–232 | 시작 시 1행 루틴·`if ( oned ) then` (72, 종료 230)의 `else` (123) 안. v점 `do m = mfu, ml` (196)·`do n = nf, nl` (197), `nu = n + 1` (199), `nm  = kgrpnt(m,n )` (201), `num = kgrpnt(m,nu)` (202). `if ( presp(nm) == 0 .and. presp(num) == 0 ) then` (204)은 `presv(nm) = 0` (206), `else` (208)는 `presv(nm) = 1` (210). 조건·두 루프 종료(212–215). 영구 건조점은 `presv(1) = 0` (219). `call SWEXCHGI ( presv, kgrpnt, 1, 1 )` (223), `if (STPNOW()) return` (224), `call periodici ( presv, kgrpnt, 1, 1 )` (228). oned 분기는 230행에서 닫힌다. 루틴은 232행에서 끝난다. 구분 주석(229·231). [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 80–88·132–140: 수위가 −flos와 같으면 else를 따라 presp=1이 된다. 유속점은 인접 수위점 둘 중 하나라도 presp=1이면 해당 마스크를 1로 설정한다(106–114·168–176·204–212).
- 72–122·123–230: 일차원 경로에는 presp/presu의 인덱스 1을 0으로 설정하거나 periodici를 호출하는 문장이 없다. 비일차원 경로에는 presp/presu/presv 각각에 해당 설정과 호출이 있다.
