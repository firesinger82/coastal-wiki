---
file: models/SWAN/raw/manuals/website/features/features.htm
lines: 127
sha256: 0ebdaeddb796cfb766c1080779e1b9e3dd5099d19151dbd637c85d201590dfde
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# features.htm — 판독 구간 기록

구간은 1행부터 127행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | Features of SWAN / 문서 머리말 — HTML 제목과 표 기반 페이지 배치를 포함한다(1–23). SWAN·SourceForge 그림을 참조하지만 두 로컬 사본은 그림 파일 없음이다(14–16). 그림을 열지 못했다. 기능 제목을 제시한다(25). |
| 28–57 | Physics — 이 페이지는 시간·공간 파랑 전파(wave propagation), 천수, 흐름·수심에 의한 굴절, 흐름·비정상 수심에 따른 주파수 이동(frequency shifting)을 나열한다(34–39). 바람에 의한 파랑 생성(wave generation by wind), 3파·4파 상호작용, 백파 소산·저면 마찰·수심 유발 쇄파(depth-induced breaking)를 나열한다(40–45). 수생 식생(aquatic vegetation)·난류 흐름·점성 유체 진흙(viscous fluid mud)에 의한 소산, 파랑 수위 상승, 실험실부터 전 지구 규모까지 전파, 장애물 투과(transmission)·정반사(specular reflection)·확산 반사(diffuse reflection), 회절을 나열한다(46–53). 원문: `            <li>Wave propagation in time` (34); `              and space, shoaling,` (35); `              refraction due to current` (36); `              and depth, frequency` (37); `              shifting due to currents` (38); `              and non-stationary depth.` (39); `            <li>Wave generation by wind.` (40); `            <li>Three- and four-wave` (41); `              interactions.` (42); `            <li>Whitecapping, bottom` (43); `              friction and depth-induced` (44); `              breaking.` (45); `            <li>Dissipation due to aquatic vegetation, turbulent flow and viscous fluid mud.` (46); `            <li>Wave-induced set-up.` (47); `            <li>Propagation from` (48); `              laboratory up to global` (49); `              scales.` (50); `            <li>Transmission through and` (51); `              reflection (specular and diffuse) against obstacles.` (52); `		<li>Diffraction.</li>` (53). |
| 58–84 | Computations — 규칙 격자·곡선 격자·삼각형 망(triangular mesh)을 직교 또는 구면 좌표계에서 사용할 수 있다고 설명한다(61–65). 중첩 계산(nested run)은 SWAN·WAVEWATCH III·WAM 입력을 사용할 수 있다고 설명한다(66–68). 직렬(serial)은 한 프로세서, 병렬(parallel)은 여러 프로세서에서 한 SWAN 프로그램을 실행한다고 설명한다(70–75). 병렬 전략은 MPI 분산 메모리(distributed memory)와 OpenMP 공유 메모리(shared memory)이다(77–80). 원문: `        <td colspan="2">SWAN` (61); `          computations can be made on a` (62); `          regular, a curvilinear` (63); `          grid and a triangular mesh in a Cartesian or` (64); `          spherical coordinate system.` (65); `          Nested runs, using input from` (66); `          either SWAN, WAVEWATCH III or` (67); `          WAM can be made with SWAN.<br>` (68); `          <br>` (69); `          SWAN runs can be done serial,` (70); `          i.e. one SWAN program on one` (71); `          processor, as well as` (72); `          parallel, i.e. one SWAN program on more than one processor. For the latter, two` (73); `          parallelization strategies are` (74); `          available:` (75); `          <ul>` (76); `            <li>distributed-memory` (77); `              paradigm using MPI and` (78); `            <li>shared-memory paradigm` (79); `              using OpenMP.</li>` (80). |
| 85–117 | Output quantities — 출력은 표·지도·시계열(timeseries)이 든 수치 파일이라고 설명한다(89–93). 1차원·2차원 스펙트럼, 유의파고(significant wave height)·파주기(wave period), 평균 파향(average wave direction)·방향 퍼짐, 스펙트럼 소스항(spectral source term), 저면 부근 궤도 운동(orbital near-bottom motion)의 제곱평균제곱근(root-mean-square), 소산, 복사응력(radiation stress) 경사에 근거한 파랑 힘(wave-induced force), 파랑 수위 상승, 회절 매개변수를 나열한다(95–112). 목록 끝은 추가 출력이 있음을 명시한다(113). 원문: `            <li>one- and two-dimensional` (95); `              spectra,` (96); `            <li>significant wave height` (97); `              and wave periods,` (98); `            <li>average wave direction` (99); `              and directional spreading,` (100); `            <li>one- and two-dimensional` (101); `              spectral source terms,` (102); `            <li>root-mean-square of the` (103); `              orbital near-bottom` (104); `              motion,` (105); `            <li>dissipation,` (106); `            <li>wave-induced force` (107); `              (based on the` (108); `              radiation-stress` (109); `              gradients),` (110); `            <li>set-up,` (111); `            <li>diffraction parameter,` (112); `            <li>and many more.</li>` (113). |
| 118–127 | Limitations / 문서 종료 — SWAN은 파랑 터널링(wave tunneling)을 고려하지 않는다고 명시한다(121–122). 이어 셀·표·본문 종료 마크업을 포함한다(123–127). 원문: `        <td colspan="2">SWAN does not` (121); `          account for wave tunneling.` (122). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14–17행: 두 `<td>`는 각각 14행과 16행에서 닫힌다. 그 뒤 17행에 추가 `</td>`가 있다.
- 14행: `https://swanmodel.sourceforge.io/platen/swanlogo.jpg` 참조는 그림 파일 없음. 로컬 대응 경로 `models/SWAN/raw/manuals/website/platen/swanlogo.jpg`에 파일이 없다. 그림 내용은 열어 확인하지 못했다.
- 15행: `http://sflogo.sourceforge.net/sflogo.php?group_id=384349&amp;type=13` 참조는 그림 파일 없음. 문서 사본 폴더에서 이 외부 그림의 로컬 사본을 찾지 못했다. 그림 내용은 열어 확인하지 못했다.
