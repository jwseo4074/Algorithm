# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

import sys
input = sys.stdin.readline
# 꿀팁 1 - 이렇게 하면 굳이 귀찮다고 안하는게 아니라 평소처럼 하는데 시간은 조금이나마 주는거잖아? 
INF = int(1e9)
# 꿀팁 2 - 양의 무한대

N, M = map(int, input().split())
startNode = int(input())
# 주어지는 그래프 정보 담는 N개 길이의 리스트
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)  # 방문처리 기록용
distance = [INF] * (N+1)   # 거리 테이블용

for _ in range(M):
    u, v, w = map(int, input().split())
    # 출발 노드 : u 
    # 도착 노드 : v
    # 간선 비용 : w
    graph[u].append((v, w))

print("graph = ", graph, "\n")
    

# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N+1):
        # 1 부터 N까지 전부 다 방문할거야

        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    print(" 안가본 노드 중에 가장 최단 거리의 노드는 ? ", index , "\n")
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작노드 -> 시작노드 거리 계산 및 방문처리
    distance[start] = 0
    visited[start] = True
    # 시작노드의 인접한 노드들에 대해 최단거리 계산
    for node in graph[start]:
        distance[node[0]] = node[1]

    # 시작노드 제외한 n-1개의 다른 노드들 처리
    for _ in range(N-1):
        # n=5, 노드가 5개면 4번 돌겠지

        now = get_smallest_node()  
        # now => 방문안했으면서 시작노드와 최단거리인 노드
        visited[now] = True        
        # 해당 노드 방문처리

        print("now = ", now, " 방문 처리 " , "\n")

        # 해당 노드의 인접한 노드들 간의 거리 계산
        for next in graph[now]:
            
            print(now, " 에서 출발할 수 있는 노드 next = ", next , "\n")

            cost = distance[now] + next[1] 
            print("cost = ", cost, " = ", now, " 까지 오는 최단거리 : ",distance[now] ,"+ ", next[0]," 까지 오는데 비용 : ", next[1] , "\n")
            # 시작->now 거리 + now->now의 인접노드 거리
            if cost < distance[next[0]]:    # cost < 시작->now의 인접노드 다이렉트 거리
                distance[next[0]] = cost

dijkstra(startNode)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])