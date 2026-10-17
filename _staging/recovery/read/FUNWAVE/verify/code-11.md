# FUNWAVE 판독 기록 전수 검증 — code-11

대상은 사용자가 지정한 판독 기록 21개다.
원문은 각 기록의 frontmatter `file:` 경로에서 확인했다.
각 구간을 `nl -ba <원문> | sed -n 'A,Bp'`로 열어 대조했다.
대조 구간 행 수는 판독 기록의 표 행을 센 값이다.
대조 원문 행 수는 빈 줄과 주석을 포함한다.
정정·보완·이상 없음은 대조를 마친 구간 행을 기준으로 센다.
원문과 기록의 정적 대조만 수행했다.
모델은 실행하지 않았다.

기록 경로의 기준은 `_staging/recovery/read/FUNWAVE/FUNWAVE-TVD/`다.

| 기록 | 대조 구간 행 수 | 대조 원문 행 수 | 완료 범위 | 정정 | 보완 | 이상 없음 | 상태 |
|---|---:|---:|---|---:|---:|---:|---|
| GNUMake/Old_Version_Makefiles/Makefile-Lightning-Intel.md | 8 | 105 | 1–105 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-MacOS-Homebrew-MPICH.md | 8 | 108 | 1–108 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Mills-Sediment.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Mills-Spherical.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Mills-Vessel-Sediment.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Mills-Vessel.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Mills.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Onyx-Meteo-intel.md | 8 | 112 | 1–112 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Onyx-Sediment-intel.md | 8 | 106 | 1–106 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Onyx-Vessel-Sediment-intel.md | 8 | 109 | 1–109 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Onyx-Vessel-intel.md | 8 | 109 | 1–109 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Onyx-intel.md | 8 | 112 | 1–112 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Topaz-intel.md | 8 | 103 | 1–103 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Topaz-sgi-OpenSS.md | 8 | 103 | 1–103 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-Topaz-sgi.md | 8 | 106 | 1–106 | 0 | 0 | 8 | 완료 |
| GNUMake/Old_Version_Makefiles/Makefile-funwaveRDE.md | 8 | 104 | 1–104 | 0 | 0 | 8 | 완료 |
| Makefile.md | 8 | 119 | 1–119 | 0 | 1 | 7 | 완료 |
| Makefile.onyx.md | 8 | 119 | 1–119 | 0 | 1 | 7 | 완료 |
| Makefile_mac.md | 8 | 120 | 1–120 | 0 | 1 | 7 | 완료 |
| Makefile_mac_single.md | 8 | 120 | 1–120 | 0 | 1 | 7 | 완료 |
| README.md.md | 1 | 4 | 1–4 | 0 | 0 | 1 | 완료 |
| 합계 | 161 | 2179 | 위 기록 21개의 전체 원문 | 0 | 4 | 157 | 완료 |

표 아래의 코드 사실 항목도 원문과 대조했다.
대상 원문에는 Fortran 조건·루프와 C 전처리 조건 블록이 없다.
대상 원문에는 CUDA·OpenACC·OpenMP 지시가 없다.
Makefile의 MPI·DEBUG 조건 안내는 주석으로 구분해 확인했다.
대상 기록에서 추출한 행 번호가 붙은 백틱 인용 1395개는 해당 원문 행과 일치했다.
대상 원문의 SHA-256은 작업 시작 시 값과 모두 같았다.
대상 기록의 frontmatter는 작업 시작 시 내용과 모두 같았다.
대상 기록의 구간 경계는 작업 시작 시 값과 모두 같았다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| Makefile.md:90–100 | vessel case 예시 안내만 요약했다. | 예시 아래의 모든 줄에서 주석을 해제하라는 원문 안내를 인용했다. [10-17 전수 검증 보완] | Makefile:92 |
| Makefile.onyx.md:90–100 | vessel case 예시 안내만 요약했다. | 예시 아래의 모든 줄에서 주석을 해제하라는 원문 안내를 인용했다. [10-17 전수 검증 보완] | Makefile.onyx:92 |
| Makefile_mac.md:91–101 | vessel case 예시 안내만 요약했다. | 예시 아래의 모든 줄에서 주석을 해제하라는 원문 안내를 인용했다. [10-17 전수 검증 보완] | Makefile_mac:93 |
| Makefile_mac_single.md:91–101 | vessel case 예시 안내만 요약했다. | 예시 아래의 모든 줄에서 주석을 해제하라는 원문 안내를 인용했다. [10-17 전수 검증 보완] | Makefile_mac_single:93 |

정정 0, 보완 4, 이상 없음 157
