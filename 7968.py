# 우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다. 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
#  두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다. 
# 예를 들어 어떤 A, B 두 사람의 덩치가 각각 (56, 177), (45, 165) 라고 한다면 A의 덩치가 B보다 큰 셈이 된다. 
# 그런데 서로 다른 덩치끼리 크기를 정할 수 없는 경우도 있다. 예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 
# 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 
# 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

# 2 ≤ N ≤ 50
# 10 ≤ x, y ≤ 200

inputList = []
N = 0

def inputFunc():
    global N
    N = int(input())
    for i in range(0, N):
        inputList.append(list(map(int, input().split())))
    # print(inputList)
    # print("inputFunc 안에 있는 N : ", N)

def calFunc():
    # print("calFunc 안에 있는 N : ", N)
    # N 이 왜 0이지?
    # 전역 변수 N인데 왜 값이 적용이 안되나
    for i in range(0, N):
        cnt = 1
        firstValue = inputList[i][0]
        # print(firstValue)
        lastValue = inputList[i][1]
        # print(lastValue)
        # 첫 번째 친구의 정보

        for j in range(0, N):
            if i == j:
                continue
                # 비교하는 둘이가 같은 애면 걍 재껴야지
            elif firstValue < inputList[j][0] and lastValue < inputList[j][1]:
                cnt += 1
                # 자기가 더 크면 cnt 하나 추가
            else:
                cnt = cnt
                # 자기가 더 작으면 그냥 그대로 유지 이건 굳이 없어도 되긴 하다

        inputList[i].append(cnt)
        

def printFunc():
    for i in range(0, N):
        print(inputList[i][2])

# print("inputFunc 시작하기 전에 있는 N : ", N)
inputFunc()
# print("inputFunc 끝나고 나서의 N : ", N)
calFunc()
# print("calFunc 끝나고 나서의 N : ", N)
printFunc()