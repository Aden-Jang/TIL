### Git Advanced

- git 영역:
  - 내가 작업하고 있는 영역-working directory
  - add 한 영역 - staging area
  - push 한 영역 - 내 repository

1. undoing : Git 작업 다시 되돌리는 것
  - Working directory 작업 단계
    - WD에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
    - git restore
      - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
      - `git restore를 통해 되돌리면 해당 내용을 복원할 수 없으니 주의!`
      - git restore {파일 이름}
      - [참고] git 2.23.0버전 이전에는 git checkout -- {파일 이름}

  - Staging Area 작업 단계
    - SA에서 반영된 파일을 WD로 되돌리기
      - git rm --cached
        - root-commit이 없는 경우(최초 커밋인 경우)
        - git rm --cached {파일 이름}
      - git restore --staged
        - root-commit이 있는 경우
        - git restore --staged {파일 이름}
        - [참고] git 2.23.0버전 이전에는 git reset HEAD {파일 이름}

  - Repository 작업 단계
    - 커밋 완료한 파일을 SA로 되돌리기
    - git commit --amend
      - 상황별로 두가지 기능으로 나뉨
        - Staging Area에 새로 올라온 내용이 없다면 직전 커밋의 메시지만 수정
        - Staging Area에 새로 올라온 내용이 있다면 직전 커밋을 덮어쓰기
      - amend(수정하다) 즉, 이전 커밋을 수정해서 새 커밋으로 남김 
      - 커밋 내용을 수정하거나 수정 사항을 새로 커밋에 추가하고 싶을 때 사용 
      - 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨

2. 버전관리 -> 버전 쌓기
  - Git reset
    - 시계를 마치 과거로 돌리는 듯한 행위로, 프로젝트를 특정 커밋(버전) 상태로 되돌림
    - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
    - git reset [옵션] {커밋 ID}
      - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성
      - 옵션은 soft, mixed, hard 중 하나를 작성
        - --soft
          - 해당 커밋으로 되돌아가고
          - 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음
        - --mixed
          - 해당 커밋으로 되돌아가고
          - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
          - git reset 옵션의 기본값
        - --hard
          - 해당 커밋으로 되돌아가고
          - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제 -> 사용시 주의할 것
          - 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음
      - [참고] git reflog
        - git reset의 hard 옵션은 wd까지 삭제하므로 위험할 수 잇음
        - git reflog로 hard로 reset하더라도 남아있는 커밋들을 볼 수 있고 복구 가능
        - git reflog에 뜨는 ID값으로 git reset --옵션 이전ID 를 치면 다시 최신으로 되돌아가기 가능
    - git revert
      - 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성
        - git revert {커밋 ID}
          - 커밋 ID는 취소하고 싶은 커밋ID를 작성
      - git reset과 차이점

    - [참고] git commit -am "커밋 이름" - add 와 commit 동시에 해줌

3. branch(master, main)
- 브랜치는 나뭇가지라는 뜻으로 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구
- 장점
  - 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
  - Git은 브랜치를 만드는 속도가 굉장히 빠르고 적은 용량을 소모함
- 브랜치는 커밋을 가리키는 포인터이다.
- git branch
  - 브랜치의 조회, 생성, 삭제와 관련된 Git 명령어
  - 조회
    - git branch - 로컬 저장소의 브랜치 목록 확인
    - git branch -r - 원격 저장소의 브랜치 목록 확인
  - 생성
    - git branch {브랜치 이름} - 새로운 브랜치 생성
    - git branch {브랜치 이름} {커밋 ID} - 특정 커밋 기준으로 브랜치 생성
  - 삭제
    - git branch -d {브랜치 이름} - 병합된 브랜치만 삭제 가능
    - git branch -D {브랜치 이름} - 강제 삭제
- git switch
  - 현재 브랜치에서 다른 브랜치로 이동하는 명령어
  - git switch {브랜치 이름} - 다른 브랜치로 이동
  - git switch -c {브랜치 이름} - 브랜치를 새로 생성 및 이동
  - git switch -c {브랜치 이름} {커밋 ID} - 특정 커밋 기준으로 브랜치 생성 및 이동
  - switch하기 전에 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의!
    - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨
- git merge
  - 분기된 브랜치들을 하나로 합치는 명령어
  - master 브랜치가 상용이므로 주로 master 브랜치에 병합
  - git merge {합칠 브랜치 이름}
    - 병합하기 전에 브랜치를 합치려고 하는 즉 메인 브랜치로 switch 해야함
    - 병합에는 세 종류가 존재
      1. Fast-Forward
        - 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
      2. 3-way Merge
        - 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법
      3. Merge Conflict
        - 두 브랜치에서 같은 부분을 수정한 경우 충돌이 발생한 부분은 작성자가 직접 해결해야함
  - [참고] HEAD는 현재 브랜치를, 각 브랜치는 자신의 최신 커밋을 가리키므로 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다.
  
### git workflow
- git 브랜치 전략
  - git-flow
  - gitgub-flow
  - gitlab-flow
  - 어떤 브랜치 전략을 사용할 것인지는 팀에서 정하는 문제
  - 브랜치를 자주 생성하는 것을 권장하며 master브랜치 하나만 하는 것은 지양해야함



git switch master -> 메인 브랜치로 이동
git merge feature/signup -> b.txt가 master에 생김

git switch feature/signup -> c.txt 파일은 없는 상태
git merge master -> 같은 히스토리를 가지게 됨

git log --online --graph -> 각 merge가 어떻게 생겼는지 그래프로 보여줌
master에서 a.txt에 내용 추가
feature/signup에서 a.txt에 내용 추가
=> master에서 git merge feature/signup 하면
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
Automatic merge failed; fix conflicts and then commit the result 나옴

git add .
git commit -m "merge feature/signup"

$ git log --oneline --graph

562e625 (HEAD -> master) merge feature/signup
|\
| * b724f4d (feature/signup) update a.txt

| a6b60cb update a.txt from master
|/

fef31a9 Merge branch 'feature/signup'
|\
| * 3acd983 add b.txt

| 4bdc473 add c.txt
|/

7279559 둘째줄 추가
db43f03 첫줄 추가
feature/signup 에 가서 git merge master 하면
fast-forward로 바로 합쳐짐

master branch로 이동 후 git branch -d feature/signup 하면
feature/signup 지워짐

git branch -> 모든 branch 확인해보면 master만 남아있음

+) HEAD
HEAD는 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로
결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
git log 혹은 cat.git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음


- Git workflow (branch를 어떻게 써야 더 이쁘게 쓰나 해서 만들어짐)
  - git-flow: 5개의 브랜치로 나누어 소스코드를 관리(대규모 프로젝트에 적합)
    - master : 현재 main version (항상 동작해야함)
      - develop : 개발해야하면 develop branch로 이동
      - feature branches : 개발 중 필요하면 생성하는 branch 개발이 끝나면 develop으로 합침
      - release branch : 합친 develope이 잘 동작하나 test, test 끝나면 master로 합침
      - hotfixes : 문제가 생기면 급하게 수정해서 바로 master로 보낼 수도 있고 develop으로 다시 보내서 수정
  - git-hub-flow
    : Pull Request 기능을 사용하도록 권장하며, 병합 후 배포가 자동화로 이루어짐
    - master/feature로 나누어서 feature에서 수정해서 master와 합침
- git-lab-flow
  - master/production/pre-production 으로 나누어 개발 내용을 바로 반영하지 않고, 배포 시기를 조절
  - 브랜치를 자주 생성하는 것을 강력히 권장하며 main(master) 브랜치 하나로만 작업하는 형태는 지양해야함

- Shared repository model
  - 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
  - master 브랜치에 직접 해발하는 것이 아니라, 기능별로 브랜치를 따로 둠
  - Pull Request 사용하여 팀원간 변경 내용에 대한 소통 진행



<GIT Advanced>

- git 영역:
    - 내가 작업하고 있는 영역-working directory
    - add 한 영역 - staging area
    - push 한 영역 - 내 repository

1. undoing : 내가 한 일을 다시 되돌리는 것
- Git에서 되돌리기는 작업 상태에 따라 세가지로 분료
	- woking directory (수정한 파일을 이전 커밋 상태로 되돌리기)
		- git restore
	- staging area
		- git rm --cached
		- git restore --staged
	- repository 작업 단계(커밋 완료 파일을 staging area로)
		- git commit --amend


- git restore
	- woking directory에서 수정한 파일을 직전 커밋으로 되돌리기
    - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
    - git resotre를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의!
    - git restore {파일 이름}   (. 이면 현재 위치에 있는 모든 파일을 restore)
    - git 2.23.0 버전 이전은 git checkout --{파일 이름}

    ```
    01_git_restore 폴더 생성해서 git 저장소로 만들기
    cd 01_git_restore
    git init
    touch a.md
    git add .
    git status ->commit 할 게 있다고 알려줌
    a.md파일에 아무거나 작성한 후 git restore . -> 작성한 게 사라짐
    ```

- staging area 작업 단계 되돌리기
    - staging area 에 반영된 파일을 working directory로 되돌리기
    - root -commit이 없는 경우 : git rm --cached
    - root -commit이 있는 경우 : git restore --staged

    - git rm --cached {파일이름}
        - git을 만들고 한번도 커밋을 안한경우
        ```
        git rm --cached a.md -> rm 'a.md'라고 나옴

        git status -> untracked files라고 나옴
        ```
    - git restore --staged {파일이름}
        - Git 저장소에 한개 이상의 커밋이 있는 경우
        - git 2.23.0 버전 이전에는 git reset HEAD {파일이름}
        ```
        [commit 남기기]
        git add .
        git commit -m "a.md"

        파일에 아무거나 입력하고 다시
        git add .
        git restore --staged a.md -> 입력한 게 바뀌진 않지만 add . 하지 않은 상태로 돌아간 것
        ```

    - git commit --amend
        - 커밋을 완료한 파일을 Staging Area로 되돌리기
        - 상황별로 두가지 기능
            - staging area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
            - staging area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기
        - amend(수정하다) 즉, 이전 커밋을 수정해서 새 커밋으로 남김
            -> 커밋 내용을 수정하거나 수정사항을 새로 커밋에 추가하고 싶을 때 사용 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨
        ```
        02_git_amend 폴더 만들고
        git init
        touch test.md
        git add .
        git commit -m "commit 01"

        git log
        git commit --amend -> 당황할만한 창 뜸 문서편집기임
        i 를 누르면 끼워넣기 가능
        커밋을 수정했습니다. 입력하고 esc 누르면 끼워넣기 사라짐
        저장하고(w) 나가기(q)
        :wq 입력하면 됨
        
        git log 해보면 commit message 수정됨


        [commit 여러줄 남기기]
        git add .
        git commit -> 문서 편집기 열림
        i -> 편집 가능
        편집 후 esc
        :wq -> 저장하고 나가기


        [test.md 파일을 문서 편집기로 편집하기]
        vi.test.md
        i -> 편집 가능
        편집 후 esc
        :wq -> 저장하고 나가기

        $ git add .

        warning: LF will be replaced by CRLF in test.md.
        The file will have its original line endings in your working directory
        -> 개행문자 차이로 나타나는 오류임
        -> git config --global core.autocrif true 하면 다시 add 가능

        git add .
        git commit --amend
        해서 커밋 내용 다시 바꿀 수 있음 => 직전 커밋이 남아있지 않다.

        ```
2. 버전관리 -> 버전 쌓기
- git reset & revert
    - git reset [옵션] {커밋 ID}
        - 프로젝트를 특정 커밋(버전) 상태로 되돌림
        - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
        - 옵션은 soft, mixed, hard 중 하나를 작성 (기본은 mixed)
        - 커밋 ID는 되돌아 가고 싶은 시점의 커밋 ID를 작성

        - --soft
            - 해당 커밋으로 되돌아가고 
            - 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음
            ```
            git reset --soft 6baf

            git status 하면  reset 된 파일은 git add . 한 상태로 되어있음
            ```
        - --mixed
            - 해당 커밋으로 되돌아가고
            - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
            - git reset 옵션의 기본 값
            ```
            git log --oneline -> 커밋 상태 확인

            git reset --mixed 6baf

            git status 하면 reset 된 파일들은 untracted 상태임
            ```
        - --hard
            - 해당 커밋으로 되돌아가고
            - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제 -> 사용시 주의!
            - 기존의 Untracted 파일은 사라지지 않고 Untracted로 남아있음
            ```
            git reset --hard 6baf

            $ git log --oneline
            6baf32f (HEAD -> master) first
            ```
        +) git reflog
            - git reset hard 옵션은 Working Directory 내용까지 삭제하므로 위험
            - git reflog 명령어를 이용하면 reset 하기 전의 과거 커밋 내역을 모두 조회 가능
            - 이후 해당 커밋으로 reset 하면 hard 옵션으로 삭제된 파일도 복구 가능
            ```
            $ git reflog
            6baf32f (HEAD -> master) HEAD@{0}: reset: moving to 6baf
            20d320d HEAD@{1}: commit: third
            1eb059e HEAD@{2}: commit: second
            6baf32f (HEAD -> master) HEAD@{3}: commit (initial): first
            ```
    - git revert {커밋 ID}
        - 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함
        - 커밋ID는 취소하고 싶은 커밋 ID를 작성
        ```
        git log --online
        second revert 해보기

        git revert 1eb0
        문서편집창 열림
        i 눌러서 수정 가능
        esc, :wq
        git log --online

        -> d883762 (HEAD -> master) Revert "second" 저 이거 잘못했어요... This reverts commit 1eb059eac1e3051a31d84188f80e1ae5626dd2c3.
        20d320d third
        1eb059e second
        6baf32f first

        => log는 남아있지만 2txt 파일이 사라짐
        ```
        git commit -am "test" => add, commit을 한번에 (add를 한 적이 잇을 때만)

3. Git branch (master, main)
- 브랜치는 나뭇가지란 뜻으로 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 Git의 도구
- 장점
    - 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
    - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
    - Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함
    - "Branch는 Commit을 가리키는 pointer임"
- 조회
    - git branch    로컬 저장소의 브랜치 목록 확인
    - git branch -r 원격 저장소의 브랜치 목록 확인
- 생성
    - git branch {브랜치 이름}              새로운 브랜치 생성
    - git branch { 브랜치 이름} {커밋 ID}   특정 커밋 기준으로 브랜치 생성
- 삭제
    - git branch -d {브랜치 이름}   병합된 브랜치만 생성 가능
    - git branch -D {브랜치 이름}   강제 삭제

- 이동
    - 현재 브랜치에서 다른 브랜치로 이동하는 명령어
    - git switch {브랜치 이름} # 다른 브랜치로 이동
    - git switch -c {브랜치 이름} # 브랜치를 새로 생성 및 이동
    - git switch -c {브랜치 이름} {커밋 ID} # 특정 커밋 기준으로 브랜치 생성 및 이동
    - 스위치 하기 전에 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의!
    - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게 됨
```
git_branch에 git init
touch a.txt

내용 추가 커밋
내용 추가 커밋

git branch feature/signup
git switch feature/signup

touch b.txt
내용 추가 커밋

git switch master ->b.txt 사라짐

touch c.txt
내용 추가 커밋

git switch feature/signup -> b.txt 다시 생기고 c.txt 사라짐
```
- git merge
    - 분기된 브랜치들을 하나로 합치는 명령어
    - master 브랜치가 상용이므로, 주로 master 브랜치에 병합
    - git merge {합칠 브랜치 이름}
    - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야함
    - 병합 종류
        - Fast-Forward : 마치 빨리 감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법 
        - 3-way-Merge : 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법
        - Merge Conflict : 두 브랜치에서 같은 부분을 수정한 경우 충돌이 발생한 부분은 작성자가 직접 해결해야함

```
git switch master -> 메인 브랜치로 이동
git merge feature/signup -> b.txt가 master에 생김

git switch feature/signup -> c.txt 파일은 없는 상태
git merge master -> 같은 히스토리를 가지게 됨


git log --online --graph -> 각 merge가 어떻게 생겼는지 그래프로 보여줌
master에서 a.txt에 내용 추가
feature/signup에서 a.txt에 내용 추가
=> master에서 git merge feature/signup 하면
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
Automatic merge failed; fix conflicts and then commit the result 나옴

git add .
git commit -m "merge feature/signup"

$ git log --oneline --graph
*   562e625 (HEAD -> master) merge feature/signup
|\
| * b724f4d (feature/signup) update a.txt
* | a6b60cb update a.txt from master
|/
*   fef31a9 Merge branch 'feature/signup'
|\
| * 3acd983 add b.txt
* | 4bdc473 add c.txt
|/
* 7279559 둘째줄 추가
* db43f03 첫줄 추가

feature/signup 에 가서 git merge master 하면
fast-forward로 바로 합쳐짐

master branch로 이동 후 git branch -d feature/signup 하면
feature/signup 지워짐

git branch -> 모든 branch 확인해보면 master만 남아있음
```

```
+) HEAD
HEAD는 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로
결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
git log 혹은 cat.git/HEAD를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음
```

- Git workflow (branch를 어떻게 써야 더 이쁘게 쓰나 해서 만들어짐)
    - git-flow: 5개의 브랜치로 나누어 소스코드를 관리(대규모 프로젝트에 적합)
        - master : 현재 main version (항상 동작해야함)
        - develop : 개발해야하면 develop branch로 이동
        - feature branches : 개발 중 필요하면 생성하는 branch 개발이 끝나면 develop으로 합침
        - release branch : 합친 develope이 잘 동작하나 test, test 끝나면 master로 합침
        - hotfixes : 문제가 생기면 급하게 수정해서 바로 master로 보낼 수도 있고 develop으로 다시 보내서 수정
    - git-hub-flow
        - Pull Request 기능을 사용하도록 권장하며, 병합 후 배포가 자동화로 이루어짐
        - master/feature로 나누어서 feature에서 수정해서 master와 합침
    - git-lab-flow
        - master/production/pre-production 으로 나누어 개발 내용을 바로 반영하지 않고, 배포 시기를 조절
    - 브랜치를 자주 생성하는 것을 강력히 권장하며 main(master) 브랜치 하나로만 작업하는 형태는 지양해야함

- Shared repository model
    - 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
    - master 브랜치에 직접 해발하는 것이 아니라, 기능별로 브랜치를 따로 둠
    - Pull Request 사용하여 팀원간 변경 내용에 대한 소통 진행

```
repository 생성
collaborators로 멤버 추가

초대 받은 사람은 메일로 온 email에서 invitation 수락

git clone 받기

touch a.txt
vi.a.txt
i
내용 추가
esc
:wq

git add .
git commit

git branch {이름}
git switch
touch b.txt
git add .
git commit -m

git switch master

git push

초대받은 사람 git clone

git push origin {branch 이름}

remotebranch 조회 명령어: git branch -r
localbranch 조회 명령어: git branch

초대받은 사람도 branch 생성해서 commit, push

pull request, new pull request aiden branch-> master branch로 보낸다고 하면 Able to merge 라고 뜨면 conflict없이 merge 가능한 상황 create pull request 누르면 commit 내용 추가 가능 오른쪽에 reviewers 로 리뷰할 사람 지정할 수 있음
create pull request 누르면 pull request가 생김


받는 사람은 confirm merge
            local 가서 git pull


git pull, push는 무조건 master branch에서만..?

원격저장소 다른 사람의 branch를 땡겨오기
git checkout -t origin/{브랜치이름}


set upstring(?) 설정하면 remote에 설치해서 git push만 해도 됨
```

- Fork & Pull model
    - 오픈 소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
    - 원본 원격 저장소를 그대로 내 원격 저장소에 복제
    - 기능 완성 후 복제한 내 원격 저장소에 Push

```
repository 생성
생성한 사람 github에 들어가기

Fork를 눌러서 내 repository로 copy 하기

내 repository에서 clone 받기

새로운 branch를 만들어서 수정
git branch sehee
git switch sehee
파일 만들어서 내용추가
add, commit

내 remote로 push
git push origin sehee

생성한 사람에게 merge 요청 가능
pull request, new pull request

head repository의 sehee branch를 생성한 사람의 master branch로 create pull request
내가 보낸 pr 승인을 생성한 사람만 할 수 있음
승인하면 merged로 뜨고 생성한 사람 repository contributor에 내 이름이 추가됨
```