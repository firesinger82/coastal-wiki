---
file: models/SWAN/raw/source_code/swan/src/SwanTranspAc.ftn90
lines: 178
sha256: 2c08f03e8c7c49b91b36ef6a5d0b6532ccede949ec342b4c13573b8b9e04bf0d
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanTranspAc.ftn90 — 판독 구간 기록

구간은 1행부터 178행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–49 | SwanTranspAc 인수 목록(1–6). 기관·GPL 3 이상·무보증 머리말(8–32), 저자·2007–2009년 이력(35–44).파작용 평형식(action balance equation)의 수송(transport) 부분 계산 목적(46–48). |
| 50–79 | 시작 시 1행 SwanTranspAc 루틴 안. ocpcomm4·swcomm2·swcomm3·swcomm4·SwanGriddata 사용(52–56), implicit none(58). 입력 전체 방향·주파수 범위와 주파수별 방향·방향별 주파수 범위 선언(62–70). 이전·현재 파작용 밀도(action density) ac1/ac2(MDC,MSC,nverts), 출력 amat(MDC,MSC,5) 선언(72–74). 행렬(matrix)의 1번은 `(l  ,m  )` 중심이다(75). 2번과 3번은 각각 `(l-1,m  )`과 `(l+1,m  )` 주파수 인접점이다(76–77). 4번과 5번은 각각 `(l  ,m-1)`과 `(l  ,m+1)` 방향 인접점이다(78–79). [10-13 전수 검증 보완] |
| 80–112 | 시작 시 1행 루틴 안. 방향·주파수·x·y 수송 속도와 군속도(group velocity) cgo, 출력 누출 계수(leak coefficient) leakcf, 전달 기반 저감 계수 obredf, 반변 기저 벡터(contravariant base vector) rdx/rdy, 출력 우변(right-hand side) rhs 선언(80–89). spcdir의 6개 열은 방향(라디안)·cos·sin·cos²·cos×sin·sin²(90–95). spcsig, 출력용 명시적(explicit)·음해적(implicit) 수송 항 trac0/trac1, 입력 anybin, CFL 기준 역류 차단 여부 출력 anyblk 선언(96–101). `integer, save :: ient = 0 ! number of entries in this subroutine` (105), 구조·소스 주석·빈 줄. 기저 성분 주석은 `rdx(b) = a^(b)_1` (87)과 `rdy(b) = a^(b)_2` (88)이다. [10-13 전수 검증 보완] |
| 113–137 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwanTranspAc')` (113). 초기화 원문은 `amat = 0.` (117), `rhs  = 0.` (118), `leakcf = 0.` (122), `trac0  = 0.` (123), `trac1  = 0.` (124)이다. `!TIMG    call SWTSTA(140)` (128) 뒤 SwanTranspX 호출(129–131). `if ( WAVAGE > 0. ) call SwanGSECorr ( rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0 )` (135)이면 정원 스프링클러 효과(garden sprinkler effect, GSE) 보정 SwanGSECorr 호출. `!TIMG    call SWTSTO(140)` (136). 두 !TIMG 행은 -timg 시간 계측 스위치가 켜진 빌드에서 실행되는 행이다(switch.pl:22·84, $tim=TRUE). [10-13 전수 검증 보완] |
| 138–150 | 시작 시 1행 루틴 안. `!TIMG    call SWTSTA(142)` (140), `if ( IREFR /= 0 ) then` (141)일 때 STRSD 호출(143–146). amat의 4·1·5번 계수, DDIR·idcmin/idcmax·cad·rhs·ac2·isstop·anybin·leakcf·trac0/trac1을 전달하여 방향 공간 수송을 더한다. 분기 종료(148), `!TIMG    call SWTSTO(142)` (149). !TIMG 두 행은 -timg 시간 계측 스위치($tim=TRUE)에서 살아난다(switch.pl:22·84). [10-13 전수 검증 보완] |
| 151–164 | 시작 시 1행 루틴 안. `!TIMG    call SWTSTA(141)` (153)는 -timg 시간 계측 스위치($tim=TRUE) 행(switch.pl:22·84). `if ( (DYNDEP .OR. ICUR /= 0) .and. ITFRE /= 0 ) then` (154) 안의 `if ( int(PNUMS(8)) == 1 ) then` (156)이면 음해적 STRSSI 호출(160–163). spcsig·cas, amat의 2·1·3번 계수, anybin·rhs·ac2·방향별 주파수 범위·전체 방향 범위·trac0/trac1을 전달한다. |
| 165–178 | 시작 시 1행 루틴·154행 주파수 수송 분기 안이며 156행 음해적 분기와 병렬. `elseif ( int(PNUMS(8)) == 2 ) then` (165)이면 명시적 STRSSB 호출(169–171). 방향 범위·주파수별 방향 범위·isstop·cax/cay/cas·ac2·spcsig·rhs·anyblk·기저 벡터·trac0을 전달한다. 156–173행 방식 선택 사슬에는 ELSE가 없다. 내부 조건은 173행에서 닫힌다. 외부 조건은 175행에서 닫힌다. `!TIMG    call SWTSTO(141)` (176)는 -timg 시간 계측 스위치($tim=TRUE)에서 살아나는 행(switch.pl:22·84). 루틴 종료(178). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 101·117–124·169–171: anyblk는 intent(out)이다. 초기화 블록에는 anyblk 대입이 없다. 이 파일에서 anyblk를 호출 인수로 전달하는 실행문은 STRSSB 경로에만 있다.
- 154–175: 주파수 수송의 방식 선택은 int(PNUMS(8))=1과 =2만 처리한다. 다른 값에 대한 else 또는 오류 보고는 이 블록에 없다.
