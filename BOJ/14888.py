N = int(input())
numList = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxVal = -1e9
minVal = 1e9

def dfs(i,resultVal):
    global add, sub, mul, div, maxVal, minVal

    if i == N:
        maxVal = max(maxVal,resultVal)
        minVal = min(minVal,resultVal)
    else:
        if add > 0:
            add -= 1
            # 하기 전에 쓰고
            dfs(i+1,resultVal + numList[i])
            # 그거 진행하고
            add += 1
            # 끝나면 다시 돌려주고
        if sub > 0:
            sub -= 1
            # 하기 전에 쓰고
            dfs(i+1,resultVal - numList[i])
            # 그거 진행하고
            sub += 1
            # 끝나면 다시 돌려주고
        if mul > 0:
            mul -= 1
            # 하기 전에 쓰고
            dfs(i+1,resultVal * numList[i])
            # 그거 진행하고
            mul += 1
            # 끝나면 다시 돌려주고
        if div > 0:
            div -= 1
            dfs(i+1, int(resultVal / numList[i]))
            # 그거 진행하고
            div += 1
            # 끝나면 다시 돌려주고

dfs(1, numList[0])

print(maxVal)
print(minVal)


# print(int(107/6))
# print(105//6)
