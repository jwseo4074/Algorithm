energy = []
tree = []
plusEnergy = []
# dieTreeList = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())

# energy = [ [ 5 for i in range(N)] for j in range(N) ]
energy = [ [5] * N for j in range(N) ]

# 처음에 5로 양분 초기화

tree = [ [ [] for i in range(N)] for j in range(N) ]
# 처음에 나무 초기화

# plusEnergy = [ [ [] for i in range(N)] for j in range(N) ]

for i in range(N):
    plusEnergy.append(list(map(int, input().split())))
    # 겨울에 추가될 양분 map

for i in range(M):
    row, col, value = map(int, input().split())
    tree[row-1][col-1].append(value)
    # 입력이 2 1 3 이면 tree[1][0] = 3 

def printTreeFunc():
    print("Tree")
    for i in range(N):
        for j in range(N):
            print(tree[i][j], end = ' ')
        print()

def printEnergyFunc():
    print("Energy")
    for i in range(N):
        for j in range(N):
            print(energy[i][j], end = ' ')
        print()

for aaa in range(K):
    print(aaa, " 년 -----------------------")
    # printTreeFunc()
    # printEnergyFunc()

    print("봄 시작")

    # 봄, 여름 같이

    for row in range(N):
        for col in range(N):
            if not tree[row][col]:
                # 나무가 없으면 바로 재껴
                continue
            
            lenTree = len(tree[row][col])
            # sumTree = sum(tree[row][col])
            # print("before sort", tree[row][col])

            # tree[row][col].sort()
            # 예를 들어서 나무가 2, 1, 5 있다 쳐

            # print("after sort", tree[row][col])
            
            
            for j in range(lenTree):
                if energy[row][col] >= tree[row][col][j]:
                    energy[row][col] -= tree[row][col][j]
                    # 양분 마이너스
                    tree[row][col][j] += 1
                    # 나이 1 증가
                else:
                    # 양분 모자라면 바로 그 때에 대해서 여름
                    # 모자랐을 때 직전까지는 한거고 모자라자마자 바로 온거니까 바로 pop 하면 되지
                    # 이게 되는 이유는 새로운 나무를 심을 때 왼쪽으로 insert(0, ) 해주니까 나이가 어린 나무가 무조건 왼쪽
                    # 그럼 문제의 조건대로 어린 나무부터 순서대로 가지

                    for k in range(j, lenTree):
                        energy[row][col] += (tree[row][col].pop() // 2)
                    break
                
            # if energy[row][col] >= sum(tree[row][col]):
            # # 안에 나무들 모두한테 양분을 줄 수 있으면?
            #     for i in range(len(tree[row][col])):

            #         energy[row][col] -= tree[row][col][i]
            #         # 양분 마이너스

            #         tree[row][col][i] += 1
            #         # 전부 나이 1 증가
                    
            # else:
            #     # 양분이 부족하면?
            #     # print("양분이 부족하다. ")
            #     # printTreeFunc()
                

            #     for i in range(len(tree[row][col])):
            #         if tree[row][col][i] <= energy[row][col]:
            #             energy[row][col] -= tree[row][col][i]
            #             # 양분 마이너스

            #             tree[row][col][i] += 1
            #             # 그 나무 나이 1 증가

            #         else:
            #             dieTreeList.append([row, col, tree[row][col][i]])
            #             tree[row][col][i] = 0
            #             # tree[row][col].remove(tree[row][col][i])

            #     while(0 in tree[row][col]):
            #         tree[row][col].remove(0)

                # i = 0
                # while(tree[row][col]):
                #     # print("tree[row][col] = ", tree[row][col])

                #     if i == len(tree[row][col]):
                #             break

                #     if tree[row][col][i] <= energy[row][col]:
                #         # 있는 양분보다 나무 나이가 작으면

                #         energy[row][col] -= tree[row][col][i]
                #         # 양분 마이너스

                #         tree[row][col][i] += 1
                #         # 그 나무 나이 1 증가
                #         i += 1

                #     else:
                #         dieTreeList.append([row, col, tree[row][col][i]])
                #         tree[row][col].remove(tree[row][col][i])
                #         # print("row = ", row, " col = ", col, " i = ", i)
                #         # print("죽는 나무 ", dieTreeList)


    # print()
    # print("봄이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()
    

    # print("여름 시작")
    # 여름

    # for row in range(N):
    #     for col in range(N):
    # 필요 없음

    # for i in range(len(dieTreeList)):
    #     # print("row = ", row, " col = ", col, " i = ", i)
        
    #     # print("추가된 양분 = ", int(dieTreeList[i][2]/2))
    #     energy[dieTreeList[i][0]][dieTreeList[i][1]] += int(dieTreeList[i][2]/2)

    # dieTreeList.clear()
    
    # # print()
    # print("여름이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()

    # print("가을 시작")
    # 가을
    # for row in range(N):
    #     for col in range(N):
    #         if tree[row][col]:
    #             for i in range(len(tree[row][col])):
    #                 if tree[row][col][i] % 5 == 0:
    #                     if row-1 >= 0 and col-1 >= 0:
    #                         tree[row-1][col-1].append(1)
    #                     if row-1 >= 0:
    #                         tree[row-1][col].append(1)
    #                     if row-1 >= 0 and col+1 < N:
    #                         tree[row-1][col+1].append(1)
    #                     if col-1 >= 0:
    #                         tree[row][col-1].append(1)
    #                     if col+1 < N:
    #                         tree[row][col+1].append(1)
    #                     if row+1 < N and col-1 >= 0:
    #                         tree[row+1][col-1].append(1)
    #                     if row+1 < N:
    #                         tree[row+1][col].append(1)
    #                     if row+1 < N and col+1 < N:
    #                         tree[row+1][col+1].append(1)
    
    print("봄, 여름 끝")
    printTreeFunc()
    printEnergyFunc()

    print()

    print("가을 시작")
    print()

    for row in range(N):
        for col in range(N):
            for age in tree[row][col]:
                if age % 5 == 0:
                    for l in range(8):
                        nx = row + dx[l]
                        ny = col + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].insert(0, 1)

    print()
    print("가을이 지나갔다")     
    printTreeFunc()
    printEnergyFunc()
    

    print("겨울 시작")
    # 겨울
    
    for row in range(N):
        for col in range(N):
            if plusEnergy[row][col]:
                energy[row][col] += plusEnergy[row][col]

    print()
    print("겨울이 지나갔다")     
    printTreeFunc()
    printEnergyFunc()

answer = 0
for row in range(N):
    for col in range(N):
        answer += len(tree[row][col])
print(answer)