inputStr = input()
lenStr = len(inputStr)
strList = []

# print("??? = ",inputStr[2:2])
for i in range(0, lenStr):
    for j in range(i, lenStr+1):
        if i == j:
            continue
        strList.append(inputStr[i:j])
        # print(strList)

# print("strList = ", strList)
convertSet = set(strList)
# print("convertSet = ", convertSet)
answerList = list(convertSet)
# print("answerList = ", answerList)
print(len(answerList))
    
