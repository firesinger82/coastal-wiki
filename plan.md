# coastal-wiki 초기 구조 결정 기록

작성: 2026-05-21
작성자: Claude Opus 4.7 (1M context) + 사용자 합의

## 목적

연안공학 도메인 지식의 **객관 레이어**를 단일 writer 위키로 관리. `D:\Study\textbook` 교과서 자료와 EFDC/ADCIRC/XBeach/Delft3D 모델 자료를 통합해 도메인 개념 중심 구조로 정리. 개인 경험은 객관화 검증 통과 후 별도 레이어로 추가.

## 결정사항

### 1. 위치: `~/coastal-wiki` (WSL2 ext4)

- 초기에 `D:\coastal-wiki`(=`/mnt/d/coastal-wiki`)로 생성했으나 2026-05-21 WSL ext4(`/home/firesinger/coastal-wiki`)로 이전.
- 이유: I/O 성능 (git/grep 5~10배), AI 주 작성자 워크플로 적합. Windows 앱(Obsidian 등)은 `\\wsl$\Ubuntu\home\firesinger\coastal-wiki`로 접근.
- 대안 검토:
  - (A) `/mnt/d/coastal-wiki` 유지 — 거부. 9P 프로토콜 오버헤드 + AI 워크플로 효율 손실.
  - (B) modeling-wiki 안에 신규 디렉토리 — 거부. 객관/경험 축 분리 흐려짐.
  - (C) modeling-wiki를 coastal-wiki/experience/로 이전 — 보류. 객관 레이어 자리 잡은 후 결정.

### 2. 구조: concepts 중심, models 부축

```
coastal-wiki/
├── concepts/                # 1차 축: 도메인 개념
│   └── <topic>/
│       ├── 01-concept.md
│       ├── 02-theory.md
│       ├── 03-analysis-methods.md
│       ├── 04-code-and-tools.md
│       ├── 05-examples.md
│       └── 06-model-application.md
├── models/                  # 2차 축: 모델 객관 자료
│   └── <model>/
│       ├── source-analysis/
│       ├── manual-notes/
│       └── web-refs/
├── textbook/                # D:\Study\textbook 통합 노트
├── examples/                # 통합 실습
└── experience/              # 검증 통과 경험 (지금 비움)
```

- 이유: 사용자 명시 — "조석이면 조석에 대한 개념·일반론·분석방법·코드까지 쫘악 정리되고 이걸 기반으로 예제 학습도 가능하고 실제 모델 적용까지 이어지게". 도메인 우선, 모델은 적용 단계.

### 3. textbook 통합: 원본은 D:\Study\textbook 유지, wiki는 노트만

- 이유: PDF는 git에 부담 (LFS 도입 회피). 교과서 자료는 변경 없음 → 원본 위치 안정.
- 방식: `textbook/notes/<topic>-<source>-chN.md` 형식으로 챕터별 발췌·요약. 상단에 `Source: D:\Study\textbook\<file> p.NN` 명시.

### 4. 파일·디렉토리 명: 영문, 본문: 한·영 자유

- 이유: git/cross-PC 안전 (한글 디렉토리는 Windows/WSL/Linux 간 인코딩 이슈 가능성).

### 5. 객관-경험 분리

- `concepts/`, `models/`에는 "내가 해보니" 화법 금지.
- 모든 단언에 출처(소스코드 file:line / 메뉴얼 페이지 / 논문 / 교과서 챕터) 인용 필수.
- 경험은 `experience/`에 들어가되 3조건 (반복 관찰, 객관 데이터 근거, 재현 가능) 모두 만족 시에만.

### 6. 동기화: git + 단일 writer

- writer = 이 PC (`~/coastal-wiki` = WSL2 ext4. Windows 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki`)
- reader = 다른 PC (git clone 후 pull)
- private repo로 push (GitHub/GitLab) — 다음 단계에서 결정

### 7. 워크플로

큰 변경 시: `plan.md` 작성 → `/codex:adversarial-review` → 반영 → 구현 → `/codex:review`

## 미결 사항

- textbook 자료 13권 중 어느 것부터 노트화할지 우선순위
- private repo 호스팅(GitHub/GitLab/self-hosted) 결정
- experience/ 레이어 도입 시점 (객관 레이어가 얼마나 채워진 후)
- modeling-wiki 통합 여부

## 검증 권장

다음 단계: `/codex:adversarial-review`로 이 구조 비판 검토.
