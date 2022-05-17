inputList = []

N = int(input())

X = list(map(int, input().split()))

for i in range(N):
    inputList.append([i, X[i], 0])

sortedList = sorted(inputList, key = lambda x : x[1])

print(sortedList)

cnt = 0

for i in range(N):
    if i == 0:
        cnt = 0
        sortedList[i][2] = 0
        continue
    
    if sortedList[i-1][1] != sortedList[i][1]:
        cnt += 1

    sortedList[i][2] = cnt

print(sortedList)

answerList = sorted(sortedList, key = lambda x : x[0])

print(answerList)


for i in range(N):
    print(answerList[i][2], end=' ')