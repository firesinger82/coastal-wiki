# 전 모델 감사 공정표 (2026-08-31, 사용자 결정)

> 애드혹 진행 정지 → 공정표 고정. 사용자 결정: **13모델 전부 FUNWAVE 수준 '감사완료'**,
> 분모 = **전체 소스(전 언어) 100%**. 이는 total-read 본 미션(모든 모델코드 2 독립판독)의 완수.

## ★★ 절대 규칙 (2026-08-31 사용자 지시)
- **전수검사는 무조건 Codex 로 수행한다.** 모델 소스 판독(R1·R2), 결함 스캔, 재감사, 적대검증 등
  **전 파일을 실제로 읽는 모든 작업은 예외 없이 Codex 태스크**로 돌린다.
- **토큰을 많이 소모하는 파트는 무조건 Codex.** Claude(오케스트레이터)는 원본 소스를 자기 컨텍스트로
  대량 읽지 않는다 — 프롬프트 작성·작은 verdict/JSON 취합·게이트·커밋·로그검증만 담당.
- 근거: Codex 는 별도 런타임(ChatGPT측)이라 Claude 토큰과 무관하며, 12M줄 규모 판독은 Codex 전담이 유일 실현안.
- 위반 예: Claude 가 소스파일을 통째로 Read 하는 것 → 금지. 필요 시 Codex 에게 위임·요약만 수신.

## 0. 목표·완료 정의 (★허위 100% 방지)
- **모델 "감사완료" = 정의된 분모 100% × [2 독립판독 + crosswalk + 확정 delta supplement + HIGH 전건 적대검증 + 사람 게이트]** — FUNWAVE 가 유일 선례.
- **분모 = 모델 소스코드 전부**(전 언어: Fortran .f/.f90/.for/.ftn·C/C++/CUDA .c/.cpp/.cu/.h·MATLAB .m·GPU .wgsl 등). 단 P0 에서 **third-party/생성/vendored 코드 분리**(예 Delft3D .hpp 대량) — 배제는 사람 승인 하에 기록(정당한 범위획정, 자기신고 완결 아님).
- 완결 판정은 **자기신고 금지** — SPEC §80 완결게이트 준용 + 사람 승인.

## 1. 규모 (전 언어 실측 2026-08-31)
총 **34,489 파일 / 12,085,347 줄** (Delft3D 24,748·ROMS 4,664·CADMAS 1,310·ADCIRC 1,131·LISFLOOD 868·EFDC 557·FUNWAVE 277·SFINCS 241·SWASH 162·Celeris 164·ShorelineS 153·XBeach 132·SWAN 82). 12M줄 × 2read ≈ 24M줄 판독 = **다세션 프로그램**.

## 2. per-모델 파이프라인 (반복 단위, Codex 판독 전담)
| 단계 | 내용 | 툴/산출 |
|---|---|---|
| **P0 scope** | Codex 가 모델 소스트리 매핑 → 분모(포함/배제) 목록 확정 → **사람 승인** | `<M>-scope.json` |
| **R1 1차** | Codex 전 파일 semantic 판독(unresolved findings) — shard 분할 | 1차 records |
| **R2 감사** | Codex 독립 blind 판독(R1 미열람, 다른 seed) — "2 독립판독" 성립 | 감사 records |
| **CW crosswalk** | blinded 대조(벤더라벨 제거·A/B 무작위) → equivalent/confirmed_delta/... | blind_shard.py·finalize_shard.py·verify_crosswalk.py |
| **SUP supplement** | confirmed_delta 원문 span 재확인 → manifest | build_supplement_manifest.py·verify_supplement.py |
| **V verify** | 확정 HIGH 독립 skeptic 적대검증 | verify 태스크 |
| **HG 사람게이트** | supplement decisions 사용자 승인(producer 자기승인 금지) | supplement-decisions.json |
| **DONE** | 분모 100%·미read 0·HIGH 전건 검증·사람 승인 → 완료판정 | PROGRESS=DONE |

★기존 4모델 코어 결함리포트(codex-defect-reports/)는 이 공정표의 **R1 예비 스캔**으로 편입(정식 R1/R2 로 승격 필요).

## 3. 순서 (phasing — 작은 것부터, 빠른 완결 확보)
- **1진(소형 Fortran)**: XBeach 132 → SFINCS 241 → EFDC 557 → ADCIRC 1,131(단 .c 475 포함) — 각 100% 완결
- **2진(중형)**: CADMAS-SURF 1,310 → FUNWAVE 잔여 24%(스크립트 처분) 마감
- **3진(비-Fortran)**: LISFLOOD-FP(C/CUDA) → ShorelineS(MATLAB) → Celeris(WGSL/JS) — 언어별 판독 프롬프트 조정
- **4진(대형)**: ROMS 4,664 → Delft3D 24,748(third-party 분리 후) — 최장기
- SWAN 82·SWASH 162(.ftn90)는 1~2진 사이 편입

## 4. 운영 규칙 (애드혹 방지)
- ★**한 모델씩 · 스텝바이스텝 (2026-08-31 사용자 지시).** 여러 모델 동시 진행 금지. 한 모델의 P0→R1→R2→CW→SUP→V→HG 를 순차로 끝낸 뒤 다음 모델. 각 단계도 순차(다음 단계 전 결과·게이트 확인). **주간한도(Codex/ChatGPT측)·5시간 윈도우(Claude측)를 살피며** 진행 — 한도 근접 시 중단·재개.
- 한 모델 내 R1/R2 shard 는 소수 병렬 가능하나, 전체 페이스는 한도 모니터링에 맞춘다.
- Codex 태스크: 배치 15-20파일. **완료판정은 companion status:completed+로그로만**(rescue 포워더 알림은 완료 아님).
- 매 태스크 **로그 sed/nl/rg real-read 검증 + 중립화 refute 확인**.
- 확정 HIGH 는 **반드시 독립 skeptic 적대검증**(REFUTE 시도) 통과분만.
- Claude = 오케스트레이션·기록·게이트만(토큰 경량). Codex = 판독 전담(별도 런타임).
- 추적: codex-defect-reports/PROGRESS.md 단일 표(모델·분모·scope확정·R1·R2·CW·SUP·V·HG·%·상태).

## 5. 완료 게이트 (모델별, 전부 참일 때만 DONE)
1. P0 분모 사람 승인(배제목록 명시)  2. R1·R2 2 독립판독 100% 파일  3. CW verify PASS(유실0)
4. confirmed_delta span 재확인  5. HIGH 전건 적대검증  6. supplement 사람 승인  7. PROGRESS·리포트·커밋 동기

## 6. 리스크·정직 공시
- 규모: 12M줄·24M read → 수 세션. Codex 처리량·요금(ChatGPT측)·필터(가끔 cyber-flag) 변수.
- Delft3D .hpp 16,504 등 third-party 배제 없으면 비현실적 — P0 분리 필수.
- 비-Fortran(C/CUDA/WGSL/MATLAB)은 판독 프롬프트·결함 클래스 조정 필요.
- 이 공정표는 santa-method 로 Codex 적대검증 후 확정 권장.
