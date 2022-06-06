from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 100000

visit = [0 for i in range(0, MAX+1)]
# print("visit = ", visit[100000])

def bfs():
    global time
    queue = deque()
    queue.appendleft((N, 0))

    while(queue):
        # input()
        X, nowtime = queue.pop()
        # print("X = ", X ," time = ", nowtime)

        if X == M:
            print(nowtime if N!=M else 0)
            break
        
        if 0 <= X <= MAX:
            if visit[X] == 0:
                visit[X] = 1
                queue.appendleft((X-1, nowtime+1))
                queue.appendleft((X+1, nowtime+1))
                queue.appendleft((2*X, nowtime+1))

bfs()

