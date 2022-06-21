# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	
# # result = [8, 10, 25]

# rows = 3	
# columns = 3	
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	
# # result = [1, 1, 5, 3]

rows = 100	
columns = 97	
queries = [[1,1,100,97]]	
#result = [1]

def solution(rows, columns, queries):
    answer = []
    matrix = []
    matrix.append([0] * (columns+1))
    for _ in range(rows):
        matrix.append([0] * (columns+1))
    # print(matrix)

    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i][j] = num 
            num += 1
    # print(matrix)

    for X in queries:
        a1 = X[0]
        a2 = X[1]
        b1 = X[2]
        b2 = X[3]
        numList = []

        corner1 = matrix[a1][a2]
        # 왼쪽 위 모서리
        corner2 = matrix[a1][b2]
        # 오른쪽 위 모서리
        corner3 = matrix[b1][b2]
        # 오른쪽 아래 모서리
        corner4 = matrix[b1][a2]
        # 왼쪽 아래 모서리
        
        # print()

        # print("매트릭스 ")
        # for i in range(rows+1):
        #     print(matrix[i])
        # print()

        # 윗 줄
        for col in range(b2, a2, -1):
            # print("row = ", a1, " col = ", col, " = ", matrix[a1][col], " => ", matrix[a1][col-1])
            matrix[a1][col] = matrix[a1][col-1]
            numList.append(matrix[a1][col-1])
        # print("윗줄 끝")
        # print("numList = ", numList)
        
        # print("매트릭스 ")
        # for i in range(rows+1):
            # print(matrix[i])
        # print()

        # 오른쪽 줄
        for row in range(b1, a1, -1):
            if row == a1+1:
                # print("row = ", row, " col = ", b2, " = ", matrix[row][b2], " => ", corner2)
                matrix[row][b2] = corner2
                numList.append(corner2)
                continue
            
            # print("row = ", row, " col = ", b2, " = ", matrix[row][b2], " => ", matrix[row-1][b2])
            matrix[row][b2] = matrix[row-1][b2]
            numList.append(matrix[row-1][b2])
        # print("오른쪽 줄 끝")
        # print("numList = ", numList)

        # print("매트릭스 ")
        # for i in range(rows+1):
            # print(matrix[i])
        # print()

        # 아래 줄
        for col in range(a2, b2):
            if col == b2-1:
                # print("row = ", b1, " col = ", col, " = ", matrix[b1][col], " => ", corner3)
                matrix[b1][col] = corner3
                numList.append(corner3)
                continue
            # print("row = ", b1, " col = ", col, " = ", matrix[b1][col], " => ", matrix[b1][col+1])
            matrix[b1][col] = matrix[b1][col+1]
            numList.append(matrix[b1][col+1])
        # print("아래줄 끝")
        # print("numList = ", numList)

        # print("매트릭스 ")
        # for i in range(rows+1):
            # print(matrix[i])
        # print()

        # 왼쪽 줄
        for row in range(a1, b1):
            if row == b1-1:
                # print("!!!")
                # print("row = ", row, " col = ", a2, " = ", matrix[row][a2], " => ", corner4)
                matrix[row][a2] = corner4
                numList.append(corner4)
                continue
            # print("row = ", row, " col = ", a2, " = ", matrix[row][a2], " => ", matrix[row+1][a2])
            matrix[row][a2] = matrix[row+1][a2]
            numList.append(matrix[row+1][a2])
        # print("왼쪽 줄 끝")
        # print("numList = ", numList)

        # print("매트릭스 ")
        # for i in range(rows+1):
            # print(matrix[i])

        # print("@@@@@@@@@@@@@@@ 다음 쿼리 @@@@@@@@@@@@@@@@@@@@@@@@@@")

        answer.append(min(numList))
        numList.clear()

    return answer

print(solution(rows, columns, queries))