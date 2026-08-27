## EFDC-000 — 감사 불합격 (2026-08-26, 보정 기준)
- aaefdc.f90 DETTMP 특이점검사 무력화 (역수 후 ==0 비교) — ★소스 확인 완료, Claude 누락
- (검증 대기) mod_scaninp.f90 MPI broadcast 누락: TOXDEP TXDRY/TXWET·VOL_VEL_MAX/VOL_DEP_MIN·MODCHAN MDCHHD/MDCHHD2
- (검증 대기) mod_scaninp.f90 SCANASER 오류진단이 NS(미대입) 출력 — use-before-assign
- (검증 대기) input.f90 NPFORT>=1 분기가 NPFORT==2 도달불가로 shadowing
- 처분: 재판독 vs Codex findings 병합 — 배치 결정 대기

## FW000·FW002 — 휴리스틱 판정 (2026-08-26): 깨끗한 누락 미확정
- Codex가 +1~3건 더 올렸으나 material 후보(etauv pivot·CONSTRUCT_HO 인터페이스)는 Claude 1차도 이미 짚음.
- .m 플롯 스크립트 델타는 경미(비material).
- ★결론: count+키워드로는 pass/fail 단정 불가. **건별 의미 대조(semantic)가 필요** → 배치 처분으로 이월.
- EFDC-000 처럼 '깨끗한 누락'이 확정된 건만 불합격 처리, 나머지는 배치서 정밀 대조.

## FW001 — 배치 이월 (2026-08-26): Fortran material 후보 30건
- 다수 Claude 1차와 겹침(breaker AGE INTENT(OUT)·etauv pivot 가드·mod_tide Iwidth·mod_time_spectra Theta_2D·mod_vessel/tracer 표제 불일치).
- 배치 검토 후보(Claude 누락 가능): wavemaker.f90 phi1 INTENT(OUT) 비주기경로 미대입 / misc.f90·mod_global.f90 MPI_CART_COORDS에 comm2d 아닌 MPI_COMM_WORLD rank 전달 / tridiagnal.f90 smsg(:,1)만 채우고 MPI_ISEND 2*Nloc 전송(버퍼 불일치) / fluxes.f90 CONSTRUCT_HO_X_MLP 소분모 검사가 나눗셈 뒤.
- 처분: 배치 semantic 대조서 Claude 누락 여부 확정 → 재판독 vs 병합.

## FW004 — 배치 이월 (2026-08-27): 메인16+하위32 병합, Fortran material 후보 위 로그
- 처분: 배치 semantic 대조 대상.
