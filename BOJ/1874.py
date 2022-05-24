from collections import deque


resultList = deque()
inputDeque = deque()

N = int(input())

for i in range(N):
    resultList.append(int(input()))

answer = []

for i in range(1, N+1):
    # print(i, " push ")
    inputDeque.append(i)
    answer.append("+")
    while(inputDeque):
        if inputDeque[-1] == resultList[0]:
            # print(inputDeque[-1] , " pop ")
            inputDeque.pop()
            resultList.popleft()
            answer.append("-")
            
        else:
            break
if inputDeque:
    print("NO") 
    # print("다음 원소")
else:
    print(*answer)