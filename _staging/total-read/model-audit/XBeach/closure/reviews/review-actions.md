# 적대적 검토 조치

## Claude 1

- 귀속 fallback은 `project-distribution`, `attribution_method=unmatched-distribution-placement`, `authorship_status=not-adjudicated`, `own_solver_count_eligible=false`로 명시했다. 프로젝트 트리 역할과 upstream 확인을 구별하며, 1,472처분을 결함 수로 읽지 않는다.
- MSI File 테이블 확인으로 실제 오류를 찾았다: 초기 hard04는 `mpich2nemesisp.dll`을 `mpich2mpi.dll`로 오인했다. 실제 dispatcher의 출력 미대입 오류 복귀를 확인해 기각을 철회하고 범위를 한정한 경고로 유지했다. `local-refutations/mpich-identity/identity-ledger.json`의 override가 초기 hard04에 우선한다. hard05 cxx.lib는 MSI 멤버와 바이트 동일성이 확인됐다.

## Claude 2

local8 판정은 전건 유지, source60 고위험 표본의 오류는 발견되지 않았다. 원문 재대조 60/60을 주장하지 않는다.

`space_distribute_space`와 `ranges_init` 사이에 13개 초기화 호출이 있다는 정밀성 지적은 원문으로 기각했다. `libxbeach.F90:158-188`의 초기화·hotstart_init_2가 먼저이며, `space_distribute_space`는207행, `ranges_init`은210행으로 두 호출 사이에는 `#endif`와 빈 줄뿐이다. 제안한 call_path는 hotstart_init_2까지 잘못 이동시키므로 적용하지 않았다. canonical의 “공간 분할 직후”와 기존 call_path를 유지한다. 리뷰어 제안도 실제 원문과 대조한다.

## Claude 3

MSI File 테이블·실제 dispatcher 반환 분기·backend 역어셈블리·cxx.lib 포인터 치환을 Claude가 독립 재현했다. 도해와 공식예제 연결 노트도 원문 대조했다. 검토 시작 시 부재했던 identity-ledger.json은 완성되어 최종 override를 담는다. mpi.lib import descriptor는 archive-level evidence로 기록했으며, 구체 실행파일의 실제 링크/로드를 입증한다는 리뷰어의 확장 해석은 채택하지 않았다.

## 문서 자체 점검에서 선행 수정

정렬률이 낮은 DOCX→PDF 위치는 페이지를 근거로 승격하지 않고 원본 DOCX 문단·표 행과 직접 인용으로 전환했다. 상호 duplicate candidate는 검토 편의를 위한 묶음이며 의미적으로 동일한 사실임을 자동 확정하지 않는다. 207 입력 ID는 계속 각각 보존한다. 같은 코드 판정과 해시를 여러 문단에 반복하지 않도록 출처와 판정의 기준 위치를 모았다.

## Claude 4

문서4편을 전부 읽고207 ID·판정·인용보존을 확인했다. 의미적 원문대조는15~20건 표본이며207 독립 재검토라고 주장하지 않는다. B1(부분정렬15행의 불명확한 페이지 근거)과 B2(71개 대응쌍을 완전 동일 사실로 보이는 문구)는 문서 자체 점검과 같은 문제로 수정했다. 개인 실행 근거를 제거한 baseline 연결 노트는 Claude3에서 검토했고 과거 내용은 archive로 보존했다.

## Codex 최종 검토 P1/P2

P1의 전체8 topic을 exact207 문장으로 재대조했다. nuh XH102→100, bedfriction101→100, dilatancy066→067, adaptation-time098삭제, posdwn069→075, dtheta070→078로 교정했다. 각 binding에 원 finding 문장과 SHA를 붙였다. 총26 독립ID/29 topic연결이며 XH100·135·147은 각각 두 근거를 갖는다. 원본 코드 인용은 바뀌지 않았다. P2는 ID→list로 바꿔 행별 JSONL/CSV가 모든 topic 근거를 보존하도록 수정했다. 26 ID/29 topic의 집합 일치와 CSV↔JSONL 전체 객체 일치 검사를 추가했으며, 잘못된6개 ID에 판정이 남지 않음을 확인했다.

## 최종 한정 재검토

[Claude5](claude-round5-recheck.md)는 P1·P2 및 B1·B2가 데이터·코드·본문에 일관되게 반영됐고 해당 수정 범위의 잔여 blocker가 없음을 확인했다. 검토의 한계를 각 보고서와 함께 보존하며, AI 교차대조를 새 사람 승인으로 표기하지 않는다.
