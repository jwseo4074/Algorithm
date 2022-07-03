def solution(priorities, location):
    answer = 0
    lenP = len(priorities)
    answerNum = priorities[location]
    cnt = 0
    answer = 0

    while priorities:
        # input()

        # print("cnt = ", cnt)
        if cnt == lenP:
            cnt = 0
            # print("change cnt = 0 ")

        X = priorities[0]
        # print("X = ", X)

        if X == 0:
            priorities.pop(0)
            priorities.append(0)

            cnt += 1
            continue

        if max(priorities) == X: 
            # print("this is max")
            answer += 1
            # print("answer = ", answer)
            priorities.pop(0)
            priorities.append(0)
            # print("priorities = ", priorities)
            
            if cnt == location and X == answerNum:
                # print("Find Answer ")
                return answer

        else:
            priorities.append(priorities.pop(0))
        
        # print("after = ", priorities)
        cnt += 1

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# 1개 이상 100개 이하의 문서가 있습니다.
# priorities = [2, 1, 3, 2]
# location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
# 1
priorities = [1,2,3,2,1]
location = 0

# 5

print(solution(priorities, location))