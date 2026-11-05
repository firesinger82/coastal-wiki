# CADMAS-SURF code-20 전수 대조

대상 기록의 frontmatter `file:` 원문을 구간별 `nl -ba <원문> | sed -n 'A,Bp'` 출력으로 대조했다.
원문은 수정하지 않았다.
모델은 실행하지 않았다.
git 작업은 수행하지 않았다.
기록 경로의 기준은 `../Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/`이다.
행 수는 원문의 빈 행과 주석을 포함한다.
정정·보완·이상 없음의 집계 단위는 기록의 구간 표 행이다.

| 기록 | 대조한 원문 행 수 | 대조한 구간 행 수 | 상태 |
|---|---:|---:|---|
| contact/mpccorr12.f.md | 35 | 3 | 완료 |
| contact/mpccorr13.f.md | 38 | 3 | 완료 |
| contact/mpccorr2.f.md | 32 | 3 | 완료 |
| contact/mpccorr3.f.md | 35 | 3 | 완료 |
| contact/mpcedge.f.md | 124 | 4 | 완료 |
| contact/mpcface.f.md | 108 | 4 | 완료 |
| contact/mpcpreb.f.md | 105 | 4 | 완료 |
| contact/mpcrank.f.md | 81 | 3 | 완료 |
| contact/mpcset.f.md | 136 | 5 | 완료 |
| contact/mpcset2.f.md | 71 | 3 | 완료 |
| contact/mpcsize.f.md | 39 | 2 | 완료 |
| contact/mpcslv.f.md | 151 | 5 | 완료 |
| contact/mpcstke.f.md | 66 | 3 | 완료 |
| contact/mpcstkf.f.md | 63 | 3 | 완료 |
| contact/mpcvrtx.f.md | 39 | 3 | 완료 |
| contact/mstnod.f.md | 33 | 2 | 완료 |
| contact/npfedge.f.md | 95 | 4 | 완료 |
| contact/npfface.f.md | 166 | 5 | 완료 |
| contact/npforced.f.md | 61 | 3 | 완료 |
| contact/npfric.f.md | 97 | 4 | 완료 |
| contact/npfricd.f.md | 41 | 3 | 완료 |
| contact/nrmvec.f.md | 10 | 1 | 완료 |
| contact/penchk.f.md | 65 | 3 | 완료 |
| contact/penst.f.md | 45 | 2 | 완료 |
| contact/resfric.f.md | 71 | 4 | 완료 |
| contact/rfcedge.f.md | 56 | 3 | 완료 |
| contact/rfcface.f.md | 49 | 3 | 완료 |
| contact/rhsidxb.f.md | 50 | 3 | 완료 |
| contact/rhsidxf.f.md | 45 | 3 | 완료 |
| contact/rhsidxr.f.md | 22 | 2 | 완료 |
| contact/rlcorr.f.md | 46 | 3 | 완료 |
| contact/rmpccal.f.md | 20 | 2 | 완료 |
| contact/slvnrm.f.md | 30 | 3 | 완료 |
| contact/spcdedge.f.md | 38 | 2 | 완료 |
| contact/spcdface1.f.md | 11 | 1 | 완료 |
| contact/spcdface2.f.md | 47 | 3 | 완료 |
| contact/spcdface3.f.md | 42 | 2 | 완료 |
| contact/stickchk.f.md | 99 | 4 | 완료 |
| contact/tredge.f.md | 23 | 2 | 완료 |
| contact/trface.f.md | 23 | 2 | 완료 |
| contact/volcd.f.md | 52 | 3 | 완료 |
| contact/volin.f.md | 25 | 2 | 완료 |
| contact/volin3.f.md | 15 | 1 | 완료 |
| contact/vrtxchk.f.md | 73 | 4 | 완료 |
| contact/vrtxsepa.f.md | 39 | 2 | 완료 |
| contact/vrtxslip.f.md | 105 | 5 | 완료 |
| contact/vrtxstk.f.md | 13 | 1 | 완료 |
| contact/wrksize.f.md | 61 | 3 | 완료 |
| femap/blk_e.f.md | 5 | 1 | 완료 |
| femap/blk_s.f.md | 7 | 1 | 완료 |

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 | 구분 |
|---|---|---|---|---|
| contact/mpcedge.f.md:81–124 | 바깥 IF를 행 번호로만 표기 | IEDQ 조건식과 122행 닫힘 명시 | 60, 81, 122 | 보완 |
| contact/mpcface.f.md:69–108 | 바깥 IF를 행 번호로만 표기 | IFCQ 조건식과 106행 닫힘 명시 | 49, 69, 106 | 보완 |
| contact/mpcedge.f.md:29–59 | J1 분기 사슬의 ELSE 부재 미기재 | ELSE가 없음을 명시 | 42–51 | 보완 |
| contact/mpcrank.f.md:56–81 | 바깥 IF·루프를 이름으로만 표기 | 조건식·루프 범위·닫힘·GOTO 목적지와 ELSE 부재 명시 | 18, 22, 27, 62–79 | 보완 |
| contact/mpcset.f.md:49–84 | 바깥 분기 조건과 닫힘 위치의 명시 부족 및 호출 용도 단정 | NIDEP 조건식과 125행 닫힘 명시 및 용도를 해석으로 구분 | 17, 68, 78, 125 | 보완 |
| contact/mpcset.f.md:85–124 | 바깥 분기 조건과 닫힘 위치의 명시 부족 | NIDEP 조건식과 125행 닫힘 명시 | 17, 68, 78, 125 | 보완 |
| contact/mpcset.f.md:125–136 | 바깥 분기 조건과 닫힘 위치의 명시 부족 | NIDEP 조건식과 125행 닫힘 명시 | 17, 68, 78, 125 | 보완 |
| contact/mpcset2.f.md:51–71 | NESTF를 삼각형 저장 항 수로 단정 | 계산 사실과 저장 용도 해석을 구분 | 65–69 | 정정 |
| contact/mpcsize.f.md:11–39 | 사각형 추가량의 분기별 조건을 생략한 요약과 바깥 루프 이름 표기 | IVRQ·IEDQ·IFCQ의 양수 조건과 루프 범위·닫힘 명시 | 8, 11–37 | 정정 |
| contact/mpcslv.f.md:66–104 | 바깥 루프를 이름으로만 표기 | I=2,NROW와 113행 닫힘 명시 | 57, 113 | 보완 |
| contact/mpcslv.f.md:105–116 | 바깥 루프를 이름으로만 표기 | I=2,NROW와 113행 닫힘 명시 | 57, 113 | 보완 |
| contact/mpcslv.f.md:1–42 | IC=0 경로와 ELSE 부재 미기재 | IC=0의 오류 출력·호출 경로 명시 | 19–40 | 보완 |
| contact/mpcstke.f.md:28–66 | 바깥 IF를 행 번호로만 표기 | 바깥 조건식과 ENDIF 위치 명시 | 12, 64 | 보완 |
| contact/mpcstkf.f.md:28–63 | 바깥 IF를 행 번호로만 표기 | 바깥 조건식과 ENDIF 위치 명시 | 12, 61 | 보완 |
| contact/mpcvrtx.f.md:22–39 | 바깥 IF를 행 번호로만 표기 | 바깥 조건식과 ENDIF 위치 명시 | 11, 37 | 보완 |
| contact/mstnod.f.md:15–33 | 바깥 SELECT CASE의 선택식 미기재 | IST 선택식과 닫힘 위치 명시 | 6, 31 | 보완 |
| contact/npfedge.f.md:1–25 | VR의 물리적 뜻을 구간 근거 없이 단정; 다른 파일에 있는 설명 근거의 출처 누락 | 코드 계산과 상대 속도 해석을 구분; 변 방향 E 계산의 보조 루틴 근거 추가 | 13–20; 8–9; util/dircos.f:8–15(정규화) | 정정 |
| contact/npfedge.f.md:26–52 | IFMDL·IDYN 분기의 ELSE 부재 미기재 및 RMU 용도 단정 | ELSE 부재와 FT 유지 경로 명시 및 RMU 의미를 해석으로 구분 | 24–51 | 보완 |
| contact/npfedge.f.md:63–95 | 바깥 IF를 행 번호로만 표기 | IEDQ 조건식과 93행 닫힘 명시 | 53, 93 | 보완 |
| contact/npfface.f.md:1–33 | VR의 물리적 뜻을 구간 근거 없이 단정 | 계산 사실과 상대 속도 해석을 구분 | 21–30 | 정정 |
| contact/npfface.f.md:34–70 | MODE 분기의 ELSE 부재 미기재 및 RMU 용도 단정 | ELSE 부재 명시 및 RMU 의미를 해석으로 구분 | 34–69 | 보완 |
| contact/npfface.f.md:71–114 | 바깥 조건·닫힘과 ELSE 부재 설명 부족 | 전체 바깥 조건식과 닫힘 및 네 분기 사슬의 ELSE 부재 명시 | 34, 43–47, 71–125 | 보완 |
| contact/npfface.f.md:115–126 | 바깥 조건식 및 ELSE 부재 설명 부족 | 전체 조건식과 닫힘 및 FT 초기값 유지 경로 명시 | 32–45, 115–125 | 보완 |
| contact/npforced.f.md:42–61 | 바깥 루프를 이름으로만 표기 | 루프 범위와 59행 닫힘 명시 | 21, 59 | 보완 |
| contact/npfric.f.md:50–73 | 바깥 루프 범위·닫힘 및 ELSE 부재 미기재 | IR·I 루프 범위와 닫힘 및 ELSE 부재 명시 | 36, 38, 50–87 | 보완 |
| contact/npfric.f.md:74–97 | 바깥 루프 범위·닫힘 미기재 | IR·I 루프 범위와 닫힘 명시 | 36, 38, 50–87 | 보완 |
| contact/npfricd.f.md:19–29 | 바깥 루프 범위·닫힘 미기재 | 루프 범위·닫힘 명시 및 ELSE 부재 명시 | 11, 19–39 | 보완 |
| contact/npfricd.f.md:30–41 | 바깥 루프 범위·닫힘 미기재 및 저장 용도 단정 | 루프 범위·닫힘 명시 및 저장 용도를 해석으로 구분 | 11, 19–39 | 보완 |
| contact/penchk.f.md:42–65 | 바깥 루프를 이름으로만 표기; 다른 파일에 있는 설명 근거의 출처 누락 | 루프 범위와 닫힘 및 GOTO 목적지 명시; 보간 연산의 보조 루틴 근거 추가 | 16–40, 61, 63; 47–48; util/rmult5.f:8–10(가중합) | 보완 |
| contact/penst.f.md:1–22 | 항상 세 RL 성분의 최소값과 I_MIN을 구한다고 서술 | 초기값 1.1D0과 갱신 조건 및 미대입 경로 명시 | 12–21 | 정정 |
| contact/rfcedge.f.md:26–56 | 바깥 IF를 행 번호로만 표기 | IEDQ 조건식과 54행 닫힘 명시 | 18, 54 | 보완 |
| contact/rfcface.f.md:22–49 | 바깥 IF를 행 번호로만 표기 | IFCQ 조건식과 47행 닫힘 명시 | 14, 47 | 보완 |
| contact/rhsidxb.f.md:43–50 | 바깥 루프를 이름으로만 표기 | II=2,NROW와 닫힘 명시 | 14, 45 | 보완 |
| contact/rhsidxf.f.md:38–45 | 바깥 루프를 이름으로만 표기 | I=2,NROW와 닫힘 명시 | 12, 40 | 보완 |
| contact/rlcorr.f.md:31–46 | 바깥 IF 조건식과 앞 분기 우선순위 설명 부족 | 연속 조건식·닫힘·앞 분기 불일치 조건 명시 | 14–15, 17, 21–22, 26–27, 31–43 | 보완 |
| contact/rlcorr.f.md:1–13 | AREACD 인수 RL을 면 좌표로 단정 | 호출 사실과 RL 의미 해석을 구분 | 7–12 | 정정 |
| contact/slvnrm.f.md:1–10 | SNRM의 법선 용도를 구간 근거 없이 단정 | 용도 설명을 해석으로 구분 | 1–9 | 정정 |
| contact/spcdface2.f.md:1–20 | IC 분기의 ELSE 부재와 반복 대입 결과 미기재 | ELSE 부재와 마지막 일치 방향의 대입 명시 | 11–19 | 보완 |
| contact/stickchk.f.md:46–72 | 바깥 SELECT의 선택식·닫힘 미기재 | IDYN 선택식과 97행 닫힘 명시 | 22–23, 97 | 보완 |
| contact/stickchk.f.md:73–99 | ISTK 전체 대입과 ISLV 조건부 IFRIC 대입을 압축하여 모호하게 서술 | ISTK 전체 대입과 IFRIC 조건부 대입을 분리하고 바깥 SELECT 명시 | 22–23, 73–97 | 정정 |
| contact/vrtxchk.f.md:63–73 | 바깥 IF의 원문 조건 및 ELSE 부재 미기재 | NSLIP 조건·닫힘과 ISLV 미갱신 경로 명시 | 36, 63–71 | 보완 |
| contact/wrksize.f.md:43–61 | 바깥 루프를 이름으로만 표기 | I 범위 및 두 루프의 닫힘 위치 명시 | 15, 21, 53, 55 | 보완 |
| contact/mpccorr12.f.md:1–10 | 다른 파일에 있는 설명 근거의 출처 누락 | 복사·가중합·차·합의 보조 루틴 근거 추가 | 7–9, 24, 29–32; util/shift1.f:16–18(복사), util/rmult5.f:8–10(가중합), util/subvec.f:9–11(차), util/addvec.f:9–11(합) | 보완 |
| contact/mpccorr13.f.md:1–11 | 다른 파일에 있는 설명 근거의 출처 누락 | 복사·보정 연산과 목표 위치 식의 근거 추가 | 7–10, 25–29, 32–35; util/shift1.f:16–18(복사), util/subvec.f:9–11(차), util/addvec.f:9–11(합), contact/spcdface1.f:6–8, contact/spcdface2.f:31–44, contact/spcdface3.f:31–39(목표 위치) | 보완 |
| contact/mpccorr2.f.md:1–9 | 다른 파일에 있는 설명 근거의 출처 누락 | 복사·합·LENCD 반환값의 보조 루틴 근거 추가 | 6–8, 23, 28–29; util/shift1.f:16–18(복사), util/addvec.f:9–11(합), contact/lencd.f:13–14(DUG에 대응하는 V34 계산) | 보완 |
| contact/mpccorr3.f.md:1–10 | 다른 파일에 있는 설명 근거의 출처 누락 | 복사·합의 보조 루틴 근거 추가 | 6–9, 31–32; util/shift1.f:16–18(복사), util/addvec.f:9–11(합) | 보완 |
| contact/mpcedge.f.md:1–28 | 다른 파일에 있는 설명 근거의 출처 누락 | 방향 벡터·삽입 정렬의 보조 루틴 근거 추가 | 11–12, 21; util/subvec.f:9–11(차), util/dircos.f:8–15(정규화), util/shiftb0.f:5–7(삽입 시 배열 이동) | 보완 |
| contact/mpcface.f.md:1–24 | 다른 파일에 있는 설명 근거의 출처 누락 | 차 벡터·삽입 정렬의 보조 루틴 근거 추가 | 8–9, 17; util/subvec.f:9–11(차), util/shiftb0.f:5–7(삽입 시 배열 이동) | 보완 |
| contact/penchk.f.md:16–41 | 다른 파일에 있는 설명 근거의 출처 누락; 좌표 복사도 IPFLG=1에 종속되는 것처럼 읽히는 요약 | 거리·좌표 복사의 보조 루틴 근거 추가; 면 제외 조건과 이후 좌표 복사의 실행 조건을 분리 | 34–39; util/length.f:6–12(거리), util/shift1.f:16–18(복사); 29–36 | 정정 |
| contact/rfcedge.f.md:1–17 | 다른 파일에 있는 설명 근거의 출처 누락 | 투영 설명의 E 정규화 근거 추가 | 13–16; util/dircos.f:8–15(E 정규화) | 보완 |
| contact/rfcface.f.md:1–13 | 다른 파일에 있는 설명 근거의 출처 누락 | 투영 설명의 E 정규화 근거 추가 | 10–12; contact/areacd.f:9–11,46(E에 대응하는 RN 반환), util/cross2.f:9–16(정규화된 외적) | 보완 |
| contact/vrtxstk.f.md:1–13 | 다른 파일에 있는 설명 근거의 출처 누락 | 거리 XL 설명의 보조 루틴 근거 추가 | 6; util/length.f:6–12(거리) | 보완 |
| contact/rhsidxb.f.md:14–42 | 다른 파일에 있는 설명 근거의 출처 누락 | 열 병합 시 중복을 추가하지 않는 의미와 복사 근거 명시 | 22, 38; util/order2.f:5–22; util/shift0.f:15–17 | 보완 |
| contact/rhsidxf.f.md:12–37 | 다른 파일에 있는 설명 근거의 출처 누락 | 열 병합 시 중복을 추가하지 않는 의미와 복사 근거 명시 | 18, 33; util/order2.f:5–22; util/shift0.f:15–17 | 보완 |

대상 기록 50개를 모두 완료했다.
대상 기록의 원문 행 수 합계는 2,803행이다.
대상 기록의 구간 표 행 수 합계는 143행이다.
보조 루틴은 설명 근거에 필요한 구간만 확인했다.
보조 루틴의 행 수는 대상 원문 행 수 합계에 포함하지 않았다.

정정 9, 보완 45, 이상 없음 89
