from collections import deque
N = int(input())
A = list(map(int, input().split()))

answer = [-1] * N
stack = deque()

for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        index = stack.pop()
        answer[index] = A[i]

    stack.append(i)
    
print(*answer)