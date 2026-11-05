# CADMAS-SURF code-19 전수 검증

검증일: 2026-11-04.

사용자가 지정한 기록 50개를 모두 완료했다.
구간 표 79행이 가리키는 원문 2,187행을 대조했다.
원문 행 수에는 빈 행과 주석 행을 포함한다.
구간 표 밖의 코드 사실도 대조했다.
각 구간의 원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
각 출력은 200행 이하였으며 잘린 출력은 없었다.
원문의 조건·대입식·선언·호출 인용을 기계적으로도 확인했다.
원문 50개의 SHA-256은 각 기록 frontmatter와 일치했다.
기록의 frontmatter와 구간 경계는 보존했다.
모델은 실행하지 않았다.

아래 기록명의 공통 경로는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/`이다.
각 원문 경로는 해당 기록 frontmatter의 `file:` 값이다.
외부 구현 인용의 `util/`은 같은 STR3D 원문 트리의 util 디렉터리이다.
경로가 없는 다른 `.f` 인용은 같은 contact 원문 디렉터리이다.

정정·보완 수는 아래 변경 목록의 행 수로 집계한다.
같은 기록·구간·유형의 변경은 한 행으로 합쳤다.
같은 구간에 정정과 보완이 함께 있으면 각 유형에 한 번씩 센다.
표 밖 코드 사실의 정정도 변경 목록에 포함했다.
이상 없음 수는 정정·보완이 필요하지 않았던 구간 표 행 수이다.

## 기록별 대조

| 기록 | 대조한 구간 표 행 수 | 대조한 원문 행 수 | 완료 범위 | 상태 |
|---|---:|---:|---|---|
| contactp.f.md | 4 | 131 | 1–131 | 완료; 정정 3, 보완 1 |
| corredge.f.md | 2 | 38 | 1–38 | 완료; 정정 1 |
| corrface1.f.md | 1 | 10 | 1–10 | 완료; 이상 없음 |
| corrface2.f.md | 2 | 43 | 1–43 | 완료; 정정 1, 보완 1 |
| corrface3.f.md | 2 | 44 | 1–44 | 완료; 이상 없음 |
| crh2edge.f.md | 3 | 103 | 1–103 | 완료; 보완 2 |
| crh2face.f.md | 2 | 54 | 1–54 | 완료; 보완 1 |
| crh2set.f.md | 1 | 39 | 1–39 | 완료; 이상 없음 |
| crh2stke.f.md | 1 | 38 | 1–38 | 완료; 이상 없음 |
| crh2stkf.f.md | 1 | 39 | 1–39 | 완료; 이상 없음 |
| crh2vrtx.f.md | 1 | 12 | 1–12 | 완료; 이상 없음 |
| csfhx.f.md | 1 | 31 | 1–31 | 완료; 이상 없음 |
| csfpn.f.md | 1 | 37 | 1–37 | 완료; 이상 없음 |
| csfte.f.md | 1 | 31 | 1–31 | 완료; 이상 없음 |
| edgechk.f.md | 1 | 15 | 1–15 | 완료; 보완 1 |
| edgedl.f.md | 1 | 23 | 1–23 | 완료; 보완 1 |
| edgeout.f.md | 1 | 16 | 1–16 | 완료; 이상 없음 |
| edgeslip.f.md | 3 | 101 | 1–101 | 완료; 정정 2, 보완 3 |
| edgestk.f.md | 1 | 19 | 1–19 | 완료; 보완 1 |
| edgquad.f.md | 1 | 22 | 1–22 | 완료; 이상 없음 |
| elcquad.f.md | 1 | 23 | 1–23 | 완료; 이상 없음 |
| enpfrcd.f.md | 1 | 12 | 1–12 | 완료; 이상 없음 |
| estfedge.f.md | 4 | 129 | 1–129 | 완료; 정정 2 |
| estfface.f.md | 4 | 149 | 1–149 | 완료; 정정 2 |
| facechk.f.md | 1 | 27 | 1–27 | 완료; 보완 1 |
| faceon.f.md | 3 | 91 | 1–91 | 완료; 보완 3 |
| faceout.f.md | 2 | 70 | 1–70 | 완료; 정정 2, 보완 1 |
| facerl.f.md | 1 | 14 | 1–14 | 완료; 보완 1 |
| facesepa.f.md | 1 | 16 | 1–16 | 완료; 정정 1 |
| facestk.f.md | 1 | 19 | 1–19 | 완료; 정정 1 |
| fricchk.f.md | 2 | 59 | 1–59 | 완료; 정정 1, 보완 1 |
| fricedge.f.md | 1 | 16 | 1–16 | 완료; 이상 없음 |
| fricface.f.md | 1 | 14 | 1–14 | 완료; 이상 없음 |
| fricint.f.md | 1 | 43 | 1–43 | 완료; 이상 없음 |
| fricset.f.md | 1 | 34 | 1–34 | 완료; 정정 1, 보완 1 |
| fricstf.f.md | 2 | 48 | 1–48 | 완료; 정정 2 |
| grazeel.f.md | 1 | 39 | 1–39 | 완료; 보완 1 |
| gsfhx.f.md | 1 | 15 | 1–15 | 완료; 이상 없음 |
| gsfpn.f.md | 1 | 15 | 1–15 | 완료; 이상 없음 |
| gsurf.f.md | 1 | 25 | 1–25 | 완료; 이상 없음 |
| gsurfq.f.md | 1 | 16 | 1–16 | 완료; 이상 없음 |
| gsurfx.f.md | 1 | 14 | 1–14 | 완료; 이상 없음 |
| initidx.f.md | 2 | 58 | 1–58 | 완료; 보완 1 |
| istchk.f.md | 2 | 97 | 1–97 | 완료; 정정 1, 보완 1 |
| lencd.f.md | 1 | 17 | 1–17 | 완료; 보완 1 |
| lhsidx.f.md | 2 | 54 | 1–54 | 완료; 보완 1 |
| mktehx.f.md | 3 | 125 | 1–125 | 완료; 정정 1 |
| mktepn.f.md | 3 | 60 | 1–60 | 완료; 정정 1 |
| mpccorr.f.md | 1 | 31 | 1–31 | 완료; 정정 1 |
| mpccorr11.f.md | 1 | 11 | 1–11 | 완료; 이상 없음 |

합계는 위 기록별 표에서 센 구간 표 79행과 원문 2,187행이다.

## 정정·보완 목록

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| [정정] contactp.f.md:24–58 | 랭크·상태 조건을 생략한 요약과 접촉력 의미 단정 | 명령 송신 랭크와 상태 조건을 명시하고 RFCA 계산으로 기술 | contactp.f:25–56 |
| [보완] contactp.f.md:59–102 | 분기 사슬의 ELSE 부재 미기재 | ELSE·CASE DEFAULT 부재와 닫힘 행 명시 | contactp.f:78–95 |
| [정정] contactp.f.md:103–131 | 구간 자체에서 입증하지 않은 배열의 물리적 용도 단정 | 전송 배열명을 그대로 기술 | contactp.f:105–127 |
| [보완] corrface2.f.md:1–20 | ELSE 부재와 루프 종료 레이블 미기재 | 분기와 루프의 종료를 명시 | corrface2.f:11–19 |
| [정정] edgeslip.f.md:56–101 | 힘 크기로 비교한다고 요약하고 ELSE 부재를 뭉뚱그림. 상위 ELSEIF 조건 생략과 힘 의미 단정 | 부호 있는 값의 비교와 각 분기 사슬의 ELSE 부재 명시. 앞 분기 실패 조건과 비교 변수명 명시 | edgeslip.f:56–99; 56–72 |
| [정정] estfedge.f.md:23–60 | 구간 근거 없이 근사식이라고 단정 | 초기화와 대각 성분 대입을 직접 기술 | estfedge.f:25–31 |
| [정정] estfface.f.md:24–84 | 근사·고착·속도 의미 단정과 IDYN 분기의 상위 조건 생략 | 대입식과 IFMDL·IDYN의 중첩 관계 명시 | estfface.f:24–83 |
| [정정] fricchk.f.md:12–59 | 계수의 물리적 의미 단정과 오류 메시지·분기·GOTO 대상 설명 생략 | 배열 계산을 직접 기술하고 오류 출력과 분기 및 레이블을 명시 | fricchk.f:19–56 |
| [정정] facestk.f.md:1–19 | H를 구간 근거 없이 높이라고 단정 | H의 절댓값 조건으로 기술 | facestk.f:11–13 |
| [정정] facesepa.f.md:1–16 | E·F·FN의 물리적 의미를 사실로 단정 | 호출 사실과 법선 힘 해석을 분리 | facesepa.f:6–9 |
| [정정] fricset.f.md:1–34 | IFRIC=1을 새 접촉으로 단정하고 동적·이전 변위 의미를 단정. 중첩 OR 조건을 모두 충족이라는 표현으로 모호하게 기술 | 조건과 호출 인수를 직접 기술하고 ELSE 부재 명시. 바깥 OR와 안쪽 OR를 구분 | fricset.f:13–30; 13–19 |
| [보완] initidx.f.md:12–58 | 오류 메시지 설명과 GOTO 대상·루프 종료점 미기재. ORDER 정렬 삽입 설명의 외부 구현 근거 미기재 | 오류 출력과 레이블별 종료점을 명시. ORDER의 비교·삽입·중복 반환 구현 행 인용 | initidx.f:12–52; 32–39; util/order.f:5–17 |
| [보완] istchk.f.md:48–97 | CASE DEFAULT·ELSE 부재와 0 이하 값의 보존 미기재 | 선택문·분기 종료와 미대입 경로 명시 | istchk.f:59–89 |
| [보완] lhsidx.f.md:11–54 | 110 대상 문장·루프 종료 레이블·EXIT 대상 미기재 | GOTO 대상과 각 DO 종료점 및 EXIT 대상 명시 | lhsidx.f:11–51 |
| [정정] istchk.f.md:코드 사실 14–18 | 두 번째 상태 성분을 주절점 번호로 단정 | 상태별 절점 번호 또는 IEDG·IELC 열 번호로 구분 | istchk.f:59–74 |
| [보완] lencd.f.md:1–17 | 벡터 차·내적·투영 설명의 호출 루틴 근거 미기재 | 보조 루틴의 연산 구현 행을 인용 | lencd.f:6–14; util/subvec.f:9–11; util/vecml1.f:19–22; util/rmult1.f:16–18 |
| [보완] facerl.f.md:1–14 | 복사·면적 좌표 설명의 외부 구현 근거 미기재 | SHIFT1과 AREACD 구현 행 인용 | facerl.f:6–11; util/shift1.f:16–18; areacd.f:28–44 |
| [보완] facechk.f.md:1–27 | 면적 좌표·내부 판정 의미의 외부 구현 근거 미기재 | FACERL·AREACD·AREAIN 구현 행 인용 | facechk.f:11–13; facerl.f:6–11; areacd.f:28–44; areain.f:6–12 |
| [보완] faceon.f.md:1–25 | NRMVEC 법선 의미의 외부 구현 근거 미기재 | 좌표 차와 정규화 외적 구현 행 인용 | faceon.f:12–13; nrmvec.f:6–8; util/cross2.f:9–16 |
| [보완] faceon.f.md:26–68 | 면 법선·좌표·내부 판정 근거와 두 번째 SELECT의 기본 분기 부재 미기재 | AREACD·AREAIN 구현 행과 CASE DEFAULT 부재 명시 | faceon.f:39–55; areacd.f:7–48; areain.f:6–12 |
| [보완] faceon.f.md:69–91 | VOLCD·VOLIN3의 기하학적 의미 근거 미기재 | 체적 좌표 계산과 각 성분 하한 검사 구현 행 인용 | faceon.f:78–82; volcd.f:19–49; volin3.f:6–13 |
| [보완] grazeel.f.md:1–39 | VOLCD·VOLIN3의 기하학적 의미 근거 미기재 | 체적 좌표 계산과 각 성분 하한 검사 구현 행 인용 | grazeel.f:28–32; volcd.f:19–49; volin3.f:6–13 |
| [보완] edgestk.f.md:1–19 | LENCD·VECML2의 기하학적 의미 근거 미기재 | 투영 계산과 벡터 크기 구현 행 인용 | edgestk.f:9–11; lencd.f:6–14; util/vecml2.f:6–10 |
| [정정] contactp.f.md:59–102 | 힘·법선이라는 용도 단정과 보존·초기화 순서가 섞인 요약 | 배열별 대입 순서와 복사 대상을 직접 기술 | contactp.f:66–76 |
| [정정] faceout.f.md:15–70 | 변화량 자체를 임계값과 비교한다고 요약 | DABS(DRL)의 절댓값 비교로 정정 | faceout.f:29–30 |
| [정정] estfedge.f.md:1–22 | 강성 용도와 상대 변위를 구간 근거 없이 단정하고 계산 대상을 뭉뚱그림 | DU와 VR의 계산 대상을 직접 기술하고 물리적 뜻을 해석으로 분리 | estfedge.f:5–21 |
| [정정] estfface.f.md:1–23 | 강성 용도와 상대 변위 의미 단정 | DU·VR 계산을 직접 기술하고 물리적 뜻을 해석으로 분리 | estfface.f:6–22 |
| [정정] edgeslip.f.md:21–55 | F를 힘으로 단정 | F의 내적 계산과 힘 성분 해석을 분리 | edgeslip.f:27–51; util/vecml1.f:19–22 |
| [정정] fricstf.f.md:14–48 | MPCTRNS·CGADM의 용도를 호출 인수만으로 단정 | 호출 사실과 구속 변환·전역 조립 해석을 분리 | fricstf.f:38–44 |
| [정정] fricstf.f.md:1–13 | 선언 구간만으로 배열들의 물리적 용도 단정 | 선언 사실로 한정 | fricstf.f:1–12 |
| [정정] corredge.f.md:11–38 | DUG를 물리적 변위 보정량으로 단정 | 주석의 종속 성분과 DUG 대입으로 기술 | corredge.f:31–35 |
| [정정] corrface2.f.md:21–43 | DUG를 물리적 변위 보정량으로 단정 | 주석의 자유·종속 성분과 DUG 대입으로 기술 | corrface2.f:35–40 |
| [정정] faceout.f.md:1–14 | RLCORR 결과를 보정 전후 구별 없이 이전 면적 좌표로 기술 | RLCORR의 조건별 보정을 거친 좌표임을 명시 | faceout.f:9; rlcorr.f:12–43 |
| [보완] crh2edge.f.md:1–37 | SHIFT1·SUBVEC·DIRCOS·CROSS2의 호출 의미 근거 미기재 | 복사·차·정규화·외적 구현 행 인용 | crh2edge.f:10–25; util/shift1.f:16–18; util/subvec.f:9–11; util/dircos.f:8–15; util/cross2.f:9–16 |
| [보완] crh2edge.f.md:80–103 | RMULT1의 계수 나눗셈 설명 근거 미기재 | 역수를 곱하는 호출과 스칼라 곱 구현을 연결 | crh2edge.f:87·93·99; util/rmult1.f:16–18 |
| [보완] crh2face.f.md:1–24 | SHIFT1 복사 의미의 외부 구현 근거 미기재 | 복사 대입 구현 행 인용 | crh2face.f:6–9; util/shift1.f:16–18 |
| [보완] edgedl.f.md:1–23 | SHIFT1 복사 의미의 외부 구현 근거 미기재 | 복사 대입 구현 행 인용 | edgedl.f:6–10; util/shift1.f:16–18 |
| [보완] edgechk.f.md:1–15 | 표 밖 모서리 내부 허용값 설명의 외부 구현 근거 미기재 | 투영 비율과 DL 계산 근거를 연결 | edgechk.f:6–8; edgedl.f:12–20; lencd.f:6–14 |
| [보완] edgeslip.f.md:1–20 | 방향 벡터 설명의 외부 구현 근거 미기재 | 벡터 차와 정규화 구현 행 인용 | edgeslip.f:18–19; util/subvec.f:9–11; util/dircos.f:8–15 |
| [정정] mktehx.f.md:1–44 | IG의 용도를 구간 근거 없이 사면체 연결 목록으로 단정 | 직접 대입 사실과 사면체 해석을 분리 | mktehx.f:3–43 |
| [정정] mktepn.f.md:1–19 | IG의 용도를 구간 근거 없이 사면체 연결 목록으로 단정 | 직접 대입 사실과 사면체 해석을 분리 | mktepn.f:3–18 |
| [정정] mpccorr.f.md:1–31 | 선언 구간에서 배열의 다점 구속 용도를 단정 | 인수 배열 선언으로 한정 | mpccorr.f:1–6 |
| [보완] edgeslip.f.md:56–101 | 두 IF·ELSEIF 사슬의 ELSE 부재 미기재 | 56·61·72행 사슬과 62·65·68행 사슬의 ELSE 부재 및 닫힘 명시 | edgeslip.f:56–99 |
| [보완] fricchk.f.md:12–59 | 오류 메시지 설명·ELSE 부재·GOTO 대상 미기재 | WRITE와 ERRSTP 순서 및 ELSE 부재와 56행 레이블 10 명시 | fricchk.f:19–56 |
| [보완] fricset.f.md:1–34 | IST 분기 사슬의 ELSE 부재 미기재 | 21·23행 사슬은 ELSE 없이 25행에서 닫힘을 명시 | fricset.f:21–25 |
| [보완] edgeslip.f.md:21–55 | VECML1 내적 설명의 외부 구현 근거 미기재 | util/vecml1.f:19–22 인용 | edgeslip.f:31–45; util/vecml1.f:19–22 |
| [보완] faceout.f.md:1–14 | RLCORR의 면적 좌표 보정 구현 근거 미기재 | rlcorr.f:12–43 인용 | faceout.f:9; rlcorr.f:12–43 |

정정 23, 보완 24, 이상 없음 39
