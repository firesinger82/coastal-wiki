---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Propwash/Mod_Erosive_Flux.f90
lines: 45
sha256: 60d82d388b9ceb93002d117cb4f1d43cb869b425b4629cb856c9c0722972245a
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Mod_Erosive_Flux.f90 — 판독 구간 기록

구간은 1행부터 45행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | EFDC+·GPLv2·저작권 머리말(1–8), Mod_Erosive_Flux 시작(9), GLOBAL의 RKD·RK4 사용(11). 기본 private, erosive_flux 공개(13–14). erosive_flux 형식은 allocatable sub_grid_flux(:)와 total_flux 기본값 0.0을 가진다(16–21). 생성자(constructor) 인터페이스(interface)가 constructor_erosive_flux를 연결(23–26). 모듈 contains·빈 줄(28–29). 원문: `real(kind = RKD), Allocatable, Dimension(:) :: sub_grid_flux` (18); `real(kind = RKD) :: total_flux = 0.0` (19). |
| 30–45 | 시작 시 9행 Mod_Erosive_Flux 안. constructor_erosive_flux(nx) 함수 시작(31), 정수 nx 인수(33). sub_grid_flux(nx) 할당(38), 전체 0 초기화(39). self.total_flux=0 대입은 주석 처리(41); 기본값은 형식 선언 19행에 있다. 함수·모듈 종료와 빈 줄(43–45). 조건 분기·외부 계산 루틴 호출은 없다. 원문: `self.sub_grid_flux = 0.0` (39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
