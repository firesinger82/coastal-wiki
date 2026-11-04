---
file: models/Celeris/raw/source_code/Celeris-WebGPU/README.md
lines: 90
sha256: 181b223e1de3ab668692297c957a7a9483caa695cc09b6cf338fa508f0605561
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# README.md — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `Celeris-WebGPU`는 WebGPU로 확장 Boussinesq 방정식을 계산하는 실시간 연안 파랑 브라우저 앱이라고 소개한다(1–7). 원 Celeris 개발자는 Sasan Tavakkol이며 Patrick Lynett의 지도 아래 개발했다고 적는다(7). 사용자 지형·파랑 입력, 내장 예제, 일시정지·재개·표시 조절을 지원한다고 설명한다(9). 관리자는 Patrick Lynett (`University of Southern California`), 라이선스는 `MIT License`, 지원 기관은 `U.S. Army Corps of Engineers (ERDC)`, `Office of Naval Research (ONR)`, `National Science Foundation (NSF)`다(11). 원문은 open-source 앱이라고 명시한다(7). 파랑 예시는 wind waves·tsunamis·harbor oscillations다(7). 호환 브라우저 외 추가 소프트웨어 설치가 필요 없다고 설명한다(7). 대상 사용자는 연구자·엔지니어·관심 사용자다(9). 내장 예제는 실제 장소에 기반한다(9). 실행 중 매개변수 변경은 탐색 분석과 교육 시연을 지원한다(9). 커뮤니티 기여를 환영하며 아래 `Contributing` 절을 안내한다(11). [11-04 전수 검증 보완] |
| 13–26 | 기능 목록은 `Nonlinear Shallow Water (NLSW)`/Boussinesq 계산·쇄파·처오름·침수, 구성 JSON·지형·선택 파랑/마찰/영상 입력, Ventura Harbor (CA)·Santa Cruz Harbor (CA) 예제, `Explorer 3D view`, Courant·쇄파 조절이다(15–19). JPEG, GIF `up to ~100 frames`, 단일 `2D` 장 또는 시계열 스택 `up to 256 time steps`의 이진 출력을 적는다(20–23). 사용자 `3D model JSON`을 불러오며 JavaScript·WGSL·WebGPU로 클라이언트에서 실행한다고 설명한다(24–25). 구성 JSON은 simulation parameters와 domain settings를 담는다(16). 지형 파일은 elevation 격자다(16). 예제는 드롭다운에서 선택한다(17). Ventura Harbor (CA)는 wind waves 예제이며 Santa Cruz Harbor (CA)는 tsunami 예제다(17). 표시 변수는 water surface elevation·flow velocity·vorticity·wave height statistics 등이며 dynamic color map을 쓴다(18). `Explorer 3D view`는 원근 탐색을 제공한다(18). reset은 메모리를 비우고 새 시나리오를 로드한다(19). 이진 출력은 MATLAB 등 외부 분석용이다(23). `3D model JSON`은 구조물이나 landmark를 3D 화면에 추가한다(24). plugin이나 설치는 필요 없다(25). [11-04 전수 검증 보완] |
| 27–52 | 실행 주소는 `https://plynett.github.io/`다(33). 브라우저 요구는 `Chrome 113+`, `Edge`, 또는 WebGPU가 활성화된 Chromium이다(35). `Load Pre-configured Examples`·`Run Example Simulation` 또는 `Start Here: Load Simulation Datafiles`를 안내한다(36). `Configuration JSON`·`Bathymetry Data`는 `required`, `Wave Forcing Data`·`Friction Map`·`Overlay Image`·`3D Model JSON`은 `optional`이다(37–42). `Start Simulation` 이후 줌·이동·`3D Explorer`·일시정지·재개·표시·수치 매개변수 조절·출력을 할 수 있다. `Clear Memory / Reset Simulator`로 새 사례를 로드한다(43–51). 실행 주소는 저장소의 GitHub Pages 배포다(31). 수치 매개변수 예시는 flux limiter와 Courant number다(49). 출력 종류는 snapshots·GIFs·JPEG stacks·raw binary data다(50). [11-04 전수 검증 보완] |
| 53–74 | 로컬 실행 명령은 `git clone https://github.com/plynett/plynett.github.io.git` (56), `cd plynett.github.io` (57), `python -m http.server 8000` (58)이다. `http://localhost:8000`을 WebGPU 브라우저에서 열며 빌드 없이 변경 후 새로고침한다고 적는다(61). 기여 절차는 포크·브랜치, `python -m http.server` (68), 여러 시나리오·브라우저 시험, 커밋·푸시, `plynett/plynett.github.io` 대상 pull request다(67–71). `CONTRIBUTING.md`를 안내한다(73). 기여 유형은 bug fix·new feature·documentation improvement·example scenario다(65). 커밋 메시지는 명확하게 쓰며 자신의 fork로 push한다(70). `CONTRIBUTING.md`에는 issue templates와 code style을 포함한 전체 지침이 있다(73). [11-04 전수 검증 보완] |
| 75–90 | 지원은 `Lynett Wave Research Forum` (`https://www.sqrtgh.com/forum`)과 GitHub issue다(77–78). `MIT License`와 `LICENSE`를 안내한다(80–82). 원 Celeris의 Sasan Tavakkol·Patrick Lynett, `USACE ERDC`, `ONR`, `NSF`, 기여자에게 감사를 적고 끝낸다(84–90). Forum은 사용 질문용이며 GitHub issue는 bug·feature용이다(77–78). 감사 대상 기여자는 시험·문제 보고·개선에 참여한 사람이다(88). 끝인사는 `Happy wave modeling!`이다(90). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
