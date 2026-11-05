# CADMAS-SURF code-6 전수 검증

검증일: 2026-11-04.
사용자가 지정한 기록 43개를 모두 완료했다.
대조한 기록 구간 행은 164개이다.
대조한 원문 행은 5137개이다.
두 수치는 아래 기록별 표에서 합산했다.

각 구간의 원문은 `nl -ba <원문> | sed -n 'A,Bp'`로 열었다.
한 번에 연 원문은 200행 이하이다.
구간별 요약과 일본어 주석의 한국어 뜻을 대조했다.
조건·대입식·연속문·선언·호출 인수·레이블을 대조했다.
기록 끝의 코드 사실 항목도 대조했다.
원문 인용과 행 번호의 일치는 별도로 기계 확인했다.
수정 후에도 원문 인용·frontmatter·구간 경계는 바뀌지 않았다.
원문 SHA-256은 각 기록 frontmatter의 값과 일치했다.
모델은 실행하지 않았다.
원문·노트·git은 변경하지 않았다.

기록의 공통 경로는 `_staging/recovery/read/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/`이다.
원문은 각 기록의 `file:` 경로이다.
아래 원문 행 열에서 파일명을 생략한 행 번호는 해당 기록의 원문을 가리킨다.
추가 근거로 읽은 `vf_cvort.f:1–60`, `vf_careap.f:1–45`, `VF_APHYSR.h:50–100`은 같은 원문 디렉터리에 있다.

정정·보완·이상 없음의 집계 단위는 기록의 구간 행이다.
같은 구간을 여러 번 고쳤어도 같은 종류는 한 번만 센다.
정정과 보완이 함께 있는 구간은 두 항목에 각각 센다.
이상 없음은 정정·보완 표시가 없는 구간이다.
정정과 보완이 함께 있는 구간은 12개이다.

## 기록별 대조 결과

| 기록 | 상태 | 대조한 원문 범위 | 원문 행 수 | 기록 구간 행 수 | 정정 | 보완 | 이상 없음 |
|---|---|---|---:|---:|---:|---:|---:|
| [vf_k1cal.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_k1cal.f.md>) | 완료 | 1–179 | 179 | 6 | 1 | 1 | 5 |
| [vf_kgene.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_kgene.f.md>) | 완료 | 1–194 | 194 | 4 | 2 | 2 | 1 |
| [vf_m1bcgs.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_m1bcgs.f.md>) | 완료 | 1–273 | 273 | 7 | 0 | 0 | 7 |
| [vf_mzax.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzax.f.md>) | 완료 | 1–65 | 65 | 2 | 0 | 0 | 2 |
| [vf_mzbkwd.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzbkwd.f.md>) | 완료 | 1–56 | 56 | 2 | 0 | 0 | 2 |
| [vf_mzdcmp.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzdcmp.f.md>) | 완료 | 1–80 | 80 | 3 | 0 | 0 | 3 |
| [vf_mzfrwd.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzfrwd.f.md>) | 완료 | 1–57 | 57 | 2 | 0 | 0 | 2 |
| [vf_mzip.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzip.f.md>) | 완료 | 1–52 | 52 | 2 | 0 | 1 | 1 |
| [vf_mzminv.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_mzminv.f.md>) | 완료 | 1–50 | 50 | 2 | 0 | 0 | 2 |
| [vf_og1ini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_og1ini.f.md>) | 완료 | 1–143 | 143 | 4 | 0 | 1 | 3 |
| [vf_og1trn.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_og1trn.f.md>) | 완료 | 1–233 | 233 | 6 | 0 | 3 | 3 |
| [vf_ogbcin.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ogbcin.f.md>) | 완료 | 1–93 | 93 | 4 | 0 | 1 | 3 |
| [vf_ogbcnm.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ogbcnm.f.md>) | 완료 | 1–89 | 89 | 4 | 0 | 1 | 3 |
| [vf_ogbcvl.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ogbcvl.f.md>) | 완료 | 1–95 | 95 | 4 | 0 | 1 | 3 |
| [vf_ol1ini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ol1ini.f.md>) | 완료 | 1–566 | 566 | 14 | 2 | 4 | 8 |
| [vf_ol1trn.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ol1trn.f.md>) | 완료 | 1–250 | 250 | 4 | 0 | 1 | 3 |
| [vf_ol3di.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ol3di.f.md>) | 완료 | 1–192 | 192 | 6 | 1 | 2 | 4 |
| [vf_ol3dnf.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ol3dnf.f.md>) | 완료 | 1–180 | 180 | 6 | 2 | 2 | 3 |
| [vf_ol3dr.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ol3dr.f.md>) | 완료 | 1–193 | 193 | 6 | 2 | 2 | 3 |
| [vf_olbc.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_olbc.f.md>) | 완료 | 1–246 | 246 | 6 | 0 | 0 | 6 |
| [vf_om1ini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_om1ini.f.md>) | 완료 | 1–175 | 175 | 6 | 1 | 0 | 5 |
| [vf_om1trn.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_om1trn.f.md>) | 완료 | 1–161 | 161 | 5 | 2 | 4 | 1 |
| [vf_or1ini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_or1ini.f.md>) | 완료 | 1–106 | 106 | 4 | 0 | 1 | 3 |
| [vf_or1trn.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_or1trn.f.md>) | 완료 | 1–244 | 244 | 7 | 3 | 1 | 4 |
| [vf_ot1ini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ot1ini.f.md>) | 완료 | 1–157 | 157 | 5 | 0 | 2 | 3 |
| [vf_ot1trn.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_ot1trn.f.md>) | 완료 | 1–347 | 347 | 8 | 4 | 6 | 2 |
| [vf_p0barr.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0barr.f.md>) | 완료 | 1–32 | 32 | 2 | 0 | 0 | 2 |
| [vf_p0bcsc.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0bcsc.f.md>) | 완료 | 1–38 | 38 | 2 | 0 | 0 | 2 |
| [vf_p0bcsi.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0bcsi.f.md>) | 완료 | 1–38 | 38 | 2 | 0 | 0 | 2 |
| [vf_p0end.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0end.f.md>) | 완료 | 1–24 | 24 | 2 | 0 | 0 | 2 |
| [vf_p0enda.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0enda.f.md>) | 완료 | 1–27 | 27 | 2 | 0 | 0 | 2 |
| [vf_p0init.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0init.f.md>) | 완료 | 1–83 | 83 | 3 | 0 | 0 | 3 |
| [vf_p0mind.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0mind.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p0sumi.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0sumi.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p0time.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0time.f.md>) | 완료 | 1–25 | 25 | 2 | 0 | 0 | 2 |
| [vf_p1bcsc.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1bcsc.f.md>) | 완료 | 1–38 | 38 | 2 | 0 | 0 | 2 |
| [vf_p1bcsd.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1bcsd.f.md>) | 완료 | 1–38 | 38 | 2 | 0 | 0 | 2 |
| [vf_p1bcsi.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1bcsi.f.md>) | 완료 | 1–38 | 38 | 2 | 0 | 0 | 2 |
| [vf_p1maxd.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1maxd.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p1mind.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1mind.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p1mini.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1mini.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p1sumd.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1sumd.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| [vf_p1sumi.f.md](<../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p1sumi.f.md>) | 완료 | 1–40 | 40 | 2 | 0 | 0 | 2 |
| 합계 | 완료 | 대상 원문 전체 | 5137 | 164 | 20 | 36 | 120 |

## 정정·보완 목록

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| vf_k1cal.f.md:151–179 (정정·보완) | 유체 셀에서 AE 하한 미달이면 AE 하한 미달이 아니고 AK만 하한 미달이면 AK만 설정한다. | `NF(I,J,K).EQ.0`인 셀에서 AE 하한 미달이면 AE 하한 미달이 아니고 AK만 하한 미달이면 AK만 설정한다. 156–161행의 IF/ELSEIF 사슬에는 ELSE가 없다. | 155–161; 156–161 |
| vf_kgene.f.md:49–95 (정정) | x방향 두 면의 미정의 유속은 IND=0이면 격자폭 가중 보간(interpolation), 그 외에는 경곗값을 사용한다. | x방향 두 면의 미정의 유속은 IND=0이면 아래 XX 계수식을 사용한다. 그 외에는 경곗값을 사용한다. 해석: XX 계수식은 격자폭 가중 보간에 해당하는 것으로 읽힌다. | 72–95 |
| vf_kgene.f.md:96–143 (정정·보완) | y방향과 z방향 두 면에서도 IND=0 여부에 따라 격자폭 가중 보간 또는 경곗값을 사용한다. 55행 IF 분기 `IF (NF(I,J,K).EQ.0) THEN` 안. | y방향과 z방향 두 면에서도 IND=0이면 아래 YY·ZZ 계수식을 사용한다. 그 외에는 경곗값을 사용한다. 해석: YY·ZZ 계수식은 격자폭 가중 보간에 해당하는 것으로 읽힌다. 55행 IF 분기 `IF (NF(I,J,K).EQ.0) THEN` 안. 이 IF는 182행 ENDIF에서 닫힌다. I·J·K 루프는 각각 183행 레이블 100, 184행 레이블 110, 185행 레이블 120에서 닫힌다. | 96–143; 52–55, 182–185 |
| vf_kgene.f.md:144–194 (보완) | 55행 IF 분기 `IF (NF(I,J,K).EQ.0) THEN` 안. | 55행 IF 분기 `IF (NF(I,J,K).EQ.0) THEN` 안. 이 IF는 182행 ENDIF에서 닫힌다. I·J·K 루프는 각각 183행 레이블 100, 184행 레이블 110, 185행 레이블 120에서 닫힌다. | 52–55, 182–185 |
| vf_og1ini.f.md:65–104 (보완) | 유속·압력·VOF 함수(volume of fluid function) 등의 출력 플래그를 구성하여 기록한다. | 유속·압력·VOF 함수(volume of fluid function) 등의 출력 플래그를 구성하여 기록한다. 출력 대상의 대응 근거는 같은 원문 디렉터리의 `vf_og1trn.f:119–213`이다. | 88–103; vf_og1trn.f:119–213 |
| vf_og1trn.f.md:77–115 (보완) | 단계 간격 또는 시간 간격 조건으로 IO를 결정한다. | 단계 간격 또는 시간 간격 조건으로 IO를 결정한다. 80–95행의 IF/ELSEIF 사슬에는 ELSE가 없다. IGRTYP가 1도 2도 아니면 IO는 0을 유지한다. | 78–98 |
| vf_og1trn.f.md:175–209 (보완) | 경계 농도를 기록하고 와도 경곗값은 0으로 채운다. | 와도라는 의미의 근거는 같은 원문 디렉터리의 `vf_cvort.f:6,35,39`이다. NB>0이면 경계 농도를 기록한다. NB>0이고 IGRVOR가 0이 아니면 와도 경곗값을 0으로 채운다. | 175–208; vf_cvort.f:6,35,39 |
| vf_og1trn.f.md:116–148 (보완) | NB>0이면 VF_OGBCVL로 방향별 경계를 정렬하여 각 경곗값을 기록한다. | NB>0이면 VF_OGBCVL로 방향별 경곗값을 배열에 모아 기록한다. 방향별 저장 구간의 근거는 같은 원문 디렉터리의 `vf_ogbcvl.f:40–86`이다. | 126–147; vf_ogbcvl.f:40–86 |
| vf_ogbcin.f.md:72–93 (보완) | 50행에서 열린 IF/ELSEIF 문(72행에서 분기 전환 또는 종료) 안. | 50행 `IF     (NS.EQ.1 .OR. NS.EQ.2) THEN`에서 열린 분기문 안. 이 구간의 72행 ELSE는 앞선 조건과 `ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN`이 모두 거짓일 때의 분기이다. 이 IF는 83행 ENDIF에서 닫힌다. L 루프는 84행 레이블 100에서 닫힌다. | 50–84 |
| vf_ogbcnm.f.md:69–89 (보완) | 49행에서 열린 IF/ELSEIF 문(69행에서 분기 전환 또는 종료) 안. | 49행 `IF     (NS.EQ.1 .OR. NS.EQ.2) THEN`에서 열린 분기문 안. 이 구간의 69행 ELSE는 앞선 조건과 `ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN`이 모두 거짓일 때의 분기이다. 이 IF는 79행 ENDIF에서 닫힌다. L 루프는 80행 레이블 100에서 닫힌다. | 49–80 |
| vf_ogbcvl.f.md:74–95 (보완) | 52행에서 열린 IF/ELSEIF 문(74행에서 분기 전환 또는 종료) 안. | 52행 `IF     (NS.EQ.1 .OR. NS.EQ.2) THEN`에서 열린 분기문 안. 이 구간의 74행 ELSE는 앞선 조건과 `ELSEIF (NS.EQ.3 .OR. NS.EQ.4) THEN`이 모두 거짓일 때의 분기이다. 이 IF는 85행 ENDIF에서 닫힌다. L 루프는 86행 레이블 100에서 닫힌다. | 52–86 |
| vf_ol1ini.f.md:167–229 (보완) | 경사각 출력 조건도 포함한다. | 경사각 출력 조건도 포함한다. 175–184행의 소스 파형 분기에는 ELSE가 없다. 195–203행의 JD 분기에는 ELSE가 없다. 204–215행의 경계 파형 분기에는 ELSE가 없다. | 175–215 |
| vf_ol1ini.f.md:230–286 (보완) | JD=1..4 개방 경계(open boundary)와 감쇠대(damping zone) 설정을 출력한다. | JD=1..4 개방 경계(open boundary)와 감쇠대(damping zone) 설정을 출력한다. 232–240행과 252–260행의 JD별 IF/ELSEIF 사슬에는 ELSE가 없다. | 232–260 |
| vf_ol1ini.f.md:322–357 (보완) | 목록 방향 ILPARA(1)=1..6은 XY,XZ,YZ,YX,ZX,ZY에 대응한다. | 목록 방향 ILPARA(1)=1..6은 XY,XZ,YZ,YX,ZX,ZY에 대응한다. 344–356행의 IF/ELSEIF 사슬에는 ELSE가 없다. | 344–356 |
| vf_ol1ini.f.md:358–400 (정정) | 도화 영역의 미지정 끝점을 기본 범위로 바꾸고 두 방향 이상이 단일 셀 두께이면 VF_A2ERR를 호출한다. | IGRTYP가 0이 아닌 분기에서 IGRARA(1:3)의 값이 각각 1 이하이면 2로 바꾼다. IGRARA(4:6)의 값이 각각 1 이하이면 NUMI0-1, NUMJ0-1, NUMK-1로 바꾼다. 시작 첨자와 끝 첨자가 같은 방향이 둘 이상이면 VF_A2ERR에 INVALID VALUE.를 전달한다. | 358–385 |
| vf_ol1ini.f.md:431–464 (보완) | 부반복·표면 셀 유속 조건·기포·물방울·PV 상수 조건·항력 옵션을 해당 조건별로 출력한다. | 부반복·표면 셀 유속 조건·기포·물방울·PV 상수 조건·항력 옵션을 해당 조건별로 출력한다. 444–448행의 IDROP 분기 사슬에는 ELSE가 없다. IDROP가 0도 1도 아니면 이 사슬은 T-DOOR DROP 행을 출력하지 않는다. | 444–448 |
| vf_ol1ini.f.md:465–517 (정정) | 격자 수와 좌표·격자폭·중심 좌표를 전역 번호로 출력한다. | 격자 수를 출력한다. X·DX·CX, Y·DY·CY, Z·DZ·CZ라는 표제 아래 XX·YY·ZZ의 L=1,3 성분을 출력한다. 출력 첨자는 각각 I-1+IP, J-1+JP, K-1이다. 해석: DX·CX 등의 표제는 격자폭·중심 좌표를 뜻하는 것으로 읽힌다. | 465–481 |
| vf_ol1trn.f.md:89–151 (보완) | ILPTYP의 단계·시간 조건으로 출력 여부를 결정한다. | ILPTYP의 단계·시간 조건으로 출력 여부를 결정한다. 92–107행의 IF/ELSEIF 사슬에는 ELSE가 없다. ILPTYP가 1도 2도 아니면 IO는 0을 유지한다. | 90–110 |
| vf_ol3di.f.md:91–131 (보완) | 51행에서 열린 IF/ELSEIF 문(92행에서 분기 전환 또는 종료) 안. | 51행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 92행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 177행 ENDIF에서 닫힌다. | 51–177 |
| vf_ol3di.f.md:132–178 (보완·정정) | 51행에서 열린 IF/ELSEIF 문(133행에서 분기 전환 또는 종료) 안. 전역 단면 번호의 소유 여부를 검사하고 지역 인덱스로 변환한다. | 51행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 133행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 177행 ENDIF에서 닫힌다. 전역 단면 번호 M이 MS 이상이고 ME 이하인지 검사한다. 배열에서 해당 방향 첨자는 M-MS+1을 사용한다. | 51–177; 135–175 |
| vf_ol3dnf.f.md:79–119 (보완) | 39행에서 열린 IF/ELSEIF 문(80행에서 분기 전환 또는 종료) 안. | 39행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 80행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 165행 ENDIF에서 닫힌다. | 39–165 |
| vf_ol3dnf.f.md:120–166 (보완·정정) | 39행에서 열린 IF/ELSEIF 문(121행에서 분기 전환 또는 종료) 안. 단면 소유 여부를 검사하고 지역 인덱스(local index)로 변환한다. | 39행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 121행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 165행 ENDIF에서 닫힌다. 전역 단면 번호 M이 MS 이상이고 ME 이하인지 검사한다. 배열에서 해당 방향 첨자는 M-MS+1을 사용한다. | 39–165; 123–163 |
| vf_ol3dr.f.md:91–131 (보완) | 51행에서 열린 IF/ELSEIF 문(92행에서 분기 전환 또는 종료) 안. | 51행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 92행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 178행 ENDIF에서 닫힌다. | 51–178 |
| vf_ol3dr.f.md:132–179 (보완·정정) | 51행에서 열린 IF/ELSEIF 문(133행에서 분기 전환 또는 종료) 안. 전역 단면 번호 소유 여부를 검사한 뒤 지역 인덱스로 접근한다. | 51행 `IF     (ILPARA(1).EQ.1) THEN`에서 열린 분기문 안. 133행에서 다음 ELSEIF 분기로 전환한다. 이 사슬에는 ELSE가 없다. 이 IF는 178행 ENDIF에서 닫힌다. 전역 단면 번호 M이 MS 이상이고 ME 이하인지 검사한다. 배열에서 해당 방향 첨자는 M-MS+1을 사용한다. | 51–178; 135–175 |
| vf_ol3dnf.f.md:38–78 (정정) | XZ는 지역 y범위 소유 여부를 검사한다. | XZ는 `MS.LE.M .AND. M.LE.ME`를 검사한다. 이때 MS=MYGJS이고 ME=MYGJE이다. | 60–76 |
| vf_ol3dr.f.md:50–90 (정정) | XZ는 지역 y범위 소유 여부를 검사한다. | XZ는 `MS.LE.M .AND. M.LE.ME`를 검사한다. 이때 MS=MYGJS이고 ME=MYGJE이다. | 72–88 |
| vf_om1ini.f.md:69–83 (정정) | 각 내부 I,J에서 장애물 아닌 셀은 (1-GGV)*격자높이, 장애물 셀은 전체 격자높이를 누적하여 표고(elevation)를 WK01(:,:,1)에 저장한다. | 각 내부 I,J에서 NF가 -1이 아니면 `(1.0D0-GGV(I,J,K))*ZZ(2,K)`를 HWK에 누적한다. NF가 -1이면 `ZZ(2,K)`를 HWK에 누적한다. 표고 계산이라는 주석 아래 `WK01(I,J,1)=ZZ(1,2)+HWK`를 대입한다. | 69–82 |
| vf_om1trn.f.md:45–71 (보완) | iflag=0이면 IMMTYP에 따른 단계·시간 주기로 출력 여부를 판정한다. | iflag=0이면 IMMTYP에 따른 단계·시간 주기로 출력 여부를 판정한다. 49–64행의 IMMTYP 분기 사슬에는 ELSE가 없다. IMMTYP가 1도 2도 아니면 IO는 0을 유지한다. | 45–67 |
| vf_om1trn.f.md:72–91 (보완·정정) | 45행 IF 분기 `if(iflag.eq.0)then` 안. 내부 각 I,J에서 NF=-1을 제외하고 공극률(porosity)·VOF 함수(volume of fluid function)·격자높이의 곱을 수심에 누적한다. 양쪽 면 유속의 합에 같은 가중치를 곱한 후 0.5를 곱해 두 수평 유량(discharge) 성분을 저장한다. | 45행 IF 분기 `if(iflag.eq.0)then` 안. 이 분기문은 135행 `elseif(iflag.eq.-1)then`으로 전환한다. ELSE는 없다. 이 IF는 143행 endif에서 닫힌다. 수심 등 계산이라는 주석 아래 내부 각 I,J에서 NF=-1을 제외하고 `ZF=GGV(I,J,K)*FF(I,J,K)*ZZ(2,K)`를 DWK에 누적한다. 양쪽 면 유속의 합에 ZF를 곱해 UWK·VWK에 누적한다. WK01의 두 성분에는 각각 `REAL(UWK*0.5D0)`와 `REAL(VWK*0.5D0)`를 저장한다. 해석: 이 두 성분은 수심 적분 유속에 해당하는 것으로 읽힌다. | 45,135–143; 72–90 |
| vf_om1trn.f.md:92–130 (보완·정정) | 45행 IF 분기 `if(iflag.eq.0)then` 안. ma_rank>=0이면 시각·수심·두 수평 유량을 MPI_REAL로 태그 10,20,30,40에 송신하며 매번 대기한다. | 45행 IF 분기 `if(iflag.eq.0)then` 안. 이 분기문은 135행 `elseif(iflag.eq.-1)then`으로 전환한다. ELSE는 없다. 이 IF는 143행 endif에서 닫힌다. ma_rank>=0이면 REAL(TNOW)와 WK01의 첫째·둘째·셋째 성분을 MPI_REAL로 태그 10,20,30,40에 각각 송신한다. 각 송신 뒤 MPI_WAIT를 호출한다. | 45,135–143; 93–116 |
| vf_om1trn.f.md:131–161 (보완) | 45행 IF 분기 `if(iflag.eq.0)then` 안. | 45행 IF 분기 `if(iflag.eq.0)then` 안. 이 분기문은 135행 `elseif(iflag.eq.-1)then`으로 전환한다. ELSE는 없다. 이 IF는 143행 endif에서 닫힌다. | 45,135–143 |
| vf_or1ini.f.md:60–83 (보완) | IPRNT<=1이면 전체 공극률 배열을 기록한다. | 출력 대상의 대응 근거는 같은 원문 디렉터리의 `vf_or1trn.f:108–224`이다. IPRNT<=1이면 전체 공극률 배열을 기록한다. | 60–82; vf_or1trn.f:108–224 |
| vf_or1trn.f.md:1–30 (정정) | 상세 결과 파일(detailed result file) 시간별 출력 루틴의 형식과 전역·STOC·해저변동 관련 포함 파일을 선언한다. | 상세 결과 파일(detailed result file) 시간별 출력 루틴의 형식과 아래 포함 파일을 선언한다. | 1–29 |
| vf_or1trn.f.md:31–77 (정정) | 연성 유량(flux)·DELH 배열의 범위를 선언한다. | FFLXX·FFLXY·DELH 배열의 범위를 선언한다. FFLXX·FFLXY는 이 구간에서 물리적 의미를 설명하지 않는다. | 31–74 |
| vf_or1trn.f.md:78–107 (보완·정정) | IRSTYP에 따른 단계·시간 조건으로 출력 여부를 판정하고 다음 출력 시각을 갱신한다. 출력 조건을 통과하면 단계·시각·현재 시간 간격(time step)과 체적 및 선형해법 지표를 기록한다. | IRSTYP에 따른 단계·시간 조건으로 출력 여부를 판정하고 다음 출력 시각을 갱신한다. 81–96행의 IF/ELSEIF 사슬에는 ELSE가 없다. IRSTYP가 1도 2도 아니면 IO는 0을 유지한다. 출력 조건을 통과하면 NNOW,TNOW,DTNOW를 기록한다. 다음 레코드에는 FSUM,FCUT,CGBNRM,CGXNRM,ICGITR를 기록한다. | 79–99; 104–106 |
| vf_ot1ini.f.md:54–97 (보완) | 53행 IF 분기 `IF     (ITRPRM(2,L).EQ.0) THEN` 안. 물리량 코드를 유속·압력·VOF 함수(volume of fluid function)·난류·온도·농도·힘 방향·와도(vorticity) 이름으로 변환한다. | 53행 IF 분기 `IF     (ITRPRM(2,L).EQ.0) THEN` 안. 이 IF는 97행 ENDIF에서 닫힌다. L 루프는 131행 레이블 100에서 닫힌다. 물리량 코드를 유속·압력·VOF 함수(volume of fluid function)·난류·온도·농도·힘 방향·와도(vorticity) 이름으로 변환한다. 코드별 출력 대상의 근거는 같은 원문 디렉터리의 `vf_ot1trn.f:100–211,299–326`이다. | 35,53–97,131; 59–97; vf_ot1trn.f:100–211,299–326 |
| vf_ot1ini.f.md:98–132 (보완) | 35행 DO 루프 100 `DO 100 L=1,ITRNUM` 안. | 35행 DO 루프 100 `DO 100 L=1,ITRNUM` 안. L 루프는 131행 레이블 100에서 닫힌다. | 35,131 |
| vf_ot1trn.f.md:57–99 (보완·정정) | ITRTYP의 단계·시간 주기로 출력 여부를 판정한다. ITRPRM(1,L)=0은 지정 경계·조파(wave generation) 소스 수위를 복사하거나 VF_CWLVL을 호출한다. | ITRTYP의 단계·시간 주기로 출력 여부를 판정한다. 60–75행의 IF/ELSEIF 사슬에는 ELSE가 없다. ITRTYP가 1도 2도 아니면 IO는 0을 유지한다. ITRPRM(1,L)=0은 ITRPRM(3,L)=-1,-2,-3,-4이면 BCTYP(7,1:4)의 대응 값을 복사한다. -5이면 SCTYP(7)을 복사한다. 그 외에는 VF_CWLVL을 호출한다. 같은 원문 디렉터리의 `VF_APHYSR.h:55–62,91–98`은 이 값들을 조파하려는 현재 파의 높이로 설명한다. 개방 경계의 BCTYP(7,*)는 `VF_APHYSR.h:67–74`에서 더미로 설명한다. | 58–78; 82–95; VF_APHYSR.h:55–74,91–98 |
| vf_ot1trn.f.md:100–153 (정정·보완) | 96행 ELSE 분기 `ELSEIF (ITRPRM(1,L).EQ.1) THEN` 점값의 U,V는 각 점값은 0으로 시작하여 VF_P1SUMD로 전체 합을 구한다. | 82행 `IF     (ITRPRM(1,L).EQ.0) THEN`에서 열린 분기문의 96행 ELSEIF 분기 `ELSEIF (ITRPRM(1,L).EQ.1) THEN` 82행 IF는 329행 ENDIF에서 닫힌다. L 루프는 330행 레이블 100에서 닫힌다. 점값의 U,V는 각 점값은 0으로 시작하여 VF_P1SUMD로 전체 합을 구한다. 합산 의미의 근거는 같은 원문 디렉터리의 `vf_p1sumd.f:5,18–19,25–30`이다. | 82–96; 82,329–330; 101–153; vf_p1sumd.f:5,18–19,25–30 |
| vf_ot1trn.f.md:154–211 (정정·보완) | 96행 ELSE 분기 `ELSEIF (ITRPRM(1,L).EQ.1) THEN` 100행에서 열린 IF/ELSEIF 문(154행에서 분기 전환 또는 종료) 안. 와도(vorticity) 코드 17..19는 VF_CVORT를 호출한다. | 82행 `IF     (ITRPRM(1,L).EQ.0) THEN`에서 열린 분기문의 96행 ELSEIF 분기 `ELSEIF (ITRPRM(1,L).EQ.1) THEN` 100행 `IF     (ITRPRM(2,L).EQ.1) THEN`에서 열린 분기문 안. 154행에서 ELSEIF 분기로 전환한다. 이 IF는 211행 ENDIF에서 닫힌다. 바깥 82행 IF는 329행 ENDIF에서 닫힌다. L 루프는 330행 레이블 100에서 닫힌다. 와도(vorticity) 코드 17..19는 VF_CVORT를 호출한다. 와도 성분의 의미는 같은 원문 디렉터리의 `vf_cvort.f:6,35,39`에 근거한다. | 82–96; 100,154,211,329–330; 194–208; vf_cvort.f:6,35,39 |
| vf_ot1trn.f.md:212–261 (보완) | 82행에서 열린 IF/ELSEIF 문(212행에서 분기 전환 또는 종료) 안. | 82행 `IF     (ITRPRM(1,L).EQ.0) THEN`에서 열린 분기문 안. 212행에서 ELSEIF 분기로 전환한다. 이 IF는 329행 ENDIF에서 닫힌다. L 루프는 330행 레이블 100에서 닫힌다. | 82,212,329–330 |
| vf_ot1trn.f.md:299–330 (보완) | 82행에서 열린 IF/ELSEIF 문(299행에서 분기 전환 또는 종료) 안. | 82행 `IF     (ITRPRM(1,L).EQ.0) THEN`에서 열린 분기문 안. 299행에서 ELSEIF 분기로 전환한다. 이 IF는 329행 ENDIF에서 닫힌다. L 루프는 330행 레이블 100에서 닫힌다. | 82,299,329–330 |
| vf_ot1trn.f.md:262–298 (정정·보완) | 212행 ELSE 분기 `ELSEIF (ITRPRM(1,L).GE.2 .AND. ITRPRM(1,L).LE.5) THEN` 213행에서 열린 IF/ELSEIF 문(262행에서 분기 전환 또는 종료) 안. 집계 모드에 따라 최솟값·최댓값·평균·적분을 RTRVAL에 선택한다. | 82행 `IF     (ITRPRM(1,L).EQ.0) THEN`에서 열린 분기문의 212행 ELSEIF 분기 `ELSEIF (ITRPRM(1,L).GE.2 .AND. ITRPRM(1,L).LE.5) THEN` 213행 `IF     (ITRPRM(2,L).EQ.1) THEN`에서 열린 분기문 안. 262행에서 ELSEIF 분기로 전환한다. 이 IF는 289행 ENDIF에서 닫힌다. 바깥 82행 IF는 329행 ENDIF에서 닫힌다. L 루프는 330행 레이블 100에서 닫힌다. 290–298행의 집계값 선택 사슬에는 ELSE가 없다. 집계 모드에 따라 VMIN·VMAX·VAV·VINT를 RTRVAL에 선택한다. 같은 원문 디렉터리의 `vf_careap.f:40–43`은 이 값들을 최솟값·최댓값·면적 평균값·면적 적분값으로 설명한다. | 82,212; 213,262,289–298,329–330; 290–298; vf_careap.f:40–43 |
| vf_mzip.f.md:31–52 (보완) | VF_P1SUMD로 전체 합을 구하고 반환한다. | VF_P1SUMD로 전체 합을 구하고 반환한다. 합산 의미의 근거는 같은 원문 디렉터리의 `vf_p1sumd.f:5,18–19,25–30`이다. | 42–43; vf_p1sumd.f:5,18–19,25–30 |

정정 20, 보완 36, 이상 없음 120
