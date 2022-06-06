from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 100000

visit = [0 for i in range(0, MAX+1)]
# print("visit = ", visit[100000])

answerTime = -1
answerCnt = 0

def bfs():
    global answerTime
    global answerCnt

    queue = deque()
    queue.appendleft((N, 0))

    while(queue):
        input()
        X, nowtime = queue.pop()
        print("X = ", X ," time = ", nowtime, " 방문 체크")
        visit[X] = 1

        if X == M:
            print("찾았다")
            if answerTime == -1: # 처음 찾았을 때 => 최단 시간
                answerTime = nowtime

            if answerTime == nowtime: # 또 찾았을 때, 근데 같은 시간임
                answerCnt += 1
                print("AAA")
                continue
            else :
                # 시간 더 오래 걸린거는 필요없어
                print("BBB")
                break
        
        print("visit Map")
        for i in range(1, 10):
            print("i = ", i, " ", visit[i])

        for nx in [X-1, X+1, 2*X]:
            if 0 <= nx <= MAX and visit[nx] == 0:
                queue.appendleft((nx, nowtime+1))
                print("queue = ", queue)

bfs()
print(answerTime if N!=M else 0)
print(answerCnt)