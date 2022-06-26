from curses.ascii import isalnum
from itertools import permutations

def solution(expression):
    answer = 0

    operList = []
    for a in expression:
        if a == "+" or a == "-" or a =="*":
            operList.append(a)
    operList = set(operList)
    operList = list(permutations(operList, len(operList)))

    # print(operList)
    # [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]

    LL = []
    j = 0
    for i in range(len(expression)):
        # print("i = ", i, " => ", expression[i] )
        
        if expression[i] in operList[0]:
            # input()
            LL.append(expression[j:i])
            LL.append(expression[i])
            j = i+1
            
    LL.append(expression[j:])
    # print(LL) 
    # ['100', '-', '200', '*', '300', '-', '500', '+', 20]

    answer = 0

    for oper in operList:
        # input()
       
        L = []
        for x in (LL):
            L.append(x)
        
        # print("LL = ", LL)
        # print("L = ", L)

        # print("oper = ", oper)
        for operOne in oper:
            # print("operOne = ", operOne)
            while operOne in L:
                # input()

                for i in range(len(L)):
                    if L[i] == operOne:
                        # print("L[i-1] = ", L[i-1])
                        # print("L[i] = ", L[i])
                        # print("L[i+1] = ", L[i+1])

                        strVal = L[i-1] + L[i] + L[i+1]
                        resultInt = eval(strVal)

                        # print(resultInt)

                        L[i-1] = 'X'                    
                        L[i] = str(resultInt)
                        L[i+1] = 'X'

                        while 'X' in L:
                            L.remove('X')

                        # print("L = ", L)
                        break
            if len(L) == 1:
                # print("result Integer = ", L[0])
                break
        answer = max(answer, abs(int(L[0])))
        # print(answer)
    return answer

# 100 , - , 200 , * , 300 , - , 500 , + , 20
# 우선 순위 = * , - , + 이면? 
# 200 * 300 지우고 60000 넣어
# => 100 - 60000 - 500 + 20
# 그 다음 우선 순위 : -
# 100 - 60000 지우고 - ~~ 넣어
# ~~ - 500 지우고 ~~ 넣어




expression = "50*6-3*2"
result = 300
# print(str(result).isalnum())

# expression = "100-200*300-500+20"
# result = 60420

print(solution(expression))
print(result)
# * > + > - 로 연산자 우선순위를 정했을 때, 가장 큰 절댓값을 얻을 수 있습니다.
# 연산 순서는 아래와 같습니다.
# 100-200*300-500+20
# = 100-(200*300)-500+20
# = 100-60000-(500+20)
# = (100-60000)-520
# = (-59900-520)
# = -60420
# 따라서, 우승 시 받을 수 있는 상금은 |-60420| = 60420 입니다.