def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])
    print(d)
    # [(1, 0), (2, 1), (3, 2), (2, 3), (1, 4)])
    # 0 번째 -> 1, 
    # 1 번째 -> 2,
    # 2 번째 -> 2,

    # print(max(d)) => (3, 2)
    # 앞에 값( [0] )으로 최대값 산출

    while d:
        item = d.popleft()
        # 비교할 아이템 => d => (1, 0)
        print("item => ", item)
        if d and max(d)[0] > item[0]:
            d.append(item)
            print(d)
            # 금마가 최대값이 아니면 제일 뒤로 보내
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [1,2,3,2,1]
location = 0

# 5

print(solution(priorities, location))