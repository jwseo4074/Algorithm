# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.


def inputFunc() :
    inputList = []
    for i in range(0, 10):
        inputList.append(int(input()))
    return inputList

def cal(L):
    # 안에 뭐가 있는지 알고 싶다? <<< in >>>
    cnt = 0
    answerList = []

    for charVal in L:
        divideValue = charVal % 42
        if divideValue not in answerList:
            # 이미 정답 배열에 그게 있냐? 없으면 넣어라
            answerList.append(divideValue)
    print(len(answerList))
        

cal(inputFunc())
