---
file: models/SWAN/raw/manuals/website/items.htm
lines: 81
sha256: 78608ada5f29abffc46b939200f0e73c1afae3ed372e18629c51668877dba5dd
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# items.htm — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 탐색 메뉴의 기본 대상 — HTML 제목과 `<base target="home">`를 제시한다(3–4). 본문 여백과 메뉴 표 배치, home 연결을 포함한다(6–10). 원문: `<base target="home">` (4); `<BODY topmargin="50" leftmargin="10">` (6); `<table border="0" cellpadding="3" cellspacing="0" width="200" height="360">` (7); `    <td><br><br><br><a href="home.htm">home</a></td>` (10). |
| 12–27 | 모델 기능·설정·배포 메뉴 — features, settings, release notes, downloads의 상대경로 링크를 순서대로 제시한다(14·18·22·26). 행·셀 마크업도 포함한다. 원문: `    <td><a href="features/features.htm">features</a></td>` (14); `    <td><a href="settings/settings.htm">settings</a></td>` (18); `    <td><a href="modifications/modifications.htm">release notes</a> </td>` (22); `    <td><a href="download/download.htm">downloads</a> </td>` (26). |
| 28–43 | 외부 저장소·컨테이너·문서·패치 메뉴 — GitLab repository, Docker container, 모델 documentation을 새 창으로 연결한다(30·34·38). patches는 상대경로로 연결한다(42). 원문: `    <td><a href="https://gitlab.tudelft.nl/citg/wavemodels/swan" target="_blank">repository</a></td>` (30); `    <td><a href="https://hub.docker.com/r/delftwaves/swan" target="_blank">container</a></td>` (34); `    <td><a href="https://delftwaves.github.io/swan-docs/" target="_blank">documentation</a></td>` (38); `    <td><a href="problems_and_fixes/problems_and_fixes.htm">patches</a></td>` (42). |
| 44–60 | 지원·연구·출판·메일링 리스트 메뉴 — support, research, publications의 상대경로 링크를 제시한다(46·50·54). mailing list는 `target="new"`로 연결한다(58). 메뉴 표를 닫는다(60). 원문: `    <td><a href="support/support.htm">support</a></td>` (46); `    <td><a href="research_and_development/research_and_development.htm">research</a></td>` (50); `    <td><a href="references/references.htm">publications</a></td>` (54); `    <td><a href="http://sourceforge.net/mail/?group_id=384349" target="new">mailing list</a></td>` (58). |
| 61–81 | 다운로드 버튼·SourceForge 배지·책 그림 참조 / 문서 종료 — 다운로드 그림 버튼의 src·srcset과 최신 배포 링크를 제시한다(63). SourceForge community choice 배지용 div와 비동기 스크립트(asynchronous script)를 제시한다(68–72). 책 안내 페이지에 CUP.jpg 그림 참조를 연결한다(78). 기본 그림 URL 두 개와 다운로드 버튼의 srcset 대체 URL의 로컬 사본은 모두 그림 파일 없음이다. 그림을 열지 못했다. pre·행·셀·본문 종료 마크업과 빈 줄도 포함한다(61–81). 원문: `    <td><br><br><a href="https://sourceforge.net/projects/swanmodel/files/latest/download" target="new"><img alt="Download SWAN" src="https://a.fsdn.com/con/app/sf-download-button" width=138 height=24 srcset="https://a.fsdn.com/con/app/sf-download-button?button_size=2x 2x"></a>` (63); `  <div class="sf-root" data-id="384349" data-badge="oss-community-choice-black" data-metadata="achievement=oss-community-choice" style="width:80px">` (68); `      <a href="https://sourceforge.net/projects/swanmodel/" target="_blank">SWAN</a>` (69); `  <script>(function () {var sc=document.createElement('script');sc.type='text/javascript';sc.async=true;sc.src='https://b.sf-syn.com/badge_js?sf_id=384349';var p=document.getElementsByTagName('script')[0];p.parentNode.insertBefore(sc, p);})();` (71); `  </script>` (72); `    <td><a href="research_and_development/book.htm"><img border="0" src="https://swanmodel.sourceforge.io/research_and_development/platen/CUP.jpg" width="75" height="110"></a></td>` (78). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 63행: 다운로드 버튼의 srcset 대체 URL `https://a.fsdn.com/con/app/sf-download-button?button_size=2x`도 그림 파일 없음이다. 로컬 사본을 찾지 못해 그림을 열지 못했다.
- 60–64·76–79행: 메뉴 표를 60행의 `</table>`로 닫은 뒤 두 `<tr>` 블록이 나온다. 이 두 블록을 감싸는 새 `<table>` 시작 태그는 이 파일에 없다.
- 63행: `https://a.fsdn.com/con/app/sf-download-button` 참조는 그림 파일 없음. 문서 사본 폴더에서 이 외부 그림의 로컬 사본을 찾지 못했다. 그림 내용은 열어 확인하지 못했다.
- 78행: `https://swanmodel.sourceforge.io/research_and_development/platen/CUP.jpg` 참조는 그림 파일 없음. 로컬 대응 경로 `models/SWAN/raw/manuals/website/research_and_development/platen/CUP.jpg`에 파일이 없다. 그림 내용은 열어 확인하지 못했다.
