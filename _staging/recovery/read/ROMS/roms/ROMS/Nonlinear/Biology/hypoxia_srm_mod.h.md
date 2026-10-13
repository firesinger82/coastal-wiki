---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/hypoxia_srm_mod.h
lines: 117
sha256: b8c132faae93e50d73c4c7f0797315e85bac623bc20829fa3df5f867b49c1a47
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# hypoxia_srm_mod.h — 판독 구간 기록

구간은 1행부터 117행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | mod_biology 모듈 입구·저작권·MIT/X 라이선스 주석(1–8). BioIter는 비선형 해 수렴 반복 상한, ResRate는 총 생물 호흡률(respiration rate) 1/day로 설명한다(10–15). mod_param 사용·implicit none 뒤 idbio, 용존 산소(dissolved oxygen) 인덱스 iOxyg, 총 호흡률 식별자 idResR, 격자별 BioIter·ResRate를 선언한다(18–33). CONTAINS에서 절차 부분으로 넘어간다(35). |
| 37–70 | 시작 시 1행 mod_biology 안. initialize_biology 입구·목적·지역 i/ic 선언(37–48). 생물 추적자(tracer) 수 NBT는 1이다(54). DIAGNOSTICS와 DIAGNOSTICS_BIO 조건에서는 2차원 진단 수를 1, 3차원 진단 수를 0, 산소 플럭스(flux) 인덱스 iO2fx를 1로 설정한다(56–70). 원문 조건·루프·대입·전처리: `NBT=1` (54) / `#if defined DIAGNOSTICS && defined DIAGNOSTICS_BIO` (56) / `NDbio2d=1` (64) / `NDbio3d=0` (65) / `iO2fx=1` (69) / `#endif` (70). |
| 71–101 | 시작 시 1행 mod_biology·37행 initialize_biology 안. BioIter·ResRate를 각각 Ngrids 길이로 미할당일 때 할당하고 Dmem(1)에 실수 원소 수를 누적한다(76–84). idbio는 NBT 길이로 같은 처리를 한다(88–91). DIAGNOSTICS/DIAGNOSTICS_BIO 조건에서는 iDbio2를 NDbio2d 길이로 할당·메모리 집계한다(93–101). 원문 조건·루프·대입·전처리: `IF (.not.allocated(BioIter)) THEN` (76) / `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (78) / `IF (.not.allocated(ResRate)) THEN` (81) / `Dmem(1)=Dmem(1)+REAL(Ngrids,r8)` (83) / `IF (.not.allocated(idbio)) THEN` (88) / `Dmem(1)=Dmem(1)+REAL(NBT,r8)` (90) / `#if defined DIAGNOSTICS && defined DIAGNOSTICS_BIO` (93) / `IF (.not.allocated(iDbio2)) THEN` (97) / `Dmem(1)=Dmem(1)+REAL(NDbio2d,r8)` (99) / `#endif` (101). |
| 102–117 | 시작 시 1행 mod_biology·37행 initialize_biology 안. NAT+NPT+NCS+NNS 뒤에 생물 인덱스를 연속 배치하며 idbio(i)=ic+i로 설정한다(107–110). ic를 1 증가시켜 iOxyg에 넣는다(111–112). RETURN·서브루틴 종료·빈 줄·모듈 종료(114–117). 원문 조건·루프·대입·전처리: `ic=NAT+NPT+NCS+NNS` (107) / `DO i=1,NBT` (108) / `idbio(i)=ic+i` (109) / `ic=ic+1` (111) / `iOxyg=ic` (112). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·37–115: idResR를 선언하지만 initialize_biology에는 idResR 대입이 없다.
- 76–84: BioIter·ResRate는 할당과 Dmem 집계만 수행한다. 이 초기화 루틴에는 두 배열의 값 대입이 없다.
