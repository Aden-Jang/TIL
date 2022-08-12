s = 'Reverse this strings'
ss = ''
for i in s:
    ss = i+ss
print(ss)

# st1 = 1234
# st2 = 'Abc'
#
# if st1 > st2:
#     print(f'{st1} > {st2}')
# else:
#     print(f'{st1} < {st2}')

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    return i

def iota(a):
    i = a
    st = ''
    while i > 0:
        st = chr(i%10 + ord('0')) + st
        i //= 10
    return st

s = '123'
a = atoi(s)
print(a)
ss = 123
aa = iota(ss)
print(aa)