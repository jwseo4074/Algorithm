from collections import deque

def solution(maps):
    answer = 0

    # BFS 함수 정의
    def bfs(i, j, maps):
        answer = 0
        n = len(maps)
        # 로우 길이, 5
        m = len(maps[0])
        # 컬럼 길이, 5

        visited = [[0] * m for _ in range(n)]
        # print(visited)

        dx = [1, 0, -1, 0]
        dy = [0, 1,  0, -1]
        # 오른쪽, 아래쪽, 왼쪽, 위쪽

        queue = deque()
        queue.appendleft(((i,j), 1))
        # 현재 노드를 방문 처리

        visited[i][j] = 1
        
        # 큐가 빌 때까지 반복
        while queue:
            # input()

            # 큐에서 하나의 원소를 뽑아 출력
            item, answer = queue.popleft()
            row, col = item
            # print("row = ", row, " col = ", col)

            if row == n-1 and col == m-1:
                return answer
                
            for i in range(4):
                nx = col + dx[i]
                ny = row + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if visited[ny][nx] == 0 and maps[ny][nx] == 1:
                    visited[ny][nx] = 1
                    queue.append(((ny, nx), answer+1))
            # print("queue = ", queue)
        
        return -1
        
    answer = bfs(0, 0, maps)
    
    return answer

# maps = [
#     [1,0,1,1,1],
#     [1,0,1,0,1],
#     [1,0,1,1,1],
#     [1,1,1,0,1],
#     [0,0,0,0,1]
# ]	
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	

print(solution(maps))