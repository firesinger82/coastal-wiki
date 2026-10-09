---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/input_files/fort14.rst
lines: 78
sha256: 3f0ddc5afa20b250eb4740cc75c61545b1453d2fc73f31640967632e44338785
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort14.rst — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | Fort.14: Grid and Boundary Information File — 유한요소 격자(finite element grid), 수심 자료(bathymetric data)와 경계 정보의 필수 입력 파일이다(6). 원문: `The fort.14 file contains the finite element grid, the bathymetric data, and the boundary information used by ADCIRC. This file is required to run the ADCIRC model.` (6). |
| 8–22 | File Structure / 절점·요소 — 네 구간의 구성과 반복·조건부 입력 표기법을 설명한다(11). 격자 제목, 요소·절점 수, 절점 좌표·수심과 요소 연결 정보의 순서이다(13–22). 원문: `.. parsed-literal::` (13); ``    :ref:`AGRID <AGRID>` `` (15); ``    :ref:`NE <NE>`, :ref:`NP <NP>` `` (16); ``    for k=1 to :ref:`NP <NP>` `` (17); ``       :ref:`JN(k) <JN>`, :ref:`X(k) <X>`, :ref:`Y(k) <Y>`, :ref:`DP(k) <DP>` `` (18); `   end k loop` (19); ``    for k=1 to :ref:`NE <NE>` `` (20); ``       :ref:`JE(k) <JE>`, :ref:`NHY(k) <NHY>`, :ref:`NM(k,1) <NM>`, :ref:`NM(k,2) <NM>`, :ref:`NM(k,3) <NM>` `` (21); `   end k loop` (22). |
| 23–42 | File Structure / 개방·유량 경계 — 개방 경계(open boundary)의 수와 절점 목록 다음에 유량 경계(flow boundary)의 수·타입·절점 정보를 입력한다(23–41). IBTYPE 값별 육상 장벽·내부 장벽·관(pipe) 정보의 서로 다른 입력 줄을 원문으로 제시한다(36–39). 원문: ``    :ref:`NOPE <NOPE>` `` (23); ``    :ref:`NETA <NETA>` `` (24); ``    for k=1 to :ref:`NOPE <NOPE>` `` (25); ``       :ref:`NVDLL(k) <NVDLL>`, :ref:`IBTYPEE(k) <IBTYPEE>` `` (26); ``       for j=1 to :ref:`NVDLL(k) <NVDLL>` `` (27); ``          :ref:`NBDV(k,j) <NBDV>` `` (28); `      end j loop` (29); `   end k loop` (30); ``    :ref:`NBOU <NBOU>` `` (31); ``    :ref:`NVEL <NVEL>` `` (32); ``    for k=1 to :ref:`NBOU <NBOU>` `` (33); ``       :ref:`NVELL(k) <NVELL>`, :ref:`IBTYPE(k) <IBTYPE>` `` (34); ``       for j=1 to :ref:`NVELL(k) <NVELL>` `` (35); ``         :ref:`NBVV(k,j) <NBVV>`      if IBTYPE(k) = 0, 1, 2, 10, 11, 12, 20, 21, 22, 30`` (36); ``         :ref:`NBVV(k,j) <NBVV>`, :ref:`BARLANHT(k,j) <BARLANHT>`, :ref:`BARLANCFSP(k,j) <BARLANCFSP>`      if IBTYPE(k) = 3, 13, 23`` (37); ``         :ref:`NBVV(k,j) <NBVV>`, :ref:`IBCONN(k,j) <IBCONN>`, :ref:`BARINHT(k,j) <BARINHT>`, :ref:`BARINCFSB(k,j) <BARINCFSB>`, :ref:`BARINCFSP(k,j) <BARINCFSP>`      if IBTYPE(k) = 4, 24, 64`` (38); ``         :ref:`NBVV(k,j) <NBVV>`, :ref:`IBCONN(k,j) <IBCONN>`, :ref:`BARINHT(k,j) <BARINHT>`, :ref:`BARINCFSB(k,j) <BARINCFSB>`, :ref:`BARINCFSP(k,j) <BARINCFSP>`, :ref:`PIPEHT(k,j) <PIPEHT>`, :ref:`PIPECOEF(k,j) <PIPECOEF>`, :ref:`PIPEDIAM(k,j) <PIPEDIAM>`      if IBTYPE(k) = 5, 25`` (39); `      end j loop` (40); `   end k loop` (41). |
| 43–54 | Open Boundary Data / Normal Flux Boundary Types — 개방 경계와 법선 플럭스(normal flux) 경계 및 IBTYPE 상세 설명의 외부 문서 참조를 제시한다(46·52). |
| 55–78 | Example — 요소 3개·절점 4개·개방 경계와 유량 경계 없음의 예시를 소개한다(58). 입력 제목·좌표·수심·요소 연결·경계 수와 경계 절점 예시를 모두 원문으로 제시한다(60–78). 원문: `The following is a simple example of a fort.14 file for a small domain with 3 elements and 4 nodes with an open boundary and no flow boundaries:` (58); `.. code-block:: none` (60); `   Simple ADCIRC domain` (62); `   3 4    ! NE NP` (63); `   1 0.0 0.0 -10.0 ! JN X Y DP` (64); `   2 1.0 0.0 -10.0` (65); `   3 1.0 1.0 -10.0` (66); `   4 0.0 1.0 -10.0` (67); `   1 3 1 2 3 ! NE NHY NM(1,1) NM(1,2) NM(1,3)` (68); `   2 3 1 3 4` (69); `   3 3 2 3 1` (70); `   1 ! NOPE` (71); `   4 ! NETA` (72); `   4 0 ! NVDLL(1) IBTYPEE(1)` (73); `   1 1 2 ! NBDV(1,1)` (74); `   2 1 3 ! NBDV(1,2)` (75); `   3 2 3 ! NBDV(1,3)` (76); `   4 3 1 ! NBDV(1,4)` (77); `   0     ! NBOU` (78). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 28·74–77행: 형식 설명의 개방 경계 절점 입력은 `NBDV(k,j)` 한 항목이지만 예시의 해당 네 줄은 각각 `1 1 2`, `2 1 3`, `3 2 3`, `4 3 1`의 세 정수이다.
- 31–32·78행: 형식 설명은 `NBOU` 다음에 `NVEL`을 제시하지만 예시는 `0     ! NBOU`에서 끝난다.
- 21·68행: 요소 번호 필드는 형식 설명에서 `JE(k)`이지만 예시의 요소 첫 줄 주석은 `! NE NHY NM(1,1) NM(1,2) NM(1,3)`이다.
