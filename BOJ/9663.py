N = int(input())

graph = [0] * N 
totalCnt = 0

def canFix(x):
    # x 는 로우 값

    for i in range(x):
        # 0부터 건네받은 로우까지 볼거야

        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == abs(x - i):
            return False

    return True
    
    
def dfs(queenCnt):
    global totalCnt

    if queenCnt == N:
        # queenCnt => 현재 퀸의 개수, 현재 로우의 위치 => 이게 이 문제의 핵심!!!

        # queenCnt == N 이라는 말은 퀸 다 채웠고, 현재 젤 마지막 로우를 채우고 그 다음번에 왔다 라는 걸 의미

        # 사실 대각선을 체크하는 것도.. 중요해 보이지만 저건 어떻게 생각해낼 수가 있나? 다른 문제에서도 쓸 수 있을까 라는 생각을 했다.
        # 일반적이지 않은 조금은 기상천외하다? 라고 느꼈다

        totalCnt += 1
        return
        # 퀸 다 놔뒀으면 리턴
    
    # 해당 로우로 왔어. 
    # 컬럼별로 돌아야지 놔둘 때가 있는지
    else:
        for i in range(N):
            # N 번째 컬럼까지 볼거야
            
            graph[queenCnt] = i
            # queenCnt 이 지금 몇번째 로우 인지 가르쳐 주는 거야
            # i는 몇번째 컬럼인지

            # 그래서 바로 위 코드는? [queenCnt][i] 에다가 퀸을 놓겠다 가 되는거지

            if canFix(queenCnt):
                # 만약 지금 퀸을 놓을 위치가 되는 위치라면 다음 로우로 넘어가
                dfs(queenCnt+1)

        # 만약에 안됐어 그럼 => graph[queenCnt] = i
        # 바로 다음 컬럼 값으로 갱신하고 다시 확인하겠지 => visitMap 을 만들어줄 필요가 없다. 
        # 어차피 컬럼값이 갱신되면서 다음 컬럼 에다가 퀸을 놔둘 수 있는지 보거든

dfs(0)
# 여기서 제일 처음 호출하는 0은? 0번째 로우를 말하지
print(totalCnt)
