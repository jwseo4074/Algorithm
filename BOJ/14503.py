N, M = map(int, input().split())

spaceMap = []
visitMap = [ [0] * M for i in range(N) ]

dx = [-1,0,1,0]
# row
dy = [0,1,0,-1]
# col

# [0] : 위쪽, [1] : 오른쪽, [2] : 아래쪽, [3] : 왼쪽

completeClean = 0

row, col, see = map(int, input().split())
# print(row, col, see)

for i in range(N):
    spaceMap.append(list(map(int, input().split() ) ) )

def turnLeft():
    global see
    see -= 1
    if see == -1:
        see = 3
        # 위 다음 왼쪽으로 돌아

visitMap[row][col] = 1
completeClean += 1
# cnt = 1

# 처음 있는 곳 청소
# 1.현재 위치를 청소한다.

# see
# 0 -> 위
# 1 -> 오른
# 2 -> 아래
# 3 -> 왼
turnCnt = 0

while(1):    

    flag = 0

    # 2.현재 위치에서 다음을 반복하면서 인접한 칸을 탐색한다.
    # 탐색 순서 : 현재 보고 있는 방향에서 왼쪽->아래쪽->오른쪽->위쪽

    # 왼쪽 쳐다보기
    for _ in range(4):
        turnLeft()
        # 왼쪽으로 한번 회전해라

        # 다음으로 이동하려는 위치, 가려고 쳐다 본 위치
        nx = row + dx[see]
        ny = col + dy[see]

        if 0 <= nx < N and 0 <= ny < M and spaceMap[nx][ny] == 0:
            # 가려는 곳이 범위 내에 있는 곳이고, 벽이 아닌 경우

            if visitMap[nx][ny] == 0:
                # 방문 안한 곳인 경우
                visitMap[nx][ny] = 1
                # 방문 체크

                completeClean += 1
                # 청소 하기

                row = nx
                col = ny
                # 위치 실제로 이동

                #청소 한 방향이라도 했으면 다음으로 넘어감
                flag = 1
                break

    if flag == 0: # 4방향 모두 청소가 되어 있을 때,
        if spaceMap[row-dx[see]][col-dy[see]] == 1: 
            #후진했는데 벽이 나오는 경우
            print(completeClean)
            break
        else:
            # 그게 아니면 
            row = row-dx[see]
            col = col-dy[see]