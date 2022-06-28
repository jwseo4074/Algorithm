def move(r, c, d):
    global directions, n, m
    dx, dy = directions[d]
    return (r + dx) % n , (c + dy) % m

def rotate(d, node):
    if node == 'R':
        d = (d + 1) % 4
    elif node == 'L':
        d = (d - 1) % 4
        # -1 % 4 => 3
    return d

def solution(grid):
    # grid = ["SL","LR"]

    global n, m, answer, directions
    answer = []
    n = len(grid) # 2 , row
    m = len(grid[0]) # 2, col

    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    # print("visited = ", visited)
    # 모든 방향이 False인 길이 4짜리 1차원 배열 -> 이게 원소 한 개, => 이게 m(col) x n(row) 사이즈로
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]] 
    # D, L, U, R

    for r in range(n):
        for c in range(m):
            for d in range(4):
                # 아래, 왼쪽, 위, 오른쪽 전부 본다
                input()
                print("r, c, d = ", r,c,d)
                if not visited[r][c][d]:
                    cx, cy, cd = r, c, d
                    cnt = 0
                    while not visited[cx][cy][cd]:
                        # True 가 나오면 while 나와
                        visited[cx][cy][cd] = True
                        cnt += 1
                        cx, cy = move(cx, cy, cd)
                        # 다음 번 방문할 곳
                        cd = rotate(cd, grid[cx][cy])
                        # 다음 번 방문할 곳에서 방향
                    answer.append(cnt)
    return sorted(answer)

grid = ["SL","LR"]
# results = [16]

# grid = ["S"]
# results = [1,1,1,1]

# grid = ["R","R"]	
# results = [4,4]

print(solution(grid))