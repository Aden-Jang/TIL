# 장근우

# 7.14 스타트캠프 수업내용

### Git

Git = 분산 버전 관리 프로그램 버전관리 → 레포트 수정본 최종 이런것 - 변경시간, 변경사항 등만 저장하고 마지막 최종본1개 저장 깃은 자동으로 누가 언제 무엇을 왜 바꿨는지 저장해 줌
***
###분산 ↔ 중앙집중

#####중앙집중 
- 은행과 비슷. 
- 버전관리가 잘되어도 하나의 서버에 저장되어있으면 중앙집중식 버전관리

#####분산 
- 블록체인 기술(NFT)   각자 저장 - 분산버전관리 - 하나의 서버가 터져도 복구 가능
***
###GitHub 
##### Git기반의 저장소 서비스
    
버전관리는 Git 서비스는 GitLab, GitHub, Bitbucket

GitLab, GitHub차이 : GitHub은 마이크로소프트에서 관리 GitLab은 서버를 본인이 관리 가능

GitHub 쓰면 기술 유출이 될 가능성이 있음

GitHub은 공개적 - 전세계에 나를 표현 가능 - 열정, 성실함, 능력 표현 가능

GitHub 잔디밭 관리(TIL) - 하루 한칸씩 보임.
 하루에 한개씩 커밋 하기 “1일1커밋” - 성실함을 보여줌 
회사에 입사해서 가르쳐주지 않고 분석 가능한지 성실하게 할 수 있는지 볼 수 있으므로

***GitHub 닉네임 중요*** - 기업 등에서 제출할 때 보이므로

인스타랑 비슷함 사진대신 코드 이용

협업툴 1위 GitHub 82.8% 대부분이 GitHub 사용중 - 필수

2위 slack 업무용 메신저툴 카톡방의 좋은버전

3위 jira 이슈 관리 툴 - 유지보수

---
### CLI

**CLI** (Command Line Interface) : 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식 ↔ **GUI** (Graphic User Interface) : 그래픽을 통해 사용자가 컴퓨터와 상호작용하는 방식

- GUI로 못하는 것을 CLI로 함

- CLI는 GUI보다 컴퓨터 리소스 절약 가능

- GUI는 개인, CLI는 개발자가 사용

- 많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공하기 때문에 배워야함

####CLI명령어 (필수로 알아야함)

- touch : 파일 생성

- Mkdir : 새 폴더 생성

- ls : 현재 작업중인 디렉토리의 폴더/파일 목록을 보여줌

- cd : 현재 작업중인 디렉토리 변경

- start : 폴더/파일 열어줌(mac은 open)

- rm : 파일 삭제        
-r옵션(재귀적의미 타고타고타고 들어감 들어가서 모든 파일 지움)을 주면 폴더 삭제 가능
***

![Untitled](https://raw.githubusercontent.com/Aden-Jang/TIL/master/startcamp/test.assets/%EC%9E%91%EC%97%85%EC%9C%84%EC%B9%98.JPG)

SSAFY@DESKTOP(JGW@Jang-PC) MINGW64 → 컴퓨터 정보, ~ → 현재 작업중인 위치
(~= C:\Users\multicampus)

####하위폴더 이동 
cd ~ (des만 치고 tab 누르면 가장 비슷한 파일/폴더를 선택, 여러개일 경우 tab두번 누르면 그와 비슷한 이름 가진 파일/폴더 보여줌 그중에 선택)



상위폴더로 이동 cd ..

파일 만들고 지울 때 확장자까지 써줘야됨 ex) touch test.txt  rm test.txt 등

절대 경로 vs 상대경로

절대 경로 : 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것 (C:부터~~~)

상대 경로 : 현재 작업중인 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것 (./ : 현재 작업중인 폴더 ../ : 현재 작업중인 폴더의 부모 폴더)



[README.md](http://README.md)

- 프로젝트에 대한 설명문서

Repository(레포지토리) - 특정 디렉토리를 버전 관리하는 저장소

git init 명령어로 로컬 저장소 생성

.git 디렉토리에 버전 관리에 필요한 모든 것이 들어 있음 (숨김폴더) 지우면 모든 버전관리가 사라짐

git으로 버전관리되는지 확인하는 것은 뒤에 (master)가 있는지 확인하면 됨

[README.md](http://README.md) 생성    (git bash에서 touch [README.md](http://README.md))

이 파일을 버전관리하며 git을 사용 → 특정버전으로 남긴다 = 커밋(commit)한다 - 3가지 영역을 바탕으로 동작 - Working Directory, Staging Area, Repository 이 3가지 영역을 바탕으로 동작

Working Directory - 내가 작업하고 있는 실제 디렉토리

Staging Area - 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 (커밋이 저장되기 전에 임시저장되는 곳)

Repository - 커밋들이 저장되는 곳(저장소, .git 디렉토리)

# 7.15 스타트캠프 수업내용

Git 기본기

(Working Directory)WD에서 파일 만듦 → untracked 상태 →commit으로 만들고 싶은 상태를 (Staing Area)SA로 옮김 → git add명령어 사용 → staged상태(tracked상태)(git으로 버전관리하는 상태) → gir commit명령어 사용 → committed상태 → WD에 modified상태 → 다시 git add로 버전 관리…

WD → git add → SA → git commit → Rep → modified상태(WD) 반복

git status 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음

d2coding검색 -맨위에거 - 다운로드 - zip풀고 2번째꺼 (all) 설치 vscode에서 설정(ctrl+,) font family에서 맨 앞에 D2Coding 추가

git add 파일명 쓰면 파일만 하나 , git add . 하면 폴더에 있는 전체를 add함

git commit 만 치면 길게 나옴 나가고 싶으면 :q 입력

한줄로 commit하고싶으면 git commit -m “내용”을 입력하면 됨

git status 입력하면 현재 상태 확인 가능 - mofied된 상태면 add, commit가능

git log 입력하면 현재 서버에 저장된 커밋된것들을 보여줌

vscode ctrl + k, f 누르면 파일 닫기

SA를 거쳐서 commit하는 이유는 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일만 남기기 위해

2개의 커밋사이에 차이점을 찾는 명령어 git diff - 보기 불편해서 잘안씀

사용법 : git diff A(각각의 고유 아이디 앞4자리수) B(각각의 고유 아이디 앞4자리수) A,B순서 바뀌면 기준이 달라져서 -된 것이 +된것으로 바뀜 (앞에서 뒤로 어떻게 변했는지 보여줌)

local repository : 컴퓨터에 저장된 것

remote repository : 어떠한 서버에 저장된 것

github repository 생성

- repository 클릭 → name 입력 → public 다 되는데 다른사람이 올리는건 안됨 vs private 다 안됨

github과 local 연결

git remote add repo_name(원하는 별명 그러나 관례상 거의 origin씀) remote_repo의 주소(https://github.com/Aden-Jang/first_repo.git)

git push A(어디로 push할지 origin)  B(local의 브랜치를 입력 master)

git push -u(set upstream의 약자) origin master 치면 자동으로 되므로 git push만 입력해도 바로 푸쉬됨

git clone remote_repo   - remote repo를 local로 복사

github에서는 브랜치 이름이 main으로 자동생성됨 - settings에서 바꿀수 있음

git clone 주소 입력하면 깃헙에 있는 레포지토리가 로컬로 불러옴

code . 입력하면 현재 위치에서 vscode 오픈 가능

git pull  remote에서의 변경사항을 local로 땡겨오는 명령어

local과 remote의 내용이 겹칠 때 컴플릭트(conflict)났다고 함

원하는 파일 형태로 저장한 후 add, commit, push하면 됨

컴플릭트가 난 상황을 합치는 과정을 merge라고 함 

## TIL (Today I Learned)프로젝트

매일 내가 배운 것을 마크다운으로 정리해서 문서화

신입 개발자에게 요구되는 가장 큰 능력. - 꾸준히 학습 가능?

깃헙관리의 가장 첫 걸음 가장 중요