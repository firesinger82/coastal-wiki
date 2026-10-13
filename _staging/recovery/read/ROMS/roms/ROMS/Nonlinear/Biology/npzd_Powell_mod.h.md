---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Powell_mod.h
lines: 279
sha256: 1e0583983590b00e4575624a9fb7ff067cea9f48bd3fed900ed2e63f98784bad
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Powell_mod.h — 판독 구간 기록

구간은 1행부터 279행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | mod_biology 모듈 시작(1). 저작권·MIT/X 사용허가·License_ROMS.md 안내(3–8). Powell 등(2006)의 생태계(ecosystem) 매개변수 설명(10–40). AttPhy는 자기차광(self-shading) 계수 m2/millimole_N, AttSW는 1/m, BioIter는 비선형 수렴 반복 상한, BioIni는 균일 해석 초기 조건(analytical initial condition) 농도이다(12–18). DetRR·PhyMRD/PhyMRN·Vm_NO3·ZooGR·ZooMRD/ZooMRN는 1/day, K_NO3는 반포화(half-saturation) 농도 millimole_N m-3, Ivlev·PARfrac·ZooEED/ZooEEN는 무차원(nondimensional), PhyIS는 P-I 곡선 초기 기울기 m2/W, wDet/wPhy는 m/day로 설명(19–40). mod_param 사용·implicit none·주석(44–47). |
| 48–100 | 시작 시 1행 mod_biology 안. idbio와 iNO3_·iPhyt·iZoop·iSDet 식별자 선언(50–54). BioIter 정수 배열(58). `#ifdef ANA_BIOLOGY` (60)에서 BioIni(:,:) 선언(61), `#endif` (62). AttPhy·AttSW·DetRR·K_NO3·Ivlev·PARfrac 실수 allocatable(63–68). `#ifdef TANGENT` (69)에서 tl_PARfrac(70), `#endif` (71). `#ifdef ADJOINT` (72)에서 ad_PARfrac(73), `#endif` (74). PhyIS·PhyMRD·PhyMRN·Vm_NO3·wDet 선언(75–79). `#ifdef TANGENT` (80)에서 tl_wDet(81), `#endif` (82). `#ifdef ADJOINT` (83)에서 ad_wDet(84), `#endif` (85). wPhy 선언(86), `#ifdef TANGENT` (87)에서 tl_wPhy(88), `#endif` (89). `#ifdef ADJOINT` (90)에서 ad_wPhy(91), `#endif` (92). ZooEED·ZooEEN·ZooGR·ZooMRD·ZooMRN 선언(93–97), CONTAINS·주석(98–100). 이 선언에는 수치 기본값이 없다. |
| 101–123 | 시작 시 1행 mod_biology 안. initialize_biology 시작(101), 변수 할당·생물 추적자 인덱스 설정 설명(103–108), 정수 i/ic 선언(112). `NBT=4` (118)로 추적자 수를 4로 고정한다. 할당 구역 안내 주석까지 포함(120–123). |
| 124–158 | 시작 시 1행 mod_biology·101행 initialize_biology 안. 미할당 조건은 `IF (.not.allocated(BioIter)) THEN` (124), `IF (.not.allocated(AttPhy)) THEN` (129), `IF (.not.allocated(AttSW)) THEN` (134), `IF (.not.allocated(DetRR)) THEN` (139), `IF (.not.allocated(K_NO3)) THEN` (144), `IF (.not.allocated(Ivlev)) THEN` (149), `IF (.not.allocated(PARfrac)) THEN` (154)이다. BioIter·AttPhy·AttSW·DetRR·K_NO3·Ivlev·PARfrac를 각각 Ngrids 크기로 할당(125·130·135·140·145·150·155). 메모리 계수 증분은 `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (126·131·136·141·146·151·156)이다. 각 조건 종료·빈 줄까지 포함(127–158). |
| 159–197 | 시작 시 1행 mod_biology·101행 initialize_biology 안. `#ifdef TANGENT` (159)에서 `IF (.not.allocated(tl_PARfrac)) THEN` (160)이면 tl_PARfrac(Ngrids) 할당(161), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (162), 조건 종료(163), `#endif` (164). `#ifdef ADJOINT` (166)에서 `IF (.not.allocated(ad_PARfrac)) THEN` (167)이면 ad_PARfrac(Ngrids) 할당(168), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (169), 조건 종료(170), `#endif` (171). `IF (.not.allocated(PhyIS)) THEN` (173), `IF (.not.allocated(PhyMRD)) THEN` (178), `IF (.not.allocated(PhyMRN)) THEN` (183), `IF (.not.allocated(Vm_NO3)) THEN` (188), `IF (.not.allocated(wDet)) THEN` (193)이면 PhyIS·PhyMRD·PhyMRN·Vm_NO3·wDet를 Ngrids 크기로 할당(174·179·184·189·194). 계수 증분은 `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (175·180·185·190·195)이다. 조건 종료·빈 줄까지 포함(196–197). |
| 198–230 | 시작 시 1행 mod_biology·101행 initialize_biology 안. `#ifdef TANGENT` (198)에서 `IF (.not.allocated(tl_wDet)) THEN` (199)이면 tl_wDet(Ngrids) 할당(200), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (201), 조건 종료(202), `#endif` (203). `#ifdef ADJOINT` (205)에서 `IF (.not.allocated(ad_wDet)) THEN` (206)이면 ad_wDet(Ngrids) 할당(207), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (208), 조건 종료(209), `#endif` (210). `IF (.not.allocated(wPhy)) THEN` (212)이면 wPhy(Ngrids) 할당(213), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (214), 조건 종료(215). `#ifdef TANGENT` (217)에서 `IF (.not.allocated(tl_wPhy)) THEN` (218)이면 tl_wPhy(Ngrids) 할당(219), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (220), 조건 종료(221), `#endif` (222). `#ifdef ADJOINT` (224)에서 `IF (.not.allocated(ad_wPhy)) THEN` (225)이면 ad_wPhy(Ngrids) 할당(226), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (227), 조건 종료(228), `#endif` (229). 빈 줄 포함(230). |
| 231–255 | 시작 시 1행 mod_biology·101행 initialize_biology 안. 미할당 조건은 `IF (.not.allocated(ZooEED)) THEN` (231), `IF (.not.allocated(ZooEEN)) THEN` (236), `IF (.not.allocated(ZooGR)) THEN` (241), `IF (.not.allocated(ZooMRD)) THEN` (246), `IF (.not.allocated(ZooMRN)) THEN` (251)이다. ZooEED·ZooEEN·ZooGR·ZooMRD·ZooMRN를 각각 Ngrids 크기로 할당(232·237·242·247·252). 메모리 계수 증분은 `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (233·238·243·248·253)이다. 각 조건 종료·주석까지 포함(234–255). |
| 256–279 | 시작 시 1행 mod_biology·101행 initialize_biology 안. `IF (.not.allocated(idbio)) THEN` (258)이면 idbio(NBT)를 할당(259), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (260), 조건 종료(261). 기본 추적자 수 합은 `ic=NAT+NPT+NCS+NNS` (267). i=1..NBT 루프(268–270)에서 `idbio(i)=ic+i` (269). 성분별 인덱스는 `iNO3_=ic+1` (271), `iPhyt=ic+2` (272), `iZoop=ic+3` (273), `iSDet=ic+4` (274)이다. 주석·RETURN·initialize_biology 종료·빈 줄·mod_biology 종료(275–279). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 60–62·101–277: ANA_BIOLOGY에서 BioIni(:,:)를 선언하지만 initialize_biology에는 BioIni를 할당하거나 값을 대입하는 문장이 없다.
- 124–261: 배열 할당 블록은 크기를 할당하고 Dmem(1)을 증가시킨다. 이 루틴에는 BioIter·생물 매개변수·tl_/ad_ 배열의 수치 값을 초기화하는 대입문이 없다.
- 258–260: idbio의 할당 크기는 NBT이지만 Dmem(1)의 증분은 REAL(Ngrids,r8)이다.
