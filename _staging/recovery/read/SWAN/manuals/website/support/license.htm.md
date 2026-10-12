---
file: models/SWAN/raw/manuals/website/support/license.htm
lines: 70
sha256: 47cfb1ab22d7b7cded2a7b162793c44ed30128216558d1735f91b07966d0eb46
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# license.htm — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | SWAN License / 문서 머리말 — HTML 제목과 표 기반 페이지 배치, 라이선스 제목을 포함한다(1–26). SWAN·SourceForge 로고를 참조한다(12–14). 두 로컬 사본은 그림 파일 없음이며 그림을 열지 못했다. |
| 27–44 | 적용 라이선스와 저작권 표기 — SWAN은 모든 사용자와 개발자에게 GNU General Public License 조건 아래 자유롭게 제공된다고 적는다(27–30). 소스의 서브루틴(subroutine)·함수(function)·모듈(module) 첫 페이지에 이어지는 문구가 붙는다고 설명한다(31–35). SWAN의 풀어쓴 이름과 3세대 파랑 모델(third-generation wave model) 문구를 제시한다(38–40). 저작권 주체는 Delft University of Technology이며 연도 표기는 1993–2024이다(41–43). 원문 41행의 저작권 기호는 판독 도구 출력에서 대체 문자로 보였다. 원문: `        <td colSpan="2">The SWAN program` (27); `          is freely available to all users and` (28); `          developers under the terms of the` (29); `          GNU General Public License. On` (30); `          the first page of all parts of` (31); `          the source code, i.e.` (32); `          subroutines, functions and` (33); `          modules, the following text is` (34); `          attached:<br>` (35); `            SWAN (Simulating WAves` (38); `            Nearshore); a third` (39); `            generation wave model<br>` (40); `            1993-2024 Delft University of` (42); `            Technology<br>` (43). [10-13 전수 검증 보완] |
| 45–54 | 재배포·수정 조건과 보증 부재 — Free Software Foundation이 발행한 GPL 버전 3 또는 사용자가 선택한 이후 버전 조건으로 재배포·수정할 수 있다고 적는다(45–48). 유용하기를 기대하지만 어떤 보증도 없으며 상품성(merchantability) 또는 특정 목적 적합성의 묵시적 보증도 없다고 명시한다(50–53). 허용·버전 선택·보증 부재를 원문 그대로 옮긴다. 원문: `            This program is free software: you can redistribute it and/or modify` (45); `            it under the terms of the GNU General Public License as published by` (46); `            the Free Software Foundation, either version 3 of the License, or` (47); `            (at your option) any later version.<br>` (48); `            <br>` (49); `            This program is distributed in the hope that it will be useful,` (50); `            but WITHOUT ANY WARRANTY; without even the implied warranty of` (51); `            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the` (52); `            GNU General Public License for more details.<br>` (53). |
| 55–70 | 라이선스 사본·연락처 / 문서 종료 — 프로그램과 함께 GPL 사본을 받았어야 하며 그렇지 않으면 GNU 라이선스 페이지를 보라고 적는다(55–58). GPL 그림을 참조하지만 로컬 사본은 그림 파일 없음이다(57). 그림을 열지 못했다. 추가 정보 연락처를 제시한다(60). 목록·표·본문·HTML 종료와 빈 줄을 포함한다(61–70). 원문: `            You should have received a copy of the GNU General Public License` (55); `            along with this program.  If not, see` (56); `            <img src="https://swanmodel.sourceforge.io/support/gplv3-77x31.png" alt="" style="float: right;" /><br>` (57); `            <a href="http://www.gnu.org/licenses/" target="_blank">http://www.gnu.org/licenses/</a>.<br>` (58); `            For more information contact m.zijlema@tudelft.nl` (60). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 12–15행: 두 `<td>`는 각각 12행과 14행에서 닫힌다. 그 뒤 15행에 추가 `</td>`가 있다.
- 41행: `<font size="2">` 안의 저작권 기호는 원본 바이트 `0xA9`이다. `nl -ba` 판독 도구의 UTF-8 출력에서는 `�`로 표시되었다.
- 12행: `https://swanmodel.sourceforge.io/platen/swanlogo.jpg` 참조는 그림 파일 없음. 로컬 대응 경로 `models/SWAN/raw/manuals/website/platen/swanlogo.jpg`에 파일이 없다. 그림 내용은 열어 확인하지 못했다.
- 13행: `http://sflogo.sourceforge.net/sflogo.php?group_id=384349&amp;type=13` 참조는 그림 파일 없음. 문서 사본 폴더에서 이 외부 그림의 로컬 사본을 찾지 못했다. 그림 내용은 열어 확인하지 못했다.
- 57행: `https://swanmodel.sourceforge.io/support/gplv3-77x31.png` 참조는 그림 파일 없음. 로컬 대응 경로 `models/SWAN/raw/manuals/website/support/gplv3-77x31.png`에 파일이 없다. 그림 내용은 열어 확인하지 못했다.
