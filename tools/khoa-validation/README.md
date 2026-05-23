# tools/khoa-validation/

`experience/khoa-multi-station-tide-validation-2026.md` 재현용 스크립트와 결과.

## 파일

| 파일 | 역할 |
|---|---|
| `fetch_khoa_tide.py` | KHOA OpenAPI에서 정점 1년치 조위 다운로드 (모든 정점 호출) |
| `fetch_one.py` | 단일 정점 다운로드 — `launch_parallel.sh`가 5-worker로 호출 |
| `launch_parallel.sh` | 5개 worker 병렬 실행 launcher (15 정점 ~30분) |
| `analyze_utide.py` | UTide 조화분해 → 분조 진폭/위상 → KHOA 공식값 비교 |
| `logs/` | fetch 실행 로그 (정점별 시간·결측 정보) |
| `results/` | 정점별 분석 결과 JSON + `ALL_RESULTS.json` 통합 |

## 재현 절차

1. **사전 요구사항**:
   - Python 3 + 가상환경 (`utide`, `pandas`, `numpy`)
   - KHOA OpenAPI 키 (data.go.kr 가입 발급)

2. **환경 변수**:
   ```bash
   export KHOA_API_KEY="<your key>"
   ```

3. **실행**:
   ```bash
   cd ~/coastal-wiki/tools/khoa-validation
   mkdir -p data results
   ./launch_parallel.sh        # 15 정점 1년 조위 다운로드 (~30분, 병렬)
   python analyze_utide.py     # 조화분해 → results/ALL_RESULTS.json
   ```

4. **결과 검증**:
   - 본 디렉토리의 `results/ALL_RESULTS.json` (2026-05-21 실행분) 과 비교
   - 분조 진폭 ±0.1% 이내면 재현 성공

## data/ 제외 사유

`.gitignore`에 `data/` 등록 — raw CSV 약 7.7MB. KHOA OpenAPI 호출로 재다운 가능하므로 git에 포함하지 않음. `launch_parallel.sh` 실행 시 자동 생성됨.

## 정점 list (15)

DT_0001 인천, DT_0004 안산, DT_0005 부산, DT_0006 군산, DT_0007 묵호, DT_0008 평택, DT_0009 여수, DT_0010 통영, DT_0011 거제도, DT_0012 진도, DT_0013 목포, DT_0014 서귀포, DT_0015 제주, DT_0016 모슬포, DT_0017 흑산도

(자세한 정점 정보는 `fetch_one.py` PORTS dict)
