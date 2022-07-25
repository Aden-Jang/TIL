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
