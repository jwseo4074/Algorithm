# import math

# progresses = [93, 30, 55]
# # progresses = [95, 90, 99, 99, 80, 99]		
# speeds = [1, 30, 5]
# # speeds = [1, 1, 1, 1, 1, 1]
# # 정답 : [2, 1], [1, 3, 2]
# def solution(progresses, speeds):
#     answer = []
#     remainTime = []

#     # 남은 시간 (걸리는 시간)
#     for i in range(len(progresses)):
#         # print("a = ", (100 - progresses[i]) / speeds[i])
#         # print("b = ", float(100 - progresses[i]) / speeds[i])
#         # print("c = ", math.ceil(float(100 - progresses[i]) / speeds[i]))
#         remainTime.append(math.ceil((100 - progresses[i]) / speeds[i]))
#         # 반올림 = round, 올림 = ceil, 
#     # print(remainTime)
   
    
#     count = 0
#     for a in progresses:
#         if a > count:
#             answer.append(1)
#             count = a
#         else:
#             answer[-1] += 1

#     # print(answer)
#     return answer

# # solution(progresses, speeds)


progresses = [93, 30, 55]
# progresses = [95, 90, 99, 99, 80, 99]		
speeds = [1, 30, 5]
# speeds = [1, 1, 1, 1, 1, 1]
# 정답 : [2, 1], [1, 3, 2]
def solution(progresses, speeds):
    answer = []

    # 작업이 없을 때까지 반복
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            # 하루 작업 했다. speeds[i] => 작업량 하루치 작업
        
        # 하루 작업 하고 나면 => 94, 60, 60
        # 하루 작업 하고 나면 => 95, 90, 65
        # 하루 작업 하고 나면 => 100, 240, 90
        cnt = 0
        while progresses and progresses[0] >= 100:
            # 제일 첫 번째 작업이 작업 끝났어 => 100
            progresses.pop(0)
            # 첫 번째 작업 pop
            speeds.pop(0)
            # 첫 번째 작업에 해당하는 속도 pop
            cnt += 1
            # cnt = 1 -> 100 끝난거 한개

            # 다시 while문 돌았을 때 두 번째꺼도 100 넘었어
            # 그럼 그거 pop 하고 cnt = 2 돼
            # 이제 작업 끝난게 없어 => 세 번째꺼는 100이 안돼 => 다시 while 돌아

        if cnt > 0:
            answer.append(cnt)
        
    return answer