"""
첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다.
( 1 <= N , M <= 1000 )
두번째 줄부터 N+1 번째 줄까지 얼음틀의 형태가 주어집니다.
이때 구멍이 뚫려있는 부분은 0 , 그렇지 않은 부분은 1입니다.
한번에 만들 수 있는 아이스크림의 개수를 출력합니다.
입력 예시
4 5
00110
00011
11111
00000

"""

def dfs(x, y):
    global row
    global col

    if x<=-1 or x>=row or y<=-1 or y>=col :
        print("범위 밖임")
        return False
    if graph[x][y] == 0 :
        print("\n 방문 안한곳이네")
        ## 방문하지 않은곳이다 ?
        graph[x][y] = 1
        print("x= ", x , "y= " ,y,"방문처리 해줌")
        ## 방문처리 해주고
        ## 상 하 좌 우 전부 다시 ㄱ
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    print("방문 한곳임 그냥 false 리턴함 ")
    return False

row,col = map(int, input().split())

graph = []
for i in range(row):
    graph.append(list(map(int,input())))
result = 0
for i in range(row):
    for j in range(col):
        if dfs(i,j) == True:
            result += 1
print(result)


