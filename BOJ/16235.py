# 5 2 1
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 3 2 3 2
# 2 1 3
# 3 2 3

energy = []
tree = []
plusEnergy = []

N, M, K = map(int, input().split())

energy = [ [ 5 for i in range(N)] for j in range(N) ]
# 처음에 5로 양분 초기화

tree = [ [ [] for i in range(N)] for j in range(N) ]
# 처음에 나무 초기화

plusEnergy = [ [ 0 for i in range(N)] for j in range(N) ]

for i in range(N):
    plusEnergy[i] = list(map(int, input().split()))
    # 겨울에 추가될 양분 map

# print(plusEnergy)

for i in range(M):
    row, col, value = map(int, input().split())
    tree[row-1][col-1].append(value)
    # 입력이 2 1 3 이면 tree[1][0] = 3 

# print(max(tree[1][0]))


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

dieTreeList = []

for i in range(K):
    # K년 동안

    # print("봄 시작")
    # 봄
    for row in range(N):
        for col in range(N):
            if not tree[row][col]:
                # 나무가 없으면 바로 재껴
                continue
            
            if energy[row][col] < max(tree[row][col]):
                # 죽는 나무 체크

                dieTreeList.append([row, col, max(tree[row][col])])
                # row, col, 나이
                # print("죽는 나무 ", dieTreeList)

                tree[row][col].remove(max(tree[row][col]))
            # 양분이 부족하면 나무 죽어

            else:
                # 양분 있으면 나이만큼 줄이고 나이 + 1 

                maxIndex = tree[row][col].index(max(tree[row][col]))
                # 여러 나무들이 모여있을 때 최대값이 있는 인덱스는?

                energy[row][col] -= tree[row][col][maxIndex]
                # 나이 증가해주기 전에 있는 양분에서 나이만큼 줄여야지
                
                tree[row][col][maxIndex] += 1

    # print()
    # print("봄이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()
    

    # print("여름 시작")
    # 여름
    for row in range(N):
        for col in range(N):
            for i in range(len(dieTreeList)):
                # print("row = ", row, " col = ", col, " i = ", i)
                if dieTreeList[i][0] == row and dieTreeList[i][1] == col:
                    # print("추가된 양분 = ", int(dieTreeList[i][2]/2))
                    energy[row][col] += int(dieTreeList[i][2]/2)
    dieTreeList.clear()
    
    # print()
    # print("여름이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()

    # print("가을 시작")
    # 가을
    for row in range(N):
        for col in range(N):
            if tree[row][col] and max(tree[row][col]) % 5 == 0:
                if row-1 >= 0 and col-1 >= 0:
                    tree[row-1][col-1].append(1)
                if row-1 >= 0:
                    tree[row-1][col].append(1)
                if row-1 >= 0 and col+1 < N:
                    tree[row-1][col+1].append(1)
                if col-1 >= 0:
                    tree[row][col-1].append(1)
                if col+1 < N:
                    tree[row][col+1].append(1)
                if row+1 < N and col-1 >= 0:
                    tree[row+1][col-1].append(1)
                if row+1 < N:
                    tree[row+1][col].append(1)
                if row+1 < N and col+1 < N:
                    tree[row+1][col+1].append(1)
    # print()
    # print("가을이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()
    

    # print("겨울 시작")
    # 겨울
    
    for row in range(N):
        for col in range(N):
            energy[row][col] += plusEnergy[row][col]

    # print()
    # print("겨울이 지나갔다")     
    # printTreeFunc()
    # printEnergyFunc()

answer = 0
for row in range(N):
    for col in range(N):
        answer += len(tree[row][col])
print(answer)