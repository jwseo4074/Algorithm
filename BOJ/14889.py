N = int(input())
Nlist = [i for i in range(0,N)]

from itertools import combinations  

inputMap = []
for i in range(N):
    inputMap.append(list(map(int, input().split())))

minVal = 1e9

# startTeam = []
# linkTeam = []

cnt = 0

# Nlist = [i for i in range(1,N+1)]
# print(Nlist)

totalList = []
combiList = list(combinations(Nlist, int(N/2)))

for oneVal in combiList:
    startTeam = list(oneVal)
    linkTeam = [x for x in Nlist if x not in startTeam]
    totalList.append([startTeam, linkTeam])

def funcProcess():
    global minVal

    for Team in totalList:
        startTeam = Team[0]
        linkTeam = Team[1]
        sumStart = 0
        sumLink = 0
        # print("startTeam = ", startTeam)
        # print("linkTeam = ", linkTeam)


        # startTeam =  [0, 1, 4]
        for i in range(0, len(startTeam)):
            # print("i = ", i)
            for j in range(i+1, len(startTeam)):
                # print("i = ", i , " j = ", j, " startTeam[i] = ", startTeam[i], " startTeam[j] = ", startTeam[j]) 
                sumStart += inputMap[startTeam[i]][startTeam[j]] + inputMap[startTeam[j]][startTeam[i]]
        # print("sumStart = ", sumStart)
        # startTeam 합 구하기
        
        # linkTeam = [2,3,5]
        for i in range(len(linkTeam)):
            for j in range(i+1, len(linkTeam)):
                sumLink += inputMap[linkTeam[i]][linkTeam[j]] + inputMap[linkTeam[j]][linkTeam[i]]
        # print("sumLink = ", sumLink)
        # linkTeam 합 구하기
        
        
        minVal = min(minVal, abs(sumStart-sumLink))
        # print("minVal = ", minVal)
        # 최소값 구하기
        # print("minVal = ", minVal)

funcProcess()
print(minVal)

