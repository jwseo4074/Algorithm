# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

import heapq
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

# print("graph = ", graph, "\n")

# 이까진 코드 전과 동일

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0을 설정하여, 큐에 삽입

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 큐가 비어있지 않으면 계속 진행
        print( " 현재 큐 = ", q , "\n")
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, nowNode  = heapq.heappop(q)
        print("dist = ", dist, "nowNode = ", nowNode, "\n")
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[nowNode] < dist:
            print("이미 처리된 적 있는 노드라서 continue 할거야", "\n")
            print("( distance[", nowNode, "] = ", distance[nowNode] ,")  < ", dist ,"\n")
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node in graph[nowNode]:
            cost = dist + node[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node[0]]:    # cost < 시작->now의 인접노드 다이렉트 거리
                distance[node[0]] = cost
                
                for i in range(1, N+1):
                    print(i, " = ", distance[i])

                heapq.heappush(q, (cost, node[0]))

dijkstra(startNode)

for i in range(1, N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
