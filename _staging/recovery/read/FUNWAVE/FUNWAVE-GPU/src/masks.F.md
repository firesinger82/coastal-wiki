---
file: models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/masks.F
lines: 205
sha256: ad99caf45ed2e0e148ce3bbacc38cc561cd0c930c836a510dda7026ea1961d07
reader: codex gpt-6.1-sol
read_date: 2026-10-17
---

# masks.F — 판독 구간 기록

구간은 1행부터 205행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–50 | masks.F·FUNWAVE-TVD 소속·2016년 저작권·Simplified BSD 재배포 조건·무보증 머리말(1–44). UPDATE_MASK가 마스크(mask)를 갱신하며 fluxes 루틴에서도 갱신한다는 설명(46–47). 2010년 이력과 구분 주석(48–50). 이 구간은 전처리 조건 밖이다. |
| 51–73 | UPDATE_MASK는 GLOBAL을 사용하고 할당 가능 MASKtmp·ETAtmp를 선언한다(51–55). `# if defined (PARALLEL)` (56) 참 구간만 myvar를 선언하고 `# endif` (58). 두 임시 배열을 `(Mloc,Nloc)`로 할당한다(60–61). 직렬 코드의 유령 격자점(ghost cell) MASK를 유지한다는 주석(63). `#if defined(PARALLEL)` (65) 참 구간에서 phi_int_exch를 MASK·MASK9에 호출하며 `#endif` (68)로 닫는다. PARALLEL 미정의 시 선언·교환을 제외하며 `#else`는 없다. `MASKtmp=MASK` (70)로 복사한다. `ETAtmp=ETA` (71)로 복사한다. `Dmass = ZERO` (72)로 초기화한다. [10-17 전수 검증 보완] |
| 74–111 | 시작 시 51행 UPDATE_MASK 안이다. `DO J=Jbeg-2,Jend+2`·`DO I=Ibeg-2,Iend+2` (74–75). `IF(MASK_STRUC(I,J)==1)THEN` (77) 안에서 `IF(MASK(I,J)<1)THEN` (78)이면 침수(flooding) 후보를 검사한다. 서쪽 `IF(MASK(I-1,J)==1.AND.Eta(I-1,J)>Eta(I,J))THEN` (80), 동쪽 `IF(MASK(I+1,J)==1.AND.Eta(I+1,J)>Eta(I,J))THEN` (84), 남쪽 `IF(MASK(I,J-1)==1.AND.Eta(I,J-1)>Eta(I,j))THEN` (88), 북쪽 `IF(MASK(I,J+1)==1.AND.Eta(I,J+1)>Eta(I,j))THEN` (92)의 각 참 분기는 `MASKtmp(I,J)=1`로 설정한다(81·85·89·93). 78행의 `ELSE` (96)에서는 `IF(Eta(I,J)<-Depth(I,J))THEN` (97)이면 건조(drying) 처리로 `MASKtmp(I,J)=0` (98), `ETAtmp(I,J)=MinDepth-Depth(I,J)` (99). 그 안 `IF(I.GE.Ibeg.AND.I.LE.Iend.AND.J.GE.Jbeg.AND.J.LE.Jend)THEN` (101)이면 `# if defined (CARTESIAN)` (102) 참 구간에서 `Dmass = Dmass + (ETAtmp(I,J)-ETA(I,J))*DX*DY` (103), `# else` (104)의 CARTESIAN 미정의 구간에서 `Dmass = Dmass + (ETAtmp(I,J)-ETA(I,J))*DX(I,J)*DY(I,J)` (105)를 계산한다. `# endif` (106)와 모든 실행 조건 종료(107–110). PARALLEL 여부와 무관하게 이 루프를 컴파일한다. 네 이웃 검사는 각각 별도의 IF이다. 이 IF들에는 ELSE가 없다(80–94). 내부 영역 IF는 107행에서 닫힌다. 건조 IF는 108행에서 닫힌다. MASK IF는 109행에서 닫힌다. MASK_STRUC IF는 110행에서 닫힌다. [10-17 전수 검증 보완] |
| 112–135 | 시작 시 51행 UPDATE_MASK·`DO J=Jbeg-2,Jend+2` (74)·`DO I=Ibeg-2,Iend+2` (75) 안이다. `IF(MASK_STRUC(I,J)==1)THEN` (77)은 `ENDIF` (110)에서 닫혔다. 건조 시 DepthX·DepthY 재설정의 배경과 정확도 영향에 관한 주석, Makefile의 `-DIGNORE_BIG_SLOPE` 설명(112–118). `# if defined (IGNORE_BIG_SLOPE)` (119) 참 구간은 주석만 있으며 대입이 없다(120). `# else` (121)의 IGNORE_BIG_SLOPE 미정의 구간은 `IF(MASK(I,J)<1)THEN` (122)이면 `DepthX(I,J)=Depth(I-1,J)` (123), `DepthX(I+1,J)=Depth(I+1,J)` (124), `DepthY(I,J)=Depth(I,J-1)` (125), `DepthY(I,J+1)=Depth(I,J+1)` (126)을 대입한다. `ENDIF` (127)·`# endif` (128) 종료, 두 루프 종료(130–131). 그 뒤 `MASK=MASKtmp` (133)로 갱신한다. `ETA=ETAtmp` (134)로 갱신한다. CARTESIAN·PARALLEL 여부는 이 구간 선택에 관여하지 않는다. [10-17 전수 검증 보완] |
| 136–160 | 시작 시 51행 UPDATE_MASK 안이며 앞 격자 루프 밖이다. `DO J=Jbeg-1,Jend+1`·`DO I=Ibeg-1,Iend+1` (136–137). `IF(VISCOSITY_BREAKING)THEN` (138) 참 분기는 점성 쇄파(viscosity breaking)에 MASK9를 쓰지 않는다는 주석만 있다(139). `ELSE` (140)에서는 `MASK9(I,J)=MASK(I,J)*MASK(I-1,J)*MASK(I+1,J)  &` (141); `*MASK(I+1,J+1)*MASK(I,J+1)*MASK(I-1,J+1) &` (142); `*MASK(I+1,J-1)*MASK(I,J-1)*MASK(I-1,J-1)` (143)를 계산한다. 그 안 `IF(ABS(Eta(I,J))/MAX(DEPTH(I,J),MinDepthFrc)>SWE_ETA_DEP)THEN` (144)이면 `MASK9(I,J)=ZERO` (145). 수위비 IF는 `ENDIF` (146)에서 닫힌다. VISCOSITY_BREAKING IF는 `ENDIF` (148)에서 닫힌다. I·J 루프는 각각 150·151행에서 닫힌다. `# if defined(PARALLEL)` (153) 참 구간에서 PHI_INT_EXCH를 MASK·MASK9에 호출하며 `# endif` (156). PARALLEL 미정의 시 교환을 제외하고 `#else`는 없다. 임시 배열 해제(158–159). [10-17 전수 검증 보완] |
| 161–185 | 시작 시 51행 UPDATE_MASK 안이다. `# if defined (CHECK_MASS_CONSERVATION)` (161)이 참일 때만 이후 201행까지 질량 보존(mass conservation) 보정을 컴파일하며 미정의 시 제외하고 `#else`는 없다. `WetArea = ZERO` (164)로 초기화한다. 내부 격자 루프는 `DO J=Jbeg,Jend` (165)·`DO I=Ibeg,Iend` (166)이다. 이 바깥 플래그 안의 `# if defined (CARTESIAN)` (168) 참 구간은 `IF(MASK(I,J)>0)THEN` (169)이면 `WetArea = WetArea + DX*DY` (170). `# else` (172)의 CARTESIAN 미정의 구간은 `IF(MASK(I,J)>0)THEN` (173)이면 `WetArea = WetArea + DX(I,J)*DY(I,J)` (174). `# endif` (176), 루프 종료(177–178). 같은 바깥 플래그 안의 `# if defined (PARALLEL)` (180) 참 구간에서 MPI_ALLREDUCE·MPI_SUM으로 WetArea와 Dmass를 각각 합산하고 `WetArea = myvar` (182)와 `Dmass = myvar` (184)를 대입한다(181–184). `# endif` (185). 따라서 MPI 합산은 CHECK_MASS_CONSERVATION과 PARALLEL이 모두 정의될 때만 컴파일한다. [10-17 전수 검증 보완] |
| 186–205 | 시작 시 51행 UPDATE_MASK·`# if defined (CHECK_MASS_CONSERVATION)` (161)의 참 구간 안이다. `# if defined (CARTESIAN)` (188) 참 구간에서 `DwetEta = Dmass / Max(DX*DY,WetArea)` (189), `# else` (190)의 CARTESIAN 미정의 구간에서 `DwetEta = Dmass / Max(DX(1,1)*DY(1,1),WetArea)` (191). `# endif` (192). `DO J=Jbeg,Jend` (194)·`DO I=Ibeg,Iend` (195)에서 `IF(MASK(I,J) >0) ETA(I,J)= ETA(I,J) - DwetEta` (196)로 보정한다. 루프 종료(197–198). 이후 ETA 교환은 Main.F의 경계조건(boundary condition) 처리에서 한다는 주석(199). `# endif` (201)로 질량 보존 전처리를 닫는다. 이 수위 보정은 PARALLEL 여부와 무관하다. 종료 주석·루틴 종료·마지막 빈 줄(202–205). [10-17 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 74–75·80–92: 루프는 내부 영역에서 두 격자점 바깥까지 진행한다. 이웃 조건은 그 위치에서 다시 한 격자점 바깥의 MASK·Eta를 참조한다. 이 루틴에는 Nghost 크기 검사가 없다.
- 98·122–134: 건조 판정 결과는 먼저 MASKtmp에 기록한다. DepthX·DepthY 재설정 조건은 MASKtmp가 아니라 갱신 전 MASK를 사용한다.
- 138–148: VISCOSITY_BREAKING 참 분기에는 MASK9 대입이 없다. MASK9의 9점 곱과 수위비 검사는 ELSE 안에만 있다.
- 168–176·188–196: CARTESIAN 미정의 시 DwetEta 분모의 최소 면적은 DX(1,1)*DY(1,1)이다. 보정 루프의 각 격자점 면적을 이 최소값 계산에 사용하지 않는다.
