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

## InfoBox 메타데이터 전체 판독

[infobox-read.json](infobox-read.json)에 967줄 전체·동일 SHA 6경로를 기록했다. 누적 Java 47/413종·270경로, 남은 Java 366종/Python 150종이다.

InfoBox는 TimeBoundingBox를 상속하고 overlap을 재정의하지 않는다. Drawable → InfoBox → TimeBoundingBox의 기반 상속 관계는 확인됐으며 하위 구현의 재정의는 별도다. InfoBox의 직렬화 메서드는 상속된 시간 경계를 기록하지 않고 category index(int), 정보 바이트 수(short), 정보 바이트만 처리한다. 하위 클래스가 시간 경계를 어떻게 저장하는지는 해당 구현에서 확인해야 한다.

resolveCategory는 유효한 index의 범주를 찾지 못하면 UnknownType-index라는 State 범주를 기본 색·폭 1로 만들어 map에 등록한다. releaseCategory는 공유 범주의 used를 false로 바꾸고 참조를 비우며 index는 유지한다. CategoryMap의 미사용 범주 제거와 연결되는 동작이다.

정보 해석은 최초 접근 시 플래그를 먼저 올리고 InfoType별 InfoValue 읽기에 위임한다. 정보 바이트를 바꾸는 setter나 readObject에는 이 플래그·기존 해석값의 초기화가 없다. 해석 도중 IOException이면 스택을 출력하고 System.exit(1)을 호출한다. 출력 문자열 생성도 해석을 유발하므로 단순 toString이라고 무조건 부작용 없는 경로로 취급할 수 없다. 실제 종료나 오래된 값 표시를 재현한 것은 아니며 호출 순서는 후속 판독 범위다. writer는 전체 배열을 쓰고 reader는 양수 signed short 길이만 읽는다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## 정보 형식과 값

[info-value-read.json](info-value-read.json)에 InfoType 308줄·InfoValue 495줄 전체를 결속했다. 누적 Java 49/413종·282경로, 남은 Java 364종/Python 150종이다.

| 태그 | 이름 | 값의 Java 형식 | 값 IO |
|---|---|---|---|
| s | STR | String | mixed 문자열 |
| h | INT2 | Short | short |
| d / x | INT4 / BYTE4 | Integer | int |
| l / X | INT8 / BYTE8 | Long | long |
| e | FLT4 | Float | float |
| E | FLT8 | Double | double |

InfoValue의 readObject/writeObject는 1바이트 InfoType 태그까지 처리한다. readValue/writeValue는 이미 정해진 type에 따라 값만 처리하며 InfoBox가 사용하는 경로는 readValue다. BYTE4/BYTE8은 정수와 같은 IO를 쓰지만 문자열 표시에서 16진수로 바뀐다. getByteSize의 문자열 계산은 문자 수+3이므로 기존 mixed writer의 인코딩된 바이트 길이와 구분한다.

setValue는 null type/value를 허용하고 나머지는 wrapper 형식을 검사하지만, type/value 생성자는 그대로 저장한다. 알 수 없는 nonnull 태그의 값 IO는 IOException을 던지므로 앞서 읽은 InfoBox의 종료 경로와 이어진다. null type은 이 분기에 앞서 역참조된다. 원본 프로그램 실행이나 실제 입력 오류 발생을 검증한 결과는 아니다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## 중첩 스택과 표시 위치 3종

[nesting-drawn-read.json](nesting-drawn-read.json)에 NestingStacks·DrawnBox·DrawnBoxSet 655줄 전체를 기록했다. 누적 Java 52/413종이며 361종·Python 150종은 남아 있다.

NestingStacks는 펼쳐지지 않은 표시 행에만 스택을 만든다. 현재 구간을 포함하지 않는 스택 꼭대기는 빼고, 포함하는 항목이 있으면 그 중첩 계수에 감소율을 곱한다. 없으면 초기 높이를 사용한다. 초기 높이와 감소율 기본값은 모두 0.8이다. 새 객체는 스택에 넣지만 계수 저장은 호출자 Drawable이 하며 parent 참조는 이 경로에서 설정하지 않는다. initialize 뒤 첫 reset은 플래그만 바꾸고 이후 reset부터 내용을 지운다.

DrawnBox는 head/tail의 이전 픽셀 위치를 보관한다. State는 폭 t-h가 1 이하일 때 두 끝 중 하나만 이전 위치의 1픽셀 이내여도 true다. Arrow는 두 끝 모두, Event는 head만 1픽셀 이내인지 검사한다. 일반적인 기하 포함 검사로 해석하지 않는다. DrawnBoxSet는 행 수 N에 대해 state/event N개와 arrow N²개 배열을 만들며 펼쳐진 행의 항목은 null로 둔다. 사용 시 행 번호·초기화·트리 변경 동기화는 호출자 확인이 필요하다. 실제 GUI 실행이나 표시 정확도 검증은 하지 않았다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## SLOG2 객체 버퍼 3종

[drawable-buffer-read.json](drawable-buffer-read.json)에 BufForObjects·내부 비교기·BufForDrawables의 전체 934줄과 18경로를 기록했다. 누적 Java 55/413종·318경로, 남은 Java 358종/Python 150종이다.

공통 버퍼는 시간 경계(16), 노드 ID(6), 블록 포인터(12)를 순서대로 저장해 34바이트다. BufForDrawables는 두 목록의 int 개수까지 기본 42바이트이고 각 항목에 Primitive=0/Composite=1 태그를 붙인다. State primitive와 composite는 nestable에, 다른 primitive는 nestless에 추가한다. 쓰기는 공통 헤더 뒤 nestless, nestable 순이다.

쓰기 전 시작 시각 정렬을 요청하지만 reorder는 기록된 comparator와 다를 때만 실제 정렬한다. add는 정렬 상태를 무효화하지 않으므로 쓰기 후 항목 추가 같은 호출 순서는 후속 확인이 필요하다. add는 시간 경계도 늘리지 않는다. empty는 저장 완료 플래그가 있을 때만 비우며 ID·시간·파일 위치는 유지한다.

읽기는 목록을 교체하고 범주를 연결하지만 total_bytesize를 먼저 초기화하지 않는다. 알 수 없는 태그는 오류 출력 후 반복을 계속하며 payload 길이를 건너뛰는 처리가 없다. 입력은 두 목록 모두 composite 태그를 허용하지만 getNumOfPrimitives는 nestless의 개수를 그대로 센다. 소스 수준의 조건과 가정이며 실제 잘못된 로그나 반복 사용을 시험한 결과는 아니다. Primitive/Composite의 내부 IO 및 상위 호출 흐름은 후속 판독 대상이다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## 행 계층 매핑과 Method

[lineid-method-read.json](lineid-method-read.json)에 LineIDMap 977줄·Method 122줄 전체와 12경로를 기록했다. 누적 Java 57/413종·330경로, 남은 Java 356종/Python 150종이다.

LineIDMap은 LineID → 계층별 Integer 배열의 TreeMap이다. 저장은 title, 계층 수, 각 열 이름, 매핑 수, 각 LineID와 계층 값, Method 수(short)와 Method 목록 순이다. 읽기는 기존 map을 지우지 않고 put하며 같은 키는 대체한다. 이전 BufForObjects의 identity map 생성은 계층 수 1에 id → [id]를 넣는 특수 경우와 연결된다.

YCoordMap에서 가져올 때 열 이름·평탄 배열 크기가 예상과 다르면 경고를 내지만 변환은 계속한다. 반대 변환은 예상 크기로 배열을 할당하고 실제 값 배열 길이만큼 써서, 부족하면 마지막에 명시적 예외를 내고 초과는 그 전에 배열 경계를 넘을 수 있다. 일반 writer는 실제 배열 길이 대신 계층 수만큼 쓴다는 차이가 있다. 입력 유효성 문제의 실제 발생 여부는 시험하지 않았다.

Method는 4바이트 정수 식별자로 1을 CONNECT_COMPOSITE_STATE로 정의한다. 연결 동작 자체의 구현은 이 클래스에 없다. 원본 main의 임시 파일 읽기/쓰기 데모는 실행하지 않았으며 YCoordMap과 실제 연결 호출은 후속 판독 대상이다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## YCoordMap과 누적 집계

[ycoord-read.json](ycoord-read.json)에 YCoordMap 279줄 전체를 기록했다. 행·열 수, 제목, 열 이름과 평탄 int 배열을 보관하고 Method ID를 객체로 만든다. map/label 배열을 복사하거나 크기를 검증하지 않는다. getter와 setMethods도 참조를 직접 전달한다. 따라서 LineIDMap 변환 전후의 메타데이터 배열 공유가 확인됐으며 소비자의 유효성 검사가 별도로 필요하다. 실제 프로그램은 실행하지 않았다.

[coverage.json](coverage.json)은 원본 SHA와 각 직접 판독 영수증을 결속해 누적 집합을 집계한다. Java 58/413종·336경로에 직접 판독 근거가 있고 Java 355종/Python 150종은 남아 있다. 집계는 판독 기록의 존재/중복/범위 확인이며 의미 판독의 외부 승인이 아니다. 원래 추출 영수증과 archive 인벤토리의 당시 상태는 바꾸지 않는다. 전체 gate NOT_PASSED·신규 사람 승인 없음.

## Shadow buffer 판독 보충

`shadow-buffer-read.json`은 BufForShadows 전체 750줄 및 동일 SHA 6개 경로를 결박한다. topology와 vertex line ID 목록별 집계, category weight 위임, 입력/출력 목록과 크기 누적을 확인했다. 반복 write는 목록을 비우지 않으며 empty는 saved 상태에서만 작동한다. 정상 호출자의 순서 보장은 아직 확인하지 않았다. 누적 Java 59/413종, 342개 경로이며 Java 354종·Python 150종이 남는다.

## Shadow 판독 보충

`shadow-read.json`은 Shadow 전체 1425줄과 동일 SHA 6개 경로를 결박한다. 객체 수 가중 평균, 병합 전후 기간에 따른 비율 재조정, 상태 exclusion 계산 후 임시 자료 해제, 직렬화와 preview 호출을 확인했다. output map의 toString에는 Object[]를 CategoryWeight[]로 cast하는 경로가 있다. 정상 호출에서의 도달 여부와 CategoryWeight/Primitive 내부는 별도 확인 대상이다. 누적 Java 60/413종·348경로이며 전체 gate는 NOT_PASSED다.

## Category weight 계열 판독

`category-weight-read.json`은 CategoryRatios/Summary/Weight 및 내부 comparator·marker 10종의 전체 909줄을 결박한다. 비율은 float 곱셈/덧셈이며 정규화하지 않는다. 직렬화는 index(int), inclusive(float), exclusive(float), count(long)의 20바이트다. 이미 연결된 CategoryWeight의 resolveCategory도 false이므로 Shadow의 short-circuit 조건과 연결된다. comparator의 뺄셈 overflow/NaN 방어는 없다. 정상 입력에서의 도달 여부를 별도로 확인해야 한다. 누적 Java 70/413종·408경로이며 전체 gate NOT_PASSED다.

## Primitive 판독 보충

`primitive-read.json`은 전체 955줄과 6개 동일 SHA 경로를 결박한다. 복사 생성자의 Coord 복사와 setter의 참조 공유를 구분했다. 배열 입력 생성자는 last_vtx_idx를 설정하지 않으며, 직렬화의 vertex 수는 signed short로 축소한다. 실제 호출에서의 영향은 별도 확인 대상이다. line ID 목록은 vertex 순서와 중복을 보존하므로 shadow 집계 키와 연결된다. 누적 Java 71/413종·414경로, 전체 gate NOT_PASSED.

## Composite 판독 보충

`composite-read.json`은 두 클래스 전체 1049줄·12개 경로를 결박한다. write는 공유 primitive 배열을 정렬하고 read는 child parent를 설정하지만 setter는 parent를 설정하지 않는다. 내부 iterator는 overlap=false에서 인덱스를 증가시키지 않고 반복한다. 생성자/next의 prefetch도 이 경로에 들어갈 수 있다. 정상 호출 도달 여부는 미확정이다. 누적 Java 73/413종·426경로, 전체 gate NOT_PASSED.

## Output TreeNode 판독

`output-node-read.json`은 전체 TreeNode 표시 내용을 결박한다. category-null Composite 분해, shadow 생성/기간 갱신/가중치 초기화/병합/shift/저장 후 empty를 연결했다. 상위 driver가 이 순서를 보장하는지는 후속 판독 대상이다. 전체 gate NOT_PASSED.

## 출력 흐름 판독

`output-flow-read.json`은 TreeTrunk/OutputLog 전체 723줄을 결박한다. TreeTrunk가 finalizeLatestTime 후 writeTreeNode를 호출하면 OutputLog가 vertical merge/horizontal shift 후 저장하고, TreeTrunk가 empty한다. flush는 root 요약 후 last marker를 비운다. OutputLog.close는 trunk flush를 호출하지 않으므로 converter 순서가 남은 확인 대상이다. 정상 경로의 순서 근거이며 모든 입력/오류 경로의 승인으로 확대하지 않는다.

## CLOG2 converter 판독

`clog2-converter-read.json`은 전체 764줄을 결박한다. 기본 시간 검사는 off이며 -tc/-tcc에서만 검사한다. 정상 EOF는 trunk flush 후 category/line ID map 기록, output/input close 순서다. 빈 trace는 close 후 output 삭제를 시도한다. parse 오류 일부는 입력명이 있으면 부분 옵션으로 계속될 수 있다. 이 기록은 입력 decoder의 정확성이나 모든 trace의 순서 보장이 아니다.

## CLOG converter 판독

`clog-converter-read.json`은 전체 750줄을 직접 확인한 근거다. CLOG2 converter와 달리 clogTOdrawable decoder를 사용하며 YCoordMap 분기가 없다. 출력 map list는 EOF flush 후 identity map 하나로 구성한다. 시간 검사 기본 off와 flush/map/close 순서는 공통이다. help의 Clog2Slog 표기 차이도 보존했다. 입력 decoder와 실제 자료 검증으로 확대하지 않는다.

## InputAPI/Kind 판독

`input-kind-read.json`은 전체 172줄을 결박한다. InputAPI는 peek와 5개 getter 선언만 제공하며 소비·정렬·close 규약을 구현하지 않는다. Kind는 정수 index의 값 동등성을 구현하지만 converter는 정적 객체 identity로 분기한다. decoder의 반환 방식은 후속 판독 대상이다. 전체 승인 미발급.

## TRACE converter 판독

`trace-converter-read.json`은 전체 864줄을 결박한다. Composite/YCoordMap을 지원하고 static initializer에서 TraceInput을 로드한다. 도움말/미인식 옵션/위치 인자를 filespec으로 이어 붙이며 빈 문자열을 null 검사로 거르지 못한다. 정상 EOF 출력 순서는 기존 converter와 연결된다. 네이티브 입력 구현과 실행 검증은 별도다.

## TRACE 입력 래퍼 판독

`trace-input-read.json`은 InputLog/DobjDef 전체 236줄을 결박한다. 초기 EVENT/STATE/ARROW 제공 후 native 정수를 정적 Kind로 바꾸므로 정상 index의 identity 연결이 확인됐다. 미지 index는 null, 초기 세 개 이후 native topology 요청은 null topology로 이어질 수 있다. native 함수는 선언만 있으며 실제 파일/객체 처리 의미는 완료 처리하지 않는다. DobjDef의 shape 검사와 Category 설정도 기록했다.

2026-09-12 CLOG2 InputLog와 TopologyIterator/YCoordMapIterator 전체 437줄 판독. 정적 Kind 반환 및 topology→content→좌표 맵 전환과 최초 arrow category 특례를 확인했다. ContentIterator 본문과 superclass는 미판독으로 남긴다. 누적 Java 86/413종·472경로, 잔여 Java 327종/Python 150종. 근거: `clog2-input-shell-read.json`.

2026-09-12 CLOG2 ContentIterator 전체 1,193줄 판독. hasNext가 레코드를 소비하고 next가 저장 객체를 반환하는 계약, Category/Primitive만 생성하는 경로, reflective handler 오류 처리와 미매칭 통계의 중복 집계 가능성을 기록했다. 저수준 레코드·Topo 매칭·ID 맵은 별도 미판독이다. 누적 Java 87/413종·474경로, 잔여 Java 326종/Python 150종. 근거: `clog2-content-read.json`.

2026-09-12 CLOG2 상태/화살표 매칭과 지원 클래스 7종 전체 791줄 판독. 상태 FIFO 매칭, 실패한 종료 이벤트의 예외 전달, 메시지 수신 선행 시 크기 0 저장 경로를 확인했다. 원본은 수정하지 않았다. 누적 Java 94/413종·488경로, 잔여 Java 319종/Python 150종. ID 맵과 저수준 레코드는 별도 미판독이다. 근거: `clog2-matching-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 ID 맵·ID 값·LineID 3종 전체 586줄 판독. 사용 항목 필터와 두 좌표 보기 생성, ID 누락 시 경고 후 null 참조, 전역 크기 기반 ID 계산의 무검사 정수 연산을 확인했다. 누적 Java 97/413종·494경로, 잔여 Java 316종/Python 150종. 저수준 레코드와 preamble 초기화는 별도 미판독이다. 근거: `clog2-idmap-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 RecHeader/RecMsg/RecBare/RecCargo 4종 전체 517줄 판독. 읽기 실패 시 부분/이전 필드 보존과 상위 반환값 미검사, skip 길이 미검사, Cargo의 매회 새 배열 할당을 확인했다. 누적 Java 101/413종·502경로, 잔여 Java 312종/Python 150종. stream/preamble 및 다른 레코드는 별도 미판독이다. 근거: `clog2-record-input-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 InputLog/MixedDataInputStream/Preamble 3종 전체 943줄 판독. preamble 실패 반환값 무시와 전역 ID 설정 누락 가능성, 짧은 블록 EOF 처리, 고정 문자열 NUL 조건을 연결했다. 누적 Java 104/413종·508경로, 잔여 Java 309종/Python 150종. 다른 레코드와 상수는 별도 미판독이다. 근거: `clog2-stream-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Const/RecComm/UUID 3종 전체 352줄 판독. 빈 호환 버전 목록, UUID 내부 읽기 실패에도 RecComm이 48을 반환하는 경로, CommFree와 UUID가 ID 맵 삭제/키에 쓰이지 않는 연결을 확인했다. 누적 Java 107/413종·514경로, 잔여 Java 306종/Python 150종. 근거: `clog2-comm-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 RecColl/RecDefConst/RecSrc/RecTshift 4종 전체 380줄 판독. 본문 converter가 집단통신·상수 이름·소스 위치·시간 이동 body를 건너뛰는 경로와 실제 skip 길이 미검사를 연결했다. 누적 Java 111/413종·522경로, 잔여 Java 302종/Python 150종. 근거: `clog2-skipped-records-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 상태/이벤트/메시지 정의와 ObjDef 4종 전체 552줄 판독. 임시 이벤트 ID 생성, stateID와 Category 번호의 분리, 메시지 형식과 정보 버퍼의 연결을 확인했다. 누적 Java 115/413종·530경로, 잔여 Java 298종/Python 150종. 근거: `clog2-definitions-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Topo_Event/Obj_Event/ColorNameMap 3종 전체 404줄 판독. 단일 좌표 이벤트 생성, 색상 이름 콜론 suffix 생략과 기본색 fallback, null/잘못된 행 처리의 한계를 확인했다. 누적 Java 118/413종·536경로, 잔여 Java 295종/Python 150종. ColorAlpha 내부와 진단 CLI는 별도 미판독이다. 근거: `clog2-event-color-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 ColorAlpha 전체 400줄 판독. 5바이트 저장과 입력 생성자/무동작 readObject의 차이, RGB 제곱합 비교, 216색 중 215개 인덱스 순환 및 전역 fallback 상태를 확인했다. 누적 Java 119/413종·542경로, 잔여 Java 294종/Python 150종. 근거: `color-alpha-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 Category 전체 1,030줄 판독. 색상 입력 생성자 사용, 폭 byte/배열 short 범위 미검사, 형식 문자열 null과 빈 문자열의 차이, 비직렬화 표시 플래그와 shadow 정의를 확인했다. 누적 Java 120/413종·548경로, 잔여 Java 293종/Python 150종. 근거: `category-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print 진단 CLI 전체 243줄 판독. 출력 카테고리 목록의 shadow 포함, 즉시 Primitive 출력과 사후 정의 출력의 차이, 실제 파일 크기와 누적 바이트 출력의 차이를 기록했다. 누적 Java 121/413종·550경로, 잔여 Java 292종/Python 150종. Print_1pass/Print_2pass는 별도 미판독이다. 근거: `clog2-print-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print_1pass 전체 1,087줄 판독. 상태 메서드의 RecBare/RecCargo 인자형 불일치로 인한 종료 경로, 현재 stateform만 집계하는 미매칭 통계, 일반 converter와 다른 정의/레코드 처리 범위를 기록했다. 누적 Java 122/413종·552경로, 잔여 Java 291종/Python 150종. 근거: `clog2-print-onepass-read.json` (bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 CLOG2 Print_2pass 전체 1,043줄 판독. 첫 상태 정의의 RecBare/RecCargo reflection 불일치, 상태 정의 부재 시 마지막 통계의 null 참조, 두 pass 모두 type0 이후 다음 블록을 읽는 경로를 확인했다. 누적 Java 123/413종·554경로, 잔여 Java 290종/Python 150종. 근거: `clog2-print-twopass-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 하위 CLOG2/TRACE Print 2종 전체 923줄 판독. CLOG2 type0 이후 다음 블록 요청과 레코드 직접 출력, TRACE 선택적 시간 검사·도움말 이전 native load·빈 파일명 검사의 한계를 기록했다. 누적 Java 125/413종·558경로, 잔여 Java 288종/Python 150종. 근거: `lowlevel-print-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인과 구분한다.

2026-09-12 base.topology Event/Line/State 3종 전체 762줄 판독. DrawnBox 선기록, 경계 잘림 차이, 이벤트 초기 반폭/전체 폭 불일치와 상태 Insets 비반영 선택 판정을 기록했다. 누적 Java 128/413종·564경로, 잔여 Java 285종/Python 150종. 근거: `basic-topology-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증이나 독립 의미 승인이 아니다.

2026-09-12 StateBorder 선택기·구현 8종 전체 543줄 판독. 좌우 경계 플래그, 위아래 선의 무조건 호출, 색상 변경 잔류와 XOR 모드 비복원, 알 수 없는 이름의 null 반환을 기록했다. 누적 Java 136/413종·580경로, 잔여 Java 277종/Python 150종. 근거: `state-border-read.json` (XBeach connectivity/bytecode-read). 원본 실행·실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 PreviewEvent 전체 354줄 판독. 중심 시각만 사용하는 표시 생략, 화면 경계 제외, 두 반타원과 세로선, 표시 높이와 타원 선택 높이의 1픽셀 차이를 기록했다. 누적 Java 137/413종·582경로, 잔여 Java 276종/Python 150종. 근거: `preview-event-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 Arrow 전체 619줄 판독. 방향별 화살촉 stroke 적용 차이, NaN 동등 비교의 도달 불가 분기, 같은 픽셀 끝점의 수직 화살촉 처리와 한쪽 경계 검사 한계를 기록했다. 누적 Java 138/413종·584경로, 잔여 Java 275종/Python 150종. 근거: `arrow-render-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 SummaryArrow 전체 423줄 판독. 카테고리별 공통 시작 시간, 객체 수 정수 나눗셈 기반 선 굵기, 밑 0·빈 배열·0시간 길이의 미검사, 굵기를 반영하지 않는 Line 선택 판정을 기록했다. 누적 Java 139/413종·586경로, 잔여 Java 274종/Python 150종. 근거: `summary-arrow-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 SummaryState 전체 889줄 판독. 표시 방식 4종의 시간/행 배치, 준비 단계와 그리기·선택 단계의 가시성 검사 차이, 배경색 객체 동일성 비교, 카테고리 우선 선택과 전체 상자 fallback을 기록했다. 누적 Java 140/413종·588경로, 잔여 Java 273종/Python 150종. 근거: `summary-state-read.json` (XBeach connectivity/bytecode-read). 실제 화면 검증·독립 의미 승인은 아니다.

2026-09-12 CategoryTimeBox 계열 6종 전체 238줄 판독. 비율·색상·가시성의 원본 가중치/카테고리 위임, 네 정렬기의 시간 구간 비참조, null 가중치 미검사를 확인했다. 누적 Java 146/413종·600경로, 잔여 Java 267종/Python 150종. 근거: `category-timebox-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 TimeAveBox 전체 672줄 판독. 비율/개수 가중 합산, 삽입 순서 중첩 계산, 계산 후 timeblock null 처리, 무필터·일회 생성·직접 반환 카테고리 배열을 확인했다. SummaryState 가시성/오래된 표시 구간 문제의 하위 연결 근거를 추가했다. 누적 Java 147/413종·602경로, 잔여 Java 266종/Python 150종. 근거: `timeave-box-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 CategorySummaryF/CategoryWeightF 및 보조·선택 7종 전체 485줄 판독. double 개수 계산과 float 표시, NaN 개수 정렬 및 인덱스 뺄셈 한계, category 참조/캐시 인덱스 연결을 확인했다. category-timebox 기록의 F 정렬기 “이전 판독” 표현은 정수형 CategoryWeight와 혼동한 것으로 정정한다. F 본체는 이번 최초 판독이며 기존 집계에는 포함되지 않았다. 누적 Java 154/413종·616경로, 잔여 Java 259종/Python 150종. 근거: `float-statistics-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 BufForTimeAveBoxes 전체 891줄 판독. 행별 새 상자의 중첩 계산→배열 초기화→배치 순서를 확인해 앞선 캐시/재호출 위험의 정상 초기화 경로 적용 범위를 좁혔다. 행 매핑 누락 미검사와 화살표 우선·HashMap 첫 일치 선택도 기록했다. 누적 Java 155/413종·618경로, 잔여 Java 258종/Python 150종. 근거: `timeave-buffer-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 PreviewState 전체 1,035줄 판독. 표시 6방식의 픽셀 배분·가시성 반영, 그리기에서 갱신한 치수에 의존하는 선택 판정, 누적 방식 x 여백 재검사 부재를 기록했다. 인벤토리 base/ 미판독은 0이지만 전체 gate는 미통과다. 누적 Java 156/413종·620경로, 잔여 Java 257종/Python 150종. 근거: `preview-state-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 SLOG2 BufStub/IteratorOfGroupObjects 2종 전체 267줄 판독. 대리 버퍼의 경고·null/초기값 반환과 toString 캐시 변경, 최초 그룹 준비 및 그룹 전환의 hasNext 의존성을 기록했다. 누적 Java 158/413종·624경로, 잔여 Java 255종/Python 150종. 근거: `input-helpers-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 입력 TreeNode/그림자 순회기 5종 전체 596줄 판독. 생성자의 최초 그룹 준비, 겹치지 않는 버퍼 생략, 음수 자식 수의 null 처리와 직접 반환 배열을 확인했다. 누적 Java 163/413종·634경로, 잔여 Java 250종/Python 150종. 근거: `input-treenode-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 입력 TreeFloor/순회기 3종 전체 571줄 판독. 노드 목록의 얕은 복사와 방향 선택을 연결했다. prune의 내림차순 삭제 방향 불일치에 따른 빈 맵 접근 가능성을 정적 흐름으로 기록했으며 실제 호출 조건은 후속 확인한다. TimeBoundingBox.contains(double)는 양쪽 끝점을 포함함을 직접 재확인했다. 누적 Java 166/413종·640경로, 잔여 Java 247종/Python 150종. 근거: `input-treefloor-read.json` (XBeach connectivity/bytecode-read). 독립 의미 승인은 아니다.

2026-09-12 TreeFloorList/병합 순회기/입력 TreeTrunk 3종 전체 1,848줄 판독. prune 공개 경로와 확대·스크롤 경로가 다름을 확인하여 앞선 조건부 결함의 적용 범위를 제한했다. 층별 병합 조건, static 루트 시간 범위의 인스턴스 간 공유, 자식 읽기 null 처리와 깊이/확대값 검증 부재를 기록했다. 누적 Java 169/413종·646경로, 잔여 Java 244종/Python 150종. 근거: `input-floorlist-trunk-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 InputLog/전체 실객체 순회기 2종 전체 1,089줄 판독. 메타데이터 IO 실패 exit와 트리 노드 실패 null 반환의 차이를 TreeTrunk 호출자에 연결했다. 포인터 null 판정과 시작/종료 끝점의 반개구간 필터를 직접 재확인했으며 잘못된 topology 번호, 빈 leaf 집합, 구간 경계 제외 조건을 기록했다. 누적 Java 171/413종·650경로, 잔여 Java 242종/Python 150종. 근거: `slog-inputlog-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 PrintSerially/PrintRecursively 2종 전체 1,183줄 판독. 옵션 순서 의존성, 숫자 변환 실패 후 계속 진행, NaN 검사 통과, 재귀 출력의 루트 읽기 실패/빈 자료 혼동을 기록했다. 순차 출력의 인접 정렬 표시는 완전성 검증이 아니며 재귀 출력 모드 간 선택 범위도 다르다. 누적 Java 173/413종·654경로, 잔여 Java 240종/Python 150종. 근거: `slog-print-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 SLOG2 Navigator 전체 1,181줄 판독. 출력 모드 변경 시 시간창 갱신 단락 평가, 초기 changedPrintAll 잔존, 첫 숫자 토큰 오류의 catch 내부 배열 접근, EOF 미처리를 확인했다. 현 인벤토리의 SLOG2 input 패키지 판독은 채웠으나 전체 모델 gate는 미통과다. 누적 Java 174/413종·656경로, 잔여 Java 239종/Python 150종. 근거: `slog-navigator-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 CLOG2 상수 내부 클래스/고정 길이 선언 9종 전체 186줄 판독. 레코드 종류0..11, 통신 종류와 메시지 SEND/RECV 번호, 24/32/40바이트 선언을 기존 실제 레코드 처리 판독과 구분해 연결했다. 자체 IO/검증은 없다. 누적 Java 183/413종·674경로, 잔여 Java 230종은 viewer 계열이며 Python 150종도 미판독이다. 근거: `clog2-constant-companions-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer SwingWorker 계열/Routines 5종 전체 665줄 판독. interrupt 후 즉시 참조 제거와 실제 작업 종료를 구분하고 예외 시 finished 미예약, 시작 전 get 순환 가능성, 시간 눈금/색상/마우스 보조 연산의 경계 조건을 기록했다. 누적 Java 188/413종·684경로, 잔여 Java 225종/Python 150종. 근거: `viewer-worker-routines-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LogFileChooser/디렉터리 필터 3종 전체 363줄 판독. applet/일반 모드의 필터·탐색 차이, 확장자 기본 로케일 소문자 처리와 설정값 대소문자 비대칭, 숨김/끝점 파일명 조건을 기록했다. 필터 통과는 존재·읽기 가능·로그 내용 검증이 아니다. 누적 Java 191/413종·690경로, 잔여 Java 222종/Python 150종. 근거: `viewer-filechooser-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer TopControl/TopWindow 계열 6종 전체 327줄 판독. Legend→Timeline 및 First→Legend/Preference→exit 종료 연결, 창 교체 시 남는 Control 참조와 자동 배치의 화면 크기 캐시/경계 조건을 기록했다. 이 계층에는 직접 작업 취소·로그 닫기 처리가 없으며 실제 프레임 구현은 후속 판독한다. 누적 Java 197/413종·702경로, 잔여 Java 216종/Python 150종. 근거: `viewer-topwindow-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer ActableTextField/Alias/LabeledComboBox 3종 전체 291줄 판독. 액션 전달의 위임, 별칭의 원본 참조 보존, 콤보 Boolean 선택의 직접 형변환과 활성화 상태의 내부 위임 범위를 기록했다. 누적 Java 200/413종·708경로, 잔여 Java 213종/Python 150종. 근거: `viewer-combo-alias-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LabeledFloatSlider 전체 299줄 판독. 내부 위치0/10000의1/9999 보정, 표시 끝점과 설정 범위의 차이, 같은 위치/변경 위치에 따른 텍스트 정규화 경로를 기록했다. 부모 텍스트 파싱은 후속 확인한다. 누적 Java 201/413종·710경로, 잔여 Java 212종/Python 150종. 근거: `viewer-float-slider-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LabeledTextField/문서 리스너 2종 전체 579줄 판독. 초기 빈 텍스트, listener 등록 직후 null 및 중복 등록, 숫자 파싱 실패 시 정수 최소값/실수 최소 양수 반환을 슬라이더 입력 처리에 연결했다. 문서 이벤트는 액션을 직접 발행하지 않는다. 누적 Java 203/413종·714경로, 잔여 Java 210종/Python 150종. 근거: `viewer-textfield-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer CustomCursor 전체 224줄 판독. 클래스 초기화 시 커서 리소스4종의 순차 로딩, 고정 hotspot(1,1), 권장 크기 캔버스에 무배율 그리기와 실패 fallback 부재를 기록했다. 실제 플랫폼/리소스 성공 여부를 실행 검증으로 주장하지 않는다. 누적 Java 204/413종·716경로, 잔여 Java 209종/Python 150종. 근거: `viewer-cursor-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer PreferenceFrame/닫기 리스너 2종 전체 305줄 판독. 닫기의 숨김 동작과 저장 전 설정 갱신 순서, setVisible 후 Control 호출, 이전 창 정리와 새 창 조기 등록을 TopWindow 흐름에 연결했다. 실제 값 변환/파일 쓰기는 PreferencePanel/Parameters 후속 판독 범위다. 누적 Java 206/413종·720경로, 잔여 Java 207종/Python 150종. 근거: `viewer-preference-frame-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer Const 전체 213줄 판독. UI 상수와 공유 Alias 초기화, 대소문자 무시/공백 미제거 파서의 기본값 복귀 및 null 예외를 기록했다. STRING/BOOLEAN_FORMAT=null을 기존 LabeledTextField 판독에 연결했다. 누적 Java 207/413종·722경로, 잔여 Java 206종/Python 150종. 근거: `viewer-const-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer Parameters 전체 1,401줄 판독. ACTIVE_REFRESH 저장/복원 비대칭, 저장 취소 전 메모리 갱신, 설정 순차 대입 중 변환 실패 시 부분 상태 유지, 파일 IO와 렌더러 설정 전파의 분리를 연결했다. 누적 Java 208/413종·724경로, 잔여 Java 205종/Python 150종. 근거: `viewer-parameters-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer PreferencePanel 전체 1,593줄 판독. UI 입력 순차 대입, 비활성 ACTIVE_REFRESH의 복사 포함, 툴팁 조건 미검증, 슬라이더 텍스트 직접 파싱 및 렌더러 전파 호출 부재를 설정 창/Parameters에 연결했다. 누적 Java 209/413종·726경로, 잔여 Java 204종/Python 150종. viewer/common 잔여 클래스는 없다. 근거: `viewer-preference-panel-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer FirstFrame/종료 리스너 2종 전체 419줄 판독. 초기화 순서와 TopControl 버튼 위임, 숫자 인자 오류 후 GUI 진행, 현재 전역 First를 대상으로 하는 종료 콜백을 연결했다. 누적 Java 211/413종·730경로, 잔여 Java 202종/Python 150종. FirstPanel의 생성/초기화와 로그 열기는 후속 범위다. 근거: `viewer-first-frame-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer FirstPanel/리스너 계열 12종 전체 1,474줄 판독. 기존 로그 정리 후 신규 열기, 실패 시 목록 유지, ViewMap 선택 인덱스로 view_ID 덮어쓰기, 도구모음/도움말 이벤트 경로를 연결했다. 누적 Java 223/413종·754경로, 잔여 Java 190종/Python 150종. 실제 설정/로그 처리 내부는 LogFileOperations 후속 범위다. 근거: `viewer-first-panel-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LogFileOperations/worker 2종 전체 509줄 판독. 초기 설정 전파, 거부한 입력의 명시적 close 누락, 오래된 ViewMap의 null-log 차단, 공유 로그/창을 읽는 worker 경쟁 경로를 연결했다. 정상 main의 Control 설정이 설정 파일 로드보다 앞선다는 조건도 보완했다. 누적 Java 225/413종·758경로, 잔여 Java 188종/Python 150종. 근거: `viewer-logfile-operations-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer FirstMenuBar/리스너 11종 전체 554줄 판독. 메뉴→버튼 doClick 위임, 도구모음에 없는 Close/About 버튼의 메뉴 경로, 종료 확인을 거치지 않는 Exit 및 applet 분기를 연결했다. 누적 Java 236/413종·780경로, 잔여 Java 177종/Python 150종. 근거: `viewer-first-menubar-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer HTMLviewer/리스너 8종 전체 910줄 판독. 잘못된 URL 오류 처리의 null 참조, 페이지 로드 전 이력 변경/실패 시 미복원, 새 링크 이동 후 redo 유지, UI 이벤트 큐의 링크 로드를 연결했다. 누적 Java 244/413종·796경로, 잔여 Java 169종/Python 150종. viewer/first 잔여 클래스는 없다. 근거: `viewer-html-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LegendFrame/닫기 리스너 2종 전체 403줄 판독. 기존 범례/타임라인 정리 후 조기 등록, 표시 상태 변경 후 Control 호출, 독립 main 초기화 전제조건과 로그 소유권을 연결했다. 누적 Java 246/413종·800경로, 잔여 Java 167종/Python 150종. LegendPanel 내부는 후속 범위다. 근거: `viewer-legend-frame-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LegendPanel/LegendTable 2종 전체 582줄 판독. 행 선택과 표시 속성의 구분, 전역 범례 숨김, 컬럼별 메뉴/마우스 처리 연결, 초기 렌더러 표본 크기 계산을 기록했다. 누적 Java 248/413종·804경로, 잔여 Java 165종/Python 150종. 실제 데이터/정렬 변경은 LegendTableModel과 메뉴 후속 범위다. 근거: `viewer-legend-panel-table-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LegendTableModel 전체 725줄 판독. 공유 Category 편집, 목록 정렬 후 아이콘 재생성, 빈 목록의 초기 폭 계산 실패, 컬럼 반환형/편집 입력형 차이를 연결했다. 누적 Java 249/413종·806경로, 잔여 Java 164종/Python 150종. 비교자 내부와 색상 편집기는 후속 범위다. 근거: `viewer-legend-model-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer LegendComparators 10종과 CategoryIcon/Editor/Renderer/Label/Const 5종 전체 1199줄 판독. 이름 정렬의 topology→preview→name 우선순위, 비율 비교의 NaN 비대칭, 색상 편집 취소 시에도 alpha255로 확정하는 경로와 모델 ColorAlpha 계약을 연결했다. 누적 Java 264/413종·836경로, 잔여 Java 149종/Python 150종. 근거: `viewer-legend-comparators-icons-read.json` (XBeach connectivity/bytecode-read). 이전 모델 receipt의 비교자·편집기 미확정 항목을 보충하며 기존 기록은 보존한다. 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer 범례 헤더/컬럼 처리기 4종·OperationBooleanMenu 계열 7종 전체 1041줄 판독. 헤더 view→model 컬럼 변환, 우클릭 시 행 선택 유지, 실행 시 선택행 기반 표시/검색 플래그 일괄 편집, 눌림 표시 해제 누락 경로를 연결했다. 누적 Java 275/413종·858경로, 잔여 Java 138종/Python 150종. 근거: `viewer-legend-handlers-boolean-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer OperationNumberMenu/OperationStringMenu 계열 10종 전체 658줄 판독. 수치 컬럼별 비교자 선택, Creation Order의 인덱스 기준, 역순 이름 정렬 시 topology/preview 그룹도 함께 반전하는 호출 경로를 연결했다. 누적 Java 285/413종·878경로, 잔여 Java 128종/Python 150종. 근거: `viewer-legend-sort-menus-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer Triangular3DIcon 전체 578줄 판독. 헤더의 두 bool 인자별 UI 색상 분기, 위/아래 삼각형의 전체 선분 루프, Graphics 색상 미복원과 위쪽 아이콘의 우측 경계 1픽셀 초과를 연결했다. viewer/legends 고유 42종 전체 판독 근거 확보. 누적 Java 286/413종·880경로, 잔여 Java 127종/Python 150종. 근거: `viewer-legend-triangle-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer ConvertorDialog/Frame와 listener·AdvancingTextArea·WaitingContainer 10종 전체 606줄 판독. 모달 출력명 반환과 취소 null 경로, 독립 창의 Okay/Cancel/닫기 모두 JVM 종료, 패널/프로세스 취소 미확정 범위를 연결했다. 누적 Java 296/413종·900경로, 잔여 Java 117종/Python 150종. 근거: `viewer-convertor-windows-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer InputStreamThread/ProgressAction/SwingProcessWorker 3종 전체 570줄 판독. 초기화 중 프로세스 실행 실패 시 status0 잔존, 출력 수집의 비EDT 갱신·미대기 종료, 파일 크기 기반 진행률을 연결했다. 누적 Java 299/413종·906경로, 잔여 Java 114종/Python 150종. 근거: `viewer-convertor-process-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer ConvertorConst 전체 484줄 판독. 형식별 JAR/라이브러리 경로와 시스템 속성 초기화, 구분자 변경 시 TXT 경로를 UTE 경로로 덮는 참조 오류를 연결했다. 누적 Java 300/413종·908경로, 잔여 Java 113종/Python 150종. 근거: `viewer-convertor-const-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer ConvertorPanel 및 중첩 9종 전체 2424줄 판독. JAR 검사 전 출력 삭제, 현재 출력 필드 반환, 실행 실패 후 OK 활성화, Stop의 직접 finished 호출과 중복 완료 경로를 연결했다. 독립 Frame에는 실제 OK 버튼이 없음을 보충했다. 누적 Java 310/413종·928경로, 잔여 Java 103종/Python 150종. 근거: `viewer-convertor-panel-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer TimelineFrame/닫기 listener 전체 459줄 판독. 패널 생성 전 전역 창 등록, 현재 전역 창을 닫는 이벤트, 독립 main의 설정 초기화와 viewID CLI를 연결했다. 누적 Java 312/413종·932경로, 잔여 Java 101종/Python 150종. 근거: `viewer-timeline-frame-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer TimelinePanel/PreviewStateComboBox 계열/TreeTrunkPanel 5종 전체 1075줄 판독. 로그 트리·시간/행 viewport 연결과 초기화, 미리보기 변경 시 설정 창 전체 필드 덮어쓰기 및 null 참조 후 부분 갱신을 연결했다. 누적 Java 317/413종·942경로, 잔여 Java 96종/Python 150종. 근거: `viewer-timeline-panel-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer SearchCriteria/SearchTreeTrunk 2종 전체 486줄 판독. 전체 시간 검색의 선택 행·카테고리 필터, 연속 검색 커서 소거, 시간 평균 통계의 shadow/실체 병합 순서를 연결했다. 누적 Java 319/413종·946경로, 잔여 Java 94종/Python 150종. 근거: `viewer-timeline-search-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer InfoDialogForDrawable 계열과 공통 InfoDialog/Duration/Time 7종 전체 787줄 판독. 시작·클릭·끝점 중심 이동, 정적 시간 표시와 mutable 시간 범위 참조, 호출 측에 위임된 닫기 이벤트 연결을 구분했다. 누적 Java 326/413종·960경로, 잔여 Java 87종/Python 150종. 근거: `viewer-info-dialogs-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer InfoPanelForDrawable/TextAreaBuffer 2종 전체 1202줄 판독. 선택 하위 카테고리 표식 소거, 공유 여백 Component 재부착, 좌표 duration/전체 범위/평균 좌표와 가중치 표시를 구분했다. 누적 Java 328/413종·964경로, 잔여 Java 85종/Python 150종. 근거: `viewer-info-panel-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.

2026-09-12 viewer SearchPanel/SummarizableView/TimeFormat/OperationDurationPanel 계열 6종 전체 567줄 판독. 표시 시간의 단위 경계·부호 보존, 구간 통계 요청의 공유 결과 창 및 연속 클릭 경쟁 가능성을 연결했다. 누적 Java 334/413종·976경로, 잔여 Java 79종/Python 150종. 근거: `viewer-duration-operation-read.json` (XBeach connectivity/bytecode-read). 실제 실행·독립 의미 승인은 아니다.
