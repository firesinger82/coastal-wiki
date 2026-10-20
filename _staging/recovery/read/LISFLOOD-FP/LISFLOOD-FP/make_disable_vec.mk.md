---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/make_disable_vec.mk
lines: 12
sha256: 1c626629eaa43a3dc23046c8e12becccf3412c34e838477255f8235bb7d704c9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# make_disable_vec.mk — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–6 | 변형 대상(variant target)을 `variants_var += lisflood_float_disable_vec` (1)로 등록한다. `# Linkage rule FLOAT NO VECT` (3)은 링크 규칙 주석이다. 대상·의존성 규칙은 `lisflood_float_disable_vec: $(MAINOBJS:%.o=lisflood_float_disable_vec_obj/%.o)` (4)이고 링크 명령은 `$(LD) $(LDFLAGS) $(MAINOBJS:%.o=lisflood_float_disable_vec_obj/%.o)  -o lisflood_float_disable_vec` (5)이다. 2·6행은 빈 줄이다. |
| 7–12 | `# Compile main object files FLOAT NO VECT` (7)은 오브젝트 파일(object file) 컴파일 주석이다. 정적 패턴 규칙(static pattern rule)은 `$(MAINOBJS:%.o=lisflood_float_disable_vec_obj/%.o): lisflood_float_disable_vec_obj/%.o: %.cpp *.h` (8)이다. 디렉터리 생성·컴파일 명령은 `$(MD) -p lisflood_float_disable_vec_obj` (9), `$(MD) -p lisflood_float_disable_vec_obj/lisflood2` (10), `$(CC) $(CFLAGS_RELEASE) -no-vec -no-simd -D _NUMERIC_MODE=0 -c $< -o $@` (11)이다. `-no-vec`, `-no-simd`, `-D _NUMERIC_MODE=0`을 지정한다. 12행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
