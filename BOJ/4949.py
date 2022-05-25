from collections import deque

answer = []
inputStrList = []

while(1):
    inputStr = input()
    
    if inputStr == ".":
        break

    inputStrList.append(inputStr)

status = False

for inputStr in (inputStrList):
    deq1 = deque()
    status = False 

    for i in range(len(inputStr)):

        # print(inputStr[i])

        if inputStr[i] == "(":
            # print(1)
            deq1.append(1)
        if inputStr[i] == ")":
            # print(2)
            if deq1:
                if deq1[-1] == 1:
                    deq1.pop()
                else:
                    status = True
                    break
            else:
                status = True
                break

        if inputStr[i] == "[":
            # print(3)
            deq1.append(2)
        if inputStr[i] == "]":
            # print(4)
            if deq1:
                # print(5)
                if deq1[-1] == 2:
                    # print(6)
                    deq1.pop()
                else:
                    status = True
                    break
            else:
                status = True
                break

    if status == True:
        answer.append("no")
        continue

    if len(deq1) == 0 :
        answer.append("yes")
    else:
        answer.append("no")

for i in answer:
    print(i)


# YES NO 이걸로 1시간 삽질