# # 상근이는 길을 걷다가 신기한 기계를 발견했다. 기계는 매우 매우 큰 화면과 버튼 하나로 이루어져 있다.
# # 기계를 발견했을 때, 화면에는 A만 표시되어져 있었다. 버튼을 누르니 글자가 B로 변했다. 
# # 한 번 더 누르니 BA로 바뀌고, 그 다음에는 BAB, 그리고 BABBA로 바뀌었다. 상근이는 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 사실을 알게되었다.
# # 버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

# # B -> BA
# # A -> B
# # 처음에는 A

# K = int(input())
# ABstr= "A"

# for i in range(0, K):
#     ABList = list(ABstr)

#     for j in range(0, len(ABList)):
#         if ABList[j] == 'A':
#             ABList[j] = 'B'
#         elif ABList[j] == 'B':
#             ABList[j] = 'BA'

#     ABstr = ""

#     for j in range(0, len(ABList)):
#         ABstr += str(ABList[j])

# cntA = cntB = 0
# for i in range(0, len(ABstr)):
#     if ABstr[i] == "A":
#         cntA += 1
#     if ABstr[i] == "B":
#         cntB += 1

# print(cntA, cntB)



K = int(input()) + 1

answerList = []
for i in range(0,K):
    answerList.append([0,0,0])
# print(answerList)

answerList[0][0] = 1
answerList[0][1] = 0
answerList[0][2] = 1

for i in range(1, K):
    # print(i)
    answerList[i][0] = answerList[i-1][1]
    answerList[i][1] = answerList[i-1][2]
    answerList[i][2] = answerList[i][0] + answerList[i][1] 
    # print( answerList[i])

print(answerList[K-1][0], answerList[K-1][1])


# 생각의 흐름


