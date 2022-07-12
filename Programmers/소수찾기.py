def solution(numbers):
    from itertools import permutations  

    def checkFunc(n):
        if n < 2:
            return False
        
        for i in range(2, n//2+1):
            if n%i == 0:
                return False
            
        return True  

    p = []
    result = []
    for i in range(1, len(numbers)+1): 
        p.extend(permutations(numbers, i))
    
    # print("p = ", p)
    # print()
    for a in p:
        # print("a = ", a)
        # print(''.join(a))
        # print(int(''.join(a)))
        result.append(int(''.join(a)))
    # print()

    # result =  [1, 7, 17, 71]
    answer = 0
    result = set(result)
    # print("result = ", result)

    for i in result:
        if checkFunc(i):
            answer+=1
    return answer


# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# numbers	= "17"	
# 3
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

numbers = "011"	
# 2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.


print(solution(numbers))