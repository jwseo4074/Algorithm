
from curses.ascii import isalnum


def solution(grid):
    answer = []

    lenRow = 2*len(grid) + 1
    lenCol = 2*len(grid[0]) + 1
    # print(lenRow) # 5
    # print(lenCol) # 5

    totalMap = [[0] * lenCol for _ in range(lenRow)]
    # print(totalMap)

    # grid = ["SL","LR"]
    i = 0
    j = 0

    for row in range(lenRow):
        if row % 2 != 1:
            continue
        # print("row = ", row)
        for col in range(lenCol):
            if col % 2 != 1:
                continue
            # print("col = ", col)
            totalMap[row][col] = grid[i][j]
            # print("i = ", i, " j = ", j)
            if j == len(grid[0])-1:
                i += 1
                j = 0
            else:
                j += 1
            
            if i == len(grid):
                break
        if i == len(grid):
            break

    # print(totalMap)
            

    def dfs(M, row, col, D, lenRow, lenCol):
        input()
        if row == 1 and col == 1:
            # 다시 출발점으로 돌아왔으면
            return M

        if str(M[row][col]).isalpha():
            print("여기는 노드", M[row][col])
            if M[row][col] =="U":
                dfs(M, row+1, col, "U", lenRow, lenCol)

            if M[row][col] =="L":
                dfs(M, row, col-1, "L", lenRow, lenCol)

            if M[row][col]=="D":
                dfs(M, row-1, col, "D", lenRow, lenCol)

            if M[row][col]=="R":
                dfs(M, row, col+1, "R", lenRow, lenCol)

        # 방문한 곳 1로 체크
        M[row][col] = 1
        print("( ", row,",", col, " )")
        
        # 다음 갈 곳이 범위 넘어가는 곳이면 자리 이동
        
        if D =="U":
            if row == 0:
                dfs(M, lenRow-1, col, D, lenRow, lenCol)
            else:
                dfs(M, row-1, col, D, lenRow, lenCol)

        if D =="L":
            if col == 0:
                dfs(M, row, lenCol-1, D, lenRow, lenCol)
            else:
                dfs(M, row, col-1, D, lenRow, lenCol)

        if D=="D":
            if row == lenRow-1:
                dfs(M, 0, col, D, lenRow, lenCol)
            else:
                dfs(M, row+1, col, D, lenRow, lenCol)


        if D=="R":
            if col == lenCol-1:
                dfs(M, row, 0, D, lenRow, lenCol)
            else:
                dfs(M, row, col+1, D, lenRow, lenCol)

    row = 1
    col = 1
    # print(lenRow)

    print("UP 시작")
    mapUp = dfs(totalMap, row-1, col, "U", lenRow, lenCol)
    print("Right 시작")
    mapRight = dfs(totalMap, row, col+1, "R", lenRow, lenCol)
    mapDown = dfs(totalMap, row+1, col, "D", lenRow, lenCol)
    mapLeft = dfs(totalMap, row, col-1, "L", lenRow, lenCol)


    return answer

grid = ["SL","LR"]
# results = [16]

# grid = ["S"]
# results = [1,1,1,1]

# grid = ["R","R"]	
# results = [4,4]

# print(solution(grid))
print(1 % 4)