numbers = [1, 1, 1, 1, 1]
target = 3
# result = 5
# numbers = [4, 1, 2, 1]	
# target = 4	
# result = 2

# -1 +1 +1 +1 +1 = 3
# +1 -1 +1 +1 +1 = 3
# +1 +1 -1 +1 +1 = 3
# +1 +1 +1 -1 +1 = 3
# +1 +1 +1 +1 -1 = 3

def solution(numbers, target):
    global answer 
    answer = 0

    def dfs(idx, sumVal):
        input()
        global answer

        print("idx = ", idx, " sumVal = ", sumVal)
        if idx == len(numbers)-1:
            if sumVal == target:
                answer += 1
                print("Find, answer =", answer)
            return
        
            
        # print("idx = ", idx)
        dfs(idx + 1, sumVal-numbers[idx])
        dfs(idx + 1, sumVal+numbers[idx])
    
    dfs(-1,0)

    return answer

print(solution(numbers, target))