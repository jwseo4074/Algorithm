# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

randMap = []
visitMap = []
cnt = 0

def inputSize():
    a, b = map(int, input().split())
    return a, b

def makeMap(col, row):
    global cnt
    randMap.clear()
    visitMap.clear()
    cnt = 0
    for j in range(0, row):
        randMap.append(list(map(int, input().split())))
    for j in range(0, row):
        visitMap.append([0] * col)

def dfs(row, col):
    # input()
    # print("dfs 입장, row = ", row, ", col = ", col)
    if col < 0 or row < 0 or col >= len(randMap[0]) or row >= len(randMap):
        # print("범위 넘어갔어, 나가")
        return 0

    if visitMap[row][col] == 1:
        # print("이미 방문한 곳이야, 나가")
        return 0
    
    visitMap[row][col] = 1
    # print("처음 왔어 방문 체크 ", "visitMap[",row, "][", col, "]", "=", visitMap[row][col])
    # 이미 온 곳도 아니고 범위도 맞다 => 방문했다고 체크

    if(randMap[row][col] == 1):
        # 온 곳이 땅이 맞으면
    
        # print("12시 방문")
        dfs(row-1, col) 

        # print("1-2시 방문")
        dfs(row-1, col+1) 

        # print("3시 방문")
        dfs(row, col+1) 

        # print("4-5시 방문")
        dfs(row+1, col+1)

        # print("6시 방문")
        dfs(row+1, col)
        
        # print("7-8시 방문")
        dfs(row+1, col-1)

        # print("9시 방문")
        dfs(row, col-1)  

        # print("10-11시 방문")
        dfs(row-1, col-1)


def main():
    while(1):
        col, row = inputSize()
        if col == 0 and row == 0:
            return
        global cnt
        makeMap(col, row)

        for i in range(0, row):
            for j in range(0, col):
                if(visitMap[i][j] == 1 or randMap[i][j] == 0): 
                    # 방문 한 곳(발자국이 있거나)이거나 바다면 거기서 시작도 안해( 발잦국을 찍을 수 있는 가능성이 없어)
                    continue 
                cnt += 1
                # 시작하는, 발 딛고 있는 그 부분은 무조건 섬이라는 가정으로 시작
                dfs(i, j)
                # 갈 수 있는 곳은 다 가면서 발자국을 찍어
                
        print(cnt)
main()


# 시간 복잡도는 M*N