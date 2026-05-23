# SYNC.md — 다른 PC에서 이어가기 가이드

> 단일 writer 패턴. **읽기는 모든 PC**, **쓰기는 한 PC**. Reader-pull 모델.

## 1. 1회 셋업 (writer PC, 이미 완료)

### 1.1 GitHub private repo 생성

GitHub 웹 UI에서 `coastal-wiki` private 저장소 생성. 또는 gh CLI:

```bash
gh repo create coastal-wiki --private --description "Coastal engineering domain wiki — objective layer + experience"
```

### 1.2 remote 설정 + 초기 push

```bash
cd ~/coastal-wiki
git remote add origin git@github.com:firesinger82/coastal-wiki.git
git branch -M main
git push -u origin main
```

(또는 HTTPS: `https://github.com/firesinger82/coastal-wiki.git`. SSH 권장)

## 2. 다른 PC에서 처음 받기

### 2.1 환경 요구사항

- git
- (선택) Python 3 + venv — `tools/khoa-validation/` 재실행 시
- (선택) Node.js — `data/khoa-analysis/` 추출 로직 재실행 시
- (선택) Claude Code — 위키 작업 이어가기

### 2.2 clone

```bash
# WSL2 ext4 위치 권장 (속도 5-10x)
cd ~
git clone git@github.com:firesinger82/coastal-wiki.git
cd coastal-wiki
```

### 2.3 옵션 — KHOA raw data 복원 (validation 재실행 시만)

```bash
cd tools/khoa-validation
export KHOA_API_KEY="<your key>"
mkdir -p data
./launch_parallel.sh   # 15 정점 1년 조위 ~30분
```

raw CSV는 `.gitignore` 처리. 분석 결과(`results/`)는 이미 포함됨.

### 2.4 Claude 세션 이어가기 (선택)

writer PC의 `~/.claude/session-data/2026-05-23-coastal-wiki-build-session.tmp` 를 reader PC의 같은 경로로 복사 (예: USB 또는 별도 cloud sync). 이후:

```
> /resume-session 2026-05-23
```

세션 파일은 **민감 정보 가능성** (다른 프로젝트 세션도 포함)으로 git에 포함하지 않음. 별도 동기화 권장.

## 3. 일상 워크플로 — 같은 PC에서 계속

```bash
cd ~/coastal-wiki
git pull            # 다른 PC에서 작업했을 가능성 검사
# ... 편집 ...
git add -A
git commit -m "(...)"
git push
```

## 4. PC 전환 시 — writer 이전

writer PC에서:
```bash
git status          # uncommitted 0 확인
git push            # 마지막 push
```

새 writer PC에서:
```bash
git pull            # 최신 상태 받기
# 필요 시 session.tmp 별도 복사 (3.4 참조)
```

> ⚠️ **단일 writer 원칙**. 두 PC에서 동시 편집 시 충돌 가능. PC 전환 시 명시적 push/pull 사이클 권장.

## 5. 현재 진행 상태 (2026-05-23)

### 5.1 verified 산출물

| 분류 | 항목 | 위치 |
|---|---|---|
| concepts | tides/waves/currents/sediment-transport (24 파일) | `concepts/` |
| models | SWAN README + 2 verified notes | `models/SWAN/` |
| textbook | 13 verified notes (Holthuijsen, Stewart, Soulsby, KHOA 등) | `textbook/notes/` |
| **experience** | KHOA 15정점 UTide 검증 (median 0.057%) | `experience/khoa-multi-station-tide-validation-2026.md` |
| **experience** | 한국 SLR 19년 (3.94 mm/yr 평균, 서귀포 5.42) | `experience/khoa-annual-climate-trend.md` |
| **experience** | 한국 SST 9년 (1.39 °C/decade) + SLR 정합성 | `experience/khoa-sst-warming-trend.md` |
| analysis raw | SLR/SST/M2 JSON 시계열 | `data/khoa-analysis/` |
| tools | UTide validation 재현 스크립트 | `tools/khoa-validation/` |

### 5.2 다음 권장 작업 (사용자 명시)

1. `concepts/littoral-drift/` 6 파일 (연안 표사 이동)
2. `concepts/storm-surge/` 6 파일 (폭풍해일)
3. `models/EFDC/` 채우기 (sediment-transport 06 + tides 06 unlock)
4. (선택) M2 진폭 추출 2016-2019/2023-2024 보고서 — KHOA OpenAPI 직접 사용
5. (선택) SST 2012-2016 추가 추출 — 14년 전체 시계열

### 5.3 추가 분석 후보

- 한국 wave climate 14년 추세 (각 KHOA 백서 §3.19 발췌)
- 정점별 조차 변동 (대조차·평균조차) 14년 추세
- KHOA 1968-2024 50+년 SST와 본 분석 9년 비교 — 가속화 검증
- 동해 SST 단기 변동성 origin (PDO/ENSO 분석)

## 6. 문제 시 — Troubleshooting

### 6.1 git pull conflict

다른 PC에서 작업한 흔적이 있는데 같은 파일을 수정한 경우. 충돌 마커 해결 후 commit.

### 6.2 venv 재구축

WSL2 ext4와 Windows 디스크 호환성 문제 발생 시 `.venv-tools/`는 .gitignore 되어 있으므로 새 PC에서 다시 생성:

```bash
python3 -m venv .venv-tools
.venv-tools/bin/pip install -r tools/khoa-validation/requirements.txt  # (TBD)
```

### 6.3 KHOA OpenAPI 키 분실

[data.go.kr](https://data.go.kr) → 마이페이지 → 신청한 데이터 → "조위관측소 시계열" 키 재확인.

## 7. CONVENTIONS·POLICY

위키 자체 규칙: [CONVENTIONS.md](CONVENTIONS.md), [POLICY.md](POLICY.md), [BOUNDARY.md](BOUNDARY.md).
