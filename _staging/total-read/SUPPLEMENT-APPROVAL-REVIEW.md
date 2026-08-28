# supplement 승인 검토 (confirmed_delta 23)

> 승인: `supplement-decisions.json` 각 건 `status:approved`·`approver:<사람>`·`approved_at`. producer(Claude) 자기승인 불가. 부분 승인 가능. 근거 원문은 `supplement-manifest.json` authoritative_quote.


### A. dead-guard / OOB — 최고 확신(객관·무신호)
- **000·convert.f·B3** — L251-254 
- **EFDC-000·aaefdc.f90·B1** — L924-928 

### B. use-before-assign — 명확(INTENT(OUT)/미대입 분기 후 무조건 사용)
- **000·breaker.F·B0** — L112,152-155,183 
- **000·breaker_gpu.F·B0** — L137,173-174,234-237 
- **001·breaker.f90·B1** — L112,151-152,221-222 
- **001·mod_global.f90·B1** — L2101-2106 [증거:io.f90]
- **004·breaker.F·B1** — L103,161-168,238-239 
- **004·mod_tracer.F·B1** — L444,464,470-473 
- **004·mod_vessel.F·B0** — L149,263 

### C. 로직·인덱스 결함 — 명확
- **001·dispersion.f90·B0** — L379-380 
- **001·io.f90·B8** — L2428-2438 
- **001·wavemaker.f90·B0** — L102-104 
- **001·wavemaker.f90·B1** — L206,208,259 
- **001·wavemaker.f90·B4** — L2522-2524 
- **001·wavemaker.f90·B6** — L2498,2653 
- **004·io.F·B0** — L754,765,771,782-783 
- **004·mod_sediment.F·B2** — L1363-1364 
- **004·mod_sediment.F·B3** — L1593-1594 
- **004·wavemaker.F·B1** — L214,241,299 
- **004·wavemaker.F·B10** — L2836,2992 
- **004·wavemaker.F·B4** — L328,638,842 
- **004·wavemaker.F·B8** — L2860-2862,2896 

### D. doc-vs-code
- **note-000·funwave-user-manual-full.md·B5** — L3361 [증거:io.F]

### 확신도 메모
- A/B/C 모두 span 재확인 완료(base 미검출). 실무 영향도는 상이: DETTMP·OOB·Pd<0·avalanche·io 상태소실은 계산결과/데이터 직접 영향; INTENT(OUT) UBA 계열은 컴파일러 관용으로 통상 동작하나 UB·이식성 결함; dispersion VorticityMax·wavemaker 는 진단출력/파형생성 경로.
- span-gate 기각분(sediment.F MIN-cap·fluxes Gamma1=0·mkxyz beach 등)은 여기 미포함 — precision 보호됨.
