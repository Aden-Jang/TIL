### Git Advanced
1. undoing : Git 작업 다시 되돌리는 것
  - Working directory 작업 단계
    - WD에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
    - git restore
      - 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
      - `git restor를 통해 되돌리면 해당 내용을 복원할 수 없으니 주의!`
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