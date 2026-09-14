# Fable 5.1 한정 정정 검토

**결론: 차단 사유 없음** (검토 범위 한정). 패치가 도입한 주장은 evidence.json에 명시된 소스 구간이 모두 지지하며, 과거 `verified` 이력을 새 승인으로 승계하는 서술도, 실행·수치·물리 검증이나 외부 DB 품질을 확인했다는 서술도 없다. 아래는 항목별 대조 결과와 선택적 미세 수정이다.

**항목별 대조 (로컬 snapshot `6037225`)**

- **NBFR 블록 추가 줄 제거**: `read_input.F:3431–3442`의 헤더 루프 뒤에 `3450–3456`의 `ELEVALPHA`+`EMO/EFA` 루프가 바로 이어진다. 그 사이 READ는 없고 3443은 fort.19 존재 시 로그 출력뿐이다. `[blank or ELEVALPHA line]` 삭제는 정확하다.
- **EMO/EFA 첨자**: `read_input.F:3451–3454`는 `I=1..NBFR`, `J=1..NETA`로 `EMO(I,J)`를 읽고, `gwce.F:1638–1649`는 `J`=분조, `I`=노드로 `EMO(J,I)`를 쓴다. 첫 첨자=분조, 둘째=경계 노드가 맞다. harmonic-prep 도식의 `EMO(j,i)`(j=분조 루프)와 forcing-impl 43행의 기존 `EMO(I,J)`(I=분조 루프)는 서로 모순되지 않는다.
- **NBDV → NBD → 합성**: `mesh.F:1822–1834`가 `K=1..NOPE`, `I=1..NVDLL(K)` 순으로 `NBD(JNMM+I)=NBDV(K,I)`를 채운다. `read_input.F:3481`이 `initializeBoundaries()`를 호출한 뒤 `3494`가 `NBD(J),EMO(I,J),EFA(I,J)`를 기록하고, `gwce.F:1648–1649`가 `Eta2(NBD(I))`에 더한다. "격자 번호 정렬이 아니라 경계 목록 순서"라는 연결이 성립한다.
- **degree/radian·STATIM/REFTIM/TimeH**: `FACE` 변환 `3436`, `EFA` 변환 `3496`(로그 출력 후) 확인. `STATIM`·`REFTIM`은 `2534`·`2541`에서 읽히고 echo 포맷이 DAYS이며, `timestep.F:258`의 `(StaTim−RefTim)*86400`이 일→초 해석을 뒷받침한다. 합성식 `AMIG(J)*(timeh−NCYC*PER(J))+FACE(J)−EFA(J,I)`는 `gwce.F:1644,1647`과 일치한다.
- **ETRF 범위**: `timestep.F:1536`의 `TPMUL=RampTip*ETRF(J)*TPK(J)*FFT(J)`는 `1550–1556`의 ELSE 분기(`.not.tidePotential%active()`)에서만 `TIP2`에 곱해진다. 외곽 조건 `1527`은 `NTIP.EQ.2 .or. .not.active()`이므로 비활성 시 NTIP 값과 무관하게 진입한다. `SALTMUL=RampTip*FFT(J)`(`1537`)에는 ETRF가 없고, full-formula는 `1520–1521`의 별도 분기다. "ETRF=0 → full potential 적용"이라는 옛 5번 규칙은 코드와 반대였으며, 정정문의 세 경로 분리 서술은 정확하다. 기존 ETRF 절(candidate 114–122행)과도 모순되지 않는다.
- **승인·검증 범위 표기**: 새 frontmatter 필드가 `human_approval: not-issued`와 범위를 명시하고, 본문 한정 절이 실행·검증 미수행을 밝힌다. CONVENTIONS §2 54행("새 주장에 과거 HG 자동 승계 금지")과 부합한다. 검증 도구는 `citation_status`만 정규식으로 검사하므로 신규 키가 validator를 깨뜨릴 근거는 찾지 못했다. 단, validator 실행은 하지 않았다.

**선택적 미세 수정 (비차단)**

1. forcing-impl 새 문단 "`EMO(J,I)`를 `NBD(I)`에 더한다"는 축약이다. 정확히는 `EMO(J,I)*FF(J)*RampElev*cos(ARG)`를 `Eta2(NBD(I))`에 더한다(`gwce.F:1645,1649`). 한 구절 교체를 권한다.
2. CONVENTIONS §2 52행은 대조 범위·한계를 `verification_method`에 기록하라고 한다. 패치는 이를 `source_correction_scope`와 본문 절에 두고 `verification_method`는 옛 문구 그대로다. 공개 자체는 충분하므로 차단은 아니나, `verification_method` 끝에 "2026-09-14 한정 대조 절 참조" 한 구절을 덧붙이면 규약과 일치한다.
3. README 표 4행 `timestep.F:1517–1556`과 패치의 `1517–1555`가 한 줄 어긋난다. 어느 쪽이든 서브루틴 내부이므로 실질 영향은 없다.

**이 검토가 확인하지 않은 것**: 공식 웹 페이지(fort.15·parameter definitions)의 `ALPHAE` 표기와 첨자 표기, `global.F:387,1045` 선언, validator 실제 실행. 이는 evidence.json의 자기신고에 의존한다. 옛 source-needed(0.69/0.736 표준값, 외부 DB 위상규약)는 패치가 의도적으로 유지했고, 이번 delta가 그 항목에 새 모순을 만들지는 않는다.

이 검토는 소스 대조 범위 한정 검토이며 과학적 사람 게이트나 승인 발급이 아니다.
