---
file: models/SWAN/raw/source_code/swan/src/SwanVTKPDataSets.ftn90
lines: 308
sha256: b6b1a777129e369e0b7f9cb7c8ef6ab739f8c88f880360d8cb778593fb6cc323
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanVTKPDataSets.ftn90 — 판독 구간 기록

구간은 1행부터 308행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–45 | SwanVTKPDataSets 시작(1). 기관·GPL 3 이상·무보증 머리말(3–27), 저자·2022년 이력(30–36). 병렬 VTK(parallel VTK) 파일 작성 목적(38–40). VTK 형식 문서 URL은 원문의 방법 주석이다(44). |
| 46–100 | 시작 시 1행 SwanVTKPDataSets 루틴 안. ocpcomm2·ocpcomm4·swcomm1·swcomm3·m_parall·outp_data 사용(48–53), implicit none(55). 입력 mxk/myk·nvar·PVD 및 병렬 VTK 장치번호 upvd/upvt, iarr(4,0:NPROC-1)·ivtyp(nvar)·psname(8)·pstype(1)·vtkfile 선언(59–70). `integer, save     :: ient = 0          ! number of entries in this subroutine` (74), 인덱스, `logical, save     :: nowarn  = .false. ! give no warning again (only nonstationary mode)` (84), 문자 버퍼 extstr(200)·intstr/intstr2(12)·msgstr(120)·namvar(6)·pnum(4) 선언(75–93). 구조·소스 주석·빈 줄. [10-13 전수 검증 보완] |
| 101–134 | 시작 시 1행 루틴 안. `if (ltrace) call strace (ient,'SwanVTKPDataSets')` (101), xmllin1/2/3 및 SWAN 버전·프로젝트·실행 번호 출력(103–107). `if ( pstype == 'F' .or. pstype == 'H' ) then` (111)이면 PStructuredGrid, version=0.1, LittleEndian 출력(113–114). mxk-1·myk-1 문자열 변환(116·118), TXPBLA 호출(117·119), `extstr = "0 "//intstr(if:il)//" 0 "//intstr2(if2:il2)//" 0 0"` (120)로 전체 범위(extent) 생성·WholeExtent와 GhostLevel=0 출력(122–123). `elseif ( pstype == 'U' ) then` (125)이면 PUnstructuredGrid·같은 버전/바이트 순서·GhostLevel=0 출력(127–131). 격자 끝 인덱스 변환 원문은 `write(intstr(1:12),'(i12)') mxk-1` (116), `write(intstr2(1:12),'(i12)') myk-1` (118)이다. 111–133행 IF 사슬에는 ELSE가 없다. F/H/U 이외 값에서는 이 사슬의 파일 종류 태그를 출력하지 않는다. [10-13 전수 검증 보완] |
| 135–184 | 시작 시 1행 루틴 안. PPointData 시작(137–138), jvar=1..nvar 루프(142)에서 `ivtype = ivtyp(jvar)` (144)로 변수 종류 복사. `if ( ovsvty(ivtype) < 3 ) then        ! scalars` (146)이면 ovsnam의 짧은 이름으로 Float32 스칼라(scalar) PDataArray 출력(148–151). `else                                  ! vectors (three components per node!)` (153)는 Float32·NumberOfComponents=3 벡터(vector) PDataArray(155–158). PPointData 종료(164–165), 비어 있는 PCellData(169–170), PPoints 시작·`vtkline = '      <DataArray type="Float32" NumberOfComponents="3"/>'` (177) 출력·PPoints 종료(174–181). 변수 이름은 두 분기 모두 `namvar = ovsnam(ivtype)` (148·155)로 얻는다. [10-13 전수 검증 보완] |
| 185–210 | 시작 시 1행 루틴 안. `lc = .false.` (185), `ilpos = index( vtkfile, '.VT' )` (186), `if ( ilpos == 0 ) lc = .true.` (187)로 확장자 대소문자 플래그 설정. `ilpos = index( vtkfile, '_001' )` (189)로 _001 위치 탐색·`pfile = vtkfile` (190)로 파일명 복사. `if ( pstype == 'F' .or. pstype == 'H' ) then` (192)이면 구조 격자 분할 일관성 검사. `if ( maxval(iarr(3,:)) == 1 .and. (minval(iarr(4,:)) == myk .or. minval(iarr(4,:)) == 0) ) then` (196)의 iproc=1..NPROC-1 루프(198)에서 `if ( iarr(1,iproc-1) <= iarr(2,iproc-1) .and. iarr(1,iproc) <= iarr(2,iproc) ) then` (200)일 때 `if ( iarr(1,iproc) /= iarr(2,iproc-1)-1 ) then` (201)이면 msgerr(2)로 끝·시작 인덱스 불일치 보고(202–203), psname을 msgerr(0)로 보고(204–205). 202행 메시지는 끝 부분영역 번호 `iproc`와 시작 부분영역 번호 `iproc+1`을 출력한다. 인덱스 검사는 `iarr(1,iproc)`와 `iarr(2,iproc-1)-1`을 비교한다(201). 196행 검사 사슬은 231행에서 닫힌다. 192행 F/H 사슬은 298행에서 닫힌다. [10-13 전수 검증 보완] |
| 211–232 | 시작 시 1행 루틴·192행 F/H 분기 안이며 196행 검사와 병렬. `elseif ( maxval(iarr(1,:)) == 1 .and. (minval(iarr(2,:)) == mxk .or. minval(iarr(2,:)) == 0) ) then` (211)의 iproc 루프(213)에서 `if ( iarr(3,iproc-1) <= iarr(4,iproc-1) .and. iarr(3,iproc) <= iarr(4,iproc) ) then` (215)일 때 `if ( iarr(3,iproc) /= iarr(4,iproc-1)-1 ) then` (216)이면 msgerr(2)·격자 이름 msgerr(0)(217–220). `else` (226)에서는 격자 분할 오류 msgerr(3)(228–229). 검사 분기 종료(231). 217행 메시지는 끝 부분영역 번호 `iproc`와 시작 부분영역 번호 `iproc+1`의 불일치를 보고한다. 219행 메시지는 출력 격자 이름 psname을 보고한다. 이 구간에는 RETURN이 없다. [10-13 전수 검증 보완] |
| 233–253 | 시작 시 1행 루틴·192행 F/H 분기 안. iproc=1..NPROC 루프(235). iarr(1:4,iproc-1)의 각 인덱스에서 1을 뺀 값을 문자열로 변환(237·239·242·244)하고 TXPBLA 호출(238·240·243·245). 범위 문자열은 `extstr = intstr(if:il)//" "//intstr2(if2:il2)` (241), `extstr = extstr(1:len_trim(extstr))//" "//intstr(if:il)//" "//intstr2(if2:il2)//" 0 0"` (246). `if ( (iarr(1,iproc-1) > iarr(2,iproc-1) .or. iarr(3,iproc-1) > iarr(4,iproc-1)) .and. .not.nowarn ) then` (248)이면 빈 부분영역(subdomain) 경고 msgerr(1)(249–250). `if ( NSTATC /= 0 ) nowarn = .true.` (251)로 비정상(nonstationary) 모드에서는 이후 경고를 억제한다. 부분영역 인덱스 변환 원문은 `write(intstr(1:12),'(i12)') iarr(1,iproc-1)-1` (237), `write(intstr2(1:12),'(i12)') iarr(2,iproc-1)-1` (239), `write(intstr(1:12),'(i12)') iarr(3,iproc-1)-1` (242), `write(intstr2(1:12),'(i12)') iarr(4,iproc-1)-1` (244)이다. |
| 254–273 | 시작 시 1행 루틴·192행 F/H 분기·235행 iproc 루프 안. `if ( upvd > 0 ) then` (254)의 `if ( lc ) then` (255)이면 p와 프로세서 번호 출력(256), `else` (257)이면 P와 번호 출력(258). `else` (260)는 '.   ' 문자열(261). `write(pfile(ilpos+1:ilpos+3),15) iproc` (264)로 파일명의 번호 부분을 덮어쓴다. 경로와 범위를 포함한 Piece 행은 `vtkline = '    <Piece Extent="'//extstr(1:len_trim(extstr))//'" Source="'//pnum(1:len_trim(pnum))//DIRCH2//pfile(1:len_trim(pfile))//'"/>'` (266)이며 upvt에 출력(267). 루프 종료(269)·PStructuredGrid 닫기(271–272). 접두사 생성 원문은 `write(pnum(1:4),10) 'p',iproc` (256), `write(pnum(1:4),10) 'P',iproc` (258), `write(pnum(1:4),12) '.   '` (261)이다. [10-13 전수 검증 보완] |
| 274–308 | 시작 시 1행 루틴에서 192행 조건의 병렬 `else` (274). iproc 루프(276)의 `if ( upvd > 0 ) then` (278)와 `if ( lc ) then` (279)이면 p 접두사(280), `else` (281)이면 P 접두사(282), `else` (284)이면 '.' 접두사(285). `write(pfile(ilpos+1:ilpos+3),15) iproc` (288)로 pfile 번호 덮어쓰기, `vtkline = '    <Piece Source="'//pnum(1:len_trim(pnum))//DIRCH2//pfile(1:len_trim(pfile))//'"/>'` (290)로 범위 없는 Piece 경로 출력(291). 루프 종료·PUnstructuredGrid 닫기(293–296), 조건 종료(298). 포맷은 `10 format(a1,i3.3)` (299); `12 format(a4)` (300); `15 format(i3.3)` (301)로 프로세서 번호를 3자리로 고정한다. VTKFile 종료 태그 출력·루틴 종료(305–308). 접두사 생성 원문은 `write(pnum(1:4),10) 'p',iproc` (280), `write(pnum(1:4),10) 'P',iproc` (282), `write(pnum(1:4),12) '.   '` (285)이다. [10-13 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 185–190·264·288: index(vtkfile,'_001')의 반환값을 ilpos로 사용한다. ilpos=0인지 확인하는 조건 없이 ilpos+1..ilpos+3을 프로세서 번호로 덮어쓴다.
- 93·256–258·264·280–282·288·299–301: 프로세서 접두사 버퍼 pnum은 길이 4이다. 프로세서 번호 출력은 i3.3으로 고정되어 있다.
- 111–133·192·274–298: 머리말은 pstype=F/H와 =U에서만 파일 종류를 연다. Piece 출력의 else는 F/H를 제외한 모든 값을 PUnstructuredGrid 경로로 처리한다. 다른 pstype에 대한 오류 분기는 없다.
- 150·157·174–180: 변수 선언에는 PDataArray 태그를 사용한다. PPoints 내부의 좌표 선언에는 DataArray 태그를 사용한다.
- 84·248–251: nowarn은 SAVE이며 FALSE로 초기화된다. NSTATC/=0에서 첫 빈 부분영역 경고 뒤 TRUE로 바꾼다. 이 루틴에는 프레임별 또는 파일별 nowarn 재설정문이 없다.
- 196–229·201·216: 구조 격자 인접 부분영역 검사는 현재 시작 인덱스를 이전 끝 인덱스-1과 비교한다. 두 방향의 불일치는 msgerr(2)를 호출한다. 이 검사 블록에는 반환문이 없다.
- 103–306: upvt 파일 출력은 iostat를 받지 않는다. 이 루틴에는 파일 출력 상태에 대한 조건 검사가 없다.
