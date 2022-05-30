# 첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 
# 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 
# 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 
# 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)



from sys import stdin
N, M = map(int, stdin.readline().split())

inputMap = []
for i in range(N):
    oneRow = list(map(int, input().split()))
    oneRow.append(sum(oneRow))
    inputMap.append(oneRow)

# print("inputMap = ", inputMap)

answerList = []

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    sumVal = 0

    for row in range(x1, x2+1):
        # print("원래 로우의 합 = ", inputMap[row][-1])
        rowSum = inputMap[row][-1] 
        for col in range(0, N):
            # print("row = ", row, " col = ", col)
            if col < y1 or col > y2:
                # print("row = ", row, " col = ", col, " 뺄 값 = ", inputMap[row][col])
                rowSum -= inputMap[row][col]

        # print("이번 로우에서의 최종 값은 ? ", rowSum)
        sumVal += rowSum
        # print("더해지고 나서 값은 ? ", sumVal)
    answerList.append(sumVal)
    # print("answerList = ", answerList)
        
for i in range(M):
    print(answerList[i])

