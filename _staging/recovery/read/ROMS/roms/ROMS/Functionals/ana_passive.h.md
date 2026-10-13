---
file: models/ROMS/raw/source_code/roms/ROMS/Functionals/ana_passive.h
lines: 115
sha256: d18528fbfc68e552f6afc7a0f8cd1cb4fe5c6ddf2f5edac86e80dc58875ff08d
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# ana_passive.h — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ana_passive는 수동 비활성 추적자(passive inert tracer)의 해석식 초기조건을 설정한다는 머리말이다(2–14). param·ncparam·ocean 모듈과 입력 ng·tile·model, MyFile을 선언한다(16–27). 29행은 tile.h를 끼워 넣는다. ana_passive_tile에 OCEAN(ng)%t를 넘긴다(31–34). DISTRIBUTE 조건에 따라 Lanafile 또는 Lanafile과 tile=0을 검사하고 ANANAME(18)을 설정한다(38–44). RETURN과 루틴 종료를 포함한다(46–48). 원문 조건·대입·전처리 행: `character (len=*), parameter :: MyFile =                          &` (26), `&  __FILE__` (27), `#include "tile.h"` (29), `#ifdef DISTRIBUTE` (38), `IF (Lanafile) THEN` (39), `#else` (40), `IF (Lanafile.and.(tile.eq.0)) THEN` (41), `#endif` (42), `ANANAME(18)=MyFile` (43), `END IF` (44). |
| 49–80 | ana_passive_tile 입구와 param·scalars 사용이다(50–57). ASSUMED_SHAPE는 t의 하한만 선언하고 기본 분기는 수직 N(ng)·시간 슬롯 3·추적자 NT(ng)를 명시한다(65–69). i·iage·ip·itrc·j·k를 선언하고 75행에서 set_bounds.h를 끼워 넣는다. 초기조건 주석·빈 줄을 포함한다(77–80). 원문 조건·대입·전처리 행: `#ifdef ASSUMED_SHAPE` (65), `#else` (67), `#endif` (69), `#include "set_bounds.h"` (75). |
| 81–97 | 시작 시 50행 ana_passive_tile 안. MY_APPLICATION의 AGE_MEAN은 ip=1..NPT를 2씩 증가시키고 inert(ip)·inert(ip+1)를 추적자와 평균 나이(mean age) 인덱스로 사용한다(81–85). 모든 수직층·타일 지점에서 추적자 시간 슬롯 1은 ??? 자리표시자(placeholder)로 남고 슬롯 2는 슬롯 1을 복사한다(86–90). 나이의 슬롯 1은 0이고 슬롯 2는 슬롯 1을 복사한다(91–92). 루프 종료와 AGE_MEAN의 다른 분기 시작을 포함한다(93–97). 원문 조건·대입·전처리 행: `#if defined MY_APPLICATION` (81), `# ifdef AGE_MEAN` (82), `DO ip=1,NPT,2` (83), `itrc=inert(ip)` (84), `iage=inert(ip+1)` (85), `DO k=1,N(ng)` (86), `DO j=JstrT,JendT` (87), `DO i=IstrT,IendT` (88), `t(i,j,k,1,itrc)=???` (89), `t(i,j,k,2,itrc)=t(i,j,k,1,itrc)` (90), `t(i,j,k,1,iage)=0.0_r8` (91), `t(i,j,k,2,iage)=t(i,j,k,1,iage)` (92), `END DO` (93), `END DO` (94), `END DO` (95), `END DO` (96), `# else` (97). |
| 98–115 | 시작 시 `#if defined MY_APPLICATION` (81) 안·`# ifdef AGE_MEAN` (82)의 `# else` (97) 분기 안. 시작 시 50행 ana_passive_tile 안. AGE_MEAN 이외에서는 ip=1..NPT의 모든 inert 추적자에 대해 모든 수직층·타일 지점의 슬롯 1을 ???로 두고 슬롯 2로 복사한다(98–108). 109행은 AGE_MEAN을 닫는다. MY_APPLICATION 이외에서는 값이 제공되지 않았다는 문장을 둔다(110–112). RETURN과 루틴 종료를 포함한다(114–115). 원문 조건·대입·전처리 행: `DO ip=1,NPT` (98), `itrc=inert(ip)` (99), `DO k=1,N(ng)` (100), `DO j=JstrT,JendT` (101), `DO i=IstrT,IendT` (102), `t(i,j,k,1,itrc)=???` (103), `t(i,j,k,2,itrc)=t(i,j,k,1,itrc)` (104), `END DO` (105), `END DO` (106), `END DO` (107), `END DO` (108), `# endif` (109), `#else` (110), `ana_passive.h: no values provided for t(:,:,:,1,inert(itrc))` (111), `#endif` (112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 89·103: 두 초기 추적자 대입문은 우변에 ??? 자리표시자를 남긴다. 110–111행의 기본 전처리 분기는 t 값이 제공되지 않았다는 문장을 둔다.
- 68·89–92·103–104: 명시 배열 선언의 시간 슬롯 수는 3이다. 이 파일의 초기 대입은 시간 슬롯 1과 2에만 있다.
- 83–85: AGE_MEAN 루프는 ip를 2씩 늘리고 inert(ip+1)를 참조한다. 이 블록에는 NPT의 짝수 여부를 검사하는 조건문이 없다.
