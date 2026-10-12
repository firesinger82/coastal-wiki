SWAN 판독 기록 전수 검증. 검증일은 2026-10-13이다.

원문은 `models/SWAN/raw/manuals/pdfs/swanuse.pdf`이다.
대조 기준은 `/tmp/claude-1000/-home-firesinger-coastal-wiki/338e5a20-3378-4629-86f1-592f9d629b53/scratchpad/swpages/swanuse-127.png`부터 `swanuse-144.png`까지의 300dpi 쪽 이미지이다.
모든 대상 쪽 이미지를 직접 열어 보았다.
`_staging/recovery/extract/SWAN/pdf/swanuse.txt`는 보조로 사용했다.

| 기록 | 대조 구간 | 대상 행 수 | 대조한 행 수 |
|---|---|---:|---:|
| [p127-144.md](../manuals/pdfs/swanuse.pdf/p127-144.md) | p.127–144 | 18 | 18 |

행 수는 대상 기록의 쪽별 표 행을 세었다.
정정 수는 `[10-13 전수 검증 정정]` 표지가 있는 쪽 행 수이다.
보완 수는 `[10-13 전수 검증 보완]` 표지가 있는 쪽 행 수이다.
p.131·132·133·140·141의 5개 행은 정정과 보완에 각각 포함했다.
이상 없음은 수정하지 않은 p.135·144의 2개 행이다.

아래 표의 `p127-144.md`는 위 대상 기록을 뜻한다.
원문 행은 PDF 쪽 번호와 쪽 안의 위치로 식별했다.
인용은 해당 원문 행의 발췌이다.
명령 도식 인용의 연속 공백은 한 칸으로 표시했다.

| 기록:구간 | 이전 요지 | 새 요지 | 원문 행 |
|---|---|---|---|
| p127-144.md:p.127 (정정) | 인쇄되지 않은 Appendix A 라벨을 머리말에 붙였다. | 쪽에 보이는 머리말 “Definitions of variables”만 기록했다. | p.127(인쇄 119), 머리말: “Definitions of variables”. |
| p127-144.md:p.128 (정정) | 쪽에 인쇄되지 않은 FORCE 라벨을 첫 수식에 붙였다. | 쪽 첫 텐서 수식으로 기록했다. 수식은 원문과 일치하므로 유지했다. | p.128(인쇄 120), 첫 표시 수식: $S_{yy}=\rho g\int(n\sin^2\theta+n-\frac{1}{2})Ed\sigma d\theta$. 이 쪽에는 FORCE 라벨이 없다. |
| p127-144.md:p.129 (보완) | 첫 키워드가 명령 이름이라는 설명과 Section 4.1 참조를 생략했다. 추가 키워드의 역할을 생략했다. | 첫 키워드는 명령 이름임을 보완했다. 명령 목록의 Section 4.1 참조를 보완했다. 추가 키워드는 지시를 구체화함을 보완했다. | p.129(인쇄 121), B.2.1: “which is also the name of the command”; “see list in Section 4.1”; “which refines the instructions to SWAN”. |
| p127-144.md:p.130 (정정) | 쪽에 인쇄되지 않은 B.2.1 절 번호를 제목에 붙였다. | 쪽에 보이는 Spelling of keywords와 Required and optional keywords만 남겼다. | p.130(인쇄 122), 제목: “Spelling of keywords”; “Required and optional keywords”. |
| p127-144.md:p.131 (정정·보완) | 쪽에 없는 B.2.1 절 번호를 붙였다. 반복 사용의 위치 나열 예를 생략했다. 문자열이 항상 이름이라는 한정을 생략했다. | 인쇄되지 않은 B.2.1을 삭제했다. x,y 공간의 위치 나열 예를 보완했다. 도식의 문자열은 항상 이름임을 보완했다. | p.131(인쇄 123), 제목: “Repetitions of keywords and/or other data”; 첫 단락: “containing many locations in x,y-space”; 마지막 단락: “the character string is always a name”. |
| p127-144.md:p.132 (정정·보완) | 쪽에 없는 B.2.2와 Spelling of data를 제목으로 썼다. 키워드의 모든 특성이라는 한정과 일부 입력 표기를 생략했다. | 실제 머리말 Appendix B로 고쳤다. 플롯 텍스트 예를 보완했다. 복사한 변수 이름의 모든 키워드 특성을 보완했다. 수치의 항상 이름 표기와 두 번째 입력 방식의 따옴표·대괄호 규칙을 보완했다. | p.132(인쇄 124), 머리말: “Appendix B”; 첫 항목: “for text to appear in a plot”; 두 번째 항목과 마지막 항목: “with all the characteristics of a keyword”; 중간 단락: “the number is always indicated with a name”; 마지막 항목: “without the quotes”, “not between square brackets”. |
| p127-144.md:p.133 (정정·보완) | 쪽에 없는 B.2.2 절 번호를 붙였다. 필수 데이터의 표시 위치와 일부 선택 데이터라는 한정을 생략했다. 주석의 활용 가능성을 생략했다. | 인쇄되지 않은 B.2.2를 삭제했다. 필수 데이터는 개별 명령 설명에 표시함을 보완했다. 분기 도식은 일부 선택 데이터에 사용함을 보완했다. 주석이 명령 의미를 분명하게 하는 데 중요할 수 있음을 보완했다. | p.133(인쇄 125), 제목: “Required data and optional data”; 필수 데이터 단락: “indicated in the description of each individual command”; (c): “some optional data”; B.3: “Such comments may be important to the user e.g., to clarify the meaning of the commands used”. |
| p127-144.md:p.134 (정정) | 쪽에 없는 B.3 제목을 붙였다. 문장 중간에서 시작하는 원문에 앞 쪽의 ‘두 번째 $ 뒤’라는 대상을 붙였다. | 실제 머리말 Appendix B로 고쳤다. 첫 문장 조각에 보이는 ‘주석이 아니라 다시 처리할 데이터’라는 설명만 남겼다. | p.134(인쇄 126), 머리말: “Appendix B”; 첫 행: “as comment, but again as data to be processed (possibly interrupted again by $ or two $ signs)”. |
| p127-144.md:p.136 (정정) | 쪽에 없는 File swan.edt와 INPgrid 라벨을 붙였다. 쪽에 없는 DSPR의 뜻을 설명했다. | 실제 머리말 Appendix C를 기록했다. 첫 나열의 명령 이름을 추정하지 않았다. DSPR의 뜻풀이를 삭제했다. | p.136(인쇄 128), 머리말: “Appendix C”; 첫 명령 도식 행: “! AICE \| HICE \| HSS \| TSS \| DSS &”; SHAPespec 행: “PEAK\|MEAN DSPR POWer\|DEGRees”. |
| p127-144.md:p.137 (정정) | 쪽에 없는 Appendix C 라벨을 붙였다. 쪽에 없는 nested boundary 뜻풀이를 붙였다. | 실제 머리말 File swan.edt를 기록했다. 첫 명령의 인쇄 도식만 남겼다. | p.137(인쇄 129), 머리말: “File swan.edt”; 첫 명령 행: “! BOUndnest1 NEst ’fname’ CLOSed\|OPEN”. |
| p127-144.md:p.138 (정정) | 쪽에 없는 File swan.edt와 GEN3 라벨을 붙였다. U10Proxy와 DEBias의 분기 위치를 구분하지 않았다. | 실제 머리말 Appendix C를 기록했다. U10Proxy의 기본 화살표를 기록했다. DEBias가 닫는 꺾쇠 뒤에 있음을 기록했다. | p.138(인쇄 130), 머리말: “Appendix C”; 첫 도식의 첫 행: `< > DEBias [cdfac]`; 다음 행: `-> U10Proxy [windscaling]`. |
| p127-144.md:p.139 (정정) | 쪽에 없는 Appendix C와 BRE 라벨을 붙였다. | 실제 머리말 File swan.edt를 기록했다. 첫 FREQDep 구절에 다른 쪽의 명령 이름을 붙이지 않았다. | p.139(인쇄 131), 머리말: “File swan.edt”; 첫 도식 행: “! ( FREQDep [power] [fmin] [fmax] )”. |
| p127-144.md:p.140 (정정·보완) | 쪽에 없는 File swan.edt·SCAT·GRId 라벨을 붙였다. 첫 OBSTacle의 REFLec 선택 구절 전체를 묶는 괄호를 생략했다. | 실제 머리말 Appendix C를 기록했다. 첫 Kxy 분기에 다른 쪽의 명령 이름을 붙이지 않았다. REFLec 뒤의 RSPEC 또는 RDIFF 분기까지 소괄호 안에 있음을 보완했다. | p.140(인쇄 132), 머리말: “Appendix C”; 첫 도식 행: `Kxy [kxlow] [kylow] [kxlen] [kylen] [mkxc] [mkyc]`; OBSTacle의 REFLec 도식 중앙 행: `! ( REFLec [reflc] < > ) &`; 분기 행: `-> RSPEC`, `RDIFF [pown]`. |
| p127-144.md:p.141 (정정·보완) | 쪽에 없는 Appendix C·NGRID 라벨을 붙였다. SIGIMpl·SIGEXpl을 쪽에 없는 ‘주파수 선택’으로 설명했다. NUMeric 첫 소괄호의 적용 범위를 생략했다. | 실제 머리말 File swan.edt를 기록했다. 쪽에 없는 라벨과 뜻풀이를 삭제했다. 첫 소괄호가 STOPC·ACCUR 분기부터 [limiter]까지 함께 묶음을 보완했다. | p.141(인쇄 133), 머리말: “File swan.edt”; NUMeric 행: `! NUMeric (< > &`; 다음 분기 중앙 행: `! < > [limiter] ) &`; 맨 아래 도식 행: `! \| [xpn] [ypn] [alpn] [xlenn] [ylenn] [mxn] [myn]`. |
| p127-144.md:p.142 (정정) | 쪽에 없는 File swan.edt 제목을 붙였다. | 실제 머리말 Appendix C만 기록했다. | p.142(인쇄 134), 머리말: “Appendix C”. |
| p127-144.md:p.143 (정정) | 쪽에 없는 Appendix C 라벨을 붙였다. | 실제 머리말 File swan.edt만 기록했다. | p.143(인쇄 135), 머리말: “File swan.edt”. |

쪽 행의 순서와 표 열 구성은 원래 기록과 동일하다.
Frontmatter와 쪽 행 밖의 내용은 수정하지 않았다.
원문·노트·git은 수정하지 않았다.
모델은 실행하지 않았다.

정정 15, 보완 6, 이상 없음 2
