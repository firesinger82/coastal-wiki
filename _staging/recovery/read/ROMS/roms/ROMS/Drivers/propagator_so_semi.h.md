---
file: models/ROMS/raw/source_code/roms/ROMS/Drivers/propagator_so_semi.h
lines: 155
sha256: e79376de2515aa55c9e14333f92bbce673cd3dd7e668df5c46b7b404a5f7da4d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# propagator_so_semi.h — 판독 구간 기록

구간은 1행부터 155행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | `propagator_mod` 시작(1), 저작권·MIT/X 라이선스 안내(3–8). 선택한 함수의 준노름(seminorm)을 기준으로 확률 최적 모드(stochastic optimal) 연산자의 고유벡터를 구한다는 주석(10–14). Moore 등의 2004년 문헌(16–20). mod_kinds·implicit none·PRIVATE·PUBLIC propagator_so_semi·CONTAINS·주석(24–33). |
| 34–66 | 시작 시 1행 모듈 안. propagator_so_semi(RunInterval,state,ad_state) 입구(34). 매개변수·병렬·상태·시간 모듈(37–42). `#ifdef SO_SEMI_WHITE` (44)의 so_semi_white 사용(45), `#else` (46)의 so_semi_red 사용(47), `#endif` (48). FoundError 사용(49). RunInterval·state(Ngrids)는 입력, ad_state(Ngrids)는 inout(53–56). `logical, save :: FirstPass = .TRUE.` (60). ng/tile·MyFile 선언(62–65), 주석(66). |
| 67–94 | 시작 시 34행 propagator_so_semi 안. 최초 반복에서 한 번만 함수 준노름으로 수반 모델(adjoint model, ADM)을 역방향 적분한다는 주석(67–71). `Nrun=Nrun+1` (73). 격자(grid)마다 SOrec=0(74–76). `FIRST_PASS : IF (FirstPass) THEN` (78)에서 FirstPass=.FALSE.(79). 격자마다 ad_initial(ng)(83–84), `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (85). 수반 출력은 LdefADJ/LwrtADJ=.TRUE.·LcycleADJ=.FALSE.(90–94). |
| 95–115 | 시작 시 34행 propagator_so_semi·78행 FIRST_PASS 참 분기 안. 최초 시각에서만 함수 강제력을 넣는다는 주석(96–97). 격자 루프의 `IF (Master) THEN` (100)에서 ADM 적분 로그(101). DstrS=tdays·DendS=DstrS로 같은 시각을 설정(103–104). `#ifdef SOLVE3D` (107)의 ad_main3d(RunInterval)(108), `#else` (109)의 ad_main2d(RunInterval)(110), `#endif` (111). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (112). FIRST_PASS 종료·주석(114–115). |
| 116–134 | 시작 시 34행 propagator_so_semi 안. 표면 강제력(surface forcing) 변수를 포함한 포장 수반 상태 벡터를 구한다는 주석(116–119). 격자·순방향 타일(tile) 루프(121–122)의 `# ifdef SO_SEMI_WHITE` (123)에서 so_semi_white(ng,tile,Nstr(ng),Nend(ng),state(ng)%vector,ad_state(ng)%vector)(124–126), `# else` (127)에서 같은 인수의 so_semi_red(128–130), `# endif` (131). 루프 종료·주석(132–134). |
| 135–155 | 시작 시 34행 propagator_so_semi 안. 반복과 확률 최적 모드 행렬의 대각합(trace) 보고 안내(135–137). `IF (Master) THEN` (139)의 격자 루프에서 반복·수렴 Ritz 값(Ritz value) 수 Nconv·TRnorm 로그(140–145), 조건 종료(146). 로그 FORMAT(148–150), 주석·RETURN·루틴 종료·빈 줄·모듈 종료(151–155). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60·78–85·107–114: FirstPass는 SAVE 변수이며 최초 참 분기 진입 직후 거짓으로 바뀐다. 뒤의 초기화 또는 적분 오류 조건이 RETURN해도 이 파일에는 FirstPass를 참으로 되돌리는 대입이 없다.
- 121–133·139–155: so_semi_white/so_semi_red 호출 뒤에는 이 파일의 FoundError 검사가 없다. 이어지는 문장은 반복·노름 로그와 RETURN이다.
