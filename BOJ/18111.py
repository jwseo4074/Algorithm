N, M, B = map(int, input().split())
inputMap = [list(map(int, input().split())) for i in range(N)]
# print(inputMap)
nowBlock = 0 

def plusProcessFunc ( row, col, hei, block):
    if inputMap[row][col] > hei:
        block += (inputMap[row][col] - hei)
        return 2*(inputMap[row][col] - hei)
    else:
        return 0

def minusProcessFunc ( row, col, hei, block):
    state = False

    if inputMap[row][col] < hei:
        block -= (hei - inputMap[row][col])

        if block < 0:
            return -1

        else:
            return (hei - inputMap[row][col])
    else:
        return 0

answerHeight = 10e9
answerTime = 10e9

for height in range( 256, -1, -1 ):
    totalTime = 0
    nowState = False
    nowBlock = B

    dontgo = False

    # 높이가 더 높은 블럭 쟁여두기
    for i in range(N):
        for j in range(M):
            if inputMap[i][j] == height:
                pass
            else:
                totalTime += plusProcessFunc(i, j, height, nowBlock)

    # 높이가 더 낮은 블럭 채우기
    for i in range(N):
        for j in range(M):
            if inputMap[i][j] == height:
                pass
            else:
                resultFunc = minusProcessFunc(i, j, height, nowBlock)
                if resultFunc == -1:
                    nowState = True
                    break
                
                else:
                    totalTime += resultFunc
        if nowState == True:
            break

    if nowState == True:
        continue

    # print("Height = ", height, "totalTime = ", totalTime)

    if totalTime < answerTime:
        answerTime = totalTime
        answerHeight = height
    if totalTime == answerTime:
        answerHeight = max(answerHeight, height)


print( answerTime, answerHeight )