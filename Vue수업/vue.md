# Vue

### Front-end Development
- 개요
  - 우리가 앞으로 할 일은 JS를 이용한 Front-end 개발
  - Back-end 개발은 Django로 진행
  - Front-end 개발은 Vue.js 진행
  - Vue.js === JavaScript Front-end Framework
- Front-end Framework
  - Front-end(FE) 개발
    - 사용자에게 보여주는 화면 만들기
  - Web App(SPA)을 만들 때 사용하는 도구
    - SPA - Single Page Application
      - Web App과 함께 자주 등장할 용어
      - 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
      - SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
        - 어떻게 한 페이지로 모든 요청에 대응?
          - CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문
  - Web App이란?
    - 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
    - VIBE 웹 사이트 - 개발자 도구 - 디바이스 모드
    - 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 APP처럼 보이는 것
    - 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태
  - [참고] SSR(Server Side Rendering)이란?
    - 기존의 요청 처리 방식은 SSR
    - Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
    - 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행
    ![SSR1](Vue.assets/SSR1.PNG)
    ![SSR2](Vue.assets/SSR2.PNG)
  - CSR(Client Side REndering)이란?
    - 최초 한장의 HTML을 받아오는 것은 동일
      - 단, server로부터 최초로 받아오는 문서는 빈 html 문서
      ![CSR1](Vue.assets/CSR1.PNG)
      - 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
        1. 새로운 페이지를 서버에 AJAX로 요청
        2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
        3. JSON 데이터를 JS로 처리. DOM트리에 반영(렌더링)
      ![CSR2](Vue.assets/CSR2.PNG)
      ![CSR3](Vue.assets/CSR3.PNG)
  - 왜 CSR 방식을 사용하는가?
    1. 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨 
      == 클라이언트- 서버간 통신 즉, 트래픽 감소 
      == 트래픽이 감소한다 = 응답속도가 빨라진다
    2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
      - SNS에서 추천을 누를 때마다 첫 페이지로 돌아간다 = 끔찍한 APP
      - 요청이 자연스럽게 진행된다 = UX 향상
    3. BE와 FE의 작업 역역을 명확히 분리할 수 있음
      - 각자 맡은 역할을 명확이 분리한다 = 협업이 용이해짐
  - CSR은 만능일까?
    - 첫 구동시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
    - Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행하게 되면 잠깐의 로딩 시간이 필요
    - 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움
      - 서버가 제공하는 것은 텅 빈 HTML
      - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행
    - 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
  - [참고] SEO(Search Engine Optimization)
    - google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
    - 검색 = 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
    - 검색 엔진 = 웹 상에 존재하는 가능한 모든 정보들을 긁어모으는 방식으로 동작
      - 정보의 대상은 주로 HTML에 작성된 내용
      - JS가 실행된 이후의 결과를 확인하는 과정이 없음
    - 최근에는 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
      - SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전
    - 단, 단순 HTML만을 분석하는 것보다 몇 배의 리소스가 필요한 작업이기에 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결된 것은 아님
  - CSR vs SSR
    - CSR과 SSR은 흑과 백이 아님
      - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
    - SPA 서비스에서도 SSR을 지원하는 Framework이 발전하고 있음
      - Vue의 Nuxt.js
      - React의 Next.js
      - Angular Universal 등
  - 여러가지 Front-end Framework
    - Frone-end Framework == HTML + CSS + JS를 더 편하게 작업하기 위한 툴
      - React, Angular, Svelte, Vue 등
    ![2022 Front-end Framework 인기도](Vue.assets/2022%20Front-end%20Framework%20%EC%9D%B8%EA%B8%B0%EB%8F%84.PNG)
  - 프레임 워크는 더 쉽게 개발하기 위해 사용하는 것으로 꼭 사용하지 않아도 됨
  - 실제 Github는 Front-end Framework를 사용하지 않음
  - 하지만 대부분의 기업에서는 생산성과 협업을 위해 Framework를 사용해서 개발
- Vue 사용 이유
  - 쉽다, 입문자가 시작하기에 좋다
  - 구글의 Angular 개발자 출신 Evan You가 개발
    - Vue는 타 Framework에 비해 입문자가 시작하기에 좋은 Framework
    - Angular보다 가볍고, 간편하게 사용할 수 있는 Framework를 만들기 위해 퇴사
    - 2014년 Vue 발표
  - 구조가 매우 직관적
  - FE Framework를 빠르고 쉽게 학습하고 활용할 수 있음
  - 추후 필요하면 다른 FE Framework 학습시 빠르게 적응 가능
  ![Vue](Vue.assets/vue.PNG)
- Vue 없이 코드 작성하기
  - 입력 받은 값을 name 뒤에 출력하기
  - 02_html_only.html에서 진행
  ![Vue 없이 코드 작성하기1](Vue.assets/Vue%20%EC%97%86%EC%9D%B4%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B01.PNG)
  1. input tag 선택
  2. P tag 선택
  3. add EventListener 추가
  ![Vue 없이 코드 작성하기2](Vue.assets/Vue%20%EC%97%86%EC%9D%B4%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B02.PNG)
  - 입력 받은 데이터를 p tag에 추가하려고 한다면?
  - 기존에 가지고 있었던 text도 신경써야함
    - data를 관리하기 위한 추가 작업이 필요함
  ![Vue 없이 코드 작성하기3](Vue.assets/Vue%20%EC%97%86%EC%9D%B4%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B03.PNG)
- Vue CDN
  - Vue로 작업을 시작하기 위하여 CDN을 가져와야 함
  - Django == Python Web Framework
    - pip install
  - Vue === JS Front-end Framework
    - Bootstrap에서 사용하였던 CDN 방식 제공
  - Vue CDN을 위하여 Vue2 공식 문서 접속
    - https://v2.vuejs.org/
  1. Getting Started
  2. Installation
  3. Development version CDN 복사
  ![Vue2 공식문서](Vue.assets/Vue2%20%EA%B3%B5%EC%8B%9D%EB%AC%B8%EC%84%9C.PNG)
- Vue로 코드 작성하기
  - 입력 받은 값을 name 뒤에 출력하기
  - 03_html_vue.html에서 진행
  ![Vue로 코드 작성하기1](Vue.assets/Vue%EB%A1%9C%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B01.PNG)
    1. Vue CDN 가져오기
    2. Vue instance 생성
      - Vue instance - 1개의 Object
      - 정해진 속성명을 가진 Object
    3. el, data 설정
      - data에 관리할 속성 정의
    4. 선언적 렌더링 {{ }}
      - Vue data를 화면에 렌더링
  ![Vue로 코드 작성하기2](Vue.assets/Vue%EB%A1%9C%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B02.PNG)
  - [참고] Dev Tools 확인
    - Vue devtools에서 data 변경 -> DOM 반영
    - 눈에 보이는 화면을 조작하는 것이 아닌 Vue가 가진 data를 조작
    ![Dev Tools 확인](Vue.assets/Dev%20Tools%20%ED%99%95%EC%9D%B8.PNG)
  4. input tag에 v-model 작성
    - input에 값 입력 -> Vue data 반영
    - Vue data -> Dom 반영
  ![Vue로 코드 작성하기3](Vue.assets/Vue%EB%A1%9C%20%EC%BD%94%EB%93%9C%20%EC%9E%91%EC%84%B1%ED%95%98%EA%B8%B03.PNG)
- Facebook 예시
  - 한명의 유저가 이름을 변경한다면 화면에서 조작해야할 영역이 매우 많음
  ![Facebook 예시](Vue.assets/facebook%20%EC%98%88%EC%8B%9C.PNG)
  - Vanilla JS만으로 모든 데이터를 조작하면 불필요한 코드의 반복이 일어남
  ![Facebook 예시2](Vue.assets/facebook%20%EC%98%88%EC%8B%9C2.PNG)
  - Vue를 통해 데이터를 관리한다면 변경사항도 한번에 반영 가능
  ![Facebook 예시3](Vue.assets/facebook%20%EC%98%88%EC%8B%9C3.PNG)

### Vue2 vs Vue3
- Vue3
  - 2022년 2월부터 vue 프레임워크의 기본 버전이 3버전으로 전환
  - 대체적인 설정들이 Vue3을 기본으로 적용되어있음
    - ex) 공식문서, CDN, npm 등
- Vue2
  - 여전히 vue2가 많이 사용됨(legacy code)
  - 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변
  - 안정적인 측면에서는 아직 vue2가 우세한 편

### Vue instance
- MVVM Pattern
  - 소프트웨어 아키텍처 패턴의 일종
  - 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
  ![MVVM Pattern1](Vue.assets/MVVM%20Pattern.PNG)
  ![MVVM Pattern2](Vue.assets/MVVM%20Pattern2.PNG)
  - View - 우리 눈에 보이는 부분 = DOM
  - Model - 실제 데이터 = JSON
  - View Model (Vue)
    - View를 위한 Model
    - View와 연결(binding)되어 Action을 주고 받음
    - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨
  - 정리
    - MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴
    - View는 Model을 몰라요, Model도 View를 몰라요 (독립성 증가, 적은 의존성)
      - DOM은 Data를 몰라요, Data도 DOM을 몰라요
    - View 에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다
    