a = [1, 2, 3]
b = a 
# shallow copy
b[0]= 5
print(a)
print(b)

print()
# 방법 1. list의 슬라이싱을 통한 새로운 값을 할당

c = [1,2,3]
d = c[:]
c[0] = 5
print(c)
print(d)

print()
# 방법 2. deepcody 메서드 이용

import copy
e = [1,2]
f = copy.deepcopy(e)
e[1] = 5
print(e)
print(f)