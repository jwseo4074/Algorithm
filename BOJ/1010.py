def factorial(n):
    total = 1   
    for i in range(n, 1, -1):
        total *= i
    return total


for i in range(int(input())):
    N, M = map(int, input().split())
    
    answer = 0
    answer = factorial(M) // (factorial(N) * factorial(M-N))
    print(answer)

