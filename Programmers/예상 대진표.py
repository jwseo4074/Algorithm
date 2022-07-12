from collections import deque


def solution(n,a,b):
    answer = 0

    queue = deque() 
    for i in range(1, n+1):
        queue.append(i)
    print(queue)   

    while queue:
        input()

        answer += 1
        # 라운드 증가

        for _ in range(int(n/2)):
            A = queue.popleft()
            B = queue.popleft()
            print("A = ", A, " B = ", B)
            
            if A != a and B != b:
                print(1)
                queue.append(A)
                continue
            if A != b and B != a:
                print(2)
                queue.append(A)
                continue

            if A == a and B == b:
                print("정답")
                return answer

            else:
                if A == a or A == b:
                    print(3)        
                    queue.append(A)

                if B == a or B == b:
                    print(4)
                    queue.append(B)

        n = int(n/2)
        print("queue = ", queue)

N = 8	
A = 4	
B = 7	
#3
print(solution(N, A, B))