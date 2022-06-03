from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
# print(M)
inputMap = [ [0] * (M+1)]
# print(inputMap)
for i in range(1, N+1):
    inputMap.append([0] + list(input()))
# print(inputMap)

for i in range(1, N+1):
    for j in range(1, M+1):
        inputMap[i][j] = int(inputMap[i][j])

# print(inputMap)
def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        row, col = queue.popleft()
        # 처음엔 1 1 이겠지

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = col + dx[i]
            ny = row + dy[i]

            if nx < 1 or nx > M or ny < 1 or ny > N:
                continue

            if inputMap[ny][nx] == 0:
                continue
            
            if inputMap[ny][nx] == 1:
                inputMap[ny][nx] = inputMap[row][col] + 1
                queue.append((ny, nx))
    # print(inputMap)
    return inputMap[N][M]

print(bfs(1,1))
