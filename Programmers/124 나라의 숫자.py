# 1=>1	
# 2=>2	
# 3=>4	
# 4=>11	
# 5=>12	
# 6=>14
# 7=>21
# 8=>22
# 9=>24
# 10=>41

# n은 500,000,000이하의 자연수 입니다.
n = int(input())
# if n == 1:
#     x = "1"
# elif n == 2:
#     x = "2"
# elif n == 3:
#     x = "3"
# else:
#     x = ""
#     a = n%3

#     if a == 0:
#         x += "4"
#     if a == 2:
#         x += "2"
#     if a == 1:
#         x += "1"

# print(x)

# dic = {1: 1, 2: 2, 0: 4}
answer = ''
while n:
    input()
    # answer += str(dic[n % 3])
    # 나누어 떨어지면? => 4 추가
    # 2 남으면 => 2 추가
    # 1 남으면 => 1 추가
    # print("result = ", answer)

    if n % 3:
        # 3으로 나누어 떨이지지 않을 때
        answer += str(n % 3)
        n = n//3

    else:
        # 3으로 나누어 떨어질 때
        answer += "4"
        n = n//3 - 1

print(answer[::-1])
# 거꾸로 뒤집어 주기
