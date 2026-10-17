# FUNWAVE 노트 반영분 표본 검증 (2026-10-18)

- 표본: 노트에 이번에 추가된 줄(기존 노트 git diff + 줄과 새 노트 3개)에서 무작위 30줄(표 행 22, 본문 8, 시드 `FW-notes-10-18`). 검증: sonnet(Claude 하위 작업). 코드 인용과 쪽 이미지(3.0 p.21·36·44, 2.1 p.25·33)를 직접 열었다.
- 결과: OK 28, 부분 2, 틀림 0.
  - `funwave-infrastructure.md:252` (FV2-319) 부분: "FroudeCap=10은 중첩 예제 지정값"을 표본 검증자가 확인하지 못했다. Claude 확인: 2.1 매뉴얼 p.71–72 §5.6 중첩 예제(Grid_A/Grid_B) 입력 목록에 `FroudeCap = 10.0`이 있다(판독 기록 `read/FUNWAVE/FUNWAVE-TVD/doc/funwave_tvd_2.1_manual.pdf/p055-077.md`). 노트가 맞다.
  - `funwave-user-manual-full.md:370` (FI1-317) 부분: 노트가 자기 노트의 반영 전 줄 `manual-notes/funwave-user-manual-full.md:232`("그외 포맷 개발중 (p.44)")을 현재 줄처럼 인용했다. 반영 작업이 그 줄을 고쳐 현재 232행은 다른 제목이다.
- 같은 유형 전수 확인(Claude): 노트가 노트 줄을 `경로:줄` 뒤 인용문과 함께 가리킨 곳을 모두 기계로 대조했다. 인용문이 현재 파일이 아니라 반영 전 파일(HEAD)의 그 줄과 맞는 곳 66곳(64줄, user-manual-full 29, infrastructure 10, code-graph 7, gpu-source 5, physics-sources 4, source-map 3, flux-tvd 2, build-and-blackwell-port 2, dispersion-solver 1, foundational-papers 1 등)을 `HASH:models/FUNWAVE/<노트>:줄`(반영 전 노트 줄) 형식으로 바꾸고 `[10-18 표본 정정]`을 붙였다. HASH는 그 노트의 반영 전 마지막 커밋이다. 인용문 없이 "§4 FV1-550에 인용했다"처럼 보고서를 가리키는 설명 문장은 그대로 두었다.
