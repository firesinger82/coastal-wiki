# 한정 원문 대조 — 준비 상태를 가르는 두 사례

AI의 로컬 원문 대조 관찰이다. canonical 변경·전체 판독 영수증·사람 승인으로 사용하지 않는다. 원문 해시는 [readiness.json](readiness.json)의 `evidence_sha256`, 노트 해시는 같은 파일이 참조하는 기존 snapshot에 보존한다.

## A. ADCIRC 조석 입력: 근거 재사용과 설명 정정이 함께 필요

- **재사용 근거**: `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:3405–3456`을 직접 확인했다. `NBFR` 다음 분조별 `BOUNTAG`, `AMIG/FF/FACE`를 읽고, 이후 분조별 `ELEVALPHA` 및 `J=1..NETA`의 `EMO/EFA`를 읽는다. 이미 있는 두 조석 노트의 입력 블록 설명에 대응한다. 이 코드 블록만으로 외부 DB에서 값을 추출하는 절차나 DB 위상규약까지 입증하지 않는다.
- **정정 대상**: [forcing-implementation](../../models/ADCIRC/source-analysis/tide/adcirc-tide-forcing-implementation.md) 146행의 “`ETRF=0` … full tidal potential applied” 설명.
- **직접 원문**: `models/ADCIRC/raw/source_code/adcirc/src/timestep.F:1518–1557`. 1536행은 `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`이다. `tidePotential%active()`가 거짓인 전통적 분조 계산 경로에서 1554행은 이 계수를 퍼텐셜 항에 곱해 `TIP2`에 더한다. 해당 분조의 `ETRF(J)=0`이면 그 항의 계수가 0이 된다. “감쇠를 없애 전체 퍼텐셜 적용”이라는 해석과 반대다.
- **조건 보존**: 별도 `SALTMUL`은 이 곱과 분리되어 있고, `tidePotential%active()`가 참이면 앞에서 full-formula 퍼텐셜을 계산하는 다른 경로가 있다. 그 경로 내부의 ETRF 적용 여부는 이번 범위에서 미확인이다. 따라서 `ETRF=0`이 모든 퍼텐셜·SAL·개방경계 조석을 끈다고 일반화하지 않는다. 다음 정정안에서는 기존 노트가 함께 인용하는 1501–1503행도 대조한다.
- **미확정 유지**: 같은 노트 106행 ETRF 표준 수치, [harmonic-prep](../../models/ADCIRC/source-analysis/tide/adcirc-tide-harmonic-prep.md) 115행 외부 DB 위상규약·182–183행 지역 성능/SAL 정량은 이미 source-needed이다. 이번 로컬 코드 확인은 그 외부 주장의 근거를 채우지 않는다.
- **처분**: 다음 ADCIRC 두 노트 보강에서 조건부 정정안을 검토한다. 이번에는 원본 노트를 바꾸지 않았다.

## B. SWASH 쇄파: 모델 설명에 있는 조건이 비교표에서 사라짐

- **비교표**: [쇄파 비교](../../concepts/waves/wave-breaking-cross-model.md) 46행은 `α 0.6 / β 0.3`을 표시하고 56행도 `β 0.3`을 사용한다.
- **기존 모델 근거**: [swash-wetting-drying-runup](../../models/SWASH/source-analysis/swash-wetting-drying-runup.md) 78행은 beta=-1 초기 표식을 CheckPrep에서 해석하며 BDF 조건에서는 0.15, 그 외에는 0.3이라고 설명한다. 비교 노트 자체 65행에도 이 조건은 이미 적혀 있다.
- **직접 원문**: `models/SWASH/raw/source_code/swash/src/SwashCheckPrep.ftn90:1060–1092`. `isurf==1`에서 `pnums(6)==3`, `pnums(7)==-1`, `psurf(2)==-1`이면 1078행 `psurf(2)=0.15`; 그 외 아직 -1이면 1082행 `=0.3`. 앞선 1065–1068행에서는 beta가 양수도 -1도 아니면 경고 후 0.3으로 바꾼다. 명시 입력한 양의 beta를 이 자동선택으로 덮는다는 뜻은 아니다.
- **처분**: 새로운 모델 자료 전수 수집보다, 이미 검토된 조건을 비교표와 같은 노트의 요약 문장에 일관되게 전달하는 정정이 필요하다. 다른 쇄파 옵션의 공개 갭까지 해소했다고 보지 않는다.

## C. 원문을 새로 판독하지 않은 나머지 관찰

[연직혼합 비교](../../concepts/currents/vertical-mixing-cross-model.md) 60행은 ADCIRC MY2.5 안정함수·표면/저면 q² 경계식을 미커버로 명시한다. [저면마찰 비교](../../concepts/currents/bottom-friction-cross-model.md) 73행도 ADCIRC의 남은 갭을 밝힌다. 이는 기존 문서에 공개된 상태를 옮긴 것이며 이번에 해당 솔버를 새로 검증한 결론이 아니다.

ADCIRC manifest의 초기 PDF 미수집 기록, SWASH README의 초기 노트 수 표, SFINCS 초기 sha 미기록과 이후 Galibier 확정 기록은 현황을 읽을 때 시점을 구분해야 하는 사례다. 이 조사에서는 원본·manifest·모델 README를 자동 수정하지 않았다.
