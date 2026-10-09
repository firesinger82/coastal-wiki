---
file: models/ADCIRC/raw/source_code/adcirc/prep/post_global.F
lines: 160
sha256: ed82b35e757185b41abddea972494316f697945ce2a26f20434a33b5cee47396
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# post_global.F — 판독 구간 기록

구간은 1행부터 160행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | ADCIRC 명칭과 1994–2025년 저작권 머리말(1–4). GNU Lesser General Public License 3 이상에 따른 재배포·수정 허용과 무보증 안내(5–19). 주석은 버전 45.07의 fort.71·fort.72·fort.73 및 NOFF 배열 처리 추가(20–21), 45.06의 재시작 파일(hot start file) 형식 변경 대응(22), 45.11의 3차원 관측 지점(recording station) 대응(23), 45.12 갱신(24)을 적는다. |
| 25–38 | `MODULE POST_GLOBAL` 시작과 `IMPLICIT NONE`(25–26). 크기 관련 정수 MNPROC·MNP·MNE·MNPP·MNSTAE·MNSTAV·MNHARF·MNWLAT·MNWLON을 선언한다(28). MNSTAC 주석은 전체 영역 농도 관측 지점 수를 적는다(29). MNSTAM 주석은 전체 영역 기상 관측 지점 수를 적는다(30). MNEP 주석은 부분 영역(subdomain)의 최대 요소(element) 수를 적는다(31). PARM14의 NELG·NNODG(32–34)와 STRING14의 80자 AGRID(35–37)를 선언한다. 빈 줄과 구분 주석을 포함한다(27·38). 이 구간의 선언에는 초기값이 없다. |
| 39–55 | 시작 시 25행 `POST_GLOBAL` 모듈 안. PARM15의 IM·NWS(39–41), 지점 출력용 NOUTE/NSPOOLE/NSTAE·NOUTV/NSPOOLV/NSTAV·NOUTC/NSPOOLC/NSTAC·NOUTM/NSPOOLM/NSTAM(42–45), 전체 출력용 NOUTGE/NSPOOLGE·NOUTGV/NSPOOLGV·NOUTGC/NSPOOLGC·NOUTGW/NSPOOLGW(46–49), NHASE·NHASV·NHAGE·NHAGV를 정수로 선언한다(50). STRING15의 RUNDES·RUNID는 각각 80자이다(53–54). 구분 주석을 포함한다(51–52·55). 이 구간에는 값 대입이나 조건 분기가 없다. |
| 56–71 | 시작 시 25행 `POST_GLOBAL` 모듈 안. PARM15-3DVS의 IDEN은 3차원 실행 유형, NFEN은 수직 절점(vertical node) 수라는 주석이 있다(56–58). 지점 출력 정수 I3DSD/NSPO3DSD/NSTA3DD·I3DSV/NSPO3DSV/NSTA3DV·I3DST/NSPO3DST/NSTA3DT와 REAL(8) 시간 쌍 TO3DSDS/TO3DSDF·TO3DSVS/TO3DSVF·TO3DSTS/TO3DSTF를 선언한다(59–64). 전체 출력 정수 I3DGD/NSPO3DGD·I3DGV/NSPO3DGV·I3DGT/NSPO3DGT와 REAL(8) 시간 쌍 TO3DGDS/TO3DGDF·TO3DGVS/TO3DGVF·TO3DGTS/TO3DGTF를 선언한다(65–70). 끝 구분 주석을 포함한다(71). 기본값 대입은 없다. |
| 72–83 | 시작 시 25행 `POST_GLOBAL` 모듈 안. ELESTAT의 TOUTSE·TOUTFE·TOUTSGE·TOUTFGE(72–73), VELSTAT의 TOUTSGV·TOUTFGV·TOUTSV·TOUTFV(75–76), CONSTAT의 TOUTSC·TOUTFC·TOUTSGC·TOUTFGC 및 TOUTSGW·TOUTFGW를 REAL(8)로 선언한다(78–80). 기상 관측 지점 절의 TOUTFM·TOUTSM도 REAL(8)이다(81–82). 구분 주석과 빈 줄을 포함한다(74·77·83). 실행문은 없다. |
| 84–95 | 시작 시 25행 `POST_GLOBAL` 모듈 안. 각도와 라디안 변환(degrees-to-radians/radians-to-degrees) 주석 아래 CONVERT의 DEG2RAD·RAD2DEG·R을 REAL(8)로 선언한다(84–88). 직접 접근 저장 장치(Direct Access Storage Device, DASD) 파일 조작 주석 아래 NBYTE를 정수로 선언한다(89–94). 끝 구분 주석을 포함한다(95). 변환 계수나 NBYTE의 값을 설정하는 문장은 없다. |
| 96–114 | 시작 시 25행 `POST_GLOBAL` 모듈 안. 자료 분할(data decomposition) 선언 머리말과 지역 매핑(local mapping) 주석(96–103). 주석은 NSTACP·IMAP_STAC_LG를 아직 사용하지 않는다고 적는다(104). LOCALI의 NPROC와 할당 가능 배열(allocatable array) NNODP·NELP·NOD_RES_TOT·NSTAEP·NSTAVP·NSTACP를 정수로 선언한다(106–110). 부분 영역 기압 관측 지점 수라는 주석과 정수 배열 NSTAMP 선언을 포함한다(111–112). 구분 주석을 포함한다(105·113–114). 배열 크기나 값은 이 구간에서 설정하지 않는다. |
| 115–129 | 시작 시 25행 `POST_GLOBAL` 모듈 안. 지역에서 전체로 대응하는 매핑(local-to-global mapping)의 정수 할당 가능 2차원 배열 IMAP_NOD_LG·IMAP_EL_LG·IMAP_STAE_LG·IMAP_STAV_LG·IMAP_STAC_LG·IMAP_STAM_LG를 선언한다(115–123). IMAP_STAM_LG 주석은 기압을 적는다(123). 전체에서 지역으로 대응하는 매핑(global-to-local mapping)의 정수 할당 가능 2차원 배열 IMAP_NOD_GL을 선언한다(125–128). 구분 주석을 포함한다(124·129). 실행문은 없다. |
| 130–140 | 시작 시 25행 `POST_GLOBAL` 모듈 안. 3DVS의 정수 할당 가능 1차원 배열 NNSTA3DDP·NNSTA3DVP·NNSTA3DTP와 2차원 배열 IMAP_STA3DD_LG·IMAP_STA3DV_LG·IMAP_STA3DT_LG를 선언한다(130–135). 선언 종료 머리말과 빈 줄을 포함한다(136–140). 이 구간에는 배열 할당이나 초기화가 없다. |
| 141–160 | 시작 시 25행 `POST_GLOBAL` 모듈 안. `CONTAINS`(141), 빈 줄(142), `SUBROUTINE ALLOC_MAIN1()` 입구와 구분 주석(143–144). NNODP·NELP·NOD_RES_TOT·NSTAEP·NSTAVP·NSTACP·NSTAMP를 각각 MNPROC 크기로 할당한다(145–148). IMAP_NOD_LG는 (MNPP,MNPROC), IMAP_EL_LG는 (MNEP,MNPROC), IMAP_NOD_GL은 (2,MNP)로 할당한다(149–151). 빈 줄을 포함한다(152). 지점 매핑 IMAP_STAE_LG·IMAP_STAV_LG·IMAP_STAC_LG·IMAP_STAM_LG는 각각 (MNSTAE,MNPROC)·(MNSTAV,MNPROC)·(MNSTAC,MNPROC)·(MNSTAM,MNPROC)로 할당한다(153–156). 이 루틴(routine)에는 조건 분기나 다른 루틴 호출이 없다. 구분 주석, 루틴 종료, 모듈 종료와 마지막 빈 줄을 포함한다(157–160). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–31·145–156: 배열 할당 크기에 사용하는 모듈 정수의 선언에는 초기값이 없다. 이 파일에는 해당 정수의 값을 설정하는 대입문이 없다.
- 104·110·122·147·155: 주석은 NSTACP·IMAP_STAC_LG를 아직 사용하지 않는다고 적는다. ALLOC_MAIN1은 두 배열을 할당한다.
- 132–135·143–158: NNSTA3DDP·NNSTA3DVP·NNSTA3DTP·IMAP_STA3DD_LG·IMAP_STA3DV_LG·IMAP_STA3DT_LG를 할당 가능 배열로 선언한다. ALLOC_MAIN1에는 이 여섯 배열의 할당문이 없다.
- 143–158: ALLOC_MAIN1에는 할당 여부를 검사하는 조건이 없다. ALLOCATE 문에는 STAT 지정이 없다. 할당된 배열 원소의 값을 초기화하는 대입문도 없다.
