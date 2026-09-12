# 배포 아카이브 바이트코드 판독

2026-09-12. [추출/역어셈블리 영수증](disassembly-receipt.json), [launcher 직접 판독](launcher-read.json). 원본 클래스 바이트와 AI 판독/도구 출력은 구분한다.

기존 unread 1,284개 경로를 원본 SHA로 묶으면 Java 413종과 Python 150종, 총 563종이다. Java는 설치된 JDK jdeps 모듈의 javap로 private 선언·메서드 명령·descriptor·상수를 출력했다(87,653줄). JAR 프로그램 자체는 실행하지 않았다. 전체 추출 결과를 자동으로 읽음 처리하지 않는다. Python 150개는 아직 미판독이다.

이번에 직접 읽은 클래스는 Dialogs, RuntimeExecCommand, Launcher, Launcher$InputStreamThread 네 개다. 모든 표시된 선언·메서드 명령과 예외 테이블을 읽었으며, 실제 Java 원본이나 실행 시험으로 대신하지 않았다. SHA가 같은 12개 archive/member 경로에 근거를 재사용한다. 이 launcher 판독 시점의 409종 다른 Java 클래스는 역어셈블리만 준비된 상태다. 과거 archive-content-inventory.json은 당시 상태로 유지한다.

Launcher는 시스템 속성과 사용자 설정(.jumpshot_launcher.conf)을 읽고, JVM·옵션·viewer JAR 경로를 조립해 별도 프로세스를 실행한다. 기본 JVM 옵션은 -Xms64m -Xmx256m, 대상은 jumpshot.jar다. main에 들어온 인수는 실행 인수로 전달하지 않는다. JVM/파일의 존재·읽기 가능 여부를 확인하고, config 변경 안내와 설정 저장, 비정상 종료 대화상자를 처리한다. 이는 배포된 분석 도구의 진입점이며 XBeach 물리 계산 루틴이 아니다.

RuntimeExecCommand는 JVM 경로·JAR 경로를 하나의 인수로 추가하고 JVM 옵션은 공백 tokenizer로 나눈다. 문자열 배열 캐시는 자체 add helper에서 무효화하지만 상속된 ArrayList mutator를 모두 override하지 않는다. 출력 수집 스레드는 줄 단위로 prefix를 출력하고 선택적으로 버퍼에 쌓는다. 종료 플래그를 내리는 메서드에는 interrupt/stream close가 없고, launcher의 waitFor 뒤 reader join도 없다. 여기서는 관측한 구현만 기록하며 런타임 결함 판정을 발급하지 않는다.

검증은 1,284개 경로 집합·원본 member SHA·563개 고유 집합·413개 클래스/출력 해시와 launcher 네 클래스의 재역어셈블리 일치를 확인한다. 자체 구조 검증이며 의미 판독의 독립 승인이나 전체 gate 통과가 아니다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## 기본 입출력 9종 추가 판독

[base/io 판독 영수증](base-io-read.json)에 465줄 전체와 원본 SHA가 같은 54경로를 결속했다. 누적 Java 13/413종·66경로 판독, Java 400종과 Python 150종은 미판독이다. 인터페이스 4종은 선언, 구현 5종은 모든 표시 명령을 읽었다.

문자열 writer는 인코딩을 지정하지 않은 getBytes 결과 길이를 short로 좁혀 기록하고 바이트 전체를 쓴다. reader는 signed short가 양수일 때만 읽는다. 비양수 길이에 대해 stream은 빈 문자열, random-access file은 null을 반환한다. 제한 읽기는 min(length, limit)만 소비하고 초과 payload를 건너뛰지 않는다. getStringByteSize는 String.length()+2로 계산한다. 각 구현의 관측이며 실제 파일 오류 발생이나 실행 환경 인코딩을 검증한 결과가 아니다.

BufArrayOutputStream은 내부 배열을 직접 반환한다. BufArrayPipedStream은 resize 시점의 배열을 입력과 공유하고, 기본 생성 후 reset에는 null guard가 없다. 용량 확장 이후 호출자 사용은 후속 연결 분석 범위다.

호출자 부분 대조: [Header 역어셈블리](disassembly/4f0bfbf7d7965f95c8cf6740727e53fa0088a2ee7455328f72d07cceff8b1b08.txt) 162–185줄은 SLOG 2.0.6의 길이 10으로 제한 읽기 후 즉시 다음 short를 읽는다. 507–525줄은 같은 문자열로 헤더 크기를 계산한다. 저장된 길이가 제한보다 크다면 초과 바이트가 다음 필드로 넘어가는 조건을 코드에서 추론할 수 있다. 이 부분 대조 시점에는 Header 전체 판독으로 집계하지 않았다. 원본 프로그램과 tmpfile 데모는 실행하지 않았다.

## SLOG2 헤더와 디렉토리 7종

[slog2-header-read.json](slog2-header-read.json)의 각 원본 SHA·역어셈블리 전체 행 범위·관측에 근거한다. Header, FileBlockPtr, Const, CategoryMap, LineIDMapList, TreeDirValue, TreeDir의 전체 표시 내용을 읽었다. 누적 Java 20/413종이며 393종과 Python 150종은 남아 있다.

Header는 버전, 자식 수(short), leaf 크기(int), 최대 깊이(short), 버퍼 크기(int), 일곱 블록 포인터를 순서대로 쓴다. FileBlockPtr는 long 위치와 int 크기로 12바이트다. Header의 BYTESIZE 계산값은 108이며 버전 문자열의 실제 저장 바이트 수는 기존 입출력 구현의 인코딩에 의존한다. 형식 확인은 SLOG 2 접두부, 호환 메시지는 SLOG 2.0.6 완전 일치 여부를 사용한다. 헤더 읽기 자체에는 버전 거부나 숫자 범위 검사가 없다.

CategoryMap은 범주 index로 map을 구성하고 미사용 범주 제거 메서드를 제공한다. LineIDMapList는 목록 순서대로 읽고 쓴다. TreeDir는 노드 ID와 시간 경계/블록 포인터 값을 연결한다. 세 컨테이너 모두 readObject가 기존 내용을 먼저 지우지 않으며 음수 개수에 명시적 오류를 내지 않는다. TreeDir의 전용 put은 possible-root이고 깊이가 더 클 때 root를 복사해 갱신한다. 상속된 map 수정 경로의 root 일관성은 이 클래스에 보완 코드가 없다.

Const의 버전 이력은 원본에 실린 호환성 설명으로 읽었다. 실제 호환성 시험으로 간주하지 않는다. TreeNodeID·TimeBoundingBox·Category·LineIDMap 내부와 파일 입력 진입점의 검증 순서는 후속 판독 대상이다. 전체 gate NOT_PASSED, 신규 사람 승인 없음.

## TreeNodeID와 정렬 5종

[slog2-node-read.json](slog2-node-read.json)에 본체와 내부 클래스 4종의 전체 표시 588줄을 기록했다. 동일 SHA 30경로에 대응하며 누적 Java 25/413종·138경로다. Java 388종·Python 150종은 미판독이다.

노드 ID는 depth(short)와 xpos(int)의 6바이트다. leaf는 depth=0, 가능한 root는 xpos=0이다. 부모 이동은 depth를 1 늘리고 xpos를 전달받은 분기 수로 정수 나눗셈한다. TreeDir의 전용 put과 연결하면 xpos=0인 후보 중 기존보다 큰 depth만 root로 복사한다.

두 comparator 모두 depth 내림차순이다. 같은 depth 안에서만 Increasing은 xpos 오름차순, Decreasing은 내림차순이다. 따라서 둘은 전체 순서를 뒤집은 관계가 아니다. 필드는 public mutable이고 equals는 TreeNodeID 인수의 overload만 표시된다. 키를 삽입한 뒤 수정하는 호출 경로는 후속 확인이 필요하다. 원본 main은 comparator 없는 TreeMap과 두 comparator TreeSet을 순서대로 구성하지만, 이를 실행 결과로 간주하지 않는다. 모든 표시 메서드·초기화·빈 marker 클래스까지 판독했으며 외부 의미 승인이나 전체 gate 통과는 아니다.

## 파일명·열거·표시 순회 7종

[slog2-iteration-read.json](slog2-iteration-read.json)에 TraceName, Permutation 및 IteratorOfAll/Fore/BackDrawables, IteratorOfFore/BackPrimitives의 전체 표시 내용을 결속했다. 누적 Java 32/413종, 남은 Java 381종·Python 150종이다.

TraceName은 소문자 확장자를 구분하며 clog2/clog/rlog/txt만 직접 slog2로 바꾼다. 나머지는 delimiter 묶음을 밑줄로 바꾸고 slog2 확장자를 덧붙인다. 이미 slog2인 이름도 이 분기로 들어간다. 빈 문자열 또는 delimiter뿐인 문자열은 내부 charAt(0)에 도달하므로 뒤쪽 기본 파일명 분기만 보고 빈 입력 처리가 보장된다고 할 수 없다. 이는 바이트코드 관측이며 실행 시험은 아니다.

Permutation은 중복 없는 순열이 아니라 각 자리 값이 0부터 children-1까지 변하는 배열 열거다. 0번 자리부터 carry하고 현재 배열의 복사본을 반환한다. 열거 상한은 Math.pow를 long으로 변환하며 nextElement 자체에는 소진 검사가 없다.

Drawables 정방향/역방향 순회는 목록을 해당 방향으로 훑어 시간 구간 overlap 조건을 통과한 항목을 반환한다. AllDrawables는 두 입력의 앞 항목을 비교해 병합하고 동률이면 nestable을 먼저 선택한다. Primitives 순회는 Composite에 기본 객체 추가를 위임하고 같은 시작 시각 비교기의 TreeSet에서 정방향은 first, 역방향은 last를 꺼낸다. 입력이 끝난 뒤 집합의 잔여 항목도 소비한다. 모든 순회기의 remove는 빈 메서드이며 보통의 소진 후 next는 null을 반환한다. 입력 정렬 조건·중복 제거·overlap 의미는 Drawable/Composite의 후속 판독과 함께 검증할 범위다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## 시간 경계와 좌표 11종

[time-coord-read.json](time-coord-read.json)에 TimeBoundingBox 계열 7종·Coord 계열 3종·CoordPixelXform 인터페이스의 전체 표시 내용을 기록했다. 누적 Java 43/413종이며 370종·Python 150종은 남아 있다.

TimeBoundingBox는 earliest/latest double 두 개를 그 순서대로 읽고 쓴다. TreeDirValue의 시간 경계 16바이트와 FileBlockPtr 12바이트를 합하면 앞서 관측한 28바이트다. 기본값은 (+∞,−∞), ALL_TIMES는 (−∞,+∞)다. 정상 순서의 NaN 없는 구간에서 overlap은 양쪽 끝점을 포함한다. 따라서 [0,1]과 [1,2]의 교집합은 [1,1]이고 길이는 0이다. contains는 양끝 포함, WithinLeft는 [시작,끝), WithinRight는 (시작,끝]이다. remove는 대응하는 시작 또는 끝이 정확히 일치할 때 한 경계만 옮기므로 일반 구간 차집합 연산으로 해석하면 안 된다.

| 비교기 | 우선 키 | 동률 키 |
|---|---|---|
| IncreasingStarttime | 시작 오름차순 | 끝 내림차순 |
| DecreasingStarttime | 시작 내림차순 | 끝 오름차순 |
| IncreasingFinaltime | 끝 오름차순 | 시작 내림차순 |
| DecreasingFinaltime | 끝 내림차순 | 시작 오름차순 |

표는 NaN 없는 값의 비교다. 입력 유효성/NaN 검사는 없으며 객체 setter는 경계를 정규화하지 않는다. Coord는 time(double)와 lineID(int)의 12바이트다. LineIDOrder는 두 int의 뺄셈을 반환하며 time은 비교하지 않는다. CoordPixelXform은 시간/행과 픽셀 간 변환 등 선언만 포함한다. Drawable/InfoBox 상속 경로 및 Composite 재정의 여부는 후속 판독으로 확인하며 이 기반 클래스만으로 모든 런타임 객체의 overlap을 확정하지 않는다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## Drawable 비교와 표시 분기 3종

[drawable-order-read.json](drawable-order-read.json)에 Drawable·Drawable$Order·Topology의 전체 756줄과 동일 SHA 18경로를 결속했다. 누적 Java 46/413종·264경로, 남은 Java 367종/Python 150종이다.

Drawable.Order는 시간 비교가 동률일 때 객체 identity, category index, 시작 vertex lineID, 끝 vertex lineID 순서로 처리한다. 정수 키들은 시간 방향과 관계없이 앞에서 뒤를 뺀다. 다른 객체라도 모든 비교 키가 같으면 경고를 출력하고 0을 반환한다. 앞선 Primitives 순회기의 TreeSet이 이런 객체들을 비교상 같은 항목으로 처리할 조건이 확인됐다. 실제 로그에서 발생했다는 주장은 아니다.

Drawable은 InfoBox를 상속하며 overlap을 직접 재정의하지 않는다. [InfoBox 선언](disassembly/032382185c66e318384f74fbf2bb7dd791bd2f4cad288a807e3c04e78e58055a.txt) 2줄은 TimeBoundingBox 상속을 확인해 주지만 InfoBox 전체 판독은 아직 하지 않았다. initExclusion은 전체 길이에서 전달된 구간별 교집합 길이를 각각 빼며 구간의 합집합을 만들거나 결과를 0으로 제한하지 않는다. 중복되는 구간을 전달하는 호출 여부는 후속 확인 대상이다.

그리기는 범주의 Topology에 따라 Event(0), State(1), Arrow(2) 순서로 분기하고 각 추상 draw/hit 메서드에 위임한다. Topology의 readObject는 int 값을 검사 없이 저장한다. Drawable 생성자에는 row_ID를 INVALID_ROW로 설정하는 명령이 없지만 미초기화 판정은 그 sentinel을 검사한다. 하위 클래스·호출자의 초기화까지 읽은 뒤 실제 영향을 판단한다. 전체 gate NOT_PASSED·신규 사람 승인 없음.
