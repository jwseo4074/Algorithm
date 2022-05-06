# # 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# # 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# # 고른 수열은 오름차순이어야 한다.

# N, M = map(int, input().split())

# numList = []

# def dfs():
#     if len(numList) == M:
#         for i in range(0, M):
#             if i == M-1:
#                 # 젤 마지막 전에꺼 비교할 때는 예외처리
#                 if numList[M-2] > numList[M-1]:
#                     return
#                 else:
#                     continue
#             else:
#                 if numList[i] > numList[i+1]:
#                     return
#                 else:
#                     continue
#         for i in range(0, M):
#             print(numList[i],'',end='')
#         print()

#         return

#     for i in range(1, N+1):
#         if i not in numList:
#             numList.append(i)
#             dfs()
#             numList.pop()
    
# dfs()

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

N, M = map(int, input().split())

numList = []

def dfs(idx):
    if len(numList) == M:
        for a in numList:
            print(a,'', end='')
        print()

    for i in range(idx, N+1):
        # if 문 도 필요가 없지
        # 왜 ? 당연히 넘어오는 i 보다 큰 걸 넣어줬으니까 무조건 모든 경우에 True 겠지
        numList.append(i)
        dfs(i+1)
        numList.pop()

        # 오름차순이잖아? 인덱스로 출발점을 넘겨주면 돼 그럼 당연히 뒤에 애들은 그거보단 크겠지 

dfs(1)