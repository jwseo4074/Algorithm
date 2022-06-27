arr = [1,2,3,3,3,3,4,4]
# 4,2
# arr = [3,2,4,4,2,5,2,5,5]
# 3,2,3
# arr = [3,5,7,9,1]
# -1

arrDict = dict()
answer = []
for i in range(len(arr)):
    if arr[i] not in arrDict.keys():
        arrDict[arr[i]] = 1
    else:
        arrDict[arr[i]] += 1 
    
for dictKey in arrDict.keys():
    if arrDict[dictKey] != 1:
        answer.append(arrDict[dictKey])

if len(answer) == 0:
    print([-1])
else:
    print(answer)

