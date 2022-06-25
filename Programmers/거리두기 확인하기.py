# 응시자가 앉아있는 자리(P)를 의미합니다.	
# 빈 테이블(O)을 의미합니다.	
# 파티션(X)을 의미합니다.

def solution(places):

    def checkFunc(matrix):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == "P":
                    
                    # if 상하좌우가 P이면:
                    # 오른쪽
                    if col+1 <= 4 and matrix[row][col+1] == "P":
                        return 0
                    
                    # 왼쪽
                    if col-1 >= 0 and matrix[row][col-1] == "P":
                        return 0

                    # 아래쪽
                    if row+1 <= 4 and matrix[row+1][col] == "P":
                        return 0
                    
                    # 위쪽
                    if row-1 >= 0 and matrix[row-1][col] == "P":
                        return 0    
                    
                    # if 대각선 방향이 P인데 양쪽으로 X가 아닌 경우
                    # 오른쪽 위 - 1 사분면
                    if col+1 <= 4 and row-1 >= 0 and matrix[row-1][col+1] == "P":
                        if matrix[row-1][col] == "O" or matrix[row][col+1] == "O":
                            return 0
                    
                    # 오른쪽 아래 - 2 사분면
                    if col+1 <= 4 and row+1 <= 4 and matrix[row+1][col+1] == "P":
                        if matrix[row+1][col] == "O" or matrix[row][col+1] == "O":
                            return 0
                    
                    # 왼쪽 아래 - 3 사분면
                    if col-1 >= 0 and row+1 <= 4 and matrix[row+1][col-1] == "P":
                        if matrix[row+1][col] == "O" or matrix[row][col-1] == "O":
                            return 0
                    
                    # 왼쪽 위 - 4 사분면
                    if col-1 >= 0 and row-1 >= 0 and matrix[row-1][col-1] == "P":
                        if matrix[row-1][col] == "O" or matrix[row][col-1] == "O":
                            return 0
                    
                    # if 직선 거리로 중간에 테이블 두고 사람 있는 경우 -> 맨해튼 거리가 땩 2
                    # 오른쪽
                    if col+2 <= 4 and matrix[row][col+1] == "O" and matrix[row][col+2]=="P":
                        return 0
                    
                    # 왼쪽
                    if col-2 >= 0 and matrix[row][col-1] == "O" and matrix[row][col-2]=="P":
                        return 0

                    # 아래쪽
                    if row+2 <= 4 and matrix[row+1][col] == "O" and matrix[row+2][col]=="P":
                        return 0
                    
                    # 위쪽
                    if row-2 >= 0 and matrix[row-1][col] == "O" and matrix[row-2][col]=="P":
                        return 0    

        return 1

    answer = []
    for L in places:
        # print(L)
        mapA = []

        for row in L:
            mapA.append(list(row))
        
        # matrix
        # P O O O P 
        # O X X O X 
        # O P X P X 
        # O O X O X 
        # P O X X P
        
        X = checkFunc(mapA)
        answer.append(X)
        
    return answer

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]
# results = [1, 0, 1, 1, 1]
print(solution(places))

