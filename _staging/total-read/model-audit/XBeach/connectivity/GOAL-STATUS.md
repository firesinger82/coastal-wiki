# XBeach 完了 목표 추적

2026-09-11 사용자 요청으로 GOAL 활성화: XBeach 전수 판독 → 연결 분석 → 검증 → canonical → 필요한 신규 HG를 끝까지 진행한다. 기준은 plan.md의 기존 전수 판독/연결 계획이다. 전체 gate는 NOT_PASSED이며 아래는 완료 영수증이 아니다.

- DOCX Native 486개: 현재 463개 기계적 수용. 색상 0 참조 12개·RULER 불일치 8개·Master 3개는 길이 있는 확장 payload를 보존하고 본문 구조를 판독했으나 payload 의미는 미해결. 색상/정렬 20개도 별도 진단 옵션으로 구조를 확보했으나 strict에서는 계속 거부한다. 전체 486개 구조 대응은 strict 463 + opaque 3 + 조건부 20이다. 조건부 20개 원본 WMF는 전량 시각 대조했다. 세 침투식의 연산자 부재는 현재 코드의 +1 관계와 대조했고 원본 표기는 그대로 보존했다. 암시적 시간 이산화 및 제한 조건 차이를 기록했다. 수용된 식도 전체 의미/렌더 대조는 별도다.
- 비정수압 보고서 DOC: 388개 Native 전체 구조 판독. 새 두 스트림의 Euclid Math Two/F093 글리프는 시각/의미 미확정. 작은 글리프/inline 배치 및 의미 대조 필요.
- ZIP/JAR: 과거 unread 1,284개 경로는 고유 Java 413종/Python 150종. Java 역어셈블리 전체를 준비했으며 현재 launcher·입출력·SLOG2 구조·시간/좌표·Drawable·InfoBox 등 207종(동일 SHA 722경로)을 직접 읽었다. 나머지 Java 206종·Python 150종과 PE/AR/MSI 내부 처리 범위는 미완료다. 단순 인덱스/중복 SHA를 판독 완료로 바꾸지 않는다.
- 기존 lifecycle/physics 연결 후보: 판독 전제 충족 후 entry/build/mode 및 orphan/unknown을 검증하고 확정한다.
- canonical: 기존 승인 103개·crosswalk·closure 불변 보존. 새 분석 결과의 검토본을 만들고 기존 절차에 따라 반영한다.
- 필요한 외부 검토·사람 승인: 결과물을 먼저 준비한다. 기존 승인을 새 주장에 재사용하거나 자기 승인하지 않는다.
- FUNWAVE: XBeach 완료 전에는 기존 읽기 전용 preflight 상태 유지.

상세 증거와 재현 명령은 RESUME.md, 최신 기계 검증은 resume-validation.json에 있다. GOAL은 위 모든 필수 작업이 종결되기 전까지 active로 유지한다.

2026-09-12 추가: base/io 9종 465줄을 직접 읽고 동일 SHA 54경로에 결속했다. 누적 Java 13/413종(66경로), Python 150종 미판독. [입출력 판독](bytecode-read/base-io-read.json). 전체 gate NOT_PASSED·GOAL active.

2026-09-12 후속: SLOG2 헤더·디렉토리 7종 전체 판독. 누적 Java 20/413종, 남은 Java 393종/Python 150종. [근거](bytecode-read/slog2-header-read.json). 전체 gate NOT_PASSED.
