---
file: models/ADCIRC/raw/source_code/adcirc/docs/technical_reference/output_files/fort77.rst
lines: 30
sha256: 26c0b3c393f8741a61618669613b2d56c1c23ae80674f5099da32a518f6ce486
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# fort77.rst — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | Fort.77: Time-varying Weir Output — 제목과 빈 줄을 포함한다(1–5). 문서는 시간 변화 보(time-varying weirs) 기능이 활성화되고 출력이 요청될 때 보 높이 자료를 저장한다고 적는다(4). 저장량은 fort.14의 원래 높이에 대한 변화량이다(4). 희소 형식(sparse format)은 보 절점만 저장한다(4). 절점 번호는 전역 절점 번호 체계(global node numbering system)를 따른다(4). 원문: `` This file contains time-varying weir elevation data when time-varying weirs are activated and output is requested in ADCIRC. The file records changes in elevation from the original elevations specified in the :doc:`Grid and Boundary Information File <../input_files/fort14>`. When written in sparse format, the data is recorded only for weir nodes, with node numbers referenced to the global node numbering system. `` (4). |
| 6–22 | File Structure — 문서는 헤더와 시각·반복 단계, 절점별 보 높이 변화량의 출력 순서를 제시한다(13–21). 예제는 전체 절점 수를 반복 범위로 쓴다(19). 지시문과 중간 빈 줄을 포함한다(6–22). 원문: ` .. parsed-literal:: ` (11); ``     :ref:`RUNDES <RUNDES>`, :ref:`RUNID <RUNID>`, :ref:`AGRID <AGRID>` `` (13); ``     :ref:`NDSETSE <NDSETSE>`, :ref:`NP <NP>`, :ref:`DTDP <DTDP>` * :ref:`NSPOOL_TVW <NSPOOL_TVW>`, :ref:`NSPOOL_TVW <NSPOOL_TVW>`, :ref:`IRTYPE <IRTYPE>` `` (15); ``     :ref:`TIME <TIME>`, :ref:`IT <IT>` `` (17); ``     for k=1, :ref:`NP <NP>` `` (19); ``         k, :ref:`TVW(k) <TVW>` `` (20); `     end k loop ` (21). |
| 23–30 | Notes — 문서는 원래 fort.14 높이에 대한 변화량만 기록한다고 적는다(26). 희소 형식은 보 절점만 포함한다(27). 절점 번호는 전역 절점 번호를 참조한다(28). 문서는 출력 빈도 설정과 출력 변수의 뜻을 적는다(29–30). 원문: ` * Only elevation changes relative to the original fort.14 elevations are recorded ` (26); ` * When using sparse format, only weir nodes are included in the output ` (27); ` * Node numbers (k) reference the global node numbering system ` (28); `` * The output frequency is controlled by :ref:`NSPOOL_TVW <NSPOOL_TVW>` parameter `` (29); ` * TVW(k) represents the change in elevation at node k from the original fort.14 elevation  ` (30). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 4·19–21·27: 희소 형식 설명은 보 절점만 출력한다고 적는다(4·27). 제시된 구조의 반복문은 ``    for k=1, :ref:`NP <NP>` ``이다(19). 이 파일에는 희소 형식의 반복 범위를 별도로 보여 주는 예제가 없다.
