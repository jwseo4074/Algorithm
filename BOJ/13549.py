from collections import deque
import sys
input = sys.stdin.readline

MAX = int(10e5)
N, M = map(int, input().split())
visited = [0 for _ in range(MAX+1)]
# print(visited)
answerTime = 0
answerList = []

def bfs():
    global answerTime
    global answerList

    queue = deque()
    queue.append((N, 0))
    
    while queue:
        # input()
        X, findTime = queue.pop()
        # print("X = ", X)
        

        if X == M:
            # print("찾았다 !! ")
            answerTime = findTime
            answerList.append(findTime)
            continue

        if 0 <= 2*X <= MAX and visited[2*X] == 0:
            visited[2*X] = 1
            queue.append((2*X, findTime))
            
        if 0 <= X-1 <= MAX and visited[X-1] == 0:
            visited[X-1] = 1
            queue.appendleft((X-1, findTime+1))
        if 0 <= X+1 <= MAX and visited[X+1] == 0:
            visited[X+1] = 1
            queue.appendleft((X+1, findTime+1))
        
        
        if X+1 > MAX:
            continue
        # print(queue)
bfs()
if N==M or len(answerList) == 0:
    print(0)
    
else:
    print(min(answerList))
    # print(answerList)