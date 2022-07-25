from calendar import day_name


word = 'ssafy'
print(word) # ssafy
print(id(word)) # 메모리 주소 확인 2324100369904
word = 'test'
print(word) # test
print(id(word)) # 메모리 주소 확인 2324100416688

# 문자열 조회 탐색

# .find()
print('apple'.find('p')) # 1
print('apple'.find('k')) # -1

# >>> 상태에서는 실행해도 안됨
# exit()를 입력하면 나가짐

# .index(x)
print('apple'.index('p')) # 1
#print('apple'.index('k')) # ValueError: substring not found

# .isalpha
print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True

# .isupper
print('Ab'.isupper()) # False

# .split
print('a,b,c'.split(',')) # ['a', 'b', 'c']
print('a b c'.split()) # ['a', 'b', 'c']
print('서울시 강남구 00동'.split()) # ['서울시', '강남구', '00동']
print('서울시 강남구 00동'.split()[0]) # 서울시
print('010-1234-1234'.split('-')) # ['010', '1234', '1234']

# 다양한 대소문자 변환
msg = 'hI! Everyone, I\'m ssafy'

print(msg) # hI! Everyone, I'm ssafy
print(msg.capitalize()) # Hi! everyone, i'm ssafy
print(msg.title()) # Hi! Everyone, I'M Ssafy
print(msg.upper()) # HI! EVERYONE, I'M SSAFY
print(msg.lower()) # hi! everyone, i'm ssafy
print(msg.swapcase()) # Hi! eVERYONE, i'M SSAFY

# .join
print('*'.join('ssafy')) # s*s*a*f*y
print(' '.join(['3', '5'])) # 3 5
print(' '.join(['3', '5', '8', '9'])) # 3 5 8 9

# .append()
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe, id(cafe)) # ['starbucks', 'tomntoms', 'hollys'] 2721355349120  
cafe.append('banapresso')
print(cafe, id(cafe)) # ['starbucks', 'tomntoms', 'hollys', 'banapresso'] 2721355349120
# 주소는 변하지 않음

# .insert()
cafe.insert(2, 'start')
print(cafe) # ['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso']
cafe.insert(100000, 'end')
print(cafe) # ['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'end']

# .extend()
cafe.extend(['coffee'])
print(cafe) # ['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'end', 'coffee']
cafe.extend('cup')
print(cafe) # ['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'end', 'coffee', 'c', 'u', 'p']

# .remove()
numbers = [1, 2, 3, 'hi']
print(numbers) # [1, 2, 3, 'hi']
numbers.remove('hi')
print(numbers) # [1, 2, 3]
# numbers.remove('hii') # Value Error

# .pop(i)
numbers = [1, 2, 3, 'hi']
print(numbers) # [1, 2, 3, 'hi']
word = numbers.pop()
print(word) # hi
print(numbers) # [1, 2, 3]

# .clear()
numbers = [1, 2, 3, 'hi']
numbers.clear()
print(numbers) # []

# .count(x)
numbers = [1, 2, 3, 1, 1, 1, 2, 2]
print(numbers.count(1)) # 4
print(numbers.count(100)) # 0

# .sort() - 원본 바꾸기 , sorted() - 새로운 리스트로 정렬값을 만듦
numbers = [3, 2, 5, 7]
result = numbers.sort()
print(numbers, result) # [2, 3, 5, 7] None
numbers = [3, 2, 6, 8]
# result = numbers.sorted() # 틀린 문법
result = sorted(numbers) # 맞는것
print(numbers, result) # [3, 2, 6, 8] [2, 3, 6, 8]

# .reverse()
numbers = [3, 2, 5, 1]
result = numbers.reverse()
print(numbers, result)



# 튜플

a = (1, 2, 3, 5, 1)
#a[0] = 5 # 값 변경 불가능

day_name = ('월', '화', '수', '목', '금')
print(type(day_name)) # <class 'tuple'>
print(day_name[-3]) # 수
print(day_name * 2) # ('월', '화', '수', '목', '금', '월', '화', '수', '목', ' 금')
print(id(day_name)) # 2052762477136
day_name += False, True
print(day_name) # ('월', '화', '수', '목', '금', False, True)
print(id(day_name)) # 2052758632864

# 
print('apple' in 'a') # False 거꾸로 써져있기 때문에 False
print('a' in 'apple') # True
print('hi' in 'hi I am ssafy') # True
print('서순' in ['서순', '요까일엇무', '기러기']) # True
print('서순' in ['요까일엇무', '기러기']) # False

# set

a = {}
print(type(a)) # <class 'dict'>
# set형태로 하려면 set()를 써야함

# .add() 값 하나 추가
a = {'사과', '바나나', '수박'}
print(type(a)) # <class 'set'>
print(a) # {'수박', '바나나', '사과'}
print(a.add('딸기')) # 순서가 없이 아무데나 추가됨 # None
print(a) # {'딸기', '수박', '바나나', '사과'}

# .update() 여러 값 추가 이미 있으면 따로 추가 안함
a = {'사과', '바나나', '수박'}
print(a) # {'사과', '수박', '바나나'}
a.update(['딸기', '바나나', '참외'])
print(a) # {'딸기', '참외', '사과', '바나나', '수박'}

# .remove() 버리는데 없으면 에러남
a.remove('딸기')
print(a) # {'바나나', '참외', '사과', '수박'}
# a.remove('딸기')
# print(a) # KeyError: '딸기'

# .discard() 버리는데 없어도 에러 안남
a.discard('딸기')
print(a) # {'바나나', '참외', '사과', '수박'}
a.discard('딸기')
print(a) # {'사과', '바나나', '참외', '수박'}

# .clear()
a = {'사과', '바나나', '수박', '참외', '메론'}
a.clear()
print(a) # set()

# 집합 관련 함수
a = {'사과', '바나나', '수박'}
b = {'포도', '망고'}
c = {'사과', '포도', '망고', '수박', '바나나'}
# .isdisjoint(t)
print(a.isdisjoint(b)) # True a와 b가 서로소인가?
print(a.isdisjoint(c)) # False a와 c가 서로소인가?
# .issubset(t)
print(a.issubset(c)) # True a가 c의 하위셋인가? 
print(b.issubset(c)) # True b가 c의 하위셋인가? 
print(b.issubset(a)) # False b가 a의 하위셋인가?
# .issuperset(t)
print(c.issuperset(a)) # True c가 a의 상위셋인가?
print(c.issuperset(b)) # True c가 b의 상위셋인가?
print(b.issuperset(a)) # False b가 a의 상위셋인가?


# 딕셔너리
# .pop()
my_dict = {'apple': '사과', 'banana': '바나나'}
data = my_dict.pop('apple')
print(data, my_dict) # 사과 {'banana': '바나나'}
# data = my_dict.pop('apple') # KeyError
data = my_dict.pop('apple',0)
print(data) # 0

# update()
my_dict = {'apple': '사', 'banana': '바나나'}
my_dict.update(apple = '사과')
print(my_dict) # {'apple': '사과', 'banana': '바나나'}

# 복사
# 할당
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hello'
print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]

# 얕은 복사
original_list = [1, 2, 3]
copy_list = original_list[:]
print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
copy_list[0] = 'hello'
print(original_list, copy_list) # [1, 2, 3] ['hello', 2, 3]

# 깊은 복사
import copy

a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
b = copy.deepcopy(a)
print(a, b) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b[0][2] = 'hello' 
print(a,b) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 'hello'], [4, 5, 6], [7, 8, 9]]