# 웹

## 웹 사이트의 구성 요소
- 웹 사이트란 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹 페이지로 이동하는 '링크'들이 있음. '링크'를 통해 여러 웹 페이지를 연결하는 것을 웹 사이트라고 함.
```
HTML -> 구조 담당
CSS -> 표현 담당
Javascript -> 동작 담당
```
[웹사이트의 구성요소 살펴보기](https://html-css-js.com)

## 웹 사이트와 브라우저
- 웹사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
- 해결책으로 웹 표준이 등장 
```
브라우저 -> msword 한컴문서 프로그램과 비슷
(HTML)문서 -> .hwp, .doc 파일과 비슷
```

## 웹 표준
- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)
- 팀 버너스리에서 만듦
- 예상하지 못한 결과 -> 브라우저의 문제일듯
[브라우저별 호환성 체크](https://caniuse.com)

## HTML(Hyper Text Markup Language)
- Naver 사이트에 접속해서 개발자 도구를 활용해 CSS를 삭제한다면?
    - HTML만 남은 웹사이트 확인 가능
- **웹 페이지를 작성(구조화)하기 위한 언어**
- .html(HTML파일)
#### Hyper Text
- 팀 버너스리의 이론(문서와 문서를 이을 수 있는 기술)
- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
#### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - HTML, Markdown 등
![마크업 안썼을 때](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EB%A7%88%ED%81%AC%EC%97%85%20%EC%95%88%EC%8D%BC%EC%9D%84%20%EB%95%8C.JPG?raw=true)
![마크업 썼을 때](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EB%A7%88%ED%81%AC%EC%97%85%20%EC%8D%BC%EC%9D%84%20%EB%95%8C.JPG?raw=true)
![마크업 쓰는 방법](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EB%A7%88%ED%81%AC%EC%97%85%20%EC%93%B0%EB%8A%94%20%EB%B0%A9%EB%B2%95.JPG?raw=true)

### HTML 기본 구조
- html : 문서의 최상위(root)요소
- head : 문서 메타데이터 요소
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
    - 실제 화면 구성과 관련된 내용

- head 예시
    ```
    <title> : 브라우저 상단 타이틀
    <meta> : 문서 레벨 메타데이터 요소
    <link> : 외부 리소스 연결 요소(CSS파일, favicon 등)
    <script> : 스크립트 요소(Javascript 파일/코드)
    <style> : CSS 직접 작성
    Open Graph Protocol
    - 메타 데이터를 표현하는 새로운 규약
        - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
        - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
    ```

### 정리
- html - 태그를 이용하여 구조를 만들어 브라우저를 실행하는 문서를 의미

---

## 요소
- HTML의 요소는 태그와 내용(contents)로 구성되어 있다.
```
<h1>contents</h1>
<h1>은 (여는/시작)태그
</h1>은 (닫는/종료)태그
```
- HTML의 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
        - br, hr, img, input, link, meta
    - 요소는 중첩(nested)될 수 있음 - 태그안에 또다른 태그 사용 가능
        - 요소의 중첩을 통해 하나의 문서를 구조화
        - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
            - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음
- HTML with 개발자 도구
    - elements : 해당 요소의 HTML 태그
        ![HTML 개발자 도구](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/HTML%20%EA%B0%9C%EB%B0%9C%EC%9E%90%20%EB%8F%84%EA%B5%AC.JPG?raw=true)
        - 인터넷 화면에서 우클릭 후 검사 누르면 나오는 화면
        - 빨간 동그라미 있는 것 누르면 원하는 요소를 선택할 수 있음(복잡한 형태의 경우 Elements에서 HTML 구조를 추가 탐색)

## 속성(attribute)
- 태그의 디테일한 정보를 제공하기 위해 사용
- ```<a 속성명="속성값"><\a>``` 이런 식으로 사용, 공백은 쓰면 안되고, 속성값은 ""(쌍따옴표)를 사용해야한다.
- 태그별로 사용할 수 있는 속성은 다르다
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음
- HTML Global Attribute
    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)
        - id : 문서 전체에서 유일한 고유 식별자 지정
        - class : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
        - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
        - style : inline 스타일
        - title : 요소에 대한 추가 정보 지정
        - tabindex : 요소의 탭 순서
- 주석은 \<!-- 내용 --> 이렇게 사용 (Ctrl + /으로 주로 사용)

## 시맨틱 태그
- HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
    - 예를 들어 h1 태그는 "이 페이지에서 최상위 제목"인 텍스트를 감싸는 역할(또는 의미)을 나타냄
- Non semantic 요소로는 div, span 등이 있으며 a, form, table 태그들도 시맨틱 태그로 볼 수 있음
- HTML5에서는 기존에 단순히 콘텐츠의 구획을 나타내기 위해 사용한 div태그를 대체하여 사용하기 위해 의미론적 요소를 담은 태그들이 추가됨
- 대표적인 시맨틱 태그 목록
    - header : 문서 전체나 섹션의 헤더(머리말 부분)
    - nav : 내비게이션
    - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer : 문서 전체나 섹션의 푸터(마지막 부분)
- 시맨틱 태그를 사용 해야 하는 이유
![시맨틱 태그](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EC%8B%9C%EB%A7%A8%ED%8B%B1%20%ED%83%9C%EA%B7%B8.JPG?raw=true)
    - 의미론적 마크업
        - 개발자 및 사용자 뿐만 아니라 **검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현**
        - 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
        - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
        - 검색 엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함

### 텍스트로 작성된 코드가 웹사이트가 되는 과정
- 렌더링(Rendering)
    - 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정
- DOM(Document Object Model)트리
    - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
        - HTML 문서에 대한 모델을 구성함
        - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공
    ![DOM트리](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/DOM%ED%8A%B8%EB%A6%AC.JPG?raw=true)

### HTML 문서 구조화
- 인라인 / 블록 요소
    - HTML 요소는 크게 인라인 / 블록 요소로 나눔
    - 인라인 요소는 글자처럼 취급
    - 블록 요소는 한 줄 모두 사용
- 텍스트 요소
    ![텍스트 요소](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EC%9A%94%EC%86%8C.JPG?raw=true)
    ![텍스트 요소 예시](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EC%9A%94%EC%86%8C%20%EC%98%88%EC%8B%9C.JPG?raw=true)
- 그룹 컨텐츠
    ![그룹 컨텐츠](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EA%B7%B8%EB%A3%B9%20%EC%BB%A8%ED%85%90%EC%B8%A0.JPG?raw=true)
    ![그룹 컨텐츠 예시](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EA%B7%B8%EB%A3%B9%20%EC%BB%A8%ED%85%90%EC%B8%A0%20%EC%98%88%EC%8B%9C.JPG?raw=true)

---

## form
- \<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- \<form>기본 속성
    - action : form을 처리할 서버의 URL(데이터를 보낼 곳)
    - method : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
    - enctype : method가 post인 경우 데이터의 유형
        - application/x-www-form-urlencoded : 기본값
        - multipart/form-data : 파일 전송시(input type이 file인 경우)
        - text/plain : HTML5 디버깅 용(잘 사용안함)

## input
- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- \<input> 대표적인 속성
    - name : form control에 적용되는 이름(이름/값 페어로 전송됨)
    - value : form control에 적용되는 값(이름/값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disabled 등

## input lable
- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치)환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면 리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
- \<input>에 id 속성을, \<label>에는 for 속성을 활용하여 상호 연관을 시킴
[inputtest vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/inputtest.html)

## input 유형 - 일반
- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
    - text : 일반 텍스트 입력
    - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    - email : 이메일 형식이 아닌 경우 form 제출 불가
    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    - file : accept 속성을 활용하여 파일 타입 지정 가능

## input 유형 - 항목 중 선택
- 일반적으로 label태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대하여 name을 지정하고 선택된 항목에 대한 value를 지정해야함
    - checkbox : 다중 선택
    - radio : 단일 선택
    
## input 유형 - 기타
- 다양한 종류의 input을 위한 picker를 제공
    - color : color picker
    - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    - hidden : 사용자에게 보이지 않는 input

## input 유형 - 종합
- \<input>요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
[input유형](https://developer.mozilla.org/ko/docs/Web/HTML/Element/input)

## 마크업 해보기
- 스타일링은 CSS학습 후 진행 예정
- 구조
    - 1. header
    - 2. section
    - 3. footer

[markuptest vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/markuptest.html)

---
---

## CSS(cascading Style Sheets)
- 스타일을 지정하기 위한 언어 - 선택하고, 스타일을 지정한다.
- css 구문
    ```
    h1(선택자) {
        color: blue;(선언)
        font-size(속성): 15px(값);
    }
    ```
    - 모든 h1 태그는 위 스타일대로 보여줌
- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(property) : 어떤 스타일 기능을 변경할지 결정
    - 값(value) : 어떻게 스타일 기능을 변경할지 결정
- CSS 정의 방법
    - 인라인(inline)
        - 해당 태그에 직접 style 속성을 활용
        - 인라인을 쓰게 되면 실수가 잦아짐(중복도 있을 것이고, 찾기가 어려움)
        ```html
        <body>
            <h1 style="color: red; font-size>: 20px;">Hello<\h1>
        </body>
        <!-- 이런식으로 표현  -->
        ```
    - 내부참조(emvedding) - \<style>
        - 내부 참조를 쓰게 되면 코드가 너무 길어짐
        ```html
        <head> <!-- 안에 style 하고 탭 -->
            <style>
                h1 {
                    color: blue;
                    font-size>: 100px;
                }
            </style>
        </head>
        <!-- 이런식으로 표현 -->
        ```
    - 외부참조(link file) - 분리된 CSS 파일
        - 가장 많이 쓰는 방식
        ```html
        <!-- css파일 생성 후  -->
        <head>
            <link rel="stylesheet" href="a.css">
        </head>

        <!-- a.css 파일은 아래와 같은 형태 -->
        h1 {
            color: blue;
            font-size: 20px;
        }

        <!-- 이후 <title> 밑에 link 이후 탭 누르면 href=""에 css파일 경로 입력하면 참조되어 변경됨 -->
        ```
    ![외부참조](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EC%99%B8%EB%B6%80%20%EC%B0%B8%EC%A1%B0.JPG?raw=true)
---

- CSS 시작하기 전에 - 주로 활용하는 속성 위주로 기억하자.

- CSS with 개발자 도구
    - styles : 해당 요소에 선언된 모든 CSS
    - computed : 해당 요소에 최종 계산된 CSS
    ![CSS 개발자 도구](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/CSS%20%EA%B0%9C%EB%B0%9C%EC%9E%90%20%EB%8F%84%EA%B5%AC.JPG?raw=true)

## CSS Selectors(선택자)
- 선택자 유형
    - 기본 선택자
        - 전체 선택자, 요소 선택자
        - 클래스 선택자, 아이디 선택자, 속성 선택자
    - 결합자(Combinators)
        - 자손 결합자, 자식 결합자
            - 이 위의 것들이 거의 80% (아래도 조금은 씀)
        - 일반 형제 결합자, 인접 형제 결합자
    - 의사 클래스/ 요소(Pseudo Class)
        - 링크, 동적 의사 클래스
        - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

- 선택자 with 개발자 도구
![선택자 개발자 도구](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EC%84%A0%ED%83%9D%EC%9E%90%20%EA%B0%9C%EB%B0%9C%EC%9E%90%20%EB%8F%84%EA%B5%AC.JPG?raw=true)

[selecotrstest vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/selectorstest.html)

### CSS 선택자 정리
- 요소 선택자
    - HTML 태그를 직접 선택
    - 태그 -> 서울사람
- 클래스(class) 선택자 class = ""로 지정
    - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
    - 최씨 김시 이씨 등
- 아이디(id) 선택자
    - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용
    - 여러번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
    - 지웅, 근우 등 이름

### CSS 적용 우선순위
- 범위가 좁을수록 강하다
    /* vs 태그 - 태그가 우선순위
    아이디 vs 태그 - 아이디가 우선순위
- CSS에서 나중에 입력된 것이 우선순위
- 1. 중요도(Importance) - 사용시 주의
    - !important
- 2. 우선 순위(Specificity)
    - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
- 3. CSS 파일 로딩 순서
![CSS적용 우선순위](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/CSS%EC%A0%81%EC%9A%A9%20%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84.JPG?raw=true)

### CSS 상속
- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성(프로퍼티)중에는 상속이 되는 것과 되지 않는 것들이 있다.
    - 상속 되는것 예시
        - Text 관련 요소(font, color, text-align), opacity, visibility (글자 관련)
    - 상속 되지 않는것 예시
        - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position관련 요소(position, top/right/bottom/left,z-index)등 (여백, 레이아웃 관련)

### CSS 기본 스타일
- 크기단위
    - px (픽셀)
        - 모니터 해상도의 한 화소인 '픽셀'기준
        - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
    - %
        - 백분율 단위
        - 가변적인 레이아웃에서 자주 사용
    - em 
        - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
        - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
        - 부모의 몇 배 등
    - rem
        - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
        - 최상위 요소(thml)의 사이즈를 기준으로 배수단위를 가짐
        - 기본글자 바탕으로 몇 배 등
[csstyle vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/cssstyle.html)

- 크기 단위(viewport)
    - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
    - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
    - vw(가로), vh(세로), vmin(최저), vmax(최고)
    - px는 브라우저의 크기를 변경해도 그대로
    - vw는 브라우저의 크기에 따라 크기가 변함

- 색상단위
    - 색상 키워드(backgtound-color: red;)
        - 대소문자를 구분하지 않음
        - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
    - RGB 색상(backgtound-color: rgb(0, 255, 0);)
        - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
        - '#' + 16진수 표기법
        - rgb() 함수형 표기법
    - HSL 색상(backgtound-color: rhsl(0, 100%, 50%);)
        - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
    - a는 alpha(투명도)
    ![색상 단위](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EC%83%89%EC%83%81%20%EB%8B%A8%EC%9C%84.JPG?raw=true)
    파란 체크를 많이 씀

- CSS 문서 표현 - 추후에 하나씩
    - 텍스트
        - 서체(font-family), 서체스타일(font-style, font-weight 등)
        - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
    - 컬러(color), 배경(background-image, background-color)
    - 기타 HTML 태그별 스타일링
        - 목록(li), 표(table)

### 결합자(Combicators)
- 자손 결합자(공백)
    - selectorA 하위의 모든 selectorB 요소
- 자식 결합자(>)
    - selectorA 바로 아래의 selectorB 요소
- 일반 형제 결합자(~)
    - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자(+)
    - selectorA 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택
(자손과 자식만 주로 쓰임)

---

### CSS Box model
#### CSS 원칙 1
- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

- Box model
    - 모든 HTML요소는 box형태로 되어있음
    - 하나의 박스는 네 부분(영역)으로 이루어짐
        - margin
            - 테두리 바깥의 외부 여백 배경색을 지정할 수 없다.
        - border
            - 테두리 영역
        - padding
            - 테두리 안쪽의 내부 여백 
            - 요소에 적용된 배경색, 이미지는 padding까지 적용
        - content
            - 글이나 이미지 등 요소의 실제 내용
    - box model 구성은 상 우 하 좌 순서
    (shorthand margin/padding)
    ![shorthand](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/shorthand.JPG?raw=true)
    - 왼쪽부터 상하죄우, 상하 좌우, 상 좌우 하, 상 우 하 좌 순서
    (shorthand border)
    ![shorthand border](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/shorthand%20border.JPG?raw=true)
    - width, style, color 순서로 씀
    [boxmodel vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/boxmodel.html)
    [boxmodel2 vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/boxmodel2.html)

    - box-sizing
        - 기본적으로 모든 요소의 box-sizing은 content-box
            - Padding을 제외한 순수 contents 영역만을 box로 지정
        - 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
            - 그 경우 box-sizing을 border-box로 설정

### CSS Display
#### CSS 원칙 2
- 모든 요소는 네모(박스모델)이고, 좌측 상단에 배치
- Display에 따라 크기와 배치가 달라진다.
- 대표적으로 활용되는 display
    - display : block - 블록으로 취급(한 줄 모두 사용)
        - 줄 바꿈이 일어나는 요소
        - 화면 크기 전체의 가로 폭을 차지한다.
        - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
        - block의 기본 너비는 가질 수 있는 너비의 100%
        - 너비를 가질 수 없다면 자동으로 부여되는 margin
    - display : inline - 글자로 취급
        - 줄 바꿈이 일어나지 않는 행의 일부 요소
        - content 너비만큼 가로 폭을 차지한다.
        - width, height, margin-top, margin-bottom을 지정할 수 없다.
        - 상하 여백은 line-height로 지정한다.
        - inline의 기본 너비는 컨텐츠 영역만큼
    ![속성에 따른 수평 정렬](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/%EC%86%8D%EC%84%B1%EC%97%90%20%EB%94%B0%EB%A5%B8%20%EC%88%98%ED%8F%89%20%EC%A0%95%EB%A0%AC.JPG?raw=true)

- 블록 레벨 요소와 인라인 레벨 요소
    - 블록 레벨 요소와 인라인 레벨 요소 구분(HTML 4.1까지)
    - 대표적인 블록 레벨 요소
        - div / ul, ol, li / p / hr / form 등
    - 대표적인 인라인 레벨 요소
        - span / a / img / input, label / b, em, i, strong 등

- display
    - display: inline-block
        - block과 inline 레벨 요소의 특징을 모두 가짐
        - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
    - display: none
        - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
        - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
        - 숨겼다가 보여줄 일이 있으면 hidden을, 없으면 none을 씀
    - 이외 다양한 display 속성은 [참고 사이트](https://developer.mozilla.org/ko/docs/Web/CSS/display)
    [displaytest vs코드에서 해보기](https://github.com/Aden-Jang/TIL/blob/7beec0f540020edd7f607ebfee5ae2c93c300b6f/%EC%9B%B9%EC%88%98%EC%97%85/displaytest.html)

    
### CSS position
- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
-  아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
![static](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/static.JPG?raw=true)
1. relative : 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)
    ![relative](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/relative.JPG?raw=true)
2. absolute : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - static이 아닌 가장 가까이 있는 부모/ 조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)
    - 특정 영역 위에 존재 - CSS 기본 원칙인 좌측 상단에 배치되지 않고, 부모를 기준으로 가운데 위치
    ![absolute](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/absolute.JPG?raw=true)
![absolute vs relarive](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/absolute%20vs%20relative.JPG?raw=true)
3. fixed : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계 없이 viewport를 기준으로 이동
        - 스크롤 시에도 항상 같은 곳에 위치함
    - 브라우저 기준으로 위치 - CSS 기본 원칙인 좌측상단에 배치되지 않음, 브라우저를 기준으로 우측 하단에 위치
    ![fixed](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/fixed.JPG?raw=true)
4. sticky : 스크롤에 따라 static -> fixed로 변경
    - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성
    ![sticky](https://github.com/Aden-Jang/TIL/blob/master/%EC%9B%B9%20%EC%88%98%EC%97%85/web.assets/sticky.JPG?raw=true)

## CSS 원칙 정리
- CSS 원칙 1, 2 : Normal flow
    - 모든 요소는 네모(박스모델), 좌측 상단에 배치
    - display에 따라 크기와 배치가 달라짐
- CSS 원칙 3
    - position으로 위치의 기준을 변경
        - relative : 본인의 원래 위치
        - absolute : 특정 부모의 위치
        - fixed : 화면의 위치
        - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경
