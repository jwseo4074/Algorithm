# # 어떤 숫자가 줄어들지 않는다는 것은 그 숫자의 각 자리 수보다 그 왼쪽 자리 수가 작거나 같을 때 이다.
# # 예를 들어, 1234는 줄어들지 않는다. 
# # 줄어들지 않는 4자리 수를 예를 들어 보면 0011, 1111, 1112, 1122, 2223이 있다. 줄어들지 않는 4자리수는 총 715개가 있다.
# # 이 문제에서는 숫자의 앞에 0(leading zero)이 있어도 된다. 0000, 0001, 0002는 올바른 줄어들지 않는 4자리수이다.
# # n이 주어졌을 때, 줄어들지 않는 n자리 수의 개수를 구하는 프로그램을 작성하시오.

# #  0011, 1111, 1112, 1122, 2223
# #  0000, 0001, 0002

# # n이 주어졌을 때, 줄어들지 않는 n자리 수의 개수는?


# 풀이 2

# N = int(input())
# dp = []
# for i in range(0, 10):
#     dp.append(1)
# print(dp)

# 이걸 조금이나마 간단하고 짧게 줄여서?

# n = int(input())
# dp = [1 for i in range(10)]


# 입력값 주어졌을 때 그만큼 for 문 돌기
# => for i in range(int(input())): 

answerList = []

for i in range(int(input())): 
    n = int(input())
    # n = 4

    dp = [[0 for i in range(0, 11)] for i in range(0, n+1)]

    if n == 1: 
        answerList.append(10)
        break

    dp[1] = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    dp[1].append(sum(dp[1]))
    dp[2] = [ 10, 9, 8, 7, 6 ,5, 4, 3, 2, 1]
    dp[2].append(sum(dp[2]))

    for i in range(3, n+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i-1][10]
            else:
                dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
        dp[i][10] = sum(dp[i])
        # print( "dp[", i, "][10] = ", dp[i][10])
    
    # for i in range(0, n+1):   
        # print(dp[i])
    answerList.append(dp[n][10])

for i in answerList:
    print(i)
