inputList = input().split('-')
# 55-50+40

# 55 , 50+40

# -를 경계로 나누니까 묶음은 무조건 +고 이걸 괄호 씌워서 -로 만들면 최소값이 될 수밖에 없다. 

numList = []

for i in range(len(inputList)):
    sumOfNum = 0

    if i == 0:
        numList.append(inputList[i])
        continue

    exceptPlusList = inputList[i].split('+')

    for oneNum in exceptPlusList:
        sumOfNum += int(oneNum)

    numList.append(sumOfNum)

startVal = numList[0]

for i in range(1, len(numList)):
    startVal -= int(numList[i])

print(startVal)
    
