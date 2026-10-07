---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/MPI_Utilities/mod_Variables_MPI_Write_Out.f90
lines: 267
sha256: 98ba01bcc058bb391e75f46c548473dfabc66db4ca7926a7107c4f86b55200a0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_Variables_MPI_Write_Out.f90 — 판독 구간 기록

구간은 1행부터 267행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | EFDC+ 표제·저작권·GPLv2·개발사 안내(1–11). EE_*.OUT 출력용 전역(global) 변수를 담는 모듈 설명·저자·2019-09 추가 이력(12–22). Variables_MPI_Write_Out 시작·GLOBAL 사용·implicit none·빈 줄(24–29). |
| 30–56 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. RICEWHT_global은 3차원 기본 Real allocatable(30). CUE/CUN/CVN/CVE_Global은 1차원, DZC_Global은 2차원, TAUBSED/TAUBSND/TAUB/WNDVELE/WNDVELN/PATMT_Global은 1차원 real target allocatable이다(32–43). Integer(IK4) JMN/JMX/IMN/IMX_Global은 전역 격자(grid) I/J 최소·최대라는 주석이다(45–46). LBCS_Global 정수 1차원 target allocatable(48). Values_Temp_Binary는 real(RK4) 4차원 allocatable(50). 길이 9 MPI_Outdir, LWVCELL_Global 정수 1차원, LWVMASK_Global 논리 1차원 선언(52–55). |
| 57–79 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. TBY/TBX/TSY/TSX_Global과 TBY1/TBX1/TSY1/TSX1_Global은 1차원 기본 Real target allocatable이다(57–65). LWC/LEC/LSC/LNC_Global은 1차원 정수 target allocatable(67–70). 수리(hydrodynamics)·기타 모듈 구역 주석(72). KSZ_Global은 1차원 정수 allocatable(73). ISCDRY/NATDRY/IDRY/MVEG_Global은 1차원 정수 target allocatable(75–78). 빈 줄 포함. |
| 80–114 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. BELV/DXP/DYP/HP/H1P/H2P/HWQ/H2WQ/ZBR_Global의 1차원 기본 Real target allocatable 선언(80–88). SHEAR_Global/Global2/Local/Local2 선언(90–93). EVAPSW/EVAPGW/QGW/AGWELV_Global(95–98), EVAPT/RAINT_Global(100–101), RSSBCE/RSSBCW/RSSBCN/RSSBCS_Global(103–106), UHDYE/UHDY1E/VHDXE/VHDX1E/SUB/SVB_Global(108–113)도 같은 자료형·차원·속성이다. 빈 줄 포함. |
| 115–141 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. U/V/U1/V1/W_Global(115–119), QQ/QQ1/QQL/QQL1/DML_Global(121–125), TKE3D/EPS3D/GL3D_Global(127–129)은 2차원 기본 Real target allocatable이다. QSUME_Global은 1차원, QSUM_Global은 2차원(131–132). VHDX2/UHDY2_Global은 2차원(134–135). TEMB/SHAD/ICETHICK/ICETEMP_Global은 1차원(137–140). 각 배열은 같은 Real/Target/Allocatable 속성을 사용하고 빈 줄을 포함한다. |
| 142–177 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. SAL/TEM/SFL_Global은 2차원, DYE/TOX/SED/SND_Global은 3차원 기본 Real target allocatable(142–148). 이름에 1을 붙인 같은 배열군도 동일한 차원·속성이다(150–156). KBT_Global은 1차원 정수 target allocatable, BEDMAP_Global은 1차원 정수 allocatable(158–159). BDENBED/PORBED/HBED/VDRBED_Global은 2차원 Real target allocatable(160–164), SEDB/SNDB/TOXB_Global은 3차원(165–167). HBED1/VDRBED1·SEDB1/SNDB1/TOXB1_Global도 각각 같은 차원이다(169–173). QSBDLDX/QSBDLDY_Global은 2차원(175–176). |
| 178–204 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. SEDZLJ 구역은 LAYERACTIVE_Global 2차원 integer target allocatable(178–179), TAU/D50AVG_Global 1차원 real(rkd)(180–181), BULKDENS/TSED/TSED0_Global 2차원 real(rkd)(182–184), PERSED_Global 3차원 real(rkd)(185), ERO_SED_FLX/DEP_SED_FLX/CBL/CBLTOX_Global 2차원 real(rkd)(186–189)를 선언한다. 모두 target allocatable이다. 파랑(waves) 구역은 type(Wave) WV_Global 1차원(191–192), WV_HEIGHT/PERIOD/DIR/DISSIPA_Global 1차원 Real(193–196), FXWAVE/FYWAVE_Global 2차원, QQWV3_Global 1차원, WVHUU/WVHVV/WVHUV_Global 2차원 Real을 선언한다(198–203). 이 파랑 배열들도 target allocatable이다. |
| 205–241 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. 뿌리 식물·부착생물(Rooted Plant and Epiphyte, RPEM) 구역은 WQRPS/WQRPR/WQRPE/WQRPD_Global의 1차원 Real target allocatable 및 LMASKRPEM_Global의 1차원 logical allocatable이다(205–210). 퇴적물 속성작용(sediment diagenesis) 구역은 SMPOP/SMPON/SMPOC/SMDFN/SMDFP/SMDFC_Global 2차원(212–218). SM1/2NH4·SM1/2NO3·SM1/2PO4·SM1/2H2S·SM1/2SI_Global, SMPSI/SMBST/SMT/SMCSOD/SMNSOD_Global, WQBFNH4/WQBFNO3/WQBFO2/WQBFCOD/WQBFPO4D/WQBFSAD_Global은 1차원이다(220–240). 퇴적물 속성작용 배열 모두 기본 Real target allocatable이며 빈 줄을 포함한다. |
| 242–267 | 시작 시 24행 Variables_MPI_Write_Out 선언부 안. 수체(water column) WQV_Global은 3차원 Real target allocatable(242–243). 경계 조건(boundary conditions) 구역의 NLOS/NLOE/NLOW/NLON_Global은 3차원 integer, CLOS/CLOE/CLOW/CLON_Global은 3차원 Real이며 모두 target allocatable이다(245–254). 전역 IC 필드 판독용 임시 배열(temporary arrays) I1D/I2D/I3D_Global은 정수, R1D/R2D/R3D_Global은 real(RKD), 각각 1·2·3차원 allocatable이다(256–262). 추진기 후류(propwash) SDF_Global 3차원 REAL target allocatable 선언은 주석이다(264–265). 모듈 종료·빈 줄(263·266–267). 이 파일은 선언만 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 73·75–78·158–159: KSZ_Global과 BEDMAP_Global은 allocatable 정수 배열이지만 Target 속성이 없다. 인접한 ISCDRY/NATDRY/IDRY/MVEG_Global과 KBT_Global에는 Target이 있다.
- 178–189·193–203: SEDZLJ의 실수 배열은 real(rkd)로 선언한다. 파랑 수치 배열은 기본 Real로 선언한다.
- 264–265: Propwash 구역의 유일한 SDF_Global 선언은 주석 처리되어 있다. 주석은 g/m³ 단위와 NSEDFLUME>0 용도를 적는다.

