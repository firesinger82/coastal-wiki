# 배포 아카이브 바이트코드 판독

2026-09-12. [추출/역어셈블리 영수증](disassembly-receipt.json), [launcher 직접 판독](launcher-read.json). 원본 클래스 바이트와 AI 판독/도구 출력은 구분한다.

기존 unread 1,284개 경로를 원본 SHA로 묶으면 Java 413종과 Python 150종, 총 563종이다. Java는 설치된 JDK jdeps 모듈의 javap로 private 선언·메서드 명령·descriptor·상수를 출력했다(87,653줄). JAR 프로그램 자체는 실행하지 않았다. 전체 추출 결과를 자동으로 읽음 처리하지 않는다. Python 150개는 아직 미판독이다.

이번에 직접 읽은 클래스는 Dialogs, RuntimeExecCommand, Launcher, Launcher$InputStreamThread 네 개다. 모든 표시된 선언·메서드 명령과 예외 테이블을 읽었으며, 실제 Java 원본이나 실행 시험으로 대신하지 않았다. SHA가 같은 12개 archive/member 경로에 근거를 재사용한다. 409종의 다른 Java 클래스는 역어셈블리만 준비된 상태다. 과거 archive-content-inventory.json은 당시 상태로 유지한다.

Launcher는 시스템 속성과 사용자 설정(.jumpshot_launcher.conf)을 읽고, JVM·옵션·viewer JAR 경로를 조립해 별도 프로세스를 실행한다. 기본 JVM 옵션은 -Xms64m -Xmx256m, 대상은 jumpshot.jar다. main에 들어온 인수는 실행 인수로 전달하지 않는다. JVM/파일의 존재·읽기 가능 여부를 확인하고, config 변경 안내와 설정 저장, 비정상 종료 대화상자를 처리한다. 이는 배포된 분석 도구의 진입점이며 XBeach 물리 계산 루틴이 아니다.

RuntimeExecCommand는 JVM 경로·JAR 경로를 하나의 인수로 추가하고 JVM 옵션은 공백 tokenizer로 나눈다. 문자열 배열 캐시는 자체 add helper에서 무효화하지만 상속된 ArrayList mutator를 모두 override하지 않는다. 출력 수집 스레드는 줄 단위로 prefix를 출력하고 선택적으로 버퍼에 쌓는다. 종료 플래그를 내리는 메서드에는 interrupt/stream close가 없고, launcher의 waitFor 뒤 reader join도 없다. 여기서는 관측한 구현만 기록하며 런타임 결함 판정을 발급하지 않는다.

검증은 1,284개 경로 집합·원본 member SHA·563개 고유 집합·413개 클래스/출력 해시와 launcher 네 클래스의 재역어셈블리 일치를 확인한다. 자체 구조 검증이며 의미 판독의 독립 승인이나 전체 gate 통과가 아니다. 전체 gate NOT_PASSED·신규 사람 승인 없음.
