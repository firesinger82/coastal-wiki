# 내용 검토 반영

- Fable 결과: 성공, 새 차단/중요 오류 없음. 실제 modelUsage에 주 검토 모델 `claude-fable-5-1` 확인. `claude-haiku-4-5-20251001`은 CLI 보조 호출로 함께 기록되어 있으며 Opus 대체는 없다. 원본 JSON과 모델 영수증 보존.
- 비차단 NAO 보완: README §2/§5가 설명하는 radial loading의 전지구 0.5° 제품과 지역 모델 부재를 표에 명시했다. Fable이 제시하고 이미 확인한 원문 범위이며 Codex 최종 검토에 포함한다.
- 비차단 파일명: source-index의 PDF provenance 이름을 실제 `fes2022-handbook-provenance.json`으로 수정했다(검토 도중 이미 수정되어 현재본에 반영됨).
- pending metadata를 실제 Fable 5.1 검토 이력으로 갱신했다. 사람 승인·실제 실행/입력품질/수치/물리 검증 미발급은 유지한다.
- 최종 후보는 prepare.py 재생성본의 changes.patch/install-manifest.json이다. 검토 뒤 canonical 반영·필수 staged 훅·커밋·pull/push까지 수행한다. 논문 기준해/실제 입력 검증을 수행한 것으로 확대하지 않는다.
