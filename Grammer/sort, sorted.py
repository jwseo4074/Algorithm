
record = [['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]

print(record)
record = sorted(record, key = lambda x : x[0])
sorted(record, key = lambda x : x[0])
# 아무런 변화 x, 새로운 값 생성했는데 그걸 쓰질 못하니까
print(record)


record2 = [['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]
print(record2)
record2.sort(key = lambda x : x[0])
# 그 값 자체를 변경하니까 이건 괜찮음
# 그대로 출력해도 바뀐 값이 출력됨
print(record2)