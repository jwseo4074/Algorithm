from collections import deque
import sys
input = sys.stdin.readline

MAX = 100000

N, K = map(int, input().split())
visit = [0 for i in range(0, MAX+1)]
pathList = [0 for i in range(0, MAX+1)]
answerList = deque()

def bfs():
    queue = deque()

    queue.append((N,0))
    pathList[N] = -1
    visit[N] = 1

    while queue:
        # input()
        X, nowTime = queue.pop()
        # print("X = ", X)
        if X == K:
            # print("찾았음")
            # 타고온 경로를 어떻게 기억해주냐? 
            print(nowTime)
            idx = K
            while (1):
                val = pathList[idx]
                # print("idx = ", idx)
                answerList.appendleft(idx)
                # print(idx, " 는 ", val, " 에서 왔어 ")
                # print(val)
                # val = 18, idx = 17
                if val == -1:
                    # print("val이 -1 이네 ?")
                    break
                idx = val
            print(*answerList)
            break

        
        for nx in [2*X, X+1, X-1]:
            if 0 <= nx <= MAX and visit[nx] == 0:
                visit[nx] = 1
                queue.appendleft((nx, nowTime+1))
                pathList[nx] = X
                # print(nx, " 는 ", X, " 으로 부터 왔어 ")

bfs()