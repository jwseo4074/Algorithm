inputnum = int(input())
dp = [0 for _ in range(101)]

dp[1] = 1
dp[2] = dp[1]
dp[3] = dp[1]
dp[4] = dp[1] + dp[3]
dp[5] = dp[4]

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

answer = []

for _ in range(int(inputnum)):
    x = int(input())
    answer.append(dp[x])

for i in range(inputnum):
    print(answer[i])
