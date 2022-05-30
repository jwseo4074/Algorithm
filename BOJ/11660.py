from sys import stdin

N, M = map(int, stdin.readline().split())

# inputMap = []
# for i in range(N):
#     inputMap.append(list(map(int, stdin.readline().split())))
# 이거 대신에 밑에 코드

inputMap = [[0] * (N+1)] 
# 첫 번째 로우만 먼저 만들어주고 => 어차피 안쓰는 로우

for _ in range(N):
    oneRow = [0] + list(map(int, stdin.readline().split()))
    # [0] 먼저 넣어두고 그 뒤로 추가, 어차피 0번 컬럼은 안쓰니까
    inputMap.append(oneRow)
# print(inputMap)
# 입력값이 1부터 시작하므로 (배열의 시작은 0이잖아) N+1 만큼 만들어준다.
# 나는 이전에 입력값에다가 -1 을 해줘서 풀이를 진행했는데 이게 더 편할 수 있겠다.
# 잘 익혀뒀다가 다음번에 써먹자 (컬럼, 로우 1부터 시작할 경우)

# 1. 행 별로 더하기
for i in range(1, N + 1):
    for j in range(1, N):
        inputMap[i][j + 1] += inputMap[i][j]

# 2. 열 별로 더하기
for j in range(1, N + 1):
    for i in range(1, N):
        inputMap[i + 1][j] += inputMap[i][j]

# N까지 합 다 만들어놨음 
# 이제 빼줄 차례

for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(inputMap[x2][y2] - inputMap[x1 - 1][y2] - inputMap[x2][y1 - 1] + inputMap[x1 - 1][y1 - 1])
