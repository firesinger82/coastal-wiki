---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_scope.h
lines: 189
sha256: 8e5007fa1e5c825769306dffa7fcec323b0b4e78df114ed97167ee246f6889f3
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_scope.h — 판독 구간 기록

구간은 1행부터 189행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–55 | ana_scope의 머리말은 수반 민감도(adjoint sensitivity)의 공간 범위 마스크를 설명한다(2–14). param·grid·ncparam, 입력 인수·MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_scope_tile에 Rscope·Uscope·Vscope를 넘기고 MASKING에서 rmask·umask·vmask도 추가한다(31–41). DISTRIBUTE 조건에 따라 파일 이름을 ANANAME(22)에 저장하고 끝낸다(45–55). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef MASKING` (34), `#endif` (38), `#ifdef DISTRIBUTE` (45), `IF (Lanafile) THEN` (46), `#else` (47), `IF (Lanafile.and.(tile.eq.0)) THEN` (48), `#endif` (49), `ANANAME(22)=MyFile` (50), `END IF` (51). |
| 56–107 | ana_scope_tile의 인수 목록은 MASKING에서 세 육지·바다 마스크(land/sea mask)를 추가한다(57–63). param·scalars·exchange_2d_mod를 사용하고 DISTRIBUTE에서 mp_exchange2d를 가져온다(66–72). ASSUMED_SHAPE와 MASKING에 따라 입력 마스크·출력 scope 배열의 경계를 선언한다(80–98). Imin·Imax·Jmin·Jmax·i·j·작업 배열 scope를 선언하고 106행에서 set_bounds.h를 끼워 넣는다(102–106). 원문 조건·대입·전처리 행: `#ifdef MASKING` (60), `#endif` (62), `#ifdef DISTRIBUTE` (70), `#endif` (72), `#ifdef ASSUMED_SHAPE` (80), `# ifdef MASKING` (81), `# endif` (85), `#else` (89), `# ifdef MASKING` (90), `# endif` (94), `#endif` (98), `#include "set_bounds.h"` (106). |
| 108–133 | 시작 시 57행 ana_scope_tile 안. 주석은 Land=0·Sea=1과 사유 작업 배열 mask를 적는다(109–113). DOUBLE_GYRE는 Lm·Mm 중앙에서 -5와 +10으로 사각형 경계를 계산한다(115–119). 확장 타일 범위에서 scope를 먼저 0으로 설정하고 사각형 내부만 1로 바꾼다(121–129). 기본 전처리 분기는 공간 범위 마스크 값이 제공되지 않았다는 문장을 둔다(130–132). 원문 조건·대입·전처리 행: `#ifdef DOUBLE_GYRE` (115), `Imin=-5+(Lm(ng)+1)/2` (116), `Imax=Imin+10` (117), `Jmin=-5+(Mm(ng)+1)/2` (118), `Jmax=Jmin+10` (119), `DO j=Jstrm2,Jendp2` (121), `DO i=Istrm2,Iendp2` (122), `scope(i,j)=0.0_r8` (123), `IF (((Imin.le.i).and.(i.le.Imax)).and.                        &` (124), `&        ((Jmin.le.j).and.(j.le.Jmax))) THEN` (125), `scope(i,j)=1.0_r8` (126), `END IF` (127), `END DO` (128), `END DO` (129), `#else` (130), `ana_scope.h: no values provided for spatial scope masking.` (131), `#endif` (132). |
| 134–163 | 시작 시 57행 ana_scope_tile 안. Rscope는 scope를 복사하고 MASKING에서 rmask를 곱한다(134–141). Uscope는 좌·현재 scope의 곱이고 MASKING에서 umask를 곱한다(147–154). Vscope는 아래·현재 scope의 곱이고 MASKING에서 vmask를 곱한다(155–162). 각 루프 범위·전처리 종료와 주석 줄을 포함한다(134–163). 원문 조건·대입·전처리 행: `DO j=JstrT,JendT` (134), `DO i=IstrT,IendT` (135), `Rscope(i,j)=scope(i,j)` (136), `#ifdef MASKING` (137), `Rscope(i,j)=Rscope(i,j)*rmask(i,j)` (138), `#endif` (139), `END DO` (140), `END DO` (141), `DO j=JstrT,JendT` (147), `DO i=IstrP,IendT` (148), `Uscope(i,j)=scope(i-1,j)*scope(i,j)` (149), `#ifdef MASKING` (150), `Uscope(i,j)=Uscope(i,j)*umask(i,j)` (151), `#endif` (152), `END DO` (153), `END DO` (154), `DO j=JstrP,JendT` (155), `DO i=IstrT,IendT` (156), `Vscope(i,j)=scope(i,j-1)*scope(i,j)` (157), `#ifdef MASKING` (158), `Vscope(i,j)=Vscope(i,j)*vmask(i,j)` (159), `#endif` (160), `END DO` (161), `END DO` (162). |
| 164–189 | 시작 시 57행 ana_scope_tile 안. 동서 또는 남북 주기경계(periodic boundary)가 참이면 exchange_r2d_tile·exchange_u2d_tile·exchange_v2d_tile을 호출한다(168–178). DISTRIBUTE는 mp_exchange2d에 Rscope·Uscope·Vscope의 세 배열과 NghostPoints·주기 플래그를 넘긴다(180–186). RETURN과 루틴 종료를 포함한다(188–189). 원문 조건·대입·전처리 행: `IF (EWperiodic(ng).or.NSperiodic(ng)) THEN` (168), `END IF` (178), `#ifdef DISTRIBUTE` (180), `#endif` (186). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 104·112–126: 작업 배열 선언과 실행문은 scope를 사용한다. 병렬 작업 배열 설명 주석은 mask라는 이름을 사용한다.
- 115–131: DOUBLE_GYRE만 공간 범위 값을 설정한다. 기본 전처리 분기는 “ana_scope.h: no values provided for spatial scope masking.” 문장을 둔다.
