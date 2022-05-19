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

print(tree)


# for i in range(K):
    # K년 동안

    # 봄

    
    # 여름

    # 가을

    # 겨울