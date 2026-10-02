---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/drifters.F90
lines: 69
sha256: 42c0e8bae3a881126deaa48617848576cfcfad387a1eb9c5be185d899bda76c9
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# drifters.F90 — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `drifter_module`: implicit none·private·save, drifter 공개(1–5). `drifter(s,par)`는 parameters·spacepars·xmpi_module 사용, drifter 번호·로컬 이동량·u/v 격자 인덱스 선언(7–20). |
| 23–30 | MPI에서는 `ishift=is(rank+1)-1`, `jshift=js(rank+1)-1`(24–25), 비MPI는 둘 다 0(27–28). |
| 31–39 | i=1..ndrifter, 시작시간보다 크고 종료시간보다 작은 t에서만 이동(31–32). 최근접점 식 `iu=nint(idrift-ishift-0.d5)`, `ju=nint(jdrift-jshift)`, `iv=nint(idrift-ishift)`, `jv=nint(jdrift-jshift-0.d5)`(35–38). |
| 40–52 | iu/iv=1..nx·ju/jv=1..ny 모두 만족할 때(41–44), `di=uu(iu,ju)/dsu(iu,ju)*dt`, `dj=vv(iv,jv)/dnv(iv,jv)*dt`(47–48); 분수 격자좌표 idrift/jdrift에 각각 더함(50–51). |
| 53–69 | MPI에서 로컬 영역 밖이면 두 좌표를 `huge(0.0d0)-10000.d0`로 설정(54–56). 이후 idrift·jdrift 각각 `xmpi_allreduce(...,MPI_MIN)`(61–62). 비MPI의 영역 밖 대입은 없음. 시간 조건·루프·루틴·모듈 종료(65–69). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 35·38: staggered 최근접점에서 빼는 리터럴은 문자 그대로 `0.d5`이며 `0.5d0`가 아니다. `0.d5`는 값 0인 지수 표기이다.
- 41–44: ju/jv의 상한은 s%ny이므로 ny=0이면 이 영역 안 조건을 만족하는 j 인덱스가 없다.
- 61–62: MPI_MIN은 idrift와 jdrift에 별도로 호출된다. 같은 rank의 두 좌표를 하나의 쌍으로 선택하는 코드는 이 루틴에 없다.
