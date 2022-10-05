### Database
- 정의
    - 체계화된 데이터의 모임
    - 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
    - 검색, 구조화 같은 작업을 보다 쉽게 하기 위한 조직화된 데이터를 수집하는 저장 시스템
        - 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
        - 즉 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화 하여 기억시켜 놓은 자료의 집합체
    - 이러한 Dtatbase를 조작하는 프로그램 = DBMS(Database Management System)
        - Oracle, MySQL, SQLite 등이 DBMS
        - DBMS에서 Database를 조작하기 위해 사용하는 언어를 SQL이라 함
    - 웹 개발에서 대부분의 데이터베이스는 관계형 데이터베이스 관리시스템(RDBMS)을 사용하여 SQL로 데이터와 프로그래밍을 구성

### RDB
- Realtional Database(관계형 데이터베이스)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계을 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작
- 기본 구조
    1. 스키마(Schema)
        - 테이블의 구조(Structure)
        - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것
        ![스키마](DB.assets/%EC%8A%A4%ED%82%A4%EB%A7%88.JPG)
    2. 테이블(Table)
        - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
        - 관계(Relation)라고도 부름
        ![테이블](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94.JPG)
        1. 필드(field)
            - 속성, 컬럼(Column)
        2. 레코드(record)
            - 튜플, 행(Row)
            - 테이블의 데이터는 레코드에 저장됨
        3. 기본 키(Primary KEy, PK)
            - 각 레코드의 고유한 값
                - 각각의 데이터를 구분할 수 있는 고윳값
            - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
            - 데이터베이스 관리 및 테이블간 관계 설정 시 주요하게 활용 됨
            ![기본키](DB.assets/%EA%B8%B0%EB%B3%B8%20%ED%82%A4.JPG)
- 장점
    - 데이터를 직관적으로 표현할 수 있음
    - 관련한 각 데이터에 쉽게 접근할 수 있음
    - 대량의 데이터도 효율적으로 관리 가능
- RDBMS
    - Relawtional Database Management System(관계형 데이터베이스 관리 시스템)
    - 관계형 데이터베이스를 만들고 업데이트하고 관리하는데 사용하는 프로그램
    - 예시
        - SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등
    - SQLite
        - 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
        - 안드로이드, iOS, macOS에 기본적으로 탑재되어 있으며 임베디드 소프트웨어에서도 많이 활용됨
        - 오픈 소스 프로젝트이기 때문에 자유롭게 사용 가능

        - 단점
            - 대규모 동시 처리 작업에는 적합하지 않음
            - 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음
        - 사용 이유
            - 어떤 환경에서나 실행 가능한 호환성
            - 데이터 타입이 비교적 적고 강하지 않기 때문에 유연한 학습 환경 제공
            - Django Framework의 기본 데이터베이스

### SQL
- Structured Query Language
- RDBMS의 데이터를 관리하기 위해 설계된 ```특수 목적의 프로그래밍 언어```
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
- 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음
- 정리
    - SQL은 ```데이터베이스와 상호작용하는 방법```
    - 따라서 SQL을 배우면서 데이터베이스의 동작원리 또한 익힐 수 있음

### SQL Commands
- 종류
    1. DDL(Data Definition Language) - 데이터 정의 언어
        - 관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정, 삭제)하기 위한 명령어
        - CREATE, DROP, ALTER
    2. DML(Data Manipulation Language) - 데이터 조작 언어
        - 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어
        - INSERT, SELECT, UPDATE, DELETE
    3. DCL(Data Control Language) - 데이터 제어 언어
        - 데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어
        - GRANT, REVOKE, COMMIT, ROLLBACK
        - **SQLite는 파일로 관리되는 DB이기 때문에 SQL을 이용한 접근 제한이 아닌 운영체제의 파일 접근 권한으로만 제어가능하여 DCL은 지원하지 않아 생략**

### SQL Syntax
![SQL Syntax예](DB.assets/sql%20syntax%EC%98%88.JPG)
- 모든 SQL문(statement)는 SELECT, INSERT, UPDATE등과 같은 키워드로 시작하고, 하나의 statement는 ```세미콜론(;)```으로 끝남
    - 세미콜론은 각 SQL문을 구분하는 표준 방법
- SQL 키워드는 대소문자를 구분하지 않음
    - 즉, SELECT와 select는 SQL문에서 동일한 의미
    - 하지만 대문자로 작성하는 것을 권장
- SQL에 대한 세부적인 문법 사항들은 이어지는 DDL, DML을 진행하며 익혀볼 것

- [참고] Statement & Clause
    - Statement(문)
        - 독립적으로 실행할 수 있는 완전한 코드 조각
        - statement는 clause로 구성됨
    - Clause(절)
        - statement의 하위 단위
    ![statement](DB.assets/statement.JPG)
    - SELECT statement라 부름
    - 이 statement는 다음과 같이 2개의 cllause로 구성됨
        1. SELECT column_name
        2. FROM table_name

### DDL
- 개요
    - Data definition
    - SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법을 학습
    - DDL은 테이블 구조를 관리
        - CREATE(생성), ALTER(수정), DROP(삭제)
- CREATE TABLE statement
    - Create a new tablein the database
    - 데이터베이스에 새 테이블을 만듦
    ![새 테이블 생성](DB.assets/%EC%83%88%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%EC%83%9D%EC%84%B1.JPG)
    - 실습
        - contacts 테이블 생성
        ![contacts 테이블 생성](DB.assets/contacts%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%EC%83%9D%EC%84%B1.JPG)
        - Query 실행하기
            - 실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼
            -> Run Selected Query 선택
            - 명령문을 모두 선택할 필요 없으며, 실행하고자 하는 명령문 안에 커서가 올라가 있으면 가능
            ![쿼리 실행](DB.assets/%EC%BF%BC%EB%A6%AC%20%EC%8B%A4%ED%96%89.JPG)
        - 쿼리 실행 후 테이블 및 스키마 확인
        ![쿼리 실행 후 테이블 및 스키마 확인](DB.assets/%EC%BF%BC%EB%A6%AC%20%EC%8B%A4%ED%96%89%20%ED%9B%84%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%EB%B0%8F%20%EC%8A%A4%ED%82%A4%EB%A7%88%20%ED%99%95%EC%9D%B8.JPG)
        - id 컬럼은 우리가 직접 기본 키 역할의 컬럼을 정의하지 않으면 자동으로 ```rowid```라는 컬럼으로 만들어짐
        - rowid에 대한 자세한 사항은 뒤에서 다룸
        - 먼저 테이블을 생성하면서 작성한 ```데이터 타입```과 ```제약조건```을 알아본다.

### SQLite Data Types
- 종류
    1. NULL
        - NULL value
        - 정보가 없거나 알 수 없음을 의미(missing information or unknown)
    2. INTEGER
        - 정수
        - 크기에 따라 0, 1, 2, 3, 4, 5, 6 또는 8바이트와 같은 가변 크기를 가짐
    3. REAL
        - 실수
        - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
    4. TEXT
        - 문자 데이터
    5. BLOB(Binary Large Object)
        - 입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
        - 바이너리 등 멀티미디어 파일
        - 예시
            - 이미지 데이터
    - [참고] Boolean type
        - SQLite에는 별도의 Boolean 타입이 없음
        - 대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨
    - [참고] Date & Time Datatype
        - SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없음
        - 대신 SQLite의 built-in "Date And Time Functions"으로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음
        - https://www.sqlite.org/lang_datefunc.html
    - [참고] Binary Data
        - 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일
        - 기본적으로 컴퓨터의 모든 데이터는 binary data
            - 다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것
- SQLite는 다음 규칙을 기반으로 데이터 타입 결정
    - 값에 둘러싸는 따옴표와 소수점 또는 지수가 없으면 - INTEGER
    - 값이 작은 따움표나 큰 따옴표로 묶이면 - TEXT
    - 값에 따옴표나 소수점, 지수가 없으면 - REAL
    - 값이 따옴표 없이 NULL이면 - NULL
- SQLite Datatypes 특징
    - SQLite는 다른 모든 SQL데이터베이스 엔진(MySQL, PostgreSQL등)의 정적이고 엄격한 타입(static, rigid typing)이 아닌 ```동적 타입 시스템(dynamic type system)```을 사용
        - 컬럼에 선언된 데이터 타입에 의해서가 아니라 ```컬럼에 저장된 값에 따라 데이터 타입이 결정```됨
    - 또한 테이블을 생성할 때 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨
        - 예를 들면 동일한 컬럼에 정수 1을 넣을 경우 INTEGER로 타입이 지전되고, 문자 '1'을 넣을 경우는 TEXT 타입으로 지정됨
        - 이러한 SQLite의 동적 타입 시스템을 사용하면 기존의 엄격하게 타입이 지정된 데이터베이스에서는 불가능한 작업을 유연하게 수행할 수 있음
        - 게다가 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동한다는 점
        - 다만 이는 다른 데이터베이스와의 호환성 문제가 있기 때문에 테이블 생성 시 ```데이터 타입을 지정하는 것을 권장```
    - 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환
        - 예를 들어 TEXT 타입 컬럼에 정수 1을 저장할 경우 문자 타입의 '1'로 저장됨
        - 허용 가능한 타입 변환은 다음과 같음
        ![허용 가능한 타입 변환](DB.assets/%ED%97%88%EC%9A%A9%20%EA%B0%80%EB%8A%A5%ED%95%9C%20%ED%83%80%EC%9E%85%20%EB%B3%80%ED%99%98.JPG)
    - [참고] static, rigid typing 데이터 베이스
        - statically, rigidly typed databases라고도 부름
        - 저장되는 값의 데이터 타입은 컬럼에 선언된 데이터 타입에 의해 결정된다.
        - 동작 예시
            ![static, rigid typing 데이터 베이스 동작 예시](DB.assets/static%2C%20rigid%20typing%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%8F%99%EC%9E%91%20%EC%98%88%EC%8B%9C.JPG)
        - 만약 a컬럼에 '123', b컬럼에 456 데이터를 삽입하려는 경우 삽입을 수행하기 전에 문자열 '123'을 정수 123으로 변환하고, 정수 456을 문자열 '456'으로 변환
    - Type Affinity
        - "타입 선호도"
        - 특정 컬럼에 저장된 데이터에 권장되는 타입
        - 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
            1. INTEGER
            2. TEXT
            3. BLOB
            4. REAL
            5. NUMERIC
            ![Type Affinity](DB.assets/Type%20Affinity.JPG)
        - 타입 선호도 존재 이유
            - 다른 데이터베이스 엔진 간의 ```호환성```을 최대화
            - 정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

### Constraints
- 개요
    - "제약 조건"
    - 입력하는 자료에 대해 제약을 정함
    - 제약에 맞지 않다면 입력이 거부됨
    - 사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
- 데이터 무결성
    - 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
        - 무결성이란 데이터의 정확성, 일관성을 나타냄
    - 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적
- Constraints 종류
    1. NOT NULL
        - 컬럼이 NULL값을 허용하지 않도록 지정
        - 기본적으로 테이블의 모든 컬럼은 NOT NULL제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL값을 허용함
    2. UNIQUE
        - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함
    3. PRIMARY KEY
        - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
        - 각 테이블에는 하나의 기본 키만 있음
        - 암시적으로 NOT NULL제약 조건이 포함되어 있음
        ![PRIMARY KEY](DB.assets/constraints%20primary%20key.JPG)
        ```주의) INTEGER 타입에만 사용 가능(INT, BIGINT 등은 불가능)```
    4. AUTOINCREMENT
        - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
        - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
        ![AUTOINCREMENT](DB.assets/constraints%20autoincrement.JPG)
        - Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건
    5. 그 외 기타 Constraints
- rowid의 특징
    - 테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
    - 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
    - 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
        - 값은 1에서 시작
        - 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SLQite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당(AUTOINCREMENT와 관계 없이)
    - 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)이 됨
        - 즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가능
    - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아 사용(Limits in SQLite - https://www.sqlite.org/limits.html)
    - 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL에러가 발생
        - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행애서 rowid 값을 재사용하려고 시도

### ALTER TABLE
- Modify the structure of an existing table.
- 기존 테이블의 구조를 수정(변경)
- SQLite의 ALTER TABEL문을 사용하면 기존 테이블을 다음과 같이 변경할 수 있음
    1. Rename a table
    2. Rename a column
    3. Add a new column to a table
    4. Delete a column
- https://www.sqlite.org/lang_altertable.html
- ALTER TABLE statement 예시
    ![ALTER TABLE statement 예시](DB.assets/ALTER%20TABLE%20statement%20%EC%98%88%EC%8B%9C.JPG)
    1. ALTER TABLE RENAME
        - Rename a table(테이블 명 변경)
        - 작성 및 결과 확인
        ![ALTER TABLE RENAME](DB.assets/ALTER%20TABLE%20RENAME.JPG)
    2. ALTER TABLE
        - Rename a column(컬럼명 변경)
        - 작성 및 결과 확인
            ![ALTER TABLE](DB.assets/ALTER%20TABLE.JPG)
    3. ALTER TABLE ADD COLUMN
        - Add a new column to a table(새 컬럼 추가)
        - 작성 및 결과 확인
        ![ALTER TABLE ADD COLUMN](DB.assets/ALTER%20TABLE%20ADD%20COLUMN.JPG)
        - 현재 과정에서는 일어나지 않지만 만약 테이블에 기존 데이터가 있을 경우 다음과 같은 에러가 발생
            ![ALTER TABLE ADD COLUMN2](DB.assets/ALTER%20TABLE%20ADD%20COLUMN2.JPG)
        - 이전에 이미 저장된 데이터들은 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨
        - 그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 기본값 없이는 추가될 수 없다는 에러가 발생한 것
        - 다음과 같이 ```DEFAULT``` 제약 조건을 사용하여 해결할 수 있음
            ![ALTER TABLE ADD COLUMN3](DB.assets/ALTER%20TABLE%20ADD%20COLUMN3.JPG)
        - 이렇게 하면 address컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼값은 'no address'가 됨
        - [참고] DEFAULT 제약조건
            - column 제약조건 중 하나
            - 데이터를 추가할 때 값을 생략할 시에 기본 값을 설정함
            - https://www.sqlite.org/syntax/column-constraint.html
    4. ALTER TABLE DROP COLUMN
        - Delete a column(컬럼 삭제)
        - 작성 및 결과 확인
        ![ALTER TABLE DROP COLUMN](DB.assets/ALTER%20TABLE%20DROP%20COLUMN.JPG)
        - 단, 삭제하지 못하는 경우가 있음
            - 컬럼이 다른 부분에서 참조되는 경우
                - FOREIGN KEY(외래 키)제약조건에서 사용되는 경우
            - PRYMARY KEY인 경우
            - UNIQUE 제약조건이 있는 경우
            ![ALTER TABLE DROP COLUMN2](DB.assets/ALTER%20TABLE%20DROP%20COLUMN2.JPG)

### DROP TABLE
- Remove a table from the database
- 데이터베이스에서 테이블을 제거
![데이터베이스에서 테이블을 제거](DB.assets/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%97%90%EC%84%9C%20%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9D%84%20%EC%A0%9C%EA%B1%B0.JPG)
- 존재하지 않는 테이블을 제거하면 SQLite에서 오류가 발생
![존재하지 않는 테이블을 제거 오류](DB.assets/%EC%A1%B4%EC%9E%AC%ED%95%98%EC%A7%80%20%EC%95%8A%EB%8A%94%20%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9D%84%20%EC%A0%9C%EA%B1%B0%20%EC%98%A4%EB%A5%98.JPG)
- DROP TABLE 실습
    - 작성 및 결과 확인
    ![DROP TABLE](DB.assets/DROP%20TABLE.JPG)
- 특징
    - 한 번에 하나의 테이블만 삭제할 수 있음
    - 여러 테이블을 제거하려면 여러 DROP TABLE문을 실행해야 함
    - DROP TABLE문은 실행 취소하거나 복구할 수 없음
        - 따라서 각별히 주의하여 수행해야 한다.

#### DDL 정리
- 데이터 정의 언어
- CREATE TABLE
    - 데이터 타입과 제약조건
- ALTER TABLE
    - RENAME
    - RENAME COLUMN
    - ADD COLUMN
    - DROP COLUMN
- DROP TABLE

### DML
- 개요
    - DML을 통해 데이터를 조작하기(CRUD)
    - INSERT, SELECT, UPDATE, DELETE
- command-line program - **sqlite3**
    - https://hphk.notion.site/SSAFY-8-Public-Document-9dc94ea8a050472ca00ffe8ea58586da?p=05b97c9aea4043c3ad73af6cb438017e&pm=s 참조
    - SQL문 및 commands을 사용하여 SQLite 데이터베이스와 상호 작용할 수 있는 간단한 command-line tool
    - 실행화면 예시
    ![sqlite3 실행화면](DB.assets/sqlite3%20%EC%8B%A4%ED%96%89%ED%99%94%EB%A9%B4.JPG)
    - sqlite3 사용
        1. 시작하기
        ![sqlite3 시작](DB.assets/sqlite3%20%EC%8B%9C%EC%9E%91.JPG)
        2. 데이터베이스 파일 열기
        ![sqlite3 데이터베이스 파일 열기](DB.assets/sqlite3%20%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%ED%8C%8C%EC%9D%BC%20%EC%97%B4%EA%B8%B0.JPG)
        3. 종료하기
        ![sqlite3 종료](DB.assets/sqlite3%20%EC%A2%85%EB%A3%8C.JPG)
        - 이외에 다양한 commands는 .help 명령어를 사용해 확인 가능
    - CSV 파일을 SQLite 테이블로 가져오기
        - sqlite3 tool을 사용하여 CSV파일을 테이블로 가져오는 방법
        1. DML.sql 파일 생성
        2. 테이블 생성
        ![sqlite 테이블 생성](DB.assets/sqlite%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%EC%83%9D%EC%84%B1.JPG)
        3. 데이터베이스 파일 열기
        ```$ sqlite3 mydb.sqlite3```
        4. 모드(.mode)를 csv로 설정
        ```sqlite> .mode csv```
        5. .import명령어를 사용하여 csv 데이터를 테이블로 가져오기
        ```sqlite> .import users.csv users```
        6. import된 데이터 확인하기
            - sqlite3 tool에서도 SQL문을 사용할 수 있지만, 실습의 편의와 명령어 기록을 위해 sql확장자 파일에서 진행하도록 함
            ![import된 데이터 확인하기](DB.assets/sqlite%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%ED%99%95%EC%9D%B8.JPG)

### Simple query
- **SELECT**문을 사용하여 간단하게 단일 테이블에서 데이터를 조회하기
- SELECT statement
    ```sql
    SELECT colum1, colum2 FROM table_name;
    ```
    - Query data from a table
    - 특정 테이블에서 데이터를 조회하기 위해 사용
    - 문법 규칙
        1. SELECT절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
        2. FROM절(clause)에서 데이터를 가져올 테이블을 지정
    - SELECT문은 SQLite에서 가장 복잡한 문
    - 다양한 절과 함께 사용할 수 있으며 하나씩 학습 할 예정
        - ORDER BY
        - DISTINCT
        - WHERE
        - LIMIT
        - LIKE
        - GROUP BY
    - SELECT statement 실습
        - 이름과 나이 조회하기
        ![이름과 나이 조회](DB.assets/%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EB%82%98%EC%9D%B4%20%EC%A1%B0%ED%9A%8C.JPG)
        - 전체 데이터 조회하기
            - 모든 컬럼에 대한 shorthand(약칭)인 ```*(asterisk)```를 사용할 수 있음
        ![전체 데이터 조회](DB.assets/%EC%A0%84%EC%B2%B4%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A1%B0%ED%9A%8C.JPG)
        - rowid 컬럼 조회
        ![rowid 컬럼 조회](DB.assets/rowid%20%EC%BB%AC%EB%9F%BC%20%EC%A1%B0%ED%9A%8C.JPG)

### Sorting rows
- ```ORDER BY``` 절을 사용하여 쿼리의 결과 정렬
- ORDER BY clause
    ```sql
    SELECT select_list FROM table_name
    ORDER BY column_1 ASC, column_2 DESC;
    ```
    - Sort a result set of a query
    - SELECT문에 추가하여 결과를 정렬
    - ORDER BY절은 FROM절 뒤에 위치함
    - 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
    - 이를 위해 ORDER BY절 다음에 'ASC' 또는 'DESC'
        - ASC : 오름차순(기본 값)
        - DESC : 내림차순
- ORDER BY clause 실습
    - 이름과 나이를 나이가 어린 순서대로 조회하기
    ![이름과 나이를 나이가 어린 순서대로 조회하기](DB.assets/%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EB%82%98%EC%9D%B4%EB%A5%BC%20%EB%82%98%EC%9D%B4%EA%B0%80%20%EC%96%B4%EB%A6%B0%20%EC%88%9C%EC%84%9C%EB%8C%80%EB%A1%9C%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - 이름과 나이를 나이가 많은 순서대로 조회하기
    ![이름과 나이를 나이가 많은 순서대로 조회하기](DB.assets/%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EB%82%98%EC%9D%B4%EB%A5%BC%20%EB%82%98%EC%9D%B4%EA%B0%80%20%EB%A7%8E%EC%9D%80%20%EC%88%9C%EC%84%9C%EB%8C%80%EB%A1%9C%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌잔고가 많은 순으로 정렬해서 조회하기
    ![이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌잔고가 많은 순으로 정렬해서 조회하기](DB.assets/%EC%9D%B4%EB%A6%84%2C%20%EB%82%98%EC%9D%B4%2C%20%EA%B3%84%EC%A2%8C%20%EC%9E%94%EA%B3%A0%EB%A5%BC%20%EB%82%98%EC%9D%B4%EA%B0%80%20%EC%96%B4%EB%A6%B0%EC%88%9C%EC%9C%BC%EB%A1%9C%2C%20%EB%A7%8C%EC%95%BD%20%EA%B0%99%EC%9D%80%20%EB%82%98%EC%9D%B4%EB%9D%BC%EB%A9%B4%20%EA%B3%84%EC%A2%8C%EC%9E%94%EA%B3%A0%EA%B0%80%20%EB%A7%8E%EC%9D%80%20%EC%88%9C%EC%9C%BC%EB%A1%9C%20%EC%A0%95%EB%A0%AC%ED%95%B4%EC%84%9C%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - ORDER BY절은 하나 이상의 컬럼을 정렬할 경우 첫 번째 열을 사용하여 행을 정렬하고, 그런 다음 두번째 컬럼을 사용하여 정렬 되어있는 행을 정렬하는 방식
    - 즉, 먼저 age를 기준으로 오름차순으로 정렬하고, 이 결과를 balance를 기준으로 내림차순으로 정렬한 것

- [참고] Sorting NULLs
    - NULL의 정렬 방식
    - 정렬과 관련하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주
    - 즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시되고, DESC를 사용하는 경우 결과의 끝에 NULL이 표시됨

### Filtering data
- 개요
    - 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
    - Clause
        - SELECT DISTINCT
        - WHERE
        - LIMIT
    - Operator
        - LIKE
        - IN
        - BETWEEN
- **SELECT DISTINCT** clause
    ```sql
    SELECT DISTINCT select_list FROM table_name;
    ```
    - Remove duplicate rows in the result
    - 조회 결과에서 중복된 행을 제거
    - DISTINCT절은 SELECT에서 선택적으로 사용할 수 있는 절
    - 문법 규칙
        1. DISTINCT절은 SELECT키워드 바로 뒤에 나타나야 함
        2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성
- SELECT DISTINCT 실습
    - 모든 지역 조회
    ![모든 지역 조회](DB.assets/%EB%AA%A8%EB%93%A0%20%EC%A7%80%EC%97%AD%20%EC%A1%B0%ED%9A%8C.JPG)
    - 중복 없이 모든 지역 조회하기
    ![중복 없이 모든 지역 조회하기](DB.assets/%EC%A4%91%EB%B3%B5%20%EC%97%86%EC%9D%B4%20%EB%AA%A8%EB%93%A0%20%EC%A7%80%EC%97%AD%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - 지역순으로 내림차순 정렬하여 중복 없이 모든 지역 조회하기
    ![지역순으로 내림차순 정렬하여 중복 없이 모든 지역 조회하기](DB.assets/%EC%A7%80%EC%97%AD%EC%88%9C%EC%9C%BC%EB%A1%9C%20%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EC%97%AC%20%EC%A4%91%EB%B3%B5%20%EC%97%86%EC%9D%B4%20%EB%AA%A8%EB%93%A0%20%EC%A7%80%EC%97%AD%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
        ![이름과 지역이 중복 없이 모든 이름과 지역 조회하기](DB.assets/%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EC%A7%80%EC%97%AD%EC%9D%B4%20%EC%A4%91%EB%B3%B5%20%EC%97%86%EC%9D%B4%20%EB%AA%A8%EB%93%A0%20%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EC%A7%80%EC%97%AD%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
        - 각 컬럼의 중복을 따로 계산하는 것이 아니라 두 컬럼을 하나의 집합으로 보고 중복을 제거
    - 이름과 지역이 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
    ![이름과 지역이 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기](DB.assets/%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EC%A7%80%EC%97%AD%EC%9D%B4%20%EC%A4%91%EB%B3%B5%20%EC%97%86%EC%9D%B4%20%EC%A7%80%EC%97%AD%20%EC%88%9C%EC%9C%BC%EB%A1%9C%20%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EC%97%AC%20%EB%AA%A8%EB%93%A0%20%EC%9D%B4%EB%A6%84%EA%B3%BC%20%EC%A7%80%EC%97%AD%20%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0.JPG)
    - [참고] NULL with DISTINCT
        - SQLite는 NULL값을 중복으로 간주
        - NULL값이 있는 컬럼에 DISTINCT절을 사용하면 SQLite는 NULL값의 한 행을 유지

- WHELE의 검색 조건 작성 형식
    ![]()
    - 작성 예시
    ![]()
- SQLite comparison operators(비교연산자)

- SQLite logical operators(논리연산자)
    - 일부 표현식의 truth를 테스트 할 수 있음
    - 1, 0 또는 NULL값을 반환

- WHERE 실습
    - 나이가 30살 이상인 사람들의 이름, 나이, 계좌잔고 조회하기
    ![]()
    - 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌잔고 조회하기
    ![]()
- LIKE operator
    - 
    - SQLite는 패턴 구성을 위한 두개의 와일드카드(wildcards)를 제공
        1. %(percent)
            - 0개 이상의 문자가 올 수 있음을 의미
            - 예시
                - 영% 패턴은 영으로 시작하는 모든 문자열과 일치(영, 영미, 영미리 등)
                - %도 패턴은 도로 끝나는 모든 문자열과 일치
        2. _(underscore)
            - 단일(1개) 문자가 있음을 의미
            - 예시
                - 영_ 패턴은 영으로 시작하고 총 2자리인 문자열과 일치





### A many-to-one relationship
- 개요
    - 관계형 데이터베이스에서의 외래 키 속성을 사용해 모델간 N:1관계 설정하기
- RDB(관계형 데이터베이스) 복습
    - 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
    - RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있음
- [참고] 관계(Relationship)
    - 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결
- 테이블 간 관계 예시
    ![테이블 간 관계 예시1](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94%20%EA%B0%84%20%EA%B4%80%EA%B3%84%20%EC%98%88%EC%8B%9C1.JPG)
    ![테이블 간 관계 예시2](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94%20%EA%B0%84%20%EA%B4%80%EA%B3%84%20%EC%98%88%EC%8B%9C2.JPG)
    ![테이블 간 관계 예시3](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94%20%EA%B0%84%20%EA%B4%80%EA%B3%84%20%EC%98%88%EC%8B%9C3.JPG)
    ![테이블 간 관계 예시4](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94%20%EA%B0%84%20%EA%B4%80%EA%B3%84%20%EC%98%88%EC%8B%9C4.JPG)
    ![테이블 간 관계 예시5](DB.assets/%ED%85%8C%EC%9D%B4%EB%B8%94%20%EA%B0%84%20%EA%B4%80%EA%B3%84%20%EC%98%88%EC%8B%9C5.JPG)
- RDB에서의 관계
    1. 1 : 1
        - One-to-one relationships
        - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한개와 관련된 경우
    2. ```N : 1```
        - Many-to-one relationships
        - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한개와 관련된 경우
        - 기준 테이블에 따라 (1:N)이라고도 함
        - Many-to-one relationships 예시
        ![Many-to-one relationships 예시](DB.assets/Many-to-one%20relationships%20%EC%98%88%EC%8B%9C.JPG)
    3. M : N
        - Many-to-many relationships
        - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
        - 양쪽 모두에서 N:1관계를 가짐
        - M:N에 대한 자세한 내용은 N:1 이후 진행

### 외래 키(Foreign Key)
- 외래 키(외부 키)
- 관계형 데이터 베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키에 해당하고, 이는 참조되는 측 테이블의 기본 키를 가리킴
- 참조하는 테이블의 행 1개의 값은 참조되는 측 테이블의 행 값에 대응됨
    - 이 때문에 참조하는 테이블의 행에는 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블 행 여러 개가 참조되는 테이블의 동일한 행을 참조할 수 있음
- 특징
    - 키를 사용하여 부모 테이블의 유일한 값을 참조(by 참조 무결성)
        - [참고] 참조 무결성
            - 데이터 베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성을 말함
            - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함
    - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함
    
### N:1(Comment - Article)
- 개요
    - Comment(N) - Article(1)
    - Comment 모델과 Article 모델 간 관계 설정
    - 0개 이상의 댓글은 1개의 게시글에 작성 될 수 있음
- 모델 관계 설정
    - 게시판의 게시글과 N:1 관계를 나타낼 수 있는 댓글 구현
    - N:1 관계에서 댓글을 담당할 Comment 모델은 N, Article 모델은 1이 될 것
    ![모델 관계 설정1](DB.assets/%EB%AA%A8%EB%8D%B8%20%EA%B4%80%EA%B3%84%20%EC%84%A4%EC%A0%951.JPG)
    ![모델 관계 설정2](DB.assets/%EB%AA%A8%EB%8D%B8%20%EA%B4%80%EA%B3%84%20%EC%84%A4%EC%A0%952.JPG)
- Django Relationship fields
    - 종류
        1. OneToOneField()
            - A one-to-one relationship
        2. ```ForeignKey()```
            - A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
            - ForeignKey(to, on_delete, **options)
            - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
            - 2개의 필수 위치 인자가 필요
                1. 참조하는 **model class**
                2. **on_deletd** 옵션
        3. ManyToManyField()
            - A many-to-many relationship
    
### Comment 모델 정의
![Comment 모델 정의](DB.assets/comment%20%EB%AA%A8%EB%8D%B8%20%EC%A0%95%EC%9D%98.JPG)
- 외래 키 필드는 ForignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨
- ForignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스의 단수형(소문자)으로 작성하는 것을 권장(이유는 다음 모델 참조에서 확인 예정)
- ForignKey artuments - on_delete
    - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
    - 데이터 무결성을 위해서 매우 중요한 설정
    - on_delete 옵션 값
        - **CASCADE** : 부모 객체(참조 된 객체)가 삭제 되었을 때 이를 참조하는 객체도 삭제
        - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재
    - [참고] 데이터 무결성(Data Integrity)
        - 데이터의 정확성과 일관성을 유지하고 보증하는 것
        - 데이터 베이스나 RDBMS의 중요한 기능
        - 무결성 제한의 유형
            1. 개체 무결성(Entity integrity)
            2. 참조 무결성(Referential integrity)
            3. 범위 무결성(Domain integrity)
- Migration 과정 진행
    - model.py에서 모델에 대한 수정사항이 발생했기 때문에 migration 과정을 진행
    ```$ python manage.py makemigrations```
    - 마이그레이션 파일 0002_comment.py 생성 확인
    - migrate 진행
    ```$ python manage.py migrate```
    - migrate후 Comment 모델 클래스로 인해 생성된 테이블 확인
    ![migrate후 생성된 테이블 확인](DB.assets/migrate%ED%9B%84%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%ED%99%95%EC%9D%B8.JPG)
    - ForeignKey 모델 필드로 작성된 컬럼의 이름이 **article_id**인 것을 확인
    - 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성했다면 abcd_id로 만들어짐
        - 이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장 되었던 이유
- 댓글 생성 연습
    - shell_plus 실행
    ```$ python manage.py shell_plus```
    1. 댓글 생성
    ![댓글 생성1](DB.assets/%EB%8C%93%EA%B8%80%20%EC%83%9D%EC%84%B11.JPG)
    ![댓글 생성2](DB.assets/%EB%8C%93%EA%B8%80%20%EC%83%9D%EC%84%B12.JPG)
    2. 댓글 속성 값 확인
    ![댓글 속성 값 확인](DB.assets/%EB%8C%93%EA%B8%80%20%EC%86%8D%EC%84%B1%20%EA%B0%92%20%ED%99%95%EC%9D%B8.JPG)
    3. comment 인스턴스를 통한 article 값 접근하기
    ![comment 인스턴스를 통한 article 값 접근하기](DB.assets/comment%20%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4%EB%A5%BC%20%ED%86%B5%ED%95%9C%20article%20%EA%B0%92%20%EC%A0%91%EA%B7%BC%ED%95%98%EA%B8%B0.JPG)
    4. 두번째 댓글 작성해보기
    ![두번째 댓글 작성](DB.assets/%EB%91%90%EB%B2%88%EC%A7%B8%20%EB%8C%93%EA%B8%80%20%EC%9E%91%EC%84%B1.JPG)
    - 작성된 댓글 확인해보기
    ![작성된 댓글 확인](DB.assets/%EC%9E%91%EC%84%B1%EB%90%9C%20%EB%8C%93%EA%B8%80%20%ED%99%95%EC%9D%B8.JPG)

### 관계 모델 참고
- Related manager
    - Related manager는 N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
    - Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때에 사용할 수 있는 manager를 생성
        - 우리가 이전에 모델 생성 시 **objects**라는 매니저를 통해 quertset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
- 역참조
    - 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
    - 즉, 본인을 외래키로 참조 중인 다른 테이블에 접근하는 것
    - N:1 관계에서는 1이 N을 참조하는 상황
        - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조
- ```article.comment_set.method()```
    - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
    - article.comment 형식으로는 댓글 객체를 참조 할 수 없음
        - 실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
    - 대신 Django가 역참조 할 수 있는 **comment_set** manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 없음
        - N:1관계에서 생성되는 Related manager의 이름은 참조하는 '모델명_set' 이름 규칙으로 만들어짐
    - 반면 참조 상황(Commnet -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능
- Related manager 연습
    - shell_plus 실행
    ```$ python manage.py shell_plus```
    1. 1번 게시글 조회하기
    ```$ article = Article.objects.get(pk=1)```
    2. dir() 함수를 사용해 클래스 객체가 사용할 수 있는 메서드 확인
    ![dir함수로 메서드 확인](DB.assets/dir%ED%95%A8%EC%88%98%EB%A1%9C%20%EB%A9%94%EC%84%9C%EB%93%9C%20%ED%99%95%EC%9D%B8.JPG)
    3. 1번 게시글에 작성된 모든 댓글 조회
    ![1번 게시글의 모든 댓글 조회](DB.assets/1%EB%B2%88%20%EA%B2%8C%EC%8B%9C%EA%B8%80%EC%9D%98%20%EB%AA%A8%EB%93%A0%20%EB%8C%93%EA%B8%80%20%EC%A1%B0%ED%9A%8C.JPG)
    4. 1번 게시글에 작성된 모든 댓글 출력
    ![1번 게시글의 모든 댓글 출력](DB.assets/1%EB%B2%88%20%EA%B2%8C%EC%8B%9C%EA%B8%80%EC%9D%98%20%EB%AA%A8%EB%93%A0%20%EB%8C%93%EA%B8%80%20%EC%B6%9C%EB%A0%A5.JPG)
- ForeignKey arguments - **related_name**
    ![ForeignKey arguments - related_name](DB.assets/ForeignKey%20arguments%20-%20related_name.JPG)
    - ForeignKey 클래스의 선택 옵션
    - 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있음
    - 작성 후, migration 과정이 필요
    - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 하는데 이는 추후 자연스럽게 만나볼 예정
    - 작성 후 다시 원래 코드로 복구
        - 위와 같이 변경하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체됨
- admin site 등록
    - 새로 작성한 Comment 모델을 admin site에 등록하기

### Comment 구현
- CREATE
    - 사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 작성
    ![comment create1](DB.assets/comment%20create1.JPG)
    - detail 페이지에서 CommentForm 출력(view 함수)
    ![comment create2](DB.assets/comment%20create2.JPG)
        - 기존에 ArticleForm 클래스의 인스턴스명을 form으로 작성했기 때문에 헷갈리지 않도록 comment_form으로 작성
    - detail 페이지에서 CommentForm 출력(템플릿)
    ![comment create3](DB.assets/comment%20create3.JPG)
    - detail 페이지에 출력된 CommentForm을 살펴보면 다음과 같이 출력됨
    ![comment create4](DB.assets/comment%20create4.JPG)
    - 실 서비스에서는 댓글을 작성할 때 댓글을 어떤 게시글에 작성하는지 직접 게시글 번호를 선택하지 않음
    - 실제로는 해당 게시글에 댓글을 작성하면 자연스럽게 그 게시글에 댓글이 작성되어야 함
    - 다음과 같이 출력되는 이유는 Comment 클래스의 외래 키 필드 article 또한 데이터 입력이 필요하기 때문에 출력되고 있는 것
    - 하지만, 외래 키 필드는 **사용자의 입력으로 받는 것이 아니라 view함수 내에서 받아 별도로 처리되어 저장**되어야 함
    - 외래 키 필드를 출력에서 제외 후 확인
    ![comment create5](DB.assets/comment%20create5.JPG)
    - 출력에서 제외된 외래 키 데이터는 어디서 받는가
    - detail 페이지의 url을 살펴보면 path('< int:pk>/', views.detail, name='detail')url에 해당 게시글의 pk값이 사용 되고 있음
    - 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk값
    - 이전에 학습했던 url을 통해 변수를 넘기는 **variable routing**을 사용
    ![comment create6](DB.assets/comment%20create6.JPG)
    - 작성을 마치고 보면 article 객체 저장이 이루어질 타이밍이 보이지 않음
    - 그래서 save() 메서드는 데이터베이스에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해주는 옵션 값을 제공
    - save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기
        ![comment create7](DB.assets/comment%20create7.JPG)
        - The **save()** method
            - save(commit=False)
                - Create, but don't save the now instance
                - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
                - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
    - 댓글 작성 후 테이블 확인
    ![comment create8](DB.assets/comment%20create8.JPG)
- READ
    - 작성한 댓글 목록 출력하기
    - 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
    ![comment read1]()
    - detail 템플릿에서 댓글 목록 출력하기
    ![comment read2]()
    - detail 템플릿에서 댓글 목록 출력 확인하기
    ![comment read3]()
- DELETE
    - 댓글 삭제 구현하기(url, view)
    ![comment dlelte1]()
    - 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력 될 수 있도록 함
    ![comment dlelte2]()
    - 댓글 삭제 버튼 출력 확인 및 삭제 시도해보기
    ![comment dlelte3]()
- 댓글 수정을 지금 구현하지 않는 이유
    - 댓글 수정도 게시글 수정과 마찬가지로 구현이 가능
        - 게시글 수정 페이지가 필요했던 것처럼 댓글 수정 페이지가 필요하게 됨
    - 하지만 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form 부분만 변경되어 수정 할 수 있도록 함
    - 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행하도록 함

### Comment 추가 사항
- 개요
    - 댓글에 관련된 아래 2가지 사항을 작성하면서 마무리하기
        1. 댓글 개수 출력하기
            1. DTL filter - **length** 사용
                ![댓글 개수 출력 length 사용](DB.assets/%EB%8C%93%EA%B8%80%20%EA%B0%9C%EC%88%98%20%EC%B6%9C%EB%A0%A5%20length%20%EC%82%AC%EC%9A%A9.JPG)
            2. Queryset API - **count()** 사용
                ![댓글 개수 출력 count 사용](DB.assets/%EB%8C%93%EA%B8%80%20%EA%B0%9C%EC%88%98%20%EC%B6%9C%EB%A0%A5%20count%20%EC%82%AC%EC%9A%A9.JPG)
            - detail 템플릿에 작성하기
            ![]()
            - 작성 후 출력 확인
            ![]()
        2. 댓글이 없는 경우 대체 컨텐츠 출력하기
            - DTL **for empty** 활용하기
            ![]()
            - 새로운 게시글을 작성하거나 모든 댓글을 삭제 후 확인
            ![]()

### N:1 (Article - User)
- 개요 
    - Article(N) - User(1)
    - Article모델과 User모델 간 관계 설정
    - 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

### Referencing the User model
- Django에서 User모델을 참조하는 방법
    1. settings.AUTH_USER_MODEL
        - 반환 값 : 'accounts.User' (문자열)
        - User모델에 대한 외래 키 또는 
    2. get_user_model()
        - 반환 값 : User Object (객체)
        - 현재 활성화(active)된 User 모델을 반환
        - 커스터마이징한 User 모델이 있을 경우는 
    - 정리
        - 문자열과 객체를 반환하는 특징과 Django의 내부적인 실행 원리에 관련된 것이므로 이렇게만 외우도록 한다.
        - User 모델을 참조할 때
            - models.py에서는 settings.AUTH_USER_MODEL
            - 다른 모든 곳에서는 get_user_model()

- 모델 관계 설정