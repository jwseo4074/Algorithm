# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 
# 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 
# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 4 6 => N, M
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3 => v1, v2

import heapq 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inputGraph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    inputGraph[b].append((a,c))
    inputGraph[a].append((b,c))
    # a부터 b까지 다이렉트로 비용은 c
    # graph[b] = (a,c)
    # 반대로도 넣어줘야 함

V1, V2 = map(int, input().split())
# print(graph)

inf = sys.maxsize

def dijkstra(start):
    distance_table = [inf for _ in range(N+1)]
    # N이 4면 => [inf, inf, inf, inf, inf]
    distance_table[start] = 0
    # 출발 지점에서 거리는 0

    heap = []
    heapq.heappush(heap, (0, start))
    # 출발지점에서 거리는 0

    while heap:
        # 빌 때까지 반복

        dist, nowNode = heapq.heappop(heap)
        # 거리가 가장 짧은 노드 빼와서 계산 시작

        for node in inputGraph[nowNode]:
            #현재 노드와 인접한 노드들을 확인
            cost = node[1] + dist

            if cost < distance_table[node[0]]:
            # cost(다른 노드들 거쳐서 왔을 때의 비용)와 start에서의 다이렉트 거리를 비교
                distance_table[node[0]] = cost
                heapq.heappush(heap, (cost, node[0]))

    return distance_table

one_table = dijkstra(1)
V1_table = dijkstra(V1)
V2_table = dijkstra(V2)

answer1 = one_table[V1] + V1_table[V2] + V2_table[N]
answer2 = one_table[V2] + V2_table[V1] + V1_table[N]

cnt = min(answer1, answer2)
print(cnt if cnt < inf else -1)