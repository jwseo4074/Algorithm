# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 1 ≤ M ≤ N ≤ 1,000,000

M, N = map(int, input().split())
# totalList = [ i for i in range(1, N+1)]

for i in range(M, N+1):
    state = True

    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        # 다 확인할 필요없고 제곱근까지만 보면 된다. => 시간 확실히 줄어듬
        
        # 2는 어떻게 해줄거냐? => for in range(2, 2) => nothing
        
        if i % j == 0:
            state = False
            break
    if state == True:
        print(i)


# N = int(input())
# print(int(N ** 0.5) + 1)
# # 10 => 4
# # 20 => 5
