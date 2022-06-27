s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	
# result = [2,1,3,4]

# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"	
# result = [2,1,3,4]

def solution(s):
    answer = []
    # print(s)
    L = s.split('},{')
    # print("0. L = ", L)
    L[0] = L[0][2:]
    L[-1] = L[-1][:-2]
    L.sort(key = lambda x : len(x))
    
    # print("1. L = ", L)

    for i in range(len(L)):
        L[i] = L[i].split(',')
        # print(L[i])
        L[i] = (list(map(int, L[i])))
        L[i].sort()
        # print(L[i])
    
    # print("2. L = ", L)
    # [[2], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
    
    storeVal = []
    for i in range(len(L)):
        # print("storeVal = ", storeVal)
        if i == 0:
            storeVal = L[i]
            answer.append(L[i][0])
            continue
        
        XX = L[i]
        X = XX[:]
        # 얕은 복사
        # a = [1,2,3]
        # b = a[:]

        # print("// X = ", X)
        for j in range(len(storeVal)):
            X.remove(storeVal[j])
        # print("// X = ", X)
        answer.append(X[0])
        storeVal = L[i]
    
    return answer
    
        

    # originL = []
    # maxVal = ''
    # for a in L:
    #     originL.append(a)
    #     if len(maxVal) < len(a):
    #         maxVal = a

    # resultL = list(maxVal.split(','))
    # resultL = list(map(int, resultL))
    # L = list(permutations(resultL, len(resultL)))

    # # print("2. L = ", L)
    # # print("3. originL = ", originL)
    # # L = 가능한 순서 조합 전부 -> 이 중에 답 있다

    # for i in range(len(originL)):
    #     originL[i] = originL[i].split(',')
    #     originL[i] = list(map(int, originL[i]))
    
    # print("3. originL = ", originL)

    # for permu in L:
    #     # input()
    #     print("permu = ", permu)
    #     X = []
    #     XX = []
    #     for i in range(1, len(permu)+1):
    #         for j in range(0, i):
    #             XX.append(permu[j])
    #         X.append(XX)
    #         XX = []
    #     print(" X = ", X )
    #     print(" originL = ", originL )        
        

    #     for i in range(len(X)):
    #         state = True
    #         print(" i = ", i)
    #         for j in range(len(X[i])):   
    #             if X[i][j] not in originL[i]:
    #                 state = False
    #                 break

    #             else:
    #                 print("X[i][j] = ", X[i][j])
    #                 print("originL[i] = ", originL[i])
    #                 print()
    #         if state == False:
    #             break
            
    #         if i == len(X)-1:
    #             print("찾은 듯?")
    #             answer = list(permu)
    #             return answer

print(solution(s))