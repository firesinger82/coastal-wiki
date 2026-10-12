---
file: models/ShorelineS/raw/source_code/shorelines/functions/get_fnourishment_fraction.m
lines: 105
sha256: c75a238de2ffd08155ff24c0a65dbb0851814f6d9edebac7fec44261f5b26b7b
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# get_fnourishment_fraction.m — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | 함수 시그니처 `function [fraction,i_mc_rel,idx,dxnour] = get_fnourishment_fraction(xn,yn,x_mc,y_mc,n_mc,ds_mc,shadow_mc)` (1). 해안 구간별 양빈(nourishment) 체적 비율을 구하는 목적·입출력·단위(4–20). 저작권·연락처·LGPL 2.1 이상·무보증·빈 줄(21–48). |
| 49–73 | dxnour·L1·L2·fraction 빈 배열(49–52). 구간 루프 `for i_mc = 1 : n_mc % loop over nourishments in main function` (54), get_one_polygon으로 좌표·격자 간격 추출(55–57). 양빈 양끝 거리 `dist1          = ((xc-xn(1)).^2+(yc-yn(1)).^2).^0.5;` (58); `dist2          = ((xc-xn(2)).^2+(yc-yn(2)).^2).^0.5;` (59), 최근접 인덱스 검색(60–61), 사이 인덱스 범위 `idx{i_mc}      = [min(idx1,idx2):max(idx1,idx2)];` (62). dsc의 NaN=0(65), 대표 간격 `ds0=median(dsc);` (66), get_cyclic 호출(67). 순환 조건 `if cyclic` (68), 역순 끝점 조건 `if idx1 > idx2` (69)의 양끝 연결 인덱스 `idx{i_mc} = [ 1 : idx2  idx1 : length(dist1) ] ;` (70). 자료 선택·계산·호출의 원문은 `xc             = get_one_polygon(x_mc,i_mc);` (55); `yc             = get_one_polygon(y_mc,i_mc);` (56); `dsc            = get_one_polygon(ds_mc,i_mc);` (57); `idx1           = find(dist1==min(dist1),1);` (60); `idx2           = find(dist2==min(dist2),1);` (61); `cyclic = get_cyclic(xc,yc,ds0);` (67). 추가 원문: `dsc(isnan(dsc))=0;` (65). [10-12 전수 검증 보완] |
| 74–88 | 시작 시 54행 i_mc 루프 안. get_one_polygon으로 차폐(shadowing) 마스크 추출(75), 차폐점 검색·범위 membership(76–77), 차폐 인덱스 삭제(78). 끝점 최단 거리·영향 길이 `L1(i_mc)  = min(dist1);` (80); `L2(i_mc)  = min(dist2);` (81); `dxnour(i_mc) = sum(dsc(idx{i_mc}));` (83). NaN 길이 조건 `if isnan(dxnour(i_mc))` (84)이면 0(85). 루프 종료(87). 자료 선택·계산·호출의 원문은 `[ shadowS ]    = get_one_polygon(shadow_mc,i_mc);` (75). 추가 원문: `id_shadow      = find( shadowS == 1 );` (76). `Lia            = ismember( idx{i_mc} , id_shadow );` (77). `idx{i_mc}(Lia) = [];` (78). [10-12 전수 검증 보완] |
| 89–105 | 각 양빈 끝점에 가장 가까운 구간 선택(90–91), 두 구간 번호 배열(92). 같은 구간 조건 `if length(unique(i_mc_rel)) == 1 % fix for one segment` (93)이면 첫 번호만 유지(94). 전체 구간 번호·intersect 호출(96–97), 관련 구간 번호를 삭제 목록에서 빼서 관련 없는 구간만 남기고(98), 그 구간의 idx를 빈 셀로(99), dxnour를 0으로(100) 만든다. [10-12 검증 정정] 전체 길이로 비율 정규화 `fraction = dxnour./sum(dxnour);` (103). 함수 종료와 빈 줄(104–105). 자료 선택·계산·호출의 원문은 `[~,id1] = min(L1);` (90); `[~,id2] = min(L2);` (91). 추가 원문: `i_mc_rel  = [id1 id2];` (92). `i_mc_rel = i_mc_rel(1);` (94). `i_mc_del  = 1 : n_mc;` (96). `[val,ia,ib] = intersect(i_mc_rel,i_mc_del);` (97). `i_mc_del(ib) = [];` (98). `idx(i_mc_del) = {[]};` (99). `dxnour(i_mc_del) = 0;` (100). [10-12 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·54: n_mc 입력 주석은 해안선 점 수를 적는다. 실행문은 n_mc를 구간 추출 루프 상한으로 사용한다.
- 58–62: 양빈 위치는 xn·yn의 첫 두 점으로 접근하며 입력 길이 검사는 없다.
- 90–100: 양빈의 관련 구간은 양끝 각각에 가장 가까운 구간으로 정한다. 관련 없는 구간의 idx 셀 내용은 빈 배열로 바꾼다. 해당 구간의 dxnour는 0으로 대입한다. [10-12 전수 검증 정정]
- 103: 비율 분모 sum(dxnour)가 0인지 검사하는 분기는 없다.
- 97: intersect의 val·ia는 받은 뒤 사용하지 않는다.
