# 2 5 3 1 4
# => 1 1 0 3 1 

# 2 3 4 5 6 1
# => 1 1 1 1 1 5

def solution(p):
    answer = []

    for i in range(len(p)):
        answer.append(0)

    i = 0
    # 1번 인덱스 초기화

    while(1):
        # input()
    # 2번 p[j] 찾기
        print(" i = ", i)
        minVal = len(p)+1
        minValIdx = 0
        for idx in range(i, len(p)):
            print(p)
            print("p[idx] = ", p[idx])
            if minVal > p[idx]:
                minVal = p[idx]
                minValIdx = idx
                print("minVal = ", minVal)
        
        print("최소값 = ", minVal, " 인덱스 = ", minValIdx)

        

        if i != minValIdx:
            print("바꾸기 전 ", p)
            print(p[i], p[minValIdx]," 자리 바꿈")
            temp = p[i]
            p[i] = p [minValIdx]
            p[minValIdx] = temp
            answer[i] += 1
            answer[minValIdx] += 1
            print("바꾸고 난 후 ", p)
            print("바꾸고 난 후 answer = ", answer)
        
        i += 1
       
                    
        if i == len(p):
            break
    
    return answer

print("answer = ", solution([2,3,4,5,6,1]))

# 1. 배열 인덱스, i=0 으로 초기화
# 2. p[i], p[i+1] ~ p[n-1] 중에서 가장 작은 숫자 찾기
# 여기서 찾은 숫자를 p[j]
# 3. 만약 i 랑 j 가 다르다면 p[i]와 p[j]의 값을 서로 바꿈
# 4. i에 1을 더한다.
# 만약 i 가 n 보다 작다면 2번으로 돌아가
# i가 n 이라면 알고리즘 종료



# 정답 코드
# def solution(p):
#     answer = []

#     for i in range(len(p)):
#         answer.append(0)

#     i = 0
#     # 1번 인덱스 초기화

#     while(1):
#         # input()
#     # 2번 p[j] 찾기
#         # print(" i = ", i)
#         minVal = len(p)+1
#         minValIdx = 0
#         for idx in range(i, len(p)):
#             # print(p)
#             # print("p[idx] = ", p[idx])
#             if minVal > p[idx]:
#                 minVal = p[idx]
#                 minValIdx = idx
#                 # print("minVal = ", minVal)
        
#         # print("최소값 = ", minVal, " 인덱스 = ", minValIdx)

        

#         if i != minValIdx:
#             # print("바꾸기 전 ", p)
#             # print(p[i], p[minValIdx]," 자리 바꿈")
#             temp = p[i]
#             p[i] = p [minValIdx]
#             p[minValIdx] = temp
#             answer[i] += 1
#             answer[minValIdx] += 1
#             # print("바꾸고 난 후 ", p)
#             # print("바꾸고 난 후 answer = ", answer)
        
#         i += 1
       
                    
#         if i == len(p):
#             break
    
#     return answer