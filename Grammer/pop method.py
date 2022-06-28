user_1 = [1,2,3,4,5]
user_2 = [6,7,8,9,10]
user_2.append(user_1.pop(user_1[2])) # 인덱스로 뽑아낸다
print(user_1)
print(user_2)