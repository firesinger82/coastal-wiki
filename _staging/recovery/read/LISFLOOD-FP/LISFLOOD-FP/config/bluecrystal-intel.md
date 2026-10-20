---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/bluecrystal-intel
lines: 3
sha256: d8a6a128ed3d32631e76555e058d19d8e1693f3f5943fbde81a14599589676eb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# bluecrystal-intel — 판독 구간 기록

구간은 1행부터 3행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–3 | Intel 컴파일러 옵션은 `CXXFLAGS := -std=c++14 -Wall -O3 -parallel -qopenmp -static -qopt-report=2 -qopt-report-phase=vec -xhost -ipo -D_NUMERIC_MODE=1 -D_NETCDF=0 -D_ONLY_RECT=0` (1)이다. 링크 옵션은 `LDFLAGS := -w -O3 -parallel -qopenmp -static-intel -lnuma` (2)이다. 3행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
