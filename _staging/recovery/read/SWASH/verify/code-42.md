# SWASH code-42 — 10-15 전수 검증

이 문서는 원문 대조 결과의 AI 요약이다.
대조 원문은 각 기록의 frontmatter `file:`에 지정된 파일이다.
각 구간의 원문을 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
각 명령의 원문 출력 범위는 200행 이하였다.
기록 하단의 코드 사실 항목도 해당 원문과 대조했다.

집계 단위는 구간 표의 한 행 또는 하단 코드 사실의 한 항목이다.
정정은 의미 수정이 포함된 행이다.
보완은 의미 수정 없이 누락만 추가한 행이다.
정정과 보완이 함께 있는 행은 정정으로 집계했다.
이상 없음은 대조 후 수정하지 않은 행이다.

| 기록 | 구간 행 수 | 코드 사실 항목 수 | 대조 대상 행 수 | 대조 원문 행 | 정정 | 보완 | 이상 없음 |
|---|---:|---:|---:|---|---:|---:|---:|
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md) | 94 | 13 | 107 | 1–3577 (3577행) | 6 | 72 | 29 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md) | 8 | 5 | 13 | 1–264 (264행) | 0 | 5 | 8 |
| 합계 | 102 | 18 | 120 | 3841행 | 6 | 77 | 37 |

정정·보완 목록의 원문 행은 해당 기록의 `file:`을 기준으로 한다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):176–223 | 작업 배열 초기값과 요청 플래그 대입을 산문으로만 적었다. | 보완: 0 초기값과 세 플래그의 참·거짓 대입을 원문으로 인용했다. | 188, 197–221 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):258–287 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식과 반복문을 인용했다. 블록 종료 행을 명시했다. | 226, 228, 410–412 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):288–349 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식과 반복문을 인용했다. 블록 종료 행을 명시했다. | 226, 228, 288, 410–412 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):350–400 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식과 반복문을 인용했다. 블록 종료 행을 명시했다. | 226, 228, 288, 410–412 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):401–413 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식과 반복문을 인용했다. 블록 종료 행을 명시했다. | 226, 228, 350, 380–412 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):414–462 | 건조 지점의 수직 속도 기본값을 산문으로만 적었다. 이웃 인덱스나 경계 복사 인덱스를 원문 대입식으로 인용하지 않았다. | 보완: wphy의 0 대입을 인용했다. 원문의 인덱스 이동을 포함한 대입식을 인용했다. | 452–454; 425, 461 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):463–519 | 바깥 조건식과 건조 지점의 0 대입 인용을 생략했다. 이웃 인덱스나 경계 복사 인덱스를 원문 대입식으로 인용하지 않았다. | 보완: 바깥 조건식·종료 행과 wphy의 0 대입을 인용했다. 원문의 인덱스 이동을 포함한 대입식을 인용했다. | 416–420, 463, 515–517, 551, 706–708; 470–471 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):520–552 | 바깥 조건과 반복문을 이름으로만 적었다. 이웃 인덱스나 경계 복사 인덱스를 원문 대입식으로 인용하지 않았다. | 보완: 바깥 조건식·반복문과 각각의 종료 행을 인용했다. 원문의 인덱스 이동을 포함한 대입식을 인용했다. | 416–420, 463–467, 521–551, 706–708; 526, 541 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):553–607 | 바깥 조건식과 누적 초기값 인용을 생략했다. 방향 조건의 else 부재를 생략했다. | 보완: 바깥 조건식·종료 행과 초기값을 인용했다. 방향 조건의 else 부재를 명시했다. | 416, 418, 553–567, 589–593, 706–708 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):608–655 | 바깥 조건식과 누적 초기값 인용을 생략했다. 방향 조건의 else 부재를 생략했다. | 보완: 바깥 조건식·종료 행과 초기값을 인용했다. 방향 조건의 else 부재를 명시했다. | 416, 418, 553–561, 608–640, 702–708 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):656–709 | 바깥 조건식과 0 대입 인용을 생략했다. 방향 조건의 else 부재를 생략했다. | 보완: 바깥 조건식·종료 행과 0 대입을 인용했다. 방향 조건의 else 부재를 명시했다. | 416, 418, 553–561, 657–708 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):763–800 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 763–800, 712–718, 842, 970–974, 1798, 2230 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):801–840 | 바깥 조건식과 종료 행을 생략했다. ihydro 분기 사슬의 else 부재를 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. ihydro 분기 사슬의 else 부재를 명시했다. | 801–840, 712–718, 842, 970–974, 1798, 2230 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):841–892 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 841–892, 712–718, 842, 970–974, 1798, 2230 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):893–940 | 바깥 조건식과 종료 행을 생략했다. ihydro 분기 사슬의 else 부재를 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. ihydro 분기 사슬의 else 부재를 명시했다. | 893–940, 712–718, 842, 970–974, 1798, 2230 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):941–974 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식·반복문과 각각의 종료 행을 인용했다. | 712–2230, 714–1798, 716–974, 848–972, 923–970 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):975–997 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식·반복문과 각각의 종료 행을 인용했다. | 712–2230, 714–1798 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):998–1062 | 바깥 블록을 조건식 없이 이름으로만 적었다. 이웃 인덱스나 경계 복사 인덱스를 원문 대입식으로 인용하지 않았다. | 보완: 바깥 조건식·반복문과 각각의 종료 행을 인용했다. 원문의 인덱스 이동을 포함한 대입식을 인용했다. | 712–2230, 714–1798; 1019, 1040 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1063–1076 | 바깥 블록을 조건식 없이 이름으로만 적었다. | 보완: 바깥 조건식·반복문과 각각의 종료 행을 인용했다. | 712–2230, 714–1798, 1002–1154, 1004–1152, 1005–1151 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1077–1123 | 바깥 조건식과 종료 행을 생략했다. 이웃 인덱스나 경계 복사 인덱스를 원문 대입식으로 인용하지 않았다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 원문의 인덱스 이동을 포함한 대입식을 인용했다. | 712–2230, 714–1798, 1002–1154, 1004–1152, 1005–1151; 1080, 1101 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1124–1155 | 바깥 조건식과 종료 행을 생략했다. 와도 주석의 인덱스 순열을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 와도 주석의 인덱스 순열을 인용했다. | 712–2230, 714–1798, 1002–1154, 1004–1152, 1005–1151, 1138 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1156–1200 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1201–1220 | 바깥 조건식과 종료 행을 생략했다.마찰 속도 성분의 0 대입을 인용하지 않았다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 마찰 속도 성분의 0 대입을 인용했다. | 712–2230, 714–1798, 1156–1796, 1186–1219, 1188–1217, 1189–1216, 1211–1213 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1221–1261 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1262–1306 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1307–1360 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1361–1394 | 바깥 조건식과 종료 행을 생략했다. ihydro 분기 사슬의 else 부재를 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. ihydro 분기 사슬의 else 부재를 명시했다. | 712–2230, 714–1798, 1156–1796, 1381–1394 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1395–1428 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796, 1363–1427, 1365–1425, 1366–1424 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1429–1482 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1483–1534 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796, 1431–1533 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1535–1600 | 바깥 조건식과 종료 행을 생략했다. 마찰 속도 성분의 0 대입을 인용하지 않았다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 마찰 속도 성분의 0 대입을 인용했다. | 712–2230, 714–1798, 1156–1796, 1587–1589 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1601–1633 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796, 1599–1632 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1634–1670 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1671–1716 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1717–1747 | 바깥 조건식과 종료 행을 생략했다. ihydro 분기 사슬의 else 부재를 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. ihydro 분기 사슬의 else 부재를 명시했다. | 712–2230, 714–1798, 1156–1796, 1733–1746 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1748–1780 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796, 1719–1779, 1721–1777, 1722–1776 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1781–1809 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 714–1798, 1156–1796 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1810–1871 | 바깥 조건식과 종료 행을 생략했다. 면적·마찰 누적 초기값을 산문으로만 적었다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 면적·마찰 누적 초기값을 인용했다. | 712–2230, 1814–1818 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1872–1926 | 바깥 조건식과 종료 행을 생략했다. ihydro 분기 사슬의 else 부재를 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. ihydro 분기 사슬의 else 부재를 명시했다. | 712–2230, 1810–1996, 1812–1994, 1820–1925, 1878–1887 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1927–1970 | 바깥 조건식과 종료 행을 생략했다. 마찰 속도 성분의 0 대입을 인용하지 않았다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. 마찰 속도 성분의 0 대입을 인용했다. | 712–2230, 1810–1996, 1812–1994, 1944–1946 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):1971–2000 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 712–2230, 1810–1996, 1812–1994 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2001–2061 | 바깥 조건식과 종료 행을 생략했다. 작업 속도와 면적 누적의 0 초기값 인용을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. uwrk와 totarea의 0 초기값을 인용했다. | 712–2230, 1998–2156, 2008, 2036 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2062–2093 | 바깥 조건식과 종료 행을 생략했다. 면적 누적의 초기값 인용을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. totarea의 0 초기값을 인용했다. | 712–2230, 1998–2156, 2070 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2094–2157 | 바깥 조건식과 종료 행을 생략했다. 작업 속도와 면적 누적의 0 초기값 인용을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. uwrk와 totarea의 0 초기값을 인용했다. | 712–2230, 1998–2156, 2104, 2132 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2158–2193 | 바깥 조건식과 종료 행을 생략했다. 면적 누적의 초기값 인용을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. totarea의 0 초기값을 인용했다. | 712–2230, 2168 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2194–2231 | 바깥 조건식과 종료 행을 생략했다. 면적 누적의 초기값을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. totarea의 0 초기값을 인용했다. | 712–2230, 2158–2228, 2204 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2232–2288 | 수면 경계 대입을 인용하지 않았다. 층 방향과 ihydro 분기 사슬의 else 부재를 구간 행에서 생략했다. | 보완: 수면 경계 대입을 인용했다. 층 경계·두께 식에 근거해 층 방향을 명시했다. ihydro=3의 대입 부재를 명시했다. | 2232–2243, 2269–2285 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2289–2334 | rhos를 곱하는 출력을 밀도 변환으로 단정했다. | 정정: 원문 주석의 부유 퇴적물 계산으로 고쳤다. rhos를 곱하는 대입 사실만 명시했다. | 2309–2331 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2335–2373 | 꼭짓점 인덱스 대입과 거리 초기값을 인용하지 않았다. | 보완: kvert 대입과 rdist의 0 초기값을 인용했다. | 2346, 2361 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2374–2400 | active의 참 대입을 산문으로만 적었다. 다음 구간으로 이어지는 조건의 종료 행을 생략했다. | 보완: active 대입과 바닥 높이 보간 조건의 종료 행을 인용했다. | 2387–2398, 2402–2403 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2401–2414 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 2387–2403, 2388–2402 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2415–2445 | 속력 분기의 두 번째 성분 위치 계산을 같은 성분 위치라고 축약했다. | 보완: 속력 분기의 jvy 계산을 인용했다. | 2439 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2446–2486 | 속도 방향과 격자 v의 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 대상 인덱스와 값을 인용했다. | 2468, 2483 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2487–2510 | 정수압 경로의 비정수압 출력 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 대상 인덱스와 값을 인용했다. | 2496–2497 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2542–2582 | 유량 방향과 격자 v 유량의 예외값 대입을 인용하지 않았다. | 보완: 두 예외값 대입의 대상 인덱스와 값을 인용했다. | 2563–2564, 2578–2579 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2613–2652 | active를 참으로 바꾸는 대입을 산문으로만 적었다. | 보완: 두 출력 경로의 active 대입을 인용했다. | 2626, 2646 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2683–2719 | 바람 보간에서 active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 2700 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2720–2757 | 풍향 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 대상 인덱스와 값을 인용했다. | 2752–2753 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2758–2784 | active의 참 대입을 인용하지 않았다. 일정 마찰 계수의 예외값 경로를 구간 행에서 생략했다. | 보완: active 대입을 인용했다. 예외값과 같은 계수에는 대입이 없음을 명시했다. | 2772, 2778–2780 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2801–2816 | 바깥 조건식과 종료 행을 생략했다. | 보완: 바깥 조건식·반복문과 종료 행을 인용했다. | 2787–2803, 2797–2802 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2817–2848 | 평균 속도 성분의 크기를 시간 평균 속력으로 적었다. | 정정: 시간 평균 속도 벡터의 크기로 고쳤다. 평균 성분에서 크기를 구하는 순서를 명시했다. | 2817–2845 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2849–2888 | 평균 속도 방향과 격자 v의 예외값 대입을 인용하지 않았다. 평균 속도 성분에서 얻는 방향을 시간 평균 방향으로 적었다. | 정정: 두 예외값 대입의 대상 인덱스와 값을 인용했다. 시간 평균 속도 벡터의 방향으로 고쳤다. | 2869–2870, 2884–2885; 2817–2833, 2851–2867 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2929–2948 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 2942 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):2949–2972 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 2964 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3001–3050 | 난류 계산을 사용하지 않는 경로의 예외값 대입을 인용하지 않았다. | 보완: 두 예외값 대입의 전체 지점·수직 인덱스와 값을 인용했다. | 3015, 3033 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3051–3100 | 난류 계산을 사용하지 않는 경로의 예외값 대입을 인용하지 않았다. | 보완: 두 예외값 대입의 전체 지점·수직 인덱스와 값을 인용했다. | 3065, 3083 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3101–3124 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 3116 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3165–3200 | 층별 방향의 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 지점·층 인덱스와 값을 인용했다. | 3187 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3201–3212 | 층별 격자 v의 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 전체 지점·수직 인덱스와 값을 인용했다. | 3209 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3253–3288 | 층별 방향의 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 지점·층 인덱스와 값을 인용했다. | 3275 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3289–3332 | 층별 격자 v 유량과 비정수압의 예외값 대입을 인용하지 않았다. | 보완: 두 예외값 대입의 전체 지점·수직 인덱스와 값을 인용했다. | 3297, 3315 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3333–3372 | 층별 평균 속도 성분의 크기를 시간 평균 속력으로 적었다. | 정정: 층별 시간 평균 속도 벡터의 크기로 고쳤다. | 3333–3368 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3373–3400 | 층별 평균 속도 성분의 방향을 시간 평균 방향으로 적었다. 층별 평균 속도 방향의 예외값 대입을 인용하지 않았다. | 정정: 층별 시간 평균 속도 벡터의 방향으로 고쳤다. 예외값 대입의 지점·층 인덱스와 값을 인용했다. | 3333–3354, 3373–3392; 3395 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3401–3420 | 층별 평균 격자 v의 예외값 대입을 인용하지 않았다. | 보완: 예외값 대입의 전체 지점·수직 인덱스와 값을 인용했다. | 3417 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3421–3444 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 3436 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3445–3468 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 3460 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):3469–3492 | active의 참 대입을 산문으로만 적었다. | 보완: active 대입을 인용했다. | 3484 |
| [SwashQuanOutp.ftn90.md](../swash/src/SwashQuanOutp.ftn90.md):코드 사실 7 (2267–2287·3321–3331) | 전체 압력 보간 분기는 oqproc(83)만 검사한다고 적었다. | 정정: 요청 조건과 optg에 따른 보간 경로 조건을 구분했다. ihydro 재검사가 없다는 사실을 명시했다. | 2267–2287, 3321–3331 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md):89–119 | 경계값 열 복사만 기록하고 이전 판독 시간 갱신을 생략했다. | 보완: timf1 갱신과 시간 조건·반복문의 종료 행을 인용했다. | 102, 106, 110, 243–245 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md):120–145 | 바깥 블록의 조건식을 생략했다. 경계값별 머리말의 오류 이동을 생략했다. | 보완: 바깥 조건식과 종료 행을 명시했다. 140행의 EOF·오류 이동을 인용했다. | 102, 106, 133–142, 167, 243–245 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md):146–174 | 바깥 조건식을 이름으로만 기록했다. 판독의 EOF 이동과 else 부재를 구간 행에서 생략했다. | 보완: 바깥 조건식·종료 행과 EOF 이동을 명시했다. binfo 조건의 else 부재를 명시했다. | 102, 106, 133, 146–167, 243–245 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md):175–217 | 바깥 조건식과 종료 행을 생략했다. EOF 상태 대입의 원문 표기를 축약했다. | 보완: 바깥 조건식·종료 행과 EOF 상태 기본값의 원문 인용을 보완했다. | 102, 106, 181–215, 243–245 |
| [SwashReadBndval.ftn90.md](../swash/src/SwashReadBndval.ftn90.md):218–245 | 바깥 시간 조건식을 생략했다. 동일 판독 시간의 가중치 기본값을 산문으로만 적었다. | 보완: 바깥 시간 조건식을 인용했다. wf1의 기본값 대입을 인용했다. | 102, 106, 218–245 |

SwashQuanOutp.ftn90.md의 이상 없음 구간은 `1–60`, `61–109`, `110–175`, `224–257`, `710–762`, `2511–2541`, `2583–2612`, `2653–2682`, `2785–2800`, `2889–2928`, `2973–3000`, `3125–3164`, `3213–3252`, `3493–3534`, `3535–3543`, `3544–3572`, `3573–3577`이다.
SwashQuanOutp.ftn90.md의 하단 코드 사실 중 1–6번과 8–13번은 이상이 없었다.
SwashReadBndval.ftn90.md의 이상 없음 구간은 `1–49`, `50–88`, `246–264`이다.
SwashReadBndval.ftn90.md의 하단 코드 사실 1–5번은 이상이 없었다.

두 기록의 frontmatter를 유지했다.
두 기록의 구간 경계를 유지했다.
두 원문의 SHA-256은 기록의 기존 값과 일치했다.
조건식과 산술식·기본값 대입의 인용 누락을 추가 점검했다.
인용문에 붙은 원문 행 번호도 추가 점검했다.

`switch.pl` 57–66행의 표시 제거 규칙을 대조했다.
두 원문에는 해당 전처리 표시로 시작하는 행이 없다.
SwashQuanOutp의 층 방향은 2232행의 층 경계·층 두께 주석과 2236–2243행의 식으로 확인했다.
그 식에서 경계 0은 수면이다.
경계 kmax는 바닥이다.
층 1은 최상층이다.
SwashReadBndval의 57행 주석은 두 번째 배열 차원을 두 시간 수준으로 설명한다.
이 파일에는 수직 층 방향을 판정할 계산이 없다.

모델은 실행하지 않았다.
원문·노트·git은 수정하지 않았다.

정정 6, 보완 77, 이상 없음 37
