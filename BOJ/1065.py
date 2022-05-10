# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

def inputFunc():
    X = int(input())
    return X

def calNum(numVal):
    # print(numVal)
    if numVal < 100:
        return True

    strNum = str(numVal)
    
    space = int(strNum[0]) - int(strNum[1])

    for i in range(0, len(strNum)-1):
        if (int(strNum[i])-int(strNum[i+1])) == space:
            continue
        else:
            return False
    return True

cnt = 0
N = inputFunc()
for i in range(1, N+1):
    if calNum(i) == True:
        # print("여기 안온다고?")
        cnt = cnt + 1
print(cnt)