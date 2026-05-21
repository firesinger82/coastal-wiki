# models/ADCIRC

## 정체 카드 (TBD)

- **이름**: ADCIRC (ADvanced CIRCulation Model)
- **저자/관리주체**: Luettich, Westerink 외 (UNC/Notre Dame)
- **라이선스**: 학술/연구 무료, 상업 라이선스 별도
- **공식 사이트**: adcirc.org
- **소스 위치**: TBD
- **공식 메뉴얼**: TBD (web-refs/에 정리)
- **사용 도메인**: 2D/3D 조석·해일·연안 흐름
- **주 좌표계·격자**: unstructured triangular mesh

## 하위

- `source-analysis/` — TBD
- `manual-notes/` — TBD
- `web-refs/` — adcirc.org/wiki, GitHub repo, 주요 논문

## 작성 우선순위

1. `web-refs/`에 공식 위키 핵심 페이지 + 핵심 논문 (Luettich 1991 등) 정리
2. mesh 생성 워크플로 (SMS, OceanMesh2D) 정리
3. 조석 forcing(`models/ADCIRC/source-analysis/tidal_forcing.md`) — `concepts/tides/06-model-application.md`와 연결
