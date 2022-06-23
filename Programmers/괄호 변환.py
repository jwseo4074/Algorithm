# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.


# 두 문자열 u, v로 분리합니다.
# u = "()"
# v = "))((()"
# 문자열 u가 "올바른 괄호 문자열"이므로 그대로 두고, v에 대해 재귀적으로 수행합니다.
# 다시 두 문자열 u, v로 분리합니다.
# u = "))(("
# v = "()"
# u가 "올바른 괄호 문자열"이 아니므로 다음과 같이 새로운 문자열을 만듭니다.
# v에 대해 1단계부터 재귀적으로 수행하면 "()"이 반환됩니다.
# u의 앞뒤 문자를 제거하고, 나머지 문자의 괄호 방향을 뒤집으면 "()"이 됩니다.
# 따라서 생성되는 문자열은 "(" + "()" + ")" + "()"이며, 최종적으로 "(())()"를 반환합니다.
# 처음에 그대로 둔 문자열에 반환된 문자열을 이어 붙이면 "()" + "(())()" = "()(())()"가 됩니다.

# p = "(()())()"
# result = "(()())()"

# p = ")("	
# resul = "()"

# p = "()))((()"
p = "()))(()("	

# result = "()(())()"

# p = "))()(("
# result = ""

from collections import deque

def solution(p):
    answer = ''
    
    def isTrue(X):
        deq = deque()
        for i in range(len(X)):
            # if u가 올바른 문자열인가?

            try:
                # 올바른 문자열이면 => answer 에 추가
                if X[i] == "(":
                    deq.append("(")
                else:
                    deq.pop()
                if i == len(X)-1:
                    return True

            except:
                # 아니면 새로운 문자열 만들기
                return False
                
    def Loop(X):
        input()
        if len(X) == 0:
            return X
        
        front = 0
        back = 0
        u = []
        v = []
        pLen = len(X)
        # input()
        for i in range(len(X)):
            if X[i] == "(":
                front += 1
            else:
                back += 1
            
            if front == back:
                u = X[:i+1]
                v = X[i+1:]
                break
        print(" u = ", u)
        print(" v = ", v)  

        if isTrue(u):
            # 올바른 문자열이면
            print(u," 가 올바른 문자열이다")

            resultV = Loop(v)
            print("resultV = ", resultV)
        
            resultAnswer = u+resultV
            print("resultAnswer = ", resultAnswer)
            return resultAnswer

        else:
            # u가 올바른 문자열이 아니면
            print(u," 가 올바른 문자열이 아니다.")
            makeStr = ''
            makeStr += "("
            makeStr += Loop(v)
            makeStr += ")"
            L = list(u[1:-1])
            for j in range(len(L)):
                if L[j] == "(":
                    L[j] = ")"
                else:
                    L[j] = "("

            makeStr += "".join(L)
            # print("makeStr = ", makeStr)
            
            return makeStr

    answer = Loop(p)

    return answer

# p = input()
print(solution(p))

# 이전 풀이( + 연습장 )

# # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
# #    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 
# #                                   문자열 v에 대해 1단계부터 다시 수행합니다. 
# #                                   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
# #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
# #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
# #   4-3. ')'를 다시 붙입니다. 
# #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
# #   4-5. 생성된 문자열을 반환합니다.


# # 두 문자열 u, v로 분리합니다.
# # u = "()"
# # v = "))((()"
# # 문자열 u가 "올바른 괄호 문자열"이므로 그대로 두고, v에 대해 재귀적으로 수행합니다.
# # 다시 두 문자열 u, v로 분리합니다.
# # u = "))(("
# # v = "()"
# # u가 "올바른 괄호 문자열"이 아니므로 다음과 같이 새로운 문자열을 만듭니다.
# # v에 대해 1단계부터 재귀적으로 수행하면 "()"이 반환됩니다.
# # u의 앞뒤 문자를 제거하고, 나머지 문자의 괄호 방향을 뒤집으면 "()"이 됩니다.
# # 따라서 생성되는 문자열은 "(" + "()" + ")" + "()"이며, 최종적으로 "(())()"를 반환합니다.
# # 처음에 그대로 둔 문자열에 반환된 문자열을 이어 붙이면 "()" + "(())()" = "()(())()"가 됩니다.

# # p = "(()())()"
# # result = "(()())()"

# # p = ")("	
# # resul = "()"

# # p = "()))((()"
# p = "()))(()("	

# # result = "()(())()"

# # p = "))()(("
# # result = ""

# from collections import deque
# def solution(p):
#     answer = ''
#     if len(p) == 0:
#         return answer

#     front = 0
#     back = 0
#     u = []
#     v = []
#     pLen = len(p)
#     while True:
#         # input()
#         for i in range(len(p)):
#             if p[i] == "(":
#                 front += 1
#             else:
#                 back += 1
            
#             if front == back:
#                 u = p[:i+1]
#                 v = p[i+1:]
#                 break
#         # for 문 끝나면? u, v 나눠짐
#         print(" u = ", u)
#         print(" v = ", v)   

#         deq = deque()
#         for i in range(len(u)):
#             # if u가 올바른 문자열인가?

#             try:
#                 # 올바른 문자열이면 => answer 에 추가
#                 if u[i] == "(":
#                     deq.append("(")
#                 else:
#                     deq.pop()
#                 if i == len(u)-1:
#                     answer += u
#                     break

#             except:
#                 # 아니면 새로운 문자열 만들기

#                 # 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#                 #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#                 #   4-3. ')'를 다시 붙입니다. 
#                 #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#                 makeStr = ''
#                 makeStr += "("
#                 makeStr += v
#                 makeStr += ")"
#                 L = list(u[1:-1])
#                 makeStr += "".join(L[::-1])
#                 answer += makeStr
#                 break
    
#         print("answer = ", answer)
        
#         if len(answer) == pLen:
#             break

#         p = v

#     return answer

# # p = input()
# print(solution(p))