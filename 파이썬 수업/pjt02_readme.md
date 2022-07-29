# PJT02
### 이번 PJT로 배운 새로 알게된 내용

- API불러오기 
```py
import requests
URL = http://주소
a = requests.get(URL).json()
```

- 자료를 특정 자료로 정렬
```py
sorted(value, key = lambda x:x[])
```
를 통해 특정 자료값으로 정렬 가능

---
---

### 문제당 어려웠던 부분 및 아쉬운점, 후기
---
- 문제 1
```py
import requests
# json데이터에 인덱스로 접근하는 것이 보기 좀 힘들었어서 인덱스 찾기가 살짝 어려웠다.
def popular_count():
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&page=1
    popcount = len(requests.get(URL).json()["results"])
    return popcount 

```
---
- 문제 2 - 딱히 어려웠던 것은 없음, [i]를 자꾸 깜빡하는 실수를 함
```py
import requests
from pprint import pprint

def vote_average_movies():
 
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&page=1"
    pop = []
    a = requests.get(URL).json()["results"]
    for i in range(len(a)):
        if a[i]["vote_average"] >= 8:
            pop.append(a[i])
    return pop
```
---
- 문제 3
```py
import requests
from pprint import pprint

def ranking():
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&page=1"
    a = requests.get(URL).json()["results"]
    # 정렬 과정 중 lambda함수를 사용하는 것을 몰라서 찾아봤고, 해결했다.
    r = sorted(a,key = lambda x : x['vote_average'], reverse= True)
    # 인덱스로 끊는 것 말고 head를 사용해보려 했으나 추가적인 import가 필요해 사용하지 않았다.
    return r[0:5]
```
---
- 문제 4
```py
import requests
from pprint import pprint

def recommendation(title):

    # 변수 정의할 때도 f스트링을 사용하여 쉽게 정의 가능해서 좋았다.
    URL =  f"https://api.themoviedb.org/3/search/movie?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&query={title}&page=1&include_adult=false"
    a = requests.get(URL).json()["results"]
    # return None을 어디서 해야할지 헷갈려 좀 헤멨다.
    if a == []:
        return None
    else:
        id = a[0]["id"]
    URL2 = f"https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&page=1"
    b = requests.get(URL2).json()["results"]
    rec = []
    # 인덱스로 접근하기 위해 사용하는 괄호가 많아 헷갈려 자꾸 빠트리는 실수를 범하는 것이 아쉬움
    for i in range(len(b)):
        rec.append(b[i]["title"])
    return rec
```
---
- 문제 5
```py
import requests
from pprint import pprint


def credits(title):
    URL =  f"https://api.themoviedb.org/3/search/movie?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko&query={title}&page=1&include_adult=false"
    a = requests.get(URL).json()["results"]
    if a == []:
        return None
    else:
        id = a[0]["id"]
    URL2 = f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=566bffe0702bb8b958dcfec79b92065c&language=ko"
    # 자료 형태 파악하는데 시간이 좀 걸렸다.
    actor = requests.get(URL2).json()["cast"]
    director = requests.get(URL2).json()["crew"]
    act = []
    dire = []
    # 여기서도 [i],[j]를 빼먹는 실수를 했다. 지속적으로 확인해줘야할 듯 싶다.
    for i in range(len(actor)):
        if actor[i]["cast_id"] < 10:
            act.append(actor[i]["name"])
    for j in range(len(director)):
        if director[j]["department"] == "Directing":
            dire.append(director[j]["name"])
    ans = {"cast" : act,"directing" : dire}
    return ans
```
---
# 전체적인 후기
- 코드 재사용을 하지만 변수만 계속 바꿔주는 복붙을 많이 한 것 같아 아쉬웠다.
- 따로 함수를 만든다 해도 뭔가 어떻게 작동할 지 몰라서 만들지 않았다.
