---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Franks_mod.h
lines: 197
sha256: 6d1eb249c02f3a4e5b645389de81bd7dd2e3d1ea30b99ff9f5d9d6737c6b5016
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Franks_mod.h — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | mod_biology 모듈 시작(1). 저작권·MIT/X 사용허가·License_ROMS.md 안내(3–8). Franks 등(1986)형 생물 매개변수 설명(10–28). BioIter는 비선형 수렴 반복 상한, BioIni는 균일 해석 초기 조건(analytical initial condition) 농도이다(12–15). DetRR·PhyMR·Vm_NO3·ZooGR·ZooMR·ZooMD는 1/day, K_ext는 1/m, K_NO3는 1/(millimole_N m-3), K_Phy는 millimole_N m-3, wDet는 m/day, ZooGA·ZooEC는 무차원이라는 주석이다(16–28). mod_param 사용·implicit none·주석 행(32–35). |
| 36–71 | 시작 시 1행 mod_biology 안. idbio와 iNO3_·iPhyt·iZoop·iSDet를 생물 추적자 식별자로 선언(36–42). BioIter는 정수 allocatable(46). `#ifdef ANA_BIOLOGY` (48)에서 BioIni(:,:) 선언(49), `#endif` (50). DetRR·K_ext·K_NO3·K_Phy·PhyMR·Vm_NO3·wDet는 real(r8) allocatable(51–57). `#ifdef TANGENT` (58)에서 tl_wDet 선언(59), `#endif` (60). `#ifdef ADJOINT` (61)에서 ad_wDet 선언(62), `#endif` (63). ZooGR·ZooMR·ZooMD·ZooGA·ZooEC 선언(64–68), CONTAINS·주석(69–71). 선언에 수치 기본값은 없다. |
| 72–94 | 시작 시 1행 mod_biology 안. initialize_biology 입구(72). 필요한 변수 할당과 생물 추적자 인덱스 설정 설명(74–79). i/ic 정수 지역변수 선언(83). `NBT=4` (89)로 생물 추적자 수를 4로 고정한다. 할당 구역 안내와 주석 행(91–94). |
| 95–134 | 시작 시 1행 mod_biology·72행 initialize_biology 안. 미할당 조건은 `IF (.not.allocated(BioIter)) THEN` (95), `IF (.not.allocated(DetRR)) THEN` (100), `IF (.not.allocated(K_ext)) THEN` (105), `IF (.not.allocated(K_NO3)) THEN` (110), `IF (.not.allocated(K_Phy)) THEN` (115), `IF (.not.allocated(PhyMR)) THEN` (120), `IF (.not.allocated(Vm_NO3)) THEN` (125), `IF (.not.allocated(wDet)) THEN` (130)이다. 참인 배열 BioIter·DetRR·K_ext·K_NO3·K_Phy·PhyMR·Vm_NO3·wDet를 각각 Ngrids 크기로 할당(96·101·106·111·116·121·126·131). 메모리 계수 증분의 원문은 `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (97·102·107·112·117·122·127·132)이다. 각 조건 종료와 빈 줄까지 포함(98–134). |
| 135–173 | 시작 시 1행 mod_biology·72행 initialize_biology 안. `#ifdef TANGENT` (135)에서 `IF (.not.allocated(tl_wDet)) THEN` (136)이면 tl_wDet(Ngrids)를 할당(137), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (138), 조건 종료(139), `#endif` (140). `#ifdef ADJOINT` (142)에서 `IF (.not.allocated(ad_wDet)) THEN` (143)이면 ad_wDet(Ngrids)를 할당(144), `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (145), 조건 종료(146), `#endif` (147). `IF (.not.allocated(ZooGR)) THEN` (149), `IF (.not.allocated(ZooMR)) THEN` (154), `IF (.not.allocated(ZooMD)) THEN` (159), `IF (.not.allocated(ZooGA)) THEN` (164), `IF (.not.allocated(ZooEC)) THEN` (169)이면 ZooGR·ZooMR·ZooMD·ZooGA·ZooEC를 Ngrids 크기로 할당(150·155·160·165·170). 계수 증분은 `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (151·156·161·166·171)이다. 조건 종료·주석까지 포함(172–173). |
| 174–197 | 시작 시 1행 mod_biology·72행 initialize_biology 안. `IF (.not.allocated(idbio)) THEN` (176)이면 idbio(NBT)를 할당(177), `Dmem(1)=Dmem(1)+REAL(NBT,r8)` (178), 조건 종료(179). 기본 추적자 수 합은 `ic=NAT+NPT+NCS+NNS` (185). i=1..NBT 루프(186–188)에서 `idbio(i)=ic+i` (187). 성분별 인덱스는 `iNO3_=ic+1` (189), `iPhyt=ic+2` (190), `iZoop=ic+3` (191), `iSDet=ic+4` (192)이다. RETURN·initialize_biology 종료·빈 줄·모듈 종료(194–197). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–50·72–195: ANA_BIOLOGY에서 BioIni(:,:)를 선언하지만 initialize_biology에는 BioIni를 할당하거나 값을 대입하는 문장이 없다.
- 95–179: 각 배열 할당 블록은 크기를 할당하고 Dmem(1)을 증가시킨다. 이 루틴에는 BioIter·생물 매개변수·tl_wDet/ad_wDet의 수치 값을 초기화하는 대입문이 없다.
