---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/result_check.mk
lines: 7
sha256: 296d4258b56a856f00a1a01e35708ebc066f4ae6f20f7923d4ff1b308a9f9c03
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# result_check.mk — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–3 | 결과 확인 빌드 대상과 링크 명령은 `lisflood_double_result_check: $(MAINOBJS:%.o=lisflood_double_result_check_obj/%.o)` (1), `$(LD) $(LDFLAGS) $(MAINOBJS:%.o=lisflood_double_result_check_obj/%.o) -o lisflood_double_result_check` (2)이다. 3행은 빈 줄이다. |
| 4–7 | 정적 패턴 규칙(static pattern rule)은 `$(MAINOBJS:%.o=lisflood_double_result_check_obj/%.o): lisflood_double_result_check_obj/%.o: %.cpp *.h` (4)이다. 디렉터리 생성 명령은 `$(MD) -p lisflood_double_result_check_obj` (5), `$(MD) -p lisflood_double_result_check_obj/lisflood2` (6)이다. 컴파일 명령은 `$(CC) $(CFLAGS_RELEASE) -D _NUMERIC_MODE=1 -D RESULT_CHECK=1 -c $< -o $@` (7)이며 `-D _NUMERIC_MODE=1`, `-D RESULT_CHECK=1`을 지정한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
