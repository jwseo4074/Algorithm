# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다. 
# 두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

answerList = []
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    # print("x1, y1, x2, y2 = ", x1, y1, x2, y2 );
    
    answer = 0

    for i in range(int(input())):

        cx, cy, r = map(int, input().split())
        
        # if (cx-r < x1 < cx+r) and (cy-r < y1 < cy+r) and (cx-r < x2 < cx+r) and (cy-r < y2 < cy+r):
        #     # 둘 다 안에 있는 경우
        #     continue
        # if (cx-r < x1 < cx+r) and (cy-r < y1 < cy+r):
        #     # 출발점만 안에 있는 경우
        #     answer += 1
        # if (cx-r < x2 < cx+r) and (cy-r < y2 < cy+r):
        #     # 도착점만 안에 있는 경우
        #     answer += 1

        if (((cx-x1)**2 + (cy-y1)**2) ** 0.5) < r:
            if (((cx-x2)**2 + (cy-y2)**2) ** 0.5) > r:
                answer += 1
        if (((cx-x2)**2 + (cy-y2)**2) ** 0.5) < r:
            if (((cx-x1)**2 + (cy-y1)**2) ** 0.5) > r:
                answer += 1

    answerList.append(answer)

for a in answerList:
    print(a)