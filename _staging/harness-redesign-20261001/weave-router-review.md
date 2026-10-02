# weave-os/router 도입 검토 (2026-10-02, Claude)

대상: https://github.com/weave-os/router — Go, Apache-2.0, ★5,488, 2026-04-27 생성, 2026-10-01 갱신. README·install/npm/README 기준(코드 미판독).

## 무엇인가
Anthropic·OpenAI·Gemini 호환 드롭인 프록시. 요청(action)마다 로컬 임베더 + 클러스터 점수기(Avengers-Pro 계열)로 "맞는 모델"을 골라 보냄. 목적: 비용 40–70% 절감. 호스티드(npx 한 줄, Weave 서버 경유) 또는 자체 호스팅(Postgres+대시보드). OTLP 트레이스. Claude Code 설치 시 `~/.claude/settings.json`(또는 프로젝트 settings.json)을 패치해 라우터로 보냄. 구독 계정 등록·Codex ChatGPT OAuth 보존 지원.

## 판정: 도입 안 함 (권고)
1. **푸는 문제가 다르다.** 우리 실패(목적 이탈·자기 완료 선언·지시만 있는 규칙)는 계약·증거·검증자 분리 문제. 라우터는 모델 선택·비용 최적화 — 계약/승인/receipt 기능 없음.
2. **현 규칙과 정면 충돌.** CLAUDE.md "Claude 모델 지정: 자동 fallback 금지 — 다른 모델로 대체하지 않고 실제 응답의 모델 정보 확인", 작업별 모델 배정(판정 gpt-6.1-sol / 검증 gpt-6-astra). 요청마다 모델을 자동으로 바꾸면 이 결속이 깨짐.
3. **검증자 독립성을 해칠 수 있다.** 새 하네스의 핵심 하나가 "판정과 다른 계열 검증자"인데, 라우터가 검증 요청을 같은 계열로 보낼 수 있음.
4. **설정·데이터 경로 위험.** 설치가 사용자 전역 settings.json 을 패치(07-28 managed 정책 사고처럼 전 세션에 영향). 호스티드 경로는 프롬프트가 Weave 서버를 경유. 자체 호스팅은 Postgres·대시보드 운영 부담.
5. 비용·rate-limit 은 하네스 설계 동인이 아니다(resume-gate HANDOFF "확정된 설계 원칙").

## 참고할 점
- 실행마다 모델·지연·사용량을 OTLP 트레이스로 남기는 구조는 원칙 ⑪(실행 기록)에 참고 가능. 단 Claude Code 자체 OpenTelemetry 와 codex-run 래퍼 로그로 충분 — 별도 프록시 불필요.
