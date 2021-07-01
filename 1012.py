
def dfs(row, col):
    global cnt
    if row >= m or row < 0 or col >= n or col < 0:
        print("범위 밖이에요")
        return False
    if input_map[row][col] == 1:
        dfs(row+1,col)
        dfs(row, col+1)
        return True
    else:
        return False


m = 0
n = 0
k = 0
cnt = 0
input_map = []
t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())

    input_map = [[0]*m for _ in range(n)]
    #print(input_map)

    for _ in range(k):
        col,row = map(int, input().split())
        #print("col = " , col, "row = ", row)
        input_map[row][col] = 1
        #print(col, "," , row, " " , input_map[row][col])
    for i in range (m):
        for j in range(n):
            if dfs(i,j) == True :
                cnt += 1
    print(cnt)

