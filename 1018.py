# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 
# 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 8 8
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBBBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW

# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

mapList = []
M = N = cnt = 0

def inputFunc():
    global M,N
    # 13, 10
    # 첫 번째 줄에 13

    N,M = map(int, input().split())
    for i in range(0, N):
        oneRow = input()
        mapList.append(list(oneRow))

# def printFunc():
#     for i in range(0, N):
#         for j in range(0, M):
#             print(mapList[i][j], end='')
#             # 줄바꿈 없이 출력하기
#         print()

# 입력 확인용 함수

def checkFunc():
    answerList = []

    for i in range(0, N):
        for j in range(0, M):
            if i <= N - 8 and j <= M - 8:
                startFromW = startFromWFunc(i, j)
                startFromB = startFromBFunc(i, j)
                if startFromW > startFromB:
                    # print("choose startFromB because ", "startFromW = ",startFromW, "startFromB = ", startFromB)
                    # print("i = ", i, " j = ", j, startFromB)
                    answerList.append(startFromB)
                else:
                    # print("choose startFromW because ", "startFromW = ",startFromW, "startFromB = ", startFromB)
                    # print("i = ", i, " j = ", j, startFromW)
                    answerList.append(startFromW)
    answerList.sort()

    print(answerList[0])
    # W로 시작한다고 했을 경우의 값

def startFromWFunc(startrow, startcol):
    global cnt
    cnt = 0

    for i in range(startrow, startrow + 8):
        if i % 2 == 0:
        # 짝수 로우 일 경우
            for j in range(startcol, startcol + 8):
                if j % 2 == 0:
                    # 짝수 컬럼일 경우
                    if mapList[i][j] != 'W':
                        cnt += 1
                else:
                    # 홀수 컬럼일 경우
                    if mapList[i][j] != 'B':
                        cnt += 1
        else:
        #홀수 로우일 경우
            for j in range(startcol, startcol + 8):
                if j % 2 == 0:
                    # 짝수 컬럼일 경우
                    if mapList[i][j] != 'B':
                        cnt += 1
                else:
                    # 홀수 컬럼일 경우
                    if mapList[i][j] != 'W':
                        cnt += 1
    return cnt


def startFromBFunc(startrow, startcol):
    global cnt
    cnt = 0

    for i in range(startrow, startrow + 8):
        if i % 2 == 0:
            # 짝수 로우 일 경우
            for j in range(startcol, startcol + 8):
                if j % 2 == 0:
                    # 짝수 컬럼일 경우
                    if mapList[i][j] != 'B':
                        cnt += 1
                else:
                    # 홀수 컬럼일 경우
                    if mapList[i][j] != 'W':
                        cnt += 1
        else:
        #홀수 로우일 경우
            for j in range(startcol, startcol + 8):
                if j % 2 == 0:
                    # 짝수 컬럼일 경우
                    if mapList[i][j] != 'W':
                        cnt += 1
                else:
                    # 홀수 컬럼일 경우
                    if mapList[i][j] != 'B':
                        cnt += 1
    return cnt

inputFunc()
checkFunc()


# 수행시간 112ms = 0.112s 나옴, 시간 제한은 2초
# N,M이 최대 50 이니까 최악의 경우 (42^2)*(8^2 * 2) 이다.
# 결론은 특별한 알고리즘이 필요없이 그냥 다 돌리면 됐었다는... 그런 내용...