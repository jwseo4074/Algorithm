# S = baabaa 라면
# b aa baa → bb aa → aa → '' => 1 
from collections import deque


# S = "baabaa"
S = "cdcd"
# S = cdcd	=> 더 이상 못 없애 => 0

def solution(s):
    answer = -1

    L = []
    L.append(s[0])
    
    for i in range(1, len(s)):
        # print("i = ", i)
        # print("L = ", L)
        # print("L[-1] = ", L[-1], " s[i] = ", s[i])
        if not L:
            L.append(s[i])
            continue
        if L[-1] != s[i]:
            L.append(s[i])
            continue
        else:
            L.pop()
    if L:
        return 0
    else:
        return 1


print(solution(S))