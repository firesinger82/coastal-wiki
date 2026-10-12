---
file: models/SWAN/raw/manuals/website/problems_and_fixes/problems_and_fixes.htm
lines: 97
sha256: 7779e2cf34d098d3fd15c40cf60517c342fc26ca9b32eeef45e993ff9c29e589
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# problems_and_fixes.htm — 판독 구간 기록

구간은 1행부터 97행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | Known bugs and patches / 페이지 머리말 — HTML 제목·배치·SWAN 로고·SourceForge 로고와 절 제목을 포함한다(1–24). SWAN 로고의 로컬 경로 `models/SWAN/raw/manuals/website/platen/swanlogo.jpg`는 없다(12). SourceForge 로고의 로컬 사본도 없다(13–14). 두 참조 모두 그림 파일 없음이다. 원문: `    <td><img border="0" src="https://swanmodel.sourceforge.io/platen/swanlogo.jpg" width="400" height="70"></td>` (12); `    <td><a href="http://sourceforge.net/projects/swanmodel"><img src="http://sflogo.sourceforge.net/sflogo.php?group_id=384349&amp;type=13"` (13); `        border="0" width="120" height="30" alt="Get SWAN at SourceForge.net. Fast, secure and Free Open Source software downloads" /></a></td>` (14). |
| 25–32 | SWAN 41.51 패치·업데이트 안내 — 패치는 버그 또는 문제를 해결하며 새 기능도 수시로 공개할 것이라고 적는다(27–28). 향후 업데이트도 GitLab 저장소에 추가할 예정이므로 정기 확인을 요청한다(30–31). 원문: `      For SWAN 41.51, patches are available here. These fix` (27); `      bugs and/or resolve issues. Also, new features will be released from time to time.` (28). |
| 33–43 | 패치 적용 절차 — 내려받은 패치 파일을 SWAN 소스 폴더에 두고 적용 명령을 실행해야 한다(33–38). 탭을 포함할 수 있으므로 패치 파일을 바꾸지 말아야 한다(40–41). 필요한 경우 DOS에서 UNIX 형식으로 변환하며 적용 후 소스를 다시 컴파일해야 한다(41–42). 명령·조건·의무를 원문 그대로 옮긴다. 원문: `      To apply a patch, first, you must place the downloaded patch` (33); `      files (right-clicking the file, open a new window and then save it as text file)` (34); `      in the folder where the source code of SWAN is located, and then execute the` (35); `      following command:<br>` (36); `      <br>` (37); `      <tt>patch -p0 &lt; <i>patchfile</i></tt><br>` (38); `      <br>` (39); `      It is important not to change or modify the patch files since they may` (40); `      contain tabs! If needed, use <tt>dos2unix</tt> to convert DOS to UNIX format. After applying a patch, you need to recompile` (41); `      the SWAN source code.<br>` (42). |
| 44–56 | Note to Windows users — Windows용 patch와 GNU Win32 도구 링크를 안내한다(46–47). Windows 7 이상에 관한 관리자 권한 설명을 제시한다(48). 이를 피하기 위한 문서상의 절차는 patch.exe를 patsh.exe로 바꾸고 같은 디렉터리의 patch.bat에 인수 전달 명령을 넣는 것이다(50–53). 실행 파일 이름·배치 파일 내용과 조건을 원문 그대로 옮긴다. 원문: `      <li><tt>patch</tt> is a Unix command. Download the <a href="patch.zip"><tt>patch</tt> program appropriate for Windows</a>` (46); `      (it is one of the <a href="http://unxutils.sourceforge.net/" target="_top">GNU utilities for Win32</a> that are freely available).` (47); `      <li> However, Windows 7 (or higher) demands that <tt>patch</tt> must be run with administrative privileges. To hack this, do the following:` (48); `           <ol>` (49); `           <li>Rename <tt>patch.exe</tt> to <tt>pat<b><i>s</i></b>h.exe</tt>.` (50); `           <li>Then create a batch file <tt>patch.bat</tt> in the same directory containing the following command:<br>` (51); `               <br>` (52); `               <tt>@patsh.exe %*</tt>` (53); `           </ol>` (54). |
| 57–79 | 버그 보고 / patch A 표 — 새 버그 보고의 이메일 링크와 patch ID·설명·공개일·파일 열을 포함한다(57–63). A 패치는 배열 초기화와 netCDF 사용시 일부 ASCII 출력의 더미(dummy) 처리를 수정한다(65–69). INSTALL.README 링크·machinefile localhost·swanrun을 변경한다(70–75). 공개일은 13-03-2026이며 연결된 파일은 patches/41.51.A다(78–79). 원문: `               <li>some ASCII output files treated as dummies in case of netCDF` (68); `               <li>add "https://delftwaves.github.io/swan-docs/getting_started/install.html" to INSTALL.README` (72); `               <li>add "localhost" to machinefile` (73); `               <li>small modification in swanrun related to machinefile` (74); `      13-03-2026` (78); `      </TD><TD width="100" align="center"><a href="patches/41.51.A">41.51.A</a></TD></TR>` (79). |
| 80–97 | 주석 처리한 patch B 행 / 문서 종료 — B 행 전체가 HTML 주석 안에 있고 changes·bug fix 항목은 비어 있다(80–93). 주석 안 공개일은 20-03-2024이며 파일 링크는 patches/41.45.B다(92–93). 표 닫기·셀·행·BODY 닫기로 파일이 끝난다(94–97). 원문: `<!--      <TR VALIGN=top><TD width="100" align="center">&nbsp; <b>B</b></TD><TD width="600">` (80); `      20-03-2024` (92); `      </TD><TD width="100" align="center"><a href="patches/41.45.B">41.45.B</a></TD></TR> -->` (93). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12: SWAN 로고의 참조 주소는 `https://swanmodel.sourceforge.io/platen/swanlogo.jpg`다. 로컬 `models/SWAN/raw/manuals/website/platen/` 디렉터리가 없다. 그림 파일 없음.
- 13–14: SourceForge 로고는 `http://sflogo.sourceforge.net/sflogo.php?group_id=384349&amp;type=13`을 참조한다. website 폴더의 그림 파일 검색과 폴더 목록 확인에서 로컬 사본을 찾지 못했다. 그림 파일 없음.
- 12–15: 두 로고 셀은 각각 12·14행에서 닫히며 15행에 추가 `</td>`가 있다.
- 7·10·60·94–97: 표 시작 태그는 7·10·60행에 있다. 표 종료 태그는 94행의 `</TABLE>` 한 개다. 파일은 97행의 `</BODY>`에서 끝나며 나머지 두 표의 종료 태그와 `</html>`은 없다.

