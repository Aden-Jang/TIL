# PJT01
### 이번 PJT로 배운 새로 알게된 내용

- json 패키지 불러오기
  ```py
  import json
  ```

- 딕셔너리를 만들 때 {}를 사용하면 key값에 ''를 해줘야 하지만 dict()함수를 사용해 만들면 ''를 사용하지 않아도 생성된다.

- 파일 열기
  ```py
  open('파일이름', encoding = 'utf-8')
  ```
  - utf-8은 유니코드를 위한 문자 인코딩, 이것으로 고정
  - open함수에서도 f-string사용이 가능하다

- json파일 리스트로저장하기
  ```py
  '변수명' = json.load(내용)
  ```

- pprint - print를 더 깔끔하게 해주는 함수
  ```py
  from pprint import pprint
  ```

- 딕셔너리를 value값으로 정렬하기
  ```py
  a = sorted(a.items(), key = lambda x: x[1], reverse = True)
  ```
---
---
### 문제당 어려웠던 부분 및 아쉬운점, 후기
---
- 문제 A - 딱히 없었다.
---
- 문제 B 
```py
import json
from pprint import pprint

# 리스트의 인덱스를 찾는 과정에서 []를 여러번 쓰는 과정이 헷갈려 조금 헤멨다.
# 이중 for문을 이용하지 않고 푸는 방법을 모르겠어서 우선 이중 for문으로 해결했는데 좀 복잡해 보이는 것 같아 아쉽다.
def movie_info(movie, genres):
    genre_names = []
    for j in range(len(movie["genre_ids"])):
        for i in range(len(genres)):
            if movie['genre_ids'][j] == genres[i]['id']:
                genre_names.append(genres[i]['name'])
    a = dict(
        id = movie['id'], 
        title = movie['title'], 
        poster_path = movie['poster_path'], 
        vote_average = movie['vote_average'], 
        overview = movie['overview'], 
        genre_ids = genre_names
    )
    return a 
        

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
```
---
- 문제 C
```py
import json
from pprint import pprint

# 3중 for문을 사용하다보니 더 복잡해지고, 인덱스값을 찾을 때에도 []가 3개도 들어가니 복잡하고 헷갈렸다.
# for문을 사용하지 않고 해결하는 방법도 알고싶다.
# 딕셔너리와 리스트 형태가 섞여있다보니 인덱스 값을 구할 때 key값을 넣어야 할 지,
# 숫자를 넣어야 할 지를 여러번의 시행착오를 거쳐야만 확인할 수 있었다. 
def movie_info(movies, genres):
    b = []
    for k in range(len(movies)):
        genre_names = []
        for j in range(len(movies[k]["genre_ids"])):
            for i in range(len(genres)):
                if movies[k]['genre_ids'][j] == genres[i]['id']:
                    genre_names.append(genres[i]['name'])
        a = dict(
            id = movies[k]['id'], 
            title = movies[k]['title'], 
            poster_path = movies[k]['poster_path'],
            vote_average = movies[k]['vote_average'], 
            overview = movies[k]['overview'], 
            genre_ids = genre_names
        )
        b.append(a)

    return b

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
```
---
- 문제 D
```py
import json

# 
def max_revenue(movies):
    d = 0
    for i in range(len(movies)):
        a = movies_list[i]['id']
        # f-string이 print에만 적용되는 줄 알았는데 open에도 사용할 수 있다는 것을 깨닫고 사용했다
        b = open(f'data/movies/{a}.json', encoding='utf-8')
        c = json.load(b)
        e = c['revenue']
        if e > d:
            d = e
            f = i
    return movies[f]['title']

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
```
---
- 문제 E
```py
import json


def dec_movies(movies):
    a=[]
    # 인덱싱으로 말고 날짜형식으로 변환해서 월에 해당하는 값을 구하는 것이 더 좋은 코드일 것같다.  
    for i in range(len(movies)):
        f = movies_list[i]['id']
        b = open(f'data/movies/{f}.json', encoding='utf-8')
        c = json.load(b)
        e = c['release_date']
       if e[5:7] == "12":
            a.append(movies[i]['title'])
    return a
    
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
```
---
- 문제 F - 문제E와 거의 동일한 방식으로 풀었다.
---
- 문제 G
```py
import json
# 배급사가 굉장히 다양하여 이것이 맞는 코드인지 확인하기 어려웠다
# 딕셔너리의 value값으로 정렬하는 것을 몰라 좀 헤멨다.(구글링을 통해 해결)
# 결과값이 보기에 좀 불편해서 아쉬웠다.
def company(movies):
    a = dict()
    for i in range(len(movies)):
        f = movies_list[i]['id']
        b = open(f'data/movies/{f}.json', encoding='utf-8')
        c = json.load(b)
        for j in range(len(c["production_companies"])):
            if c["production_companies"][j]["name"] not in a.keys():
                a[c["production_companies"][j]["name"]] = 1
            else:
                a[c["production_companies"][j]["name"]] = a[c["production_companies"][j]["name"]] + 1
    a = sorted(a.items(), key = lambda x: x[1], reverse = True)
    b=[]
    for i in range(len(a)):
        b.append(a[i][0])
    return b

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    print(company(movies_list))
```
---
## 전체적인 후기
- 처음에 주석을 안달았었는데 다 끝나고 주석을 달아두니 주석을 표기하는 것이 훨씬 보기에 편하다는 것을 알았다.
- 주석을 너무 많이 달면 더 읽기 불편함...
- 이전에 for문을 자주 사용하여 좀 익숙해 모든 문제를 for문을 사용해서 풀었는데, for문이 여러겹으로 겹치다보면 굉장히 복잡해져서 사용에 좀 불편을 겪었다.
- for문을 사용하지 않고 풀이하는 방법을 배우고싶다.(for문이 나쁘다는 것은 아니지만, 인덱싱을 하거나 반복하는 게 코드가 더 짧아질 것같다고 생각한다.)