---
file: models/SWAN/raw/source_code/swan/src/SwanReadEasymeshGrid.ftn90
lines: 155
sha256: 94b197b144260b8cac53ec37fabee37910b36103b1e5c9d2c54dd4f157312820
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanReadEasymeshGrid.ftn90 — 판독 구간 기록

구간은 1행부터 155행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | SwanReadEasymeshGrid를 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 신규 이력을 적는다(3–36). `<name>.n`의 정점 좌표와 `<name>.e`의 삼각형 정점을 읽는다는 목적·방법과 모듈 사용을 포함한다(40–52). |
| 54–75 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 파일명 길이 lenfnm과 기본 이름(base name) basenm 입력, 파일명·추적·입출력/할당 상태·루프·문자열·중단 변수를 선언한다(56–68). 구조·소스 구분 주석을 포함한다(70–75). 원문(행 순서): `integer, save     :: ient = 0 ! number of entries in this subroutine` (62). |
| 76–111 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 기본 이름에 '.n'을 붙여 FOR로 열고 중단을 확인한다(80–84). 첫 줄의 nverts를 읽고 xcugrd·ycugrd·vmark를 미할당일 때 순차 할당하며 실패를 처리한다(88–100). format 100으로 좌표와 경계 표지(boundary marker)를 순서대로 읽고 닫는다(104–110). format의 앞 6칸은 건너뛴다(152). 할당 실패 메시지 뒤에 `goto 900`을 실행한다(99). 두 read는 파일 끝에서 950으로 이동한다(88·105). 두 read는 판독 오류에서 910으로 이동한다(88·105). 원문(행 순서): `if (ltrace) call strace (ient,'SwanReadEasymeshGrid')` (76); `filenm = trim(basenm)//'.n'` (80); `ndsd   = 0` (81); `iostat = 0` (82); `call for (ndsd, filenm, 'OF', iostat)` (83); `if (stpnow()) goto 900` (84); `istat = 0` (89); `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (90); `if ( istat == 0 ) then` (91); `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (92); `if ( istat == 0 ) then` (94); `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (95); `if ( istat /= 0 ) then` (97); `call msgerr ( 4, 'Allocation problem in SwanReadEasymeshGrid: array xcugrd, ycugrd or vmark ' )` (98); `do j = 1, nverts` (104). [10-13 전수 검증 보완] |
| 112–142 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 기본 이름에 '.e'를 붙여 FOR로 열고 중단을 확인한다(114–118). ncells를 읽고 kvertc(3,ncells)를 할당하며 실패를 처리한다(122–127). format 200으로 셀별 세 정점과 문자 line을 읽고 닫는다(131–137). 0부터 시작하는 Easymesh 정점 번호를 1부터 시작하도록 전체 kvertc에 1을 더한다(139–141). 할당 실패 메시지 뒤에 `goto 900`을 실행한다(126). 두 read는 파일 끝에서 950으로 이동한다(122·132). 두 read는 판독 오류에서 910으로 이동한다(122·132). 원문(행 순서): `filenm = trim(basenm)//'.e'` (114); `ndsd   = 0` (115); `iostat = 0` (116); `call for (ndsd, filenm, 'OF', iostat)` (117); `if (stpnow()) goto 900` (118); `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (123); `if ( istat /= 0 ) then` (124); `call msgerr ( 4, 'Allocation problem in SwanReadEasymeshGrid: array kvertc ' )` (125); `do j = 1, ncells` (131); `kvertc = kvertc + 1` (141). [10-13 전수 검증 보완] |
| 143–155 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 레이블 900에서 반환한다(143). 판독 오류 910과 예상 밖 파일 끝 950에서 inquire로 현재 파일명을 얻고 msgerr 수준 4를 호출한다(145–150). 각 메시지 뒤에 `goto 900`을 실행한다(147·150). 입력 format는 `100 format((6x,2e22.15,i3))` (152), `200 format((5x,3i5,a))` (153)이다. 루틴 종료를 포함한다(155). 원문(행 순서): `call msgerr (4, 'error reading data from Easymesh file '//filenm )` (146); `call msgerr (4, 'unexpected end of file in Easymesh file '//filenm )` (149). [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 104–105·131–132·152–153: 정점 줄은 앞 6칸, 삼각형 줄은 앞 5칸을 건너뛰는 고정 format이다. 정점 식별 번호를 읽어서 j와 비교하는 검사는 이 루틴에 없다.
- 67·132: line은 삼각형 판독의 문자 항목으로 받는다. 이후 line 값을 사용하는 계산이나 검사는 없다.
- 84·97–100·110·118·124–127·137·143–150: close는 두 정상 판독 경로에 있다. 중단·할당 실패·판독 오류·예상 밖 파일 끝 경로는 레이블 900에서 반환하며 별도 close 문장이 없다. [10-13 전수 검증 보완]
