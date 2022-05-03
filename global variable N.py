
#  전역 변수 N. 값 초기화?
# global 이 있고 없고의 차이
# 다른 언어들이랑은 이 부분이 다르다

inputList = []
N = 0

def inputFunc():
    
    global N
    #  이게 있고 없고의 차이
    # 여기서의 N은 전역(global)의 N이다라는 걸 명시해준다

    N = int(input())
    for i in range(0, N):
        inputList.append(list(map(int, input().split())))
    # print(inputList)
    print("inputFunc 안에 있는 N : ", N)

def calFunc():
    print("calFunc 안에 있는 N : ", N)
    # N 이 왜 0이지?
    # 전역 변수 N인데 왜 값이 적용이 안되나
    for i in range(0, N):
        print(456)
        cnt = 0
        firstValue = inputList[i][0]
        print(firstValue)
        lastValue = inputList[i][1]
        print(lastValue)
        # 첫 번째 친구의 정보

        for j in range(0, N):
            if i == j:
                continue
                # 비교하는 둘이가 같은 애면 걍 재껴야지
            elif firstValue > inputList[j][0] and lastValue > inputList[j][1]:
                cnt += 1
                # 자기가 더 크면 cnt 하나 추가
            else:
                cnt = cnt
                # 자기가 더 작으면 그냥 그대로 유지 이건 굳이 없어도 되긴 하다

        inputList[i].append(cnt)
        

def printFunc():
    for i in range(0, N):
        print(inputList)

print("inputFunc 시작하기 전에 있는 N : ", N)
inputFunc()
print("inputFunc 끝나고 나서의 N : ", N)
calFunc()
print("calFunc 끝나고 나서의 N : ", N)
printFunc()
