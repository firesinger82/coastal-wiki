---
file: models/ROMS/raw/manuals/wiki/wikitext/Source_Code.wiki
lines: 14
sha256: 4f2cd57eb82f4a4ba90e61321c8b07bf32347011363d66b91216be5fd42ca12b
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# Source_Code.wiki — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | Regional Ocean Modeling System (ROMS) / 배포·지원 — 공식 커뮤니티 버전은 Rutgers에서 개발·유지한다고 적는다(1–3). Git·SVN 병행 배포에서 2025년 1월 1일부터 GitHub 단독 배포로 옮기고 SVN은 역사적 용도로 유지한다고 설명한다(3). 사용자의 해양 동역학·수치모델·컴퓨터 배경을 요구하며 등록과 포럼 지원을 권하고 GitHub에서는 사용 지원을 제공하지 않는다고 적는다(5). GitHub 위키와 공식 저장소, 문서 작성 당시 비공개인 ROMS-JEDI 인터페이스를 소개한다(7). 원문: `This official community version of '''ROMS''' is developed and maintained at Rutgers, The State University of New Jersey, New Brunswick, New Jersey, USA. Currently, '''ROMS''' source code is distributed using both [https://git-scm.com Git] and [https://subversion.apache.org Subversion]('''SVN'''). However, starting <span class="red">January 1, 2025</span>, '''ROMS''' will be exclusively distributed from its '''GitHub''' repository at [https://github.com/myroms https://github.com/myroms]. Updating the '''SVN''' repositories at [https://www.myroms.org https://www.myroms.org] will be discontinued but kept for historical reasons.` (3); `The '''ROMS''' framework is intended for users interested in ocean modeling. It requires an extensive background in ocean dynamics, numerical modeling, and computers to configure, run, and analyze the results to ensure you get the correct solution for your application. Therefore, we highly recommend users register at [https://www.myroms.org https://www.myroms.org] and set up a <span class="red">username</span> and <span class="red">password</span> to access the '''ROMS''' forum, email notifications for bugs/updates, technical support from the community, trac code maintenance history, tutorials, workshops, and publications. The User's '''ROMS''' forum has over 24,000 posts with helpful information. Technical support is limited to registered users. We do not provide user technical support, usage, or answers in '''GitHub'''.` (5); `The <span class="red">ROMS GitHub</span> repository also has its own wiki at [https://github.com/myroms/roms/wiki https://github.com/myroms/roms/wiki] with useful information and instructions. This '''GitHub''' version becomes the official '''Git''' repository for downloading, updating, improving, and correcting defects/bugs in the '''ROMS''' source code. Also, it is the version used in the <span class="red">ROMS-JEDI</span> interface hosted at [https://github.com/JCSDA-internal https://github.com/JCSDA-internal], which is currently private.` (7). |
| 9–14 | 인증 안내·로고·경고 — GitHub의 2요소 인증(two-factor authentication) 안내를 적는다(9). ROMS_circle_logo.png와 ROMS-JEDI_circle_logo.png는 캡션 없이 참조한다(11). 두 그림 모두 그림 파일 없음. 마지막 경고는 2025년 1월 1일부터 SVN 갱신을 중단했다고 적는다(14). 원문: `{{note}}<span class="mediumOrchid">Note:</span> '''GitHub''' nowadays requires two-factor authentication!` (9); `<center>[[Image:ROMS_circle_logo.png]] &nbsp; [[Image:ROMS-JEDI_circle_logo.png]]</center>` (11); `==<span class="red">WARNING:</span> <span class="blue">The updating of ROMS svn repositories has been discontinued as of</span> <span class="red">January 1, 2025</span>==` (14). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 3·14행: 배포 변경 설명은 2025년 중단을 미래형 `will be discontinued`로 적지만 마지막 경고는 같은 날짜의 중단을 완료형 `has been discontinued`로 적는다.
- 11행: `ROMS_circle_logo.png`를 캡션 없이 참조한다. 그림 파일 없음.
- 11행: `ROMS-JEDI_circle_logo.png`를 캡션 없이 참조한다. 그림 파일 없음.
