# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

N = int(input())
input_map = []
for _ in range(N):
    input_map.append(list(map(int, input())))
visit_map = [[0] * N for _ in range(N)]
count = 0
#입력
count_list = []

# 탐색 순서 => 왼 아래 오른 위
def dfs(row, col):
    global count
    # print("row = ", row, "col = ", col, "count = ", count)
    # 범위 넘으면 ? 리턴
    if row < 0 or row >= N or col < 0 or col >= N:
        return
    # 방문 했던곳이면 ? 리턴
    if visit_map[row][col] == 1:
        return
    # 집이 없으면 ? 리턴
    if input_map[row][col] == 0:
        visit_map[row][col] = 1
        return
    # 카운트가 왜 자꾸 지랄

    visit_map[row][col] = 1
    count += 1

    dfs(row, col+1) # 오른쪽
    dfs(row+1, col) # 아래쪽
    dfs(row, col-1) # 왼쪽
    dfs(row-1, col) # 위쪽

answer = 0
for row in range(N):
    for col in range(N):
        # print(row,col)
        if visit_map[row][col] == 0 and input_map[row][col] == 1:
            #  방문 안한곳이고 그자리에 집이 있으면
            count = 0
            dfs(row,col)
            count_list.append(count)
            # 한번 dfs 끝까지 타고 들어갔다가 나오면 1로 연결된 집 카운트 += 1
            answer += 1
print(answer)
count_list.sort()
for num in count_list:
    print(num)
