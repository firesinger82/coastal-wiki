---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Sediment/sediment_wrt_pio.h
lines: 75
sha256: c89781553233b0e3ef9ce345fecb0d3588b357e88c650b09514837bab2350cc1
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# sediment_wrt_pio.h — 판독 구간 기록

구간은 1행부터 75행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | 파일 내부에서 열린 전처리 조건 없음. 저작권·MIT/X 라이선스 머리말(1–13), 빈 줄·구분 주석(14–17). 머리말은 퇴적물 모델 입력 매개변수(sediment model input parameter)를 NetCDF에 쓰고 wrt_info.F에 포함한다고 적음(9–10). 16행 구분 주석은 Nemuro ecosystem model parameters라고 적음. 독립 루틴 선언은 이 파일에 없다. |
| 18–27 | 파일 내부에서 열린 전처리 조건 없음. `pio_netcdf_put_fvar`로 minlayer_thick(ng)(18–20), newlayer_thick(ng)(23–25)을 스칼라 변수로 출력. 시작·개수 인수는 (/0/)·(/0/), pioFile=pioFile. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26). 빈 줄(22·27) 포함. 계산식이나 기본값 설정은 이 블록에 없다. |
| 28–34 | 파일 내부에서 열린 전처리 조건 없음. `#ifdef BEDLOAD` (28)에서 `pio_netcdf_put_fvar`에 bedload_coeff(ng), (/0/)·(/0/), pioFile=pioFile을 전달(29–31). `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (32). `#endif` (33), 빈 줄(34). |
| 35–51 | 파일 내부에서 열린 전처리 조건 없음. `#ifdef ANA_SEDIMENT` (35)에서 `pio_netcdf_put_fvar`로 Sd50(:,ng)(36–38), Srho(:,ng)(41–43), Csed(:,ng)(46–48) 출력. 시작 (/1/)·개수 (/NST/)·pioFile=pioFile 사용. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (39·44·49). `#endif` (50), 빈 줄(40·45·51) 포함. |
| 52–75 | 파일 내부에서 열린 전처리 조건 없음. `pio_netcdf_put_fvar`로 Wsed(:,ng)(52–54), Erate(:,ng)(57–59), tau_ce(:,ng)(62–64), tau_cd(:,ng)(67–69), poros(:,ng)(72–74) 출력. 각 호출은 시작 (/1/)·개수 (/NST/)·pioFile=pioFile 사용. `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (55·60·65·70·75). 빈 줄(56·61·66·71) 포함. 계산식·단위 변환·기본값 대입은 이 파일에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·16: 머리말은 sediment model input parameters를 출력한다고 적는다. 실행 블록 앞 주석은 Nemuro ecosystem model parameters라고 적는다.
- 35–50: Sd50·Srho·Csed 출력은 실제 ANA_SEDIMENT 전처리 조건 안에 있다. 같은 대상의 sediment_wrt.h:65–80에서 해당 조건처럼 보이는 줄은 주석이다.
- 18–75: 이 PIO 헤더에는 sg_zwbl 출력 호출과 sedslope_crit_wet/dry·slopefac_wet/dry·bedload_vandera_alphaw/alphac 출력 호출이 없다. 같은 대상의 sediment_wrt.h에는 해당 호출들이 있다(27–30·38–61).
