def solution(queue1, queue2):
    answerList = []
    
    global cnt
    global upcnt
    global downcnt
    global len1
    global len2
    global sumAnswer

    len1 = len(queue1)
    len2 = len(queue2)
    
    cnt = upcnt = downcnt = 0
    sumAnswer = int((sum(queue1) + sum(queue2)) / 2)
    print("sumAnswer = ", sumAnswer)
    
    
    def dfs():
        global cnt
        global upcnt
        global downcnt
        global len1
        global len2
        global sumAnswer

        # input()
        # print("come in dfs")
        # print("queue1 = ", queue1)
        # print("queue2 = ", queue2)
        # print("sum of queue1 = ", sum(queue1))
        # print("sum of queue2 = ", sum(queue2))

        if sum(queue1) == sumAnswer:
            answerList.append(cnt)
            # print(answerList)
            # print("합이 같다. 이 때의 cnt는? ", cnt)
            return

        if len(queue1) == 1 or len(queue2) == 1:
            return

        if upcnt + downcnt > len1 + len2:
            return

        # print("< 1에서 2로 >, 1에서 하나 pop, 2로 insert")
        queue2.append(queue1.pop(0))
        cnt += 1
        upcnt += 1
        # print("queue1 = ", queue1)
        # print("queue2 = ", queue2)
        # print("cnt = ", cnt)
        # print("자리 바꾸고 나서 sum of queue1 = ", sum(queue1))
        # print("자리 바꾸고 나서 sum of queue2 = ", sum(queue2))

        # print("dfs 호출")
        dfs()
        # print("원상복구")
        queue1.insert(0, queue2.pop())
        # print("queue1 = ", queue1)
        # print("queue2 = ", queue2)
        # print("원상 복구 하고 나서 sum of queue1 = ", sum(queue1))
        # print("원상 복구 하고 나서 sum of queue2 = ", sum(queue2))
        cnt -= 1
        upcnt -= 1

        # print("< 2에서 1로 >, 2에서 하나 pop, 1로 insert")
        queue1.append(queue2.pop(0))
        cnt += 1
        downcnt += 1
        # print("queue1 = ", queue1)
        # print("queue2 = ", queue2)
        # print("cnt = ", cnt)
        # print("자리 바꾸고 나서 sum of queue1 = ", sum(queue1))
        # print("자리 바꾸고 나서 sum of queue2 = ", sum(queue2))

        # print("dfs 호출")
        dfs()
        # print("원상복구")
        queue2.insert(0, queue1.pop())
        # print("queue1 = ", queue1)
        # print("queue2 = ", queue2)
        # print("원상 복구 하고 나서 sum of queue1 = ", sum(queue1))
        # print("원상 복구 하고 나서 sum of queue2 = ", sum(queue2))
        cnt -= 1
        downcnt -= 1
        
        return

        
    if (sum(queue1) + sum(queue2)) % 2 == 0:
        # 짝수 일 때만 실행, 합쳤는데 홀수면 어케해도 안됨
        # print("제일 처음 dfs 호출")
        dfs()
    else:
        return -1
    # print("anserList = ", answerList)
    # answerList.remove(0)
    if answerList:
        answer = min(answerList)
        return answer
    return -1

print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1, 1], [1, 5]))
print(solution([1,2,3,4,5], [6,7,8,9,10]))
print(solution([2,3,4,5,6], [10]))


