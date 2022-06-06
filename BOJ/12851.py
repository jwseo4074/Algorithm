from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 100000

visit = [0 for i in range(0, MAX+1)]

answerCnt = 0
answerTime = 0

def bfs():
    global answerCnt
    global answerTime

    queue = deque()
    queue.appendleft((N, 0))

    while(queue):
        # input()
        # print("Queue = ", queue)
        X, nowtime = queue.pop()
        visit[X] = 1
        # print("visit[X] = ", visit[X])
        # X 꺼내서 방문체크

        if X == M:
            # print(nowtime if N!=M else 0)
            answerCnt += 1
            answerTime = nowtime
            continue

        else:
            for nx in [X-1, X+1, 2*X]:
                if (0 <= nx <= MAX) and (visit[nx] == 0 or visit[nx] == visit[X] + 1):
                    queue.appendleft((nx, nowtime+1))

bfs()
print(answerTime)
print(answerCnt)