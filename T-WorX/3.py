def solution(grid, k):
    answer = -1

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    N = len(grid)
    M = len(grid[0])
    
    visitMap = [ [0]*M for i in range(N)]
    # print(visitMap)
    
    def dfs(row, col, energy):
        global answer 

        if (row == N-1 and col == M-1) or visitMap[row][col] == 1:
            # 도착했으면 끝
            return
        
        if energy == 1 and grid[row][col] == ".":
            # 이 조건은 나중에 다시 생각하자. 에너지는 1 남았는데(한번 밖에 못가는데?) 그 곳이 평지가 아니면 어카노, 그 뒤에 평지까지 한참 남으면?
            energy += k
            answer += 1
            return

        energy -= 1
        # 에너지 하나 쓴다
        # 강만 아니면 갈 수 있다.

        for i in range(4):
            nx = col + dx[i]
            ny = row + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] != "#":
            # # 가려는 곳이 범위 내에 있는 곳이고, 벽이 아닌 경우

                if visitMap[nx][ny] == 0:
                    # 방문 안한 곳인 경우
                    visitMap[nx][ny] = 1
                    # 방문 체크

        
    dfs(0,0,0)

    return answer

grid = ["..FF", "###F", "###."]
print(solution(grid, 4))


# ".F.FFFFF.F"
# ".########."
# ".########F"
# "...######F"
# "##.######F"
# "...######F"
# ".########F"
# ".########."
# ".#...####F"
# "...#......"