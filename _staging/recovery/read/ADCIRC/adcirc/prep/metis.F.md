---
file: models/ADCIRC/raw/source_code/adcirc/prep/metis.F
lines: 601
sha256: 15184593c0ddc43aed4c15ed993297605f7ea4bfd974f46e947ebd3ffed9d6c7
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# metis.F — 판독 구간 기록

구간은 1행부터 601행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | ADCIRC 저작권·LGPL 3 이상·무보증 머리말(1–19). `MODULE METIS_PARTITION`·PRE_GLOBAL·IMPLICIT NONE·CONTAINS 및 빈 줄(20–27). |
| 28–67 | 시작 시 20행 모듈 안. `METIS()` 선언 및 PRE_GLOBAL·MEMORY_USAGE의 memory_usage_string 사용(28–31). METIS 4.0 그래프 분할(graph partitioning) 인터페이스·인접 관계 대칭 검사 이력 주석(32–39). 변수·옵션·메모리 크기·할당 배열 및 외부 루틴 선언(40–61). ITVECT/ITVECT2/NUMDUALS/VWGTS/NEDGES/NEDLOC는 MNP, XADJ는 MNP+1 크기로 할당한다(63–66). |
| 68–114 | 시작 시 20행 모듈·28행 METIS 안. NUMDUALS를 0으로 초기화한다(70–72). 위어(weir) 쌍 루프(73)는 `NUMDUALS(WEIR(J)) = NUMDUALS(WEIR(J))+1` (74), `NUMDUALS(WEIRD(J)) = NUMDUALS(WEIRD(J))+1` (75)로 양쪽 쌍 수를 센다. `IF (NUMDUALS(J) .ge. MAXDUALS) MAXDUALS = NUMDUALS(J)` (80)로 최대수를 구한다. IDUALS(MAXDUALS,MNP)를 할당·0 초기화한다(89–96). `IF (IDUALS(K,WEIR(J)) == 0) THEN` (100), `IF (IDUALS(K,WEIRD(J)) == 0) THEN` (109)이면 첫 빈 위치에 상대 노드를 저장하고 K 루프를 탈출한다. |
| 115–135 | 시작 시 20행 모듈·28행 METIS 안. 주기 경계 조건(periodic boundary conditions)용 임시 연결표 주석(115–118). `IF ( NPERBC > 0 ) THEN` (119)이면 NNEG_TMP(3,MNE)에 원본을 보관하고 PERBC_IDN_MAP(MNP)을 자기 번호로 초기화한다(120–126). IPERCONN의 둘째 열을 첫째 열로 매핑한다(127). 요소 루프(129)는 이 매핑으로 NNEG(:,I)를 교체한다(130). |
| 136–172 | 시작 시 20행 모듈·28행 METIS 안. 전체 간선(edge) 수·노드별 최대 후보 수를 위어 쌍까지 포함하여 산정한다. MNED·NEDLOC를 0 초기화한다(142–145). J·IEL 루프(147–148)는 `NCOUNT = NEDLOC(INODE) + 2` (150), `MNED = MNED + 2` (151)이다. `IF (IDUALS(K,INODE).NE.0) THEN` (153)이면 `NCOUNT = NCOUNT + 1` (154), `MNED = MNED + 1` (155)이다. `IF (NEDLOC(INODE) .ge. MNEDLOC) MNEDLOC = NEDLOC(INODE)` (164)로 최대 후보 수를 구한다. ADJNCY/EWGTS(MNED), CO_NODES(MNEDLOC,MNP)를 할당한다(170–171). |
| 173–221 | 시작 시 20행 모듈·28행 METIS 안. NEDGES를 0으로 초기화한다(176–178). 각 요소의 첫·둘째·셋째 꼭짓점을 기준으로 세 번 순회한다(180·194·208). 각 기준 노드에 나머지 두 꼭짓점을 추가한다(182–183·196–197·210–211). 수는 `NCOUNT = NEDGES(INODE) + 2` (184·198·212)이다. 각각 `IF (IDUALS(K,INODE).NE.0) THEN` (186·200·214)이면 `NCOUNT = NCOUNT + 1` (187·201·215)로 위어 상대 노드도 추가한다. 각 순회 뒤 NEDGES를 저장한다(191·205·219). |
| 222–267 | 시작 시 20행 모듈·28행 METIS 안. INODE 루프(226)는 후보를 ITVECT에 복사한다. `IF (NEDGES(INODE).GT.1) THEN` (230)이면 `SORT` (232) 후 `IF (ITVECT(J).NE.JNODE) THEN` (237)의 `NCOUNT = NCOUNT + 1` (238)로 중복을 제외한다. `ELSE` (243)의 `IF ( NPERBC < 0 ) THEN` (244)이면 고립 노드 메시지 및 `EXIT(1)`이다. 내부 `ELSE` (247)는 CO_NODES 첫 위치에 자기 번호, NCOUNT=1을 설정한다. `IF ( COUNT((IPERCONN(:,2) - INODE) == 0) == 0) THEN` (251)이면 주기 경계 종속 노드(slave node)가 아니므로 메시지 후 `EXIT(1)`이다. `NEDGETOT = NEDGETOT + NCOUNT` (259), `if (nedges(inode) == 0) then` (260)이면 `EXIT(1)`이다. `NEDGETOT = NEDGETOT/2` (265)로 간선 수를 저장·출력한다. |
| 268–300 | 시작 시 20행 모듈·28행 METIS 안. SYMMETRIC을 참으로 초기화하고 각 인접 노드의 역방향 목록을 검색한다(270–275). `IF (CO_NODES(K,JNODE) == INODE) THEN` (276)은 FOUND를 참으로 설정하고 탈출한다. `IF (.not. FOUND) THEN` (281)은 SYMMETRIC을 거짓으로 설정하며 메시지를 출력한다. `IF (.not. SYMMETRIC) THEN` (287)이면 `EXIT(1)`이다. 정점 가중치(vertex weight)는 NEDGES를 복사하고(295), `if ( strictBoundaries.eqv..true. ) then` (296)이면 `vwgts(inode) = vwgts(inode) + boundaryWeights(inode)` (297)이다. |
| 301–332 | 시작 시 20행 모듈·28행 METIS 안. XADJ(1)=1·ITOT=0 초기화(303–304). INODE·J 루프(305–306)는 `ITOT = ITOT + 1` (307)로 ADJNCY를 채운다. 간선 가중치는 `EWGTS(ITOT)  = (VWGTS(JNODE)+VWGTS(INODE))` (312)이며 단위 가중치 대체문은 주석이다(314). `XADJ(INODE+1) = ITOT+1` (317)로 다음 인접 목록 시작 위치를 만든다. `IDUMP = 1` (322), `IF (IDUMP.EQ.1) THEN` (323)이면 metis_graph.txt에 헤더 MNP/NEDGETOT/11/1 및 정점·인접 노드·간선 가중치를 쓴다(324–330). |
| 333–358 | 시작 시 20행 모듈·28행 METIS 안. 분할 호출 설정은 `NUMFLAG  = 1` (336), NPARTS=MNPROC(337), `OPTIONS(1) = 1` (338), `OPTIONS(2) = 3` (339), `OPTIONS(3) = 1` (340), `OPTIONS(4) = 3   !  minimize number of co-domains` (341), `OPTIONS(5) = 0` (342), `WEIGHTFLAG = 3   ! use weights for nodes and edges` (344), `OPTYPE = 2` (346). `metis_estimatememory`로 NBYTES를 받고(347–348) memory_usage_string으로 출력한다(352–353). `metis_partgraphkway`는 그래프·가중치·옵션을 받아 PROC와 EDGECUT을 반환한다(355–356). 절단 간선 수를 출력한다(358). 외부 루틴 내부는 이 파일에서 판독하지 않았다. |
| 359–395 | 시작 시 20행 모듈·28행 METIS 안. 부분 영역의 경계에서 연속 노드 수가 3 미만인 경우를 탐지하는 옛 블록 전체가 주석이다. contiguous 및 subdomainNumber를 설정·갱신하고 진단하려는 주석문이 있으며 실행되지 않는다(360–394). 마지막 빈 줄 포함(395). |
| 396–429 | 시작 시 20행 모듈·28행 METIS 안. partmesh.txt를 연다(396–397). `IF ( NPERBC > 0 ) THEN` (399)은 종속 노드의 PROC를 대응 기준 노드(master node)의 PROC로 복사한다(400). MNP개 PROC를 출력하고 닫는다(403–406). `IF ( NPERBC > 0 ) THEN` (409)은 NNEG를 원본으로 복원하고 임시 연결·매핑 배열을 해제한다(410–412). 기타 작업 배열을 명시적으로 해제한다(416–420). 서식·RETURN·METIS 종료·구분 주석과 빈 줄(422–429). |
| 430–453 | 시작 시 20행 모듈 안. 요소의 쌍대 그래프(dual graph)를 METIS_PartMeshDual로 나눈 뒤 요소 분할 EPART에서 노드 분할을 만들려는 대체 경로 설명. ESMF 격자 정의와 fort.18 호환 목적 및 호출 옵션 --partmesh_npart_from_epart 또는 대화식 −1을 주석에 적는다(437–449). 2023년 9월 이력(452). |
| 454–487 | 시작 시 20행 모듈 안. `METIS_NPART_FROM_EPART`·PRE_GLOBAL·IMPLICIT NONE(454–456). 그래프 관련 지역변수와 배열 선언(458–474), ETYPE/NV·ELMNTS·EPART/NPART·IDX·IPROC/NID 선언(475–480), 경계 진단용 변수(482–483). 외부 metis_estimatememory·METIS_PartMeshDual·METIS_PartMeshNodal 선언(485–486). |
| 488–519 | 시작 시 20행 모듈·454행 METIS_NPART_FROM_EPART 안. `ETYPE = 1 ; NV = 3 ;` (489)로 삼각형 자료를 지정한다. ELMNTS(MNE*NV), EPART(MNE), NPART(MNP), IDX(MNE,2)를 할당한다(490–492). `IF ( NPERBC > 0 ) THEN` (494)은 원본 NNEG를 보관하고 주기 노드 매핑으로 연결표를 바꾼다(495–506). `NUMFLAG = 1 ;` (513), NPARTS=MNPROC(514), `ELMNTS = reshape( NNEG, (/ MNE*NV /) ) ;` (515). `METIS_PartMeshDual`로 EPART·NPART·EDGECUT을 받는다(517–518). |
| 520–551 | 시작 시 20행 모듈·454행 METIS_NPART_FROM_EPART 안. 요소 분할로 노드 소유권을 다시 만드는 목적 주석(520–528). IDX(:,1)에 1..MNE, NPART(:)에 −1을 저장한다(529–531). `IPROCLOOP: DO IPROC = NPARTS, 1, -1` (532)에서 IDX(:,2)를 −1로 초기화하고 `IDX(:,2) = PACK( IDX(:,1), EPART == IPROC, IDX(:,2) )` (535)로 현재 영역 요소를 앞쪽에 모은다. I=1 후 `DO WHILE( IDX(I,2) > -1 )` (538)은 요소의 J=1..NV 노드를 확인한다. `IF ( NPART(NID) == -1 ) THEN` (544)이면 NPART(NID)=IPROC이다(545). `I = I + 1 ;` (549)로 다음 요소를 처리한다. |
| 552–579 | 시작 시 20행 모듈·454행 METIS_NPART_FROM_EPART·532행 IPROCLOOP 안. 옛 요소 전체 검색 방식은 주석이다(552–566). IPROCLOOP를 닫고 PROC=NPART를 복사한다(567–569). `IF ( NPERBC > 0 ) THEN` (572)은 종속 노드 PROC 복사(573), 원본 NNEG 복원 및 임시 배열 해제(575–577)를 수행한다. |
| 580–601 | 시작 시 20행 모듈·454행 METIS_NPART_FROM_EPART 안. partmesh.txt를 열고 MNP개 PROC를 쓴 뒤 닫는다(581–587). ELMNTS·EPART·NPART·IDX를 해제한다(589–591). 서식·RETURN·루틴 종료·구분 주석·빈 줄(593–600). METIS_PARTITION 모듈 종료(601). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 119·243–256: 주기 연결표 변경 조건은 NPERBC>0이다. 고립 노드 처리의 주기 경계 미사용 조건은 NPERBC<0이다. NPERBC=0은 이 처리의 else로 들어가 IPERCONN(:,2)를 참조한다.
- 63·225–232: ITVECT의 할당 크기는 MNP이다. 후보 목록 복사 상한은 NEDGES(INODE)이다. 이 복사 앞에는 NEDGES(INODE)<=MNP 검사가 없다.
- 322–331: IDUMP는 매번 1로 대입된다. 이어지는 IDUMP=1 분기는 metis_graph.txt를 출력한다.
- 58–59·359–394: contiguous와 subdomainNumber는 선언되어 있다. 이 변수들을 사용하는 경계 연속 노드 검사 블록은 전부 주석 처리되어 있다.
- 48·63·417: ITVECT2는 선언·할당·해제되지만 METIS 실행문에서 자료를 저장하거나 읽는 용도로 사용되지 않는다.
- 517–518·531–545: METIS_PartMeshDual이 반환한 NPART는 −1로 덮어쓴다. 노드 소유권은 큰 IPROC부터 순회하며 최초 미지정 노드에만 대입한다.
- 492·537–550: IDX 첫 차원은 MNE이다. DO WHILE 조건은 IDX(I,2)>−1이며 I<=MNE 조건은 없다. 루프 끝은 I를 1씩 증가시킨다.
- 531–569: NPART는 −1로 시작한다. 요소 순회에서 발견한 노드만 소유 영역을 받는다. PROC=NPART 복사 앞에는 남은 −1을 검사하는 조건이 없다.
