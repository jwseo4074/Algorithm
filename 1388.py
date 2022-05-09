# 형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 
# 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 
# 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.
# 이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 
# 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.
# 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

# 6 9
# -||--||--
# --||--||-
# |--||--||
# ||--||--|
# -||--||--
# --||--||-

# 풀이 1

# row, col = map(int, input().split())
# inputMap = [[ "-" for i in range(0,col+1)] for j in range(0, row+1)]
# visitMap = [[ 0 for i in range(0,col+1)] for j in range(0, row+1)]
# # print(inputMap)
# cnt = 0

# for i in range(0, row):
#     onerow = input()
#     for j in range(0, len(onerow)):
#         if onerow[j] == "|":
#             inputMap[i][j] = "|"
# # print(inputMap)
# # 입력 어떻게 깔끔하게 받는지 코드 보기

# def dfs(startRow, startCol):
#     global cnt

#     # input()
#     # print(startRow, startCol, " dfs 시작하려고 들어옴")

#     if startRow >= row  or startRow < 0 or startCol < 0 or startCol >= col:
#         # print("범위 넘어서 리턴")
#         return

#     if visitMap[startRow][startCol] == 1:
#         # print("이미 왔던 곳이라 리턴")
#         return
    
#     visitMap[startRow][startCol] = 1
#     # print(startRow, startCol, " 방문 체크")
#     # if startRow == row-1 or startCol == col-1:
#     #     return

#     if inputMap[startRow][startCol] == '-':
#         # print(startRow, startCol, " is -")
#         if startCol < col:
#             if inputMap[startRow][startCol+1] == '-':
#                 dfs(startRow,startCol+1)
#         else:
#             return
#     else:
#         # print("here is |")
#         if startRow < row:
#             if inputMap[startRow+1][startCol] != '-':
#                 dfs(startRow+1,startCol)
#         else:
#             return

# for i in range(0, row):
#     for j in range(0, col):
#             if visitMap[i][j] != 1:
#                 # print("i = ", i, "j = ", j)
#                 cnt += 1
#                 dfs(i,j)
#                 # print("cnt = ", cnt )
# print(cnt)

# 풀이 2

row, col = map(int, input().split())
cnt = 0
# inputMap = [[ "-" for i in range(0,col+1)] for j in range(0, row+1)]

# for i in range(0, row):
#     onerow = input()
#     for j in range(0, len(onerow)):
#         if onerow[j] == "|":
#             inputMap[i][j] = "|"


# 입력 깔끔하게 받기

inputMap = []
for _ in range(row):
    inputMap.append(list(input()))

for i in range(row):
        a = ''
        for j in range(col):
            if inputMap[i][j] == '-':
                if inputMap[i][j] != a:
                    cnt += 1
            a = inputMap[i][j]

for j in range(col):
    a = ''
    for i in range(row):
        if inputMap[i][j] == '|':
            if inputMap[i][j] != a:
                cnt += 1
        a = inputMap[i][j]

print(cnt)