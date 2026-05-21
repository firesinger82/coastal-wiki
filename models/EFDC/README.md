# models/EFDC

## 정체 카드 (TBD)

- **이름**: EFDC (Environmental Fluid Dynamics Code)
- **저자/관리주체**: 원본 — Hamrick (VIMS, 1992~). 현 분기 다수 (EFDC+, DSI EFDC, GEFDC 등)
- **라이선스**: 분기별 상이 — 확인 필요
- **공식 사이트**: TBD
- **소스 위치**: TBD (사용자 보유 분기)
- **공식 메뉴얼**: `D:\Study\textbook\692624517-EFDC.pdf`, `86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.pdf`
- **사용 도메인**: 3D 수리·수질·표사·온도·염분
- **주 좌표계·격자**: curvilinear orthogonal, sigma layer

## 하위

- `source-analysis/` — 서브루틴별 분석 (TBD)
- `manual-notes/` — 메뉴얼 노트 (TBD)
- `web-refs/` — 외부 자료 (TBD)

## 작성 우선순위

1. `manual-notes/`에 692624517-EFDC.pdf 챕터별 발췌
2. 사용자 보유 EFDC 소스 위치 확인 → `source-analysis/`에 주요 서브루틴 (CALEXP, CALPUV, CALCSER 등) 분석
3. 표사이동 부분은 `86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.pdf` 별도 정리
