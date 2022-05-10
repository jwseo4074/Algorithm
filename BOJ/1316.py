# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 3
# happy
# new
# year
# 3


def inputFunc(N, cnt):
    for i in range(0, N):
        x = input()
        cnt += calFunc(x)
    print(cnt)
    
def calFunc(inputStr):
    answerList = []
    for i in range(0, len(inputStr)):
        if i == 0:
            answerList.append(inputStr[i])
        elif inputStr[i] not in answerList:
            answerList.append(inputStr[i])
        elif inputStr[i] == inputStr[i-1]:
            answerList.append(inputStr[i])
        else:
            return 0
    return 1

cnt = 0
num = int(input())
inputFunc(num, cnt)

