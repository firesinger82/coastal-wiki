---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/npzd_Powell_wrt_pio.h
lines: 101
sha256: ae596859f6ee69475dac92e024c3b475d803c1432665d5273c64030155392009
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# npzd_Powell_wrt_pio.h — 판독 구간 기록

구간은 1행부터 101행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권·MIT/X 사용허가·License_ROMS.md 안내(1–7). Powell 등(2006)의 생태계(ecosystem) 입력 매개변수를 NetCDF에 쓰며 `wrt_info.F`에 삽입한다는 설명(9–10). C 주석 종료·빈 줄·NPZD 출력 설명(13–17). 이 파일에는 루틴 선언과 전처리 분기가 없다. |
| 18–62 | `pio_netcdf_put_ivar`로 BioIter(ng)를 BioIter에 기록(18–20). `pio_netcdf_put_fvar`로 AttSW·AttPhy·PhyIS·Vm_NO3·PhyMRD·PhyMRN·K_NO3·Ivlev의 ng 원소를 동명 변수에 기록(23–25·28–30·33–35·38–40·43–45·48–50·53–55·58–60). 각 호출의 시작·개수는 `(/0/)`이며 `pioFile = pioFile`를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (21·26·31·36·41·46·51·56·61)이다. |
| 63–101 | `pio_netcdf_put_fvar`로 ZooGR·ZooEED·ZooEEN·ZooMRD·ZooMRN·DetRR·wPhy·wDet의 ng 원소를 동명 변수에 기록(63–65·68–70·73–75·78–80·83–85·88–90·93–95·98–100). 각 호출의 시작·개수는 `(/0/)`이며 `pioFile = pioFile`를 전달한다. 오류 조건은 `IF (FoundError(exit_flag, NoError, __LINE__, MyFile)) RETURN` (66·71·76·81·86·91·96·101)이다. 마지막 행은 wDet 오류 검사이다(101). 이 파일은 매개변수 값의 계산·범위 제한 없이 출력만 수행한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–101: 이 파일의 출력 매개변수 이름에는 PARfrac가 없다.
