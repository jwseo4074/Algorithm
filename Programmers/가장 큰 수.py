def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x*3, reverse = True)
    print(numbers)
    # print(''.join(numbers))
    return str(int(''.join(numbers)))

# [6, 10, 2] => [6102, 6210, 1062, 1026, 2610, 2106]

numbers = [6, 10, 2]
# "6210"

# numbers = [3, 30, 300, 34, 5, 9, 20, 2]	
# "9 5 34 3 30 2 20"

print(solution(numbers))

# 순열로 가능한 모든 조합에서 최대값 찾는거는?