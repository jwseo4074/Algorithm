# 키 값에 list, set이 올 수 없습니다.
# 키 값은 immutable (불변한) 객체 타입이 와야 합니다. 
# 그렇기 때문에 mutable한 변할수 있는 객체 타입인 list나 set 같은 타입은 딕셔너리의 키가 될 수 없습니다 
# 키 값은 중복 될 수 없습니다.
# 동일한 키를 추가하면 나중에 추가된 키와 값에 기존의 키와 값이 덮어띄워집니다. 
# 키 값은 고유해야하기 때문입니다. 그래야 정확히 그 데이터에 접근할 수 있기 때문입니다.


# 1. 딕셔너리 생성
d = {'a' : 123123}

# 2. 값 추가
d[999] = 10
# 숫자 키, 숫자 값

d['99'] = 111
# 문자 키, 숫자 값

d['BlockDMask'] = "blog"
# 문자 키, 문자 값

d['wow'] = [1, 2, 3, 4, 5]
# 문자 키, 리스트 값

d[(1, 2)] = "this is value"
# 튜플 키, 문자 값

d[1] = (3, 'a', 5)
# 숫자 키, 튜플 값  
 
# 3. 값 접근
print("3. 딕셔너리 값 접근")
print(f'd["a"] = {d["a"]}')
print(f'd[999] = {d[999]}')
print(f'd[1] = {d[1]}')

# 숫자 키는 index와 헷갈릴 수 있음
print(f'd[(1,2)] = {d[(1,2)]}')
print(f'd["wow"] = {d["wow"]}')
print(f'd["BlockDMask"] = {d["BlockDMask"]}')

# 4. 값 변경
print("4. 딕셔너리 값 변경")
# print(f'before : d["BlockDMask"] = {d["BlockDMask"]}')d["BlockDMask"] = 'boy'print(f'after  : d["BlockDMask"] = {d["BlockDMask"]}') print(f'before : d["a"] = {d["a"]}')d["a"] = 'asdf1234'print(f'after  : d["a"] = {d["a"]}')