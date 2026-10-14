# SWASH 전수 검증 — code-52

검증일은 2026-10-15이다. 대상은 아래 세 판독 기록이다.
각 구간의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다. 한 번에 연 원문 구간은 모두 200행 이하였다.
원문 행 번호는 각 기록 frontmatter의 `file:`에 적힌 파일을 기준으로 한다.

| 기록 | 대조 원문 행 수 | 구간 기록 행 수 | 후속 사실 행 수 | 총 대조 기록 행 수 | 정정 | 보완 | 두 표지 모두 | 이상 없음 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md) | 995 | 25 | 6 | 31 | 1 | 23 | 0 | 7 |
| [m_parall.ftn.md](../swash/src/m_parall.ftn.md) | 199 | 6 | 2 | 8 | 0 | 1 | 0 | 7 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md) | 2613 | 55 | 14 | 69 | 2 | 38 | 2 | 31 |
| 합계 | 3807 | 86 | 22 | 108 | 3 | 62 | 2 | 45 |

행 수는 각 기록의 구간 표와 후속 사실 목록에서 셌다. 정정과 보완은 해당 수정 표지가 붙은 행을 각각 센 값이다. 두 표지가 함께 붙은 행은 두 항목에 각각 포함했다. 이상 없음은 두 수정 표지가 모두 없는 대조 행 수다.

`m_parall.ftn` 196–199행의 `!MPI!/impi` 설명을 `swash/switch.pl` 57–66행과 대조했다. 해당 설명은 두 스위치가 모두 적용되어야 코드가 활성화되는 규칙과 일치했다. 나머지 두 원문에는 해당 전처리 표시 행이 없다.
배열 층 방향을 설명하는 대상 문장은 없었다.
세 기록의 구간 경계와 frontmatter는 변경하지 않았다. 세 원문의 SHA-256은 각 frontmatter 값과 일치했다.
모델은 실행하지 않았다. 원문·노트·git에 쓰기 작업을 하지 않았다.

정정·보완 내역은 다음과 같다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):101–127 (보완) | 마찰 속도비라는 요약만 있었다. | s와 sold의 u/ustar 비 및 utl의 u10/uref 비를 원문 주석으로 명시했다. | 110–113 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):128–163 (보완) | alpha·wcrstp·windu 대입을 값이나 말로만 요약했다. 바깥 oned 조건의 종료 행이 생략되었다. | 매개변수 선택과 풍속 대입을 원문 식으로 인용했다. 종료 행 374를 명시했다. | 130–131, 144, 154, 160, 374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):164–188 (보완) | 바깥 oned 분기의 조건식 인용이 없었다. 바깥 oned 조건의 종료 행이 생략되었다. | 바깥 if 조건식을 원문으로 명시했다. 종료 행 374를 명시했다. | 144, 374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):189–244 (보완) | 바깥 차원 조건과 직접 풍속 대입의 원문 인용이 없었다. 바깥 oned 조건의 종료 행이 생략되었다. | 바깥 oned 조건과 windu 대입을 명시했다. 종료 행 374를 명시했다. | 144, 189, 201, 374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):245–298 (보완) | 바깥 차원 조건과 windv 대입의 원문 인용이 없었다. | oned의 거짓 분기 및 종료 행을 명시하고 windv 대입을 인용했다. | 144, 189, 255, 374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):299–334 (보완) | 바깥 차원 조건식이 생략되었다. | 바깥 oned 조건식과 종료 행을 명시했다. | 144, 189, 374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):335–375 (보완) | 바깥 oned·relwav 조건식과 각 종료 행의 대응이 생략되었다. | 원문 조건식을 명시하고 루프 및 relwav의 종료 행을 구분했다. | 144, 301, 363–374 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):376–400 (보완) | 상수 항력계수 대입의 원문 인용이 없었다. 항력 선택 사슬 및 oned 조건의 종료 행이 생략되었다. | cd=pwnd(1) 대입을 원문으로 인용했다. 종료 행 520과 951을 명시했다. | 378, 380, 384, 520, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):401–453 (보완) | 바깥 조건식, 반복 초기값 및 오류 호출의 원문 인용이 생략되었다. 항력 선택 사슬 및 oned 조건의 종료 행이 생략되었다. | 바깥 조건식·루프, nit·sold 대입, MSGERR 호출 및 반복 종료 행을 명시했다. 종료 행 520과 951을 명시했다. | 378, 380, 387, 423, 428, 436, 440–445, 520, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):454–484 (보완) | 바깥 oned 및 항력 공식 선택 조건식이 생략되었다. 항력 선택 사슬 및 oned 조건의 종료 행이 생략되었다. | 바깥 조건식과 ELSE IF 사슬임을 명시했다. 종료 행 520과 951을 명시했다. | 378, 380, 454, 520, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):485–521 (보완) | 바깥 조건식과 오류 메시지 원문이 생략되었다. | 바깥 조건식·종료 행과 오류 호출 뒤 반환 순서를 원문으로 명시했다. | 378, 380, 517–520, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):522–568 (보완) | 바깥 조건식 및 cd·rwx 대입의 원문 인용이 생략되었다. | oned 조건식·종료 행과 cd·rwx 대입을 명시했다. | 378, 522, 528, 556, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):569–606 (보완) | 바깥 조건식과 rwy 대입의 원문 인용이 생략되었다. | 바깥 조건식·종료 행과 rwy 대입을 명시했다. | 378, 524, 595, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):607–640 (보완) | 바깥 조건식과 rwx 대입의 원문 인용이 생략되었다. | 바깥 조건식·종료 행과 rwx 대입을 명시했다. | 378, 524, 636, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):641–675 (보완) | 바깥 조건식, 반복 초기값 및 오류 호출의 원문 인용이 생략되었다. | 조건식·루프·종료 행, nit·sold 대입 및 MSGERR 호출을 명시했다. | 378, 607, 611–613, 643–674, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):676–740 (보완) | 바깥 조건식, rwy·반복 초기값 및 오류 호출의 원문 인용이 생략되었다. | 바깥 조건식·종료 행, rwy·nit·sold 대입 및 MSGERR 호출을 명시했다. | 378, 607, 702–730, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):741–796 (보완) | 바깥 조건식과 rwx 대입의 원문 인용이 생략되었다. | 바깥 조건식·종료 행과 rwx 대입을 명시했다. | 378, 524, 775, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):797–800 (보완) | 바깥 조건식과 루프 종료 위치가 생략되었다. | 조건식·루프의 원문과 종료 행을 명시했다. | 378, 741, 797–799, 845–847, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):801–848 (보완) | 바깥 조건식과 rwy 대입의 원문 인용이 생략되었다. | 조건식·루프·종료 행과 rwy 대입을 명시했다. | 378, 741, 797–799, 828, 845–847, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):849–895 (보완) | 바깥 조건식과 rwx 대입의 원문 인용이 생략되었다. | 바깥 조건식·종료 행과 rwx 대입을 명시했다. | 378, 524, 878, 944, 951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):896–952 (보완) | 바깥 조건식, rwy 대입 및 오류 메시지의 원문 인용이 생략되었다. | 바깥 조건식·rwy 대입과 오류 호출 뒤 반환 순서를 명시했다. | 378, 849, 922, 939–951 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):953–975 (보완) | 건조 지점 계수의 0 대입을 말로만 적었다. | cwndu(1)의 0 대입을 원문으로 인용했다. | 955 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):976–995 (보완) | 마루 조건에서 windu의 0 대입을 말로만 적었다. | windu(i)의 0 대입을 원문으로 인용했다. | 986 |
| [SwashWindStress.ftn90.md](../swash/src/SwashWindStress.ftn90.md):후속 사실 166–187 (정정) | 비활성 이웃 인덱스를 자기 인덱스로 바꾼다고 요약했다. | nmu·ndm은 nm로 바꾸고 ndmu는 그 시점의 ndm으로 바꾸는 순서를 명시했다. | 545–547, 625–627 |
| [m_parall.ftn.md](../swash/src/m_parall.ftn.md):91–125 (보완) | KPART=-1의 자동 선택 기준이 생략되었다. | KPART=-1은 계산 모드를 기준으로 자동 선택한다는 원문 주석을 인용했다. | 121 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):100–108 (보완) | IENT·KAR·ELTYPE·BLANK 초기값을 말로만 적었다. | 각 초기값을 원문 DATA 및 대입식으로 인용했다. | 100–106 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):109–191 (보완) | 변경 이력의 LINELN=120 값이 생략되었다. | 해당 변경 주석의 120 값을 인용했다. | 159 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):192–216 (정정) | 반환하지 않은 경우 모두 줄 재설정을 수행하는 듯한 설명이었다. | EOF의 90번 분기와 50번 반환 분기를 모두 제외한 경로임을 명시했다. | 196–210 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):192–216 (보완) | IENT 및 줄 판독 상태 초기값의 원문 인용이 생략되었다. | DATA 초기값과 KARNR·KAR·ELTYPE 대입을 인용했다. | 193, 207–210 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):304–327 (보완) | IENT와 기본 키워드 대입의 원문 인용이 생략되었다. | 초기값과 문자열 길이에 따른 KEYWRD 대입식을 인용했다. | 305, 320–325 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):328–363 (보완) | 기본값 분기 조건식·종료 행과 키워드 대입 및 오류 메시지 원문이 생략되었다. | 닫힌 바깥 조건, STOP·공백 대입, 오류별 메시지 및 ELSE 없는 IF 블록들을 명시했다. | 318–358 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):470–486 (보완) | IENT 기본값의 원문 인용이 생략되었다. | DATA IENT /0/를 인용했다. | 471 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):596–628 (보완) | 초기값 및 R·ELTYPE 대입의 원문 인용이 생략되었다. | DATA·CHGVAL·NAAM_L·R·ELTYPE 대입과 ELSE 없는 독립 IF의 종료 행을 명시했다. | 597, 602–628 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):629–650 (보완) | USED 대입과 오류 메시지·출력 명령의 원문 인용이 생략되었다. | 상태 대입, 자료형 오류 보고·출력·기본값 이동 순서 및 IF 종료 행을 명시했다. | 629–650 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):651–680 (보완) | 닫힌 조건식, 오류 메시지·USED 대입 및 ELSE 없는 분기 구조가 생략되었다. | 오류 보고·항목 출력·USED 대입 후 기본값으로 진행하는 순서와 조건 구조를 명시했다. | 642, 650–677 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):787–800 (보완) | IENT·CHGVAL 초기값과 NAAM_L 대입의 원문 인용이 생략되었다. | 초기값·대입식과 ELSE 없는 자료형 분기를 명시했다. | 788, 791–800 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):801–840 (보완) | IV·ELTYPE 대입 및 오류 메시지 원문과 ELSE 없는 분기 구조가 생략되었다. | 각 대입, 오류 보고·항목 출력·기본값 이동 순서 및 분기 구조를 명시했다. | 801–836 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):946–977 (보완) | 초기값, C·ELTYPE 대입 및 문자열 길이 오류 메시지의 원문 인용이 생략되었다. | 각 대입과 오류 메시지, 내부·외부 IF의 종료 위치를 명시했다. | 947–977 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):978–1008 (보완) | 닫힌 CHAR 조건식, USED 대입 및 상태 오류 메시지의 원문 인용이 생략되었다. | 조건의 종료 위치, 상태 대입·오류 호출·출력문 및 ELSE 없는 KONT 분기를 명시했다. | 965, 977–1007 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1009–1034 (보완) | 오류 메시지, USED 및 LENCST 대입의 원문 인용이 생략되었다. | 각 오류 보고·출력·대입의 순서와 LENCST 결정식을 명시했다. | 1010–1030 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1152–1178 (보완) | 초기값 및 USED 대입의 원문 인용과 IF 종료 행이 생략되었다. | DATA·CHGVAL·NAAM_L·ELTYPE 대입과 독립 IF의 종료 행을 명시했다. | 1153–1178 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1179–1200 (보완) | 상태 대입과 오류 메시지·출력문의 원문 인용이 생략되었다. | 시간 판독 조건의 종료 위치, 상태 대입 및 오류 처리 순서를 명시했다. | 1178–1195 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1201–1227 (보완) | 오류 메시지와 USED 대입의 원문 인용 및 ELSE 없는 분기 구조가 생략되었다. | 오류별 보고·출력·상태 대입·기본값 이동 순서와 KONT 분기 구조를 명시했다. | 1199–1223 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1228–1346 (보완) | 구조 주석의 조건과 단위별 계수·환산식이 요약만 되어 있었다. | 주석의 조건과 DAY·HR·MI·SEC·ELSE 계수 및 초 환산식을 원문으로 인용했다. | 1333–1342 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1347–1370 (보완) | IENT 기본값의 원문 인용이 생략되었다. | DATA IENT /0/를 인용했다. | 1348 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1401–1488 (보완) | 구조 주석의 조건과 단위별 계수·환산식이 요약만 되어 있었다. | 주석의 조건과 DAY·HR·MI·SEC·ELSE 계수 및 초 환산식을 원문으로 인용했다. | 1475–1484 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1489–1512 (보완) | IENT 기본값의 원문 인용이 생략되었다. | DATA IENT /0/를 인용했다. | 1490 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1601–1635 (정정) | NUM1을 정수 가수라고 요약했다. | NUM1이 가수의 정수 부분 값임을 명시했다. | 1606 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1601–1635 (보완) | QUOTE·IENT·NREP의 DATA 기본값을 말로만 적었다. | 작은따옴표 표기를 포함한 DATA 문을 원문으로 인용했다. | 1633 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1636–1664 (보완) | 새 항목의 초기값과 ELTEXT 구간 대입식 및 EOR 대입의 원문 인용이 생략되었다. | NREP·JKAR·ELINT·ELREAL·ELTYPE 대입과 J:J+3 공백 대입식을 명시했다. | 1643–1661 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1665–1700 (보완) | 이전 조건의 종료 행과 STOP·EMPT·EOR 대입의 원문 인용이 생략되었다. | 닫힌 조건식과 각 상태 대입·호출·반환 경로를 명시했다. | 1655, 1664–1689 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1701–1736 (보완) | 숫자 문법·상태 대응 주석과 초기값 대입의 원문 인용이 생략되었다. | 숫자 문법, ISTATE 대응, 초기값 및 상태 변경식을 인용했다. | 1694, 1700–1736 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1737–1766 (보완) | 소수부 지수의 기본값과 판독 상태 대입의 원문 인용이 생략되었다. | JJ·IRK·ISTATE의 초기값 및 상태 변경식을 인용했다. | 1737–1762 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1767–1805 (보완) | 상태·반복 계수 대입과 오류 메시지의 원문 인용이 생략되었다. | ISTATE·NREP·ELINT 대입과 반복 계수 오류 처리 및 중첩 IF 종료 행을 명시했다. | 1770, 1780–1795 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1806–1834 (보완) | 문자열 판독 초기값과 문자·길이 대입의 원문 인용이 생략되었다. | ELTYPE·LENCST·JJ 초기값, ELTEXT 구간 대입 및 문자열 조건 종료 행을 명시했다. | 1810–1834 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1835–1863 (보완) | 이전 조건의 종료 위치와 키워드 초기값·문자 구간 대입의 원문 인용이 생략되었다. | 닫힌 조건과 ELTYPE·ISTATE·JJ·ELTEXT·LENCST·KEYWRD 대입을 명시했다. | 1809, 1834, 1842–1863 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1864–1893 (보완) | 이전 조건의 종료 위치와 줄 연결·OTHR 상태 및 문자 대입의 원문 인용이 생략되었다. | 닫힌 키워드 조건과 KARNR·ELTYPE·ELTEXT·LENCST 대입을 명시했다. | 1840, 1863, 1869–1876 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):1976–2000 (보완) | IENT·KARNR·KAR·ELTYPE 초기값과 문자 추출 대입의 원문 인용이 생략되었다. | DATA와 새 줄·줄 끝·문자 추출·EOF 경로의 대입식을 인용했다. | 1977–1995 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2090–2099 (보완) | IENT 초기값과 LTEXT·LENCST 대입의 원문 인용이 생략되었다. | DATA 및 문자 구간·길이 대입식을 인용했다. | 2091, 2094–2095 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2191–2205 (보완) | IENT·대소문자 표 초기값 및 CC 대입의 원문 인용이 생략되었다. | DATA 초기값과 문자 추출 대입을 인용했다. | 2192–2199 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2206–2295 (보완) | IENT 초기값 선언의 원문 인용이 생략되었다. | SAVE와 0 초기값을 포함한 선언을 인용했다. | 2274 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2296–2315 (보완) | EQCSTR 기본값·거짓 대입과 CC1·CC2 문자 추출식의 원문 인용이 생략되었다. | 논리값 대입 및 문자 추출 대입과 반환 분기 종료 행을 명시했다. | 2298–2312 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2401–2427 (보완) | IENT·KEYWIS 기본값과 문자 추출·논리값 대입의 원문 인용이 생략되었다. | DATA와 KEYWIS·KAR1·KAR2 대입 및 불일치 분기의 반환 경로를 명시했다. | 2409–2423 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2507–2514 (보완) | IENT 기본값과 USED 대입의 원문 인용이 생략되었다. | DATA와 ELTYPE 대입을 원문으로 인용했다. | 2508, 2512 |
| [ocpcre.ftn.md](../swash/src/ocpcre.ftn.md):2603–2613 (보완) | IENT 기본값의 원문 인용이 생략되었다. | DATA IENT /0/를 인용했다. | 2604 |

정정 3, 보완 62, 이상 없음 45
