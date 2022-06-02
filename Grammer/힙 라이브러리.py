# 최소 힙

import heapq

# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입

    for value in iterable:
        heapq.heappush(h, value)
        # 최대 힙을 구현하고 싶다면 ? -value로 넣으면 됨
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기

    for i in range(len(h)):
        result.append(heapq.heappop(h))
        # 최대 힙 : 꺼낼 때 -붙여서 꺼내면 됨
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 시간 복잡도 : O(N log N)