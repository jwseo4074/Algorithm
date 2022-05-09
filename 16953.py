# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

start, end = map(int, input().split())
cnt = 0
answerList = []

def dfs():
    global start, end, cnt

    if start == end:
        cnt += 1
        answerList.append(cnt)
        return 

    elif start > end:
        return

    start *= 2
    cnt += 1
    dfs()
    start /= 2
    cnt -= 1
    start = int(start)

    start = str(start) + "1"
    cnt += 1
    start = int(start)
    dfs()
    start = str(start)
    start = start[0:-1]
    start = int(start)
    cnt -= 1

dfs()
if len(answerList) == 0:
    print(-1)
else:
    print(min(answerList))

# strA = 256
# print(strA)
# strA = str(strA)
# print(strA)
# strA = strA + "1"
# print(strA)
# strA = strA[0:-1]
# print(strA)
