# JavaScript

### JavaScript를 배워야 하는 이유
- Wev기술의 기반이 되는 언어
  - HTML 문서의 콘텐츠를 ```동적으로 변경```할 수 있는 언어
  - Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반
- 다양한 분야로 확장이 가능한 언어
  - JavaScript는 Web을 위해 탄생한 언어로, 초기에는 언어의 특성상 많은 개발자에게 환영 받지 못함
  - 하지만 버전이 올라가면서 하나의 단단한 언어로 자리 매김을 한 언어
  - 단순히 Web 조작을 넘어서 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그래밍, 블록체인, 게임 개발 등 ```다양한 분야에서 활용이 가능한 언어```가 됨
  - 과거에는 단순히 Web Front-end를 위해서만 JavaScript 개발자를 찾았다면 이제는 그 영역이 매우 넓어져 다양한 직군에서 찾는 언어가 됨
### JavaScript 역사
- 개요
  - JavaScript의 개발 환경 전에 역사 알아보기
  - Web을 조작하기 위한 언어인 만큼 ```Web Browser와도 깊은 연관 관계가 있음```
  - 이러한 이유 때문에 JavaScript를 처음 학습할 때 다양한 용어를 접하게 되는데 역사를 통해 전체적인 그림을 그려보고자 함
- 웹 브라우저의 역할
  - URL을 통해 Web(WWW)을 탐색함
  - ```HTML/CSS/JavaScript를 이해한 뒤 해석```해서 사용자에게 하나의 화면으로 보여줌
  - 웹 서비스 이용 시 클라이언트의 역할을 함
  - 즉, 웹 페이지 코드를 이해하고, 보여주는 역할을 하는 것이 바로 웹 브라우저
- 웹 브라우저와 스크립트 언어
  - 1993, Mosaic Web Browser
    - 유저가 웹을 쉽게 탐색할 수 있게 버튼 등을 탑재한 GUI 기반의 웹 브라우저
  - 1994, Netscape Navigator
    - Mosaic Web Browser를 개선한 후속작, 시장 점유율 80% 차지
  - 이때까지만 해도 정적 웹페이지를 단순히 보여주는 용도에 그침
  - 웹 브라우저에 탑재해서 웹 페이지를 동적으로 바꿔줄 Script 언어 개발 필요
    - Script언어 
      - 소스코드를 기계어로 바꿔주는 컴파일러 없이 바로 실행 가능한 언어, 속도가 느리다는 단점이 있음
  - Netscape에서 약 10일의 개발 기간을 통해 Script언어인 Mocha 개발
  - 이후 LiveScript로 이름 변경 후 브라우저에 LiceScript를 해석해주는 Engine을 내장
  - 이후 당시 인기있던 JAVA의 명성에 기대보고자 JavaScript로 이름 변경
  - 1995, Microsoft의 Insternet Explorer
    - JavaScript를 그대로 복사한 JScript라는 언어 제작 후 이를 탑재한 Wev Browser인 Internet Explorer 출시
    - 이후 JavaScript와 JScript는 각자의 기능을 추가하기 시작
    - 개발자들은 Netscape Navigator와 Internet Explorer 각각에 대한 코드를 작성해야 하는 상황을 맞이하게 됨
  - 1996-2000, ECMA 표준 발의
    - Netscape가 정보 통신에 관한 규약을 만드는 비영리 단체 ECMA에게 JavaScript 기반의 표준안 발의 제안, ECMAScript 1 출시
    - 이후 여러가지 문법이 추가되며 ECMAScript의 버전이 올라감
    - 이 상황을 지켜보던 Microsoft
      - Windows에 Internet Explorer 기본으로 탑재
    - 결국 시장 점유율 95% 이상으로 증가, ECMAScript 표준안 지키지 않겠다 선언
  - 2001-2004, 다양한 웹 브라우저의 등장
    - ActionScript3라는 스크립트 언어를 기반으로 한 Firefox 웹 브라우저 출시
    - 개발자는 여러 브라우저를 지원하기 위해 고통받음
  - jQuert 등의 라이브러리 등장
    - 각 브라우저의 엔진에 맞는 스크립트를 여러 번 작성하는 것이 고통스러움
    - 중간에 하나의 레이어를 두고 코딩하는 것 = jQuery
      - jQuery 문법에 맞춰 작성하면 브라우저별 엔진에 맞는 스크립트 변환은 jQuert가 알아서 변환해줌
    - 이후 아주 많은 코드가 jQuery로 작성됨
  - 2008, Google의 Chrome 등장과 대통합의 시대
    - V8이라는 강력한 엔진을 탑재한 Chrome 등장
      - JavaScript 해석이 다른 웹 브라우저에 비해 월등히 빠름
      - 이로 인해 웹 브라우저가 버벅임이 없고 매우 빠르게 동작
    - Chrome의 성능 앞에서 다른 웹 브라우저 들이 함께 표준안을 만들자고 제안
  - 2009, ECMAScript5 (ES5) 표준안 제정
  - 2015, ECMAScript6 (ES6) 표준안 제정
  - 이후에도 계속해서 버전이 업데이트 되고 있으나, 큰 변화는 ```ES6에서 이루어짐```
- 정리
  - 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음




### DOM
- 개요
  - "브라우저에서의 JavaScript"
    - JavaScript는 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
    - 정적인 정보만 보여주던 웹 페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호작용을 하거나, 애니메이션 등이 동작하게 하는 것을 가능하게 함
  - [참고] 스크립트 언어(Script Language)
    - 기존에 존재하는 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍
- Browser APIs
  - 웹 프라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함
  - JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음
  - 종류
    - DOM
    - Geolocation API - 지리정보
    - WebGL - 그래픽
- DOM
  - 문서 객체 모델(Document Object Model)
  - 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
  - HTML 문서를 구조화하여 각 요소를 객체(object)로 취급
  - 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - DOM은 문서를 논리 트리로 표현
  - DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
  ![DOM](JS.assets/DOM.PNG)
  - 웹 페이지는 일종의 문서(document)
  - 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML코드 자체로 나타나기도 함
  - DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
  - DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음
- DOM에 접근하기
 - DOM을 사용하기 위해 특별히 해야 할 일은 없음
 - 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
 - 우리는 DOM의 주요 객체들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음
  - DOM의 주요 객체
    - ```window```
      - DOM을 표현하는 창
      - 가장 최상위 객체(작성시 생략 가능)
      - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
      ![window object](JS.assets/window%20object.PNG)
      - window의 메서드 예시
      ![window object2](JS.assets/window%20object2.PNG)
    - ```document```
      - 브라우저가 불러온 웹 페이지
      - 페이지 컨텐츠의 진입점 역할을 하며, < body> 등과 같은 수많은 다른 요소들을 포함하고 있음
      ![document object](JS.assets/document%20object.PNG)
      - document의 속성 예시
      ![document object2](JS.assets/document%20object2.PNG)
      - [참고] document는 window의 속성이다.
      ![document object3](JS.assets/document%20object3.PNG)
      - [참고] 파싱(Parsing)
        - 구문 분석, 해석
        - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
        ![파싱](JS.assets/%ED%8C%8C%EC%8B%B1.PNG)
    - navigator, location, history, screen 등
#### DOM 조작
- 개요
  - Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
  - DOM조작 순서
    1. 선택(Select)
    2. 조작(Manipulation)
      - 생성, 추가, 삭제 등
- 선택 관련 메서드
  - document.querySelector(selector)
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공한 CSS selector를 만족하는 첫 번째 element객체를 반환(없다면 null 반환)
  - document.querySelectorAll(selector)
    - 제공한 선택자와 일치하는 여러 element를 선택
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    - 제공한 CSS selector를 만족하는 NodeList를 반환
  - 실습
    ![선택 관련 메서드 실습1](JS.assets/%EC%84%A0%ED%83%9D%20%EA%B4%80%EB%A0%A8%20%EB%A9%94%EC%84%9C%EB%93%9C%20%EC%8B%A4%EC%8A%B51.PNG)
    ![선택 관련 메서드 실습2](JS.assets/%EC%84%A0%ED%83%9D%20%EA%B4%80%EB%A0%A8%20%EB%A9%94%EC%84%9C%EB%93%9C%20%EC%8B%A4%EC%8A%B52.PNG)

- [참고] NodeList
  - index로만 각 항목에 접근 가능
  - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
  - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
- 조작 관련 메서드
  - 조작 관련 메서드(생성)
    - document.createElement(tagName)
      - 작성한 tagName의 HTML 요소를 생성하여 반환
  - 조작 관련 메서드(입력)
    - Node.innerText
      - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text)
      - 사람이 읽을 수 있는 요소만 남김
      - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨
  - 조작 관련 메서드(추가)
    - Node.appendChild()
      - 한 Node를 특정 부모 Node의 자식 NodeList중 마지막 자식으로 삽입
      - 한 번에 오직 하나의 Node만 추가할 수 있음
      - 추가된 Node 객체를 반환
      - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
  - 조작 관련 메서드(삭제)
    - Node.removeChild()
      - Dom에서 자식 Node를 제거
      - 제거된 Node를 반환
  - 실습
    ![조작 관련 메서드 실습1](JS.assets/%EC%A1%B0%EC%9E%91%20%EA%B4%80%EB%A0%A8%20%EB%A9%94%EC%84%9C%EB%93%9C%20%EC%8B%A4%EC%8A%B51.PNG)
    ![조작 관련 메서드 실습2](JS.assets/%EC%A1%B0%EC%9E%91%20%EA%B4%80%EB%A0%A8%20%EB%A9%94%EC%84%9C%EB%93%9C%20%EC%8B%A4%EC%8A%B52.PNG)