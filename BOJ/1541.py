inputList = input().split('-')

# print(inputList)

totalNumList = []

for word in inputList:
    sumVal = 0
    numList = word.split('+')
    
    for i in range(len(numList)):
        sumVal += int(numList[i])
    
    totalNumList.append(sumVal)
    # print(sumVal)

answer = 0
for i in range(len(totalNumList)):
    if i == 0:
        answer = totalNumList[i]
    else:
        answer -= totalNumList[i]
print(answer)

