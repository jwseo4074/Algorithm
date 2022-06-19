# scoville = [1, 2, 3, 9, 10, 12]
scoville = [1, 2, 3,4,5, 9, 10, 12]
# scoville = [1,12,10,9, 2, 3]
# scoville = [10, 3, 2, 9, 13, 12]
# scoville = [10, 10, 10]
scoville = [0, 0]

K = 2

# h가 비어있지 않은 경우를 예외로 안 넣으면 최소값 빠지자마자 남은 값이 K를 넘어서 return 해버리네요

import heapq
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    # print(scoville)

    if min(scoville) >= K:
        return 0

    while True:
        input()
        if len(scoville) < 2:
            break
        if scoville[0] >= K and scoville[1] >= K:
            break

        print("before = ", scoville)
        a = heapq.heappop(scoville)
        print("a = ", a)
        b = heapq.heappop(scoville)
        print("b = ", b)
        c = a + (2*b)
        print("c = ", c)
        heapq.heappush(scoville, c)
        print("after = ",scoville)
        answer += 1
        print("answer = ", answer)

    
    if answer > 0 and scoville[0] < K:
        answer = -1

    return answer

print(solution(scoville, K))

# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# 할 때 마다 정렬? 말이 안돼 

