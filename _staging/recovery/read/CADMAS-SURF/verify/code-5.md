# CADMAS-SURF code-5 전수 대조

대상 기록 24개를 완료했다. 구간 표 115행을 원문 5,108행과 대조했다. 후속 코드 사실 44행도 대조했다. 이 수치는 아래 기록별 집계에서 합산했다.

원문은 각 기록 frontmatter의 `file:` 경로다. 원문 구간은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다. 한 번의 원문 출력은 200행 이하로 제한했다. 조건·대입식·선언·호출 인수·연속문·일본어 주석의 인용을 확인했다. 한국어 요약의 조건·부호·순서·수량·랭크와 바깥 블록의 종료 행을 대조했다.

물리적 뜻을 확인할 때 같은 원문 디렉터리의 `VF_APHYSR.h:1–110`을 보조 근거로 읽었다. 이 문서의 짧은 파일명과 원문 행은 해당 원문 디렉터리를 기준으로 한다.

기록의 frontmatter와 구간 경계는 유지했다. 대상 원문의 SHA-256은 frontmatter 값과 모두 일치한다. 원문을 수정하지 않았다. 노트와 git을 수정하지 않았다. 모델을 실행하지 않았다.

마지막 집계의 단위는 구간 표 행과 후속 코드 사실 행이다. 같은 행에 정정과 보완이 함께 있으면 각각 한 번 센다. 이상 없음은 정정과 보완이 모두 없는 대조 행 수다. 정정·보완 목록은 같은 행의 서로 다른 수정 사항을 나누어 적을 수 있다.

| 기록 | 상태 | 대조한 구간 표 행 | 대조한 후속 사실 행 | 대조한 원문 행 |
|---|---|---:|---:|---:|
| [vf_fseabt.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_fseabt.f.md) | 완료 | 7 | 4 | 326 |
| [vf_fslp2a.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_fslp2a.f.md) | 완료 | 3 | 2 | 119 |
| [vf_fslp2f.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_fslp2f.f.md) | 완료 | 2 | 1 | 77 |
| [vf_fslp3a.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_fslp3a.f.md) | 완료 | 6 | 2 | 283 |
| [vf_fslp3f.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_fslp3f.f.md) | 완료 | 5 | 1 | 194 |
| [vf_hsort.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_hsort.f.md) | 완료 | 3 | 3 | 122 |
| [vf_ii1inp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_ii1inp.f.md) | 완료 | 7 | 3 | 543 |
| [vf_iiboun.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iiboun.f.md) | 완료 | 9 | 2 | 517 |
| [vf_iicomp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iicomp.f.md) | 완료 | 3 | 1 | 124 |
| [vf_iidbg.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iidbg.f.md) | 완료 | 3 | 1 | 87 |
| [vf_iiequa.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iiequa.f.md) | 완료 | 2 | 0 | 70 |
| [vf_iifile.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iifile.f.md) | 완료 | 10 | 2 | 488 |
| [vf_iigrid.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iigrid.f.md) | 완료 | 4 | 2 | 150 |
| [vf_iimate.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iimate.f.md) | 완료 | 4 | 1 | 139 |
| [vf_iimdl.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iimdl.f.md) | 완료 | 7 | 3 | 320 |
| [vf_iiobst.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iiobst.f.md) | 완료 | 2 | 0 | 64 |
| [vf_iiopt.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iiopt.f.md) | 완료 | 5 | 1 | 187 |
| [vf_iipara.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iipara.f.md) | 완료 | 2 | 1 | 57 |
| [vf_iiporo.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iiporo.f.md) | 완료 | 7 | 2 | 258 |
| [vf_iitime.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_iitime.f.md) | 완료 | 3 | 1 | 74 |
| [vf_im1inp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_im1inp.f.md) | 완료 | 5 | 1 | 201 |
| [vf_im2inp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_im2inp.f.md) | 완료 | 5 | 1 | 201 |
| [vf_ip1inp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_ip1inp.f.md) | 완료 | 4 | 3 | 140 |
| [vf_ir1inp.f.md](../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source%20code/vf_ir1inp.f.md) | 완료 | 7 | 6 | 367 |
| 합계 | 완료 | 115 | 44 | 5108 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_fseabt.f.md:1–50 | GGV를 구간 근거 없이 공극률로 단정; 변경 표시 누락 | GGV 뜻의 근거 한계 명시; 변경 표시 보완 (정정,보완) | 23–31,39–42 |
| vf_fseabt.f.md:101–137 | 바깥 IF 이름만 표기; TIM1 이전; GOTO 대상·ELSE 부재 누락 | 조건식·종료 행·동등 경계·분기 구조 보완 (정정,보완) | 55–56,104–135 |
| vf_fseabt.f.md:138–194 | IF 사슬의 ELSE 부재 미표기 | IERR=0일 때 해당 사슬의 처리 없음 명시 (보완) | 187–192 |
| vf_fseabt.f.md:195–244 | ELSE 부재·변경 표시 누락 | 분기 구조·변경 표시 보완 (보완) | 213–243 |
| vf_fseabt.f.md:245–278 | 바깥 조건식·종료 행 및 ELSE 부재·인라인 주석 뜻 누락 | 조건식·종료 행·분기 구조·주석 뜻 보완 (보완) | 197,257–275,317 |
| vf_fseabt.f.md:279–326 | NF<0 무조건 처리처럼 요약; 용량 해석 단정; 바깥 블록·주석·GOTO 연결 누락 | ISURF와 선행 분기 조건 복원; 코드식으로 설명; 블록·주석·GOTO 보완 (정정,보완) | 197,249–254,279–324 |
| vf_fslp2a.f.md:1–28 | AA를 절편으로 단정 | 주석의 일차방정식 우변으로 정정 (정정) | 5,22 |
| vf_fslp2f.f.md:1–24 | AA를 절편으로 단정 | 주석의 일차방정식 우변으로 정정 (정정) | 5,17 |
| vf_fslp3a.f.md:1–30 | AA를 절편으로 단정 | 주석의 일차방정식 우변으로 정정 (정정) | 5,24 |
| vf_fslp3f.f.md:1–26 | AA를 절편으로 단정 | 주석의 일차방정식 우변으로 정정 (정정) | 5,19 |
| vf_fslp2a.f.md:29–85 | 스케일된 값을 체적으로 단정 | 다항식 값과 배율 명시 (정정) | 45–81 |
| vf_fslp2f.f.md:25–77 | 스케일된 값을 체적으로 단정 | 다항식 값과 배율 명시 (정정) | 41–50 |
| vf_fslp3f.f.md:27–96 | 스케일된 값을 체적으로 단정 | 다항식 값과 배율 명시 (정정) | 57–63 |
| vf_fslp3a.f.md:99–151 | 바깥 IF 이름만 표기 | 바깥 조건식과 종료 행 보완 (보완) | 65,73,84,95,148–151,237 |
| vf_fslp3a.f.md:152–206 | 바깥 IF 이름만 표기; 스케일 값을 체적으로 단정 | 바깥 조건식과 종료 행 보완 (정정,보완) | 61–65,151–206,237 |
| vf_fslp3a.f.md:207–238 | 바깥 IF 이름만 표기 | 바깥 조건식과 종료 행 보완 (보완) | 65,159,170,181,192,203,232–237 |
| vf_fslp3f.f.md:97–124 | 바깥 IF 이름만 표기 | 바깥 조건식과 종료 행 보완 (보완) | 60,64,70,78,86,94,120–124,184 |
| vf_fslp3f.f.md:125–184 | 바깥 IF 이름만 표기 | 바깥 조건식과 종료 행 보완 (보완) | 60–64,124,184 |
| vf_ii1inp.f.md:1–105 | 선언의 일본어 인라인 주석 뜻·변경 표시 누락 | MODEOBS·MODEPRS·MODEORS의 1/0 뜻과 변경 표시 보완 (보완) | 2–4,43–50,78–81,99–104 |
| vf_ii1inp.f.md:106–176 | 파일 OPEN의 랭크·INMODE 조건과 인라인 주석 뜻 누락 | 조건과 EOF 주석 뜻 보완 (보완) | 131–136,146–161 |
| vf_ii1inp.f.md:177–260 | 외부 파일 OPEN의 랭크·INMODE 조건 요약 누락 | OPEN 조건 보완 (보완) | 218–245 |
| vf_ii1inp.f.md:261–332 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 178–414 |
| vf_ii1inp.f.md:333–402 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 178–414 |
| vf_ii1inp.f.md:403–480 | 바깥 IF 이름만 표기; 랭크 접미사 누락 | 조건식과 종료 행 보완; 실제 파일 이름 복원 (정정,보완) | 178–414 |
| vf_ii1inp.f.md:481–543 | 변경 표시와 오류 레이블 연결 누락 | 변경 표시·주석 연속문·오류 이동 대상 보완 (보완) | 132,219,243,443,463–475,482–542 |
| vf_iiboun.f.md:219–251 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:252–294 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:295–337 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:338–398 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:399–451 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:452–517 | 바깥 IF 이름만 표기 | 조건식과 종료 행 보완 (보완) | 146,508 |
| vf_iiboun.f.md:145–218 | ZERO를 0으로 간주 | 원문 비교 기준 ZERO로 명시 (정정) | 194–195 |
| vf_iicomp.f.md:1–30 | 일본어 개요 주석의 미번역 | 개요 주석을 한국어로 번역 (정정) | 5 |
| vf_iidbg.f.md:1–31 | 일본어 개요 주석의 미번역 | 개요 주석을 한국어로 번역 (정정) | 5 |
| vf_iiequa.f.md:1–28 | 일본어 개요 주석의 미번역 | 개요 주석을 한국어로 번역 (정정) | 5 |
| vf_iicomp.f.md:77–124 | 바깥 IF 이름만 표기; 변수 용도 해석 미구분 | 조건식·종료 행 보완; 키워드 해석 구분 (보완) | 32,90–115 |
| vf_iidbg.f.md:54–87 | 바깥 IF 이름만 표기; RDBGTD를 속도로 단정 | 조건식·종료 행 보완; 직접 저장 사실과 해석 구분 (정정,보완) | 33,55–78 |
| vf_iifile.f.md:1–31 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iifile.f.md:147–208 | 비양수 입력 하나로 전체 영역을 바꾸는 것처럼 서술 | 각 끝점을 독립적으로 검사하고 대체함을 명시 (정정) | 171–187 |
| vf_iifile.f.md:91–146 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,36,54,145,479 |
| vf_iifile.f.md:147–208 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,479 |
| vf_iifile.f.md:209–245 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,148,479 |
| vf_iifile.f.md:246–304 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,241,479 |
| vf_iifile.f.md:305–336 | 바깥 IF 조건식·종료 행 누락; C의 추가 단어 조건 누락 | 바깥 조건식·종료 행 보완; C의 추가 단어 조건 명시 (보완) | 33,247–268,373–374,442,479 |
| vf_iifile.f.md:337–395 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,247,250,305,442,479 |
| vf_iifile.f.md:396–443 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,247,250,305,442,479 |
| vf_iifile.f.md:444–488 | 바깥 IF 조건식·종료 행 누락 | 바깥 조건식·종료 행 보완 (보완) | 33,247,479 |
| vf_iigrid.f.md:70–105 | 좌표 증가 검사 시작 조건·ELSE 부재 누락 | NL>=3 조건과 분기 구조·GOTO 대상 보완 (보완) | 79–104 |
| vf_iimate.f.md:1–29 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iimdl.f.md:1–32 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iimate.f.md:30–70 | T-DENS의 두 값 의미 불명확; 물리 뜻의 외부 근거 없음 | 기준 온도·밀도 온도 미분으로 정정; 물성 주석 인용 (정정,보완) | 38–69; VF_APHYSR.h:23–26,42–45 |
| vf_iimate.f.md:71–91 | 바깥 IF 식·종료 행 및 물리 뜻 외부 근거 누락 | 바깥 블록·물성 주석 근거 보완 (보완) | 31,66,130; VF_APHYSR.h:20–49 |
| vf_iimate.f.md:92–139 | 바깥 IF 식·종료 행 및 물리 뜻 외부 근거 누락 | 바깥 블록·물성 주석 근거 보완 (보완) | 31,82,130; VF_APHYSR.h:20–49 |
| vf_iimdl.f.md:92–115 | 바깥 IF 식·종료 행 누락 | 조건식·종료 행 보완 (보완) | 34,311 |
| vf_iimdl.f.md:116–175 | 바깥 IF 식·종료 행 누락; AMPL을 진폭으로 오독 | 조건식·종료 행 보완; AMPL은 증폭에 걸리는 주기 수 (정정,보완) | 34,311;168–171; VF_APHYSR.h:91–99 |
| vf_iimdl.f.md:176–215 | 바깥 IF 식·종료 행 누락; 네 방향 모두 설정하는 것처럼 요약 | 조건식·종료 행 보완; 선택한 한 방향만 설정 (정정,보완) | 34,311 |
| vf_iimdl.f.md:216–260 | 바깥 IF 식·종료 행 누락 | 조건식·종료 행 보완 (보완) | 34,311 |
| vf_iimdl.f.md:261–320 | 바깥 IF 식·종료 행 누락 | 조건식·종료 행 보완 (보완) | 34,311 |
| vf_iimdl.f.md:33–91 | 변수 용도의 구간 외 근거·해석 구분 누락 | 조파 경계 근거와 AMPL 뜻 추가; STREAM 차수 해석 구분 (보완) | 51–91; VF_APHYSR.h:50–66 |
| vf_iiobst.f.md:1–32 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iiopt.f.md:1–39 | 개요 주석 미번역 | 한국어 뜻 정정 (정정,보완) | 5,9,19–21,129–167 |
| vf_iipara.f.md:1–28 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iiopt.f.md:87–110 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 41,80,178 |
| vf_iiopt.f.md:111–142 | 바깥 IF 이름만 표기; LC_DEG를 중앙 경도로 단정 | 조건식·종료 행 보완; 해석 구분 (정정,보완) | 41,88,178 |
| vf_iiopt.f.md:143–187 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 41,130,178 |
| vf_iiopt.f.md:40–86 | WBUB의 속도 뜻에 대한 구간 외 근거 누락 | 헤더 주석 근거 보완 (보완) | 60–65; VF_APHYSR.h:88 |
| vf_iiporo.f.md:1–50 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 6 |
| vf_iitime.f.md:1–29 | 개요 주석 미번역 | 한국어 뜻 정정 (정정) | 5 |
| vf_iitime.f.md:54–74 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 31,47,65 |
| vf_iiporo.f.md:91–123 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 52,59,249 |
| vf_iiporo.f.md:124–156 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 52,92,249 |
| vf_iiporo.f.md:157–189 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 52,125,249 |
| vf_iiporo.f.md:190–217 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 52,158,249 |
| vf_iiporo.f.md:218–258 | 바깥 IF 이름만 표기 | 조건식·종료 행 보완 (보완) | 52,191,249 |
| vf_im1inp.f.md:148–201 | 바깥 블록 식·끝 행 및 파일 오류 이동 연결 누락 | 바깥 IF·DO와 CLOSE 조건·오류 레이블 연결 보완 (보완) | 44,105,125,175–199 |
| vf_im2inp.f.md:148–201 | 바깥 블록 식·끝 행 및 파일 오류 이동 연결 누락 | 바깥 IF·DO와 CLOSE 조건·오류 레이블 연결 보완 (보완) | 44,105,125,175–199 |
| vf_ip1inp.f.md:28–69 | 인덱스 개수 곱을 체적으로 단정; 전파 조건 요약 누락 | 셀 개수 계산으로 정정; NPROCS 조건 보완 (정정,보완) | 39–66 |
| vf_ip1inp.f.md:70–113 | 반복 종료의 IPRIT!=0 조건 누락; 바깥 IF·읽기 랭크 요약 누락 | 전체 종료 조건과 바깥 블록·읽기 랭크·이동 대상 보완 (정정,보완) | 29,71–112 |
| vf_ip1inp.f.md:114–140 | 파일 오류 레이블의 이동 관계 미표기 | OPEN·READ와 오류 레이블·GOTO 대상 보완 (보완) | 32,37,46,81,88,119–139 |
| vf_ir1inp.f.md:1–89 | 渦動粘性係数를 와동 점성으로 번역 | 동점성 의미 복원 (정정) | 37,44 |
| vf_ir1inp.f.md:153–190 | 초기 공극률 읽기에서 GGV 저장과 DUMMY 소비 조건 요약 누락 | IPRNT>1 조건과 ELSE 동작 보완 (보완) | 163–171 |
| vf_ir1inp.f.md:240–282 | WEST·EAST·SOUTH·NORTH를 주석 처리된 코드로 분류; GGV/DUMMY 분기 요약 누락 | 방향 표제 주석으로 정정; IPRNT>1 조건 명시 (정정,보완) | 242,247,252,257,273–281 |
| vf_ir1inp.f.md:283–318 | ELSE 부재와 반복 이동 대상 미표기 | 분기 구조와 GOTO·END 대상 보완 (보완) | 181,184,285–317 |
| vf_ir1inp.f.md:319–367 | 계수 설정 호출 조건과 오류 이동 관계 요약 누락 | 방정식별 호출 조건·오류 이동 관계 보완 (보완) | 91,113–118,125–299,339–366 |
| vf_fslp3f.f.md:97–124 | 계수 자체의 부호를 뒤집는 것처럼 서술 | 각 항의 가감으로 계수를 갱신함을 명시 (정정) | 97–117 |
| vf_iiboun.f.md:후속 사실 277·320·399·485 | 비활성 방정식도 조건 토큰을 해석하며 저장만 제한 | K·E·T와 C를 구분; C의 선행 LC 검사로 LEQC=0에서 유효 성분 없음 (정정) | 253–277,296–320,339–399,420–427,485 |
| vf_im1inp.f.md:후속 사실 37–38·79–91·105 | MTBZZ를 같은 호출에서 항상 다시 읽는 것으로 요약 | MTBTYP.NE.3에서만 MTBZZ를 읽음 (정정) | 37–38,72–91,105 |
| vf_im2inp.f.md:후속 사실 37–38·79–91·105 | MTBZZ2를 같은 호출에서 항상 다시 읽는 것으로 요약 | MTBTYP2.NE.3에서만 MTBZZ2를 읽음 (정정) | 37–38,72–91,105 |
| vf_iiboun.f.md:338–398 | BH를 구간 근거 없이 전달 계수로 단정 | TRAN-A·TRAN+A 분기의 입력값으로 명시 (정정) | 380–395 |
| vf_iifile.f.md:246–304 | TRN의 용도를 시간 이력으로 단정 | 이 구간의 키워드별 저장 배열로 설명 (정정) | 250–266 |
| vf_iimdl.f.md:116–175 | STREAM 차수 해석의 근거 범위 미구분 | 입력 코드 사실과 차수 해석 구분 (보완) | 135–140 |

정정과 보완이 함께 있는 행은 18행이다. 전체 대조 행은 159행이다. 위 기록별 집계와 각 행의 정정·보완 표시에서 셌다.

정정 40, 보완 64, 이상 없음 73
