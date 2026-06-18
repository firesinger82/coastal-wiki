# code/ — Delft3D FLOW+WAVE+morphology 설정 템플릿

> ⚠ **대표 구조 템플릿** (placeholder 값). 정확한 키워드·스키마는 Delft3D 공식 매뉴얼([`delft3d-flow-user-manual`](../../../models/Delft3D/manual-notes/delft3d-flow-user-manual.md)·[`delft3d-wave-user-manual`](../../../models/Delft3D/manual-notes/delft3d-wave-user-manual.md)) 참조. 본 위키는 결합 메커닉(검수 source-analysis)을 보이기 위한 구조만 제공.

| 파일 | 핵심 키워드 (검수 근거) |
|---|---|
| [`dimr_config.xml`](dimr_config.xml) | FLOW↔WAVE 교대 구동·결합주기(itcomi). COM 파일 교환([[../../../models/Delft3D/source-analysis/wave/delft3d_flow_wave_coupling]]) |
| [`morphology.mor`](morphology.mor) | **MorFac**(형태가속)·MorStt(spin-up)·MorUpd(bed 갱신=Exner) ([[../../../models/Delft3D/source-analysis/delft3d_sediment_morphology]]) |
| `flow.mdf` | (별도 미작성) FLOW 격자·수심·경계 + `Sedim`=sediment.sed·`Morph`=morphology.mor 참조·`WaveOL` online wave |
| `wave.mdw` | (별도 미작성) SWAN 격자(FLOW nesting)·파 경계·물리(GEN3/breaking) |
| `sediment.sed` | (별도 미작성) 입경 D50·밀도·sand/mud·transport formula(`iform`) |

표준 .mdf/.mdw/.sed 의 전체 키워드 reference 는 매뉴얼 manual-notes 에 정리(향후 보강). 본 예제 code/ 는 **morphodynamic 결합 고유 파일**(dimr_config·morphology.mor)에 집중.
