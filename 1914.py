

# N = int(input())

# list1 = []
# list2 = []
# list3 = []

def FuncA(start, end, temp, N):
    # if N == 1000:
    #     startList = list1
    #     endList = list3
    #     tempList = list2

    #     lastVal = startList[-1]
    #     startList.pop()
    #     endList.append(lastVal)
    #     print("1 3")
    #     # 1->3

    #     lastVal = startList[-1]
    #     startList.pop()
    #     tempList.append(lastVal)
    #     print("1 2")
    #     # 1->2

    #     lastVal = endList[-1]
    #     endList.pop()
    #     tempList.append(lastVal)
    #     print("3 2")
    #     # 3->2

    #     lastVal = startList[-1]
    #     startList.pop()
    #     endList.append(lastVal)
    #     print("1 3")
    #     # 1->3

    #     lastVal = tempList[-1]
    #     tempList.pop()
    #     startList.append(lastVal)
    #     print("2 1")
    #     # 2->1

    #     lastVal = tempList[-1]
    #     tempList.pop()
    #     endList.append(lastVal)
    #     print("2 3")
    #     # 2->3

    #     lastVal = startList[-1]
    #     startList.pop()
    #     endList.append(lastVal)
    #     print("1 3")
    #     # 1->3

    if N == 1:
        print("1 3")
    elif N == 2:
        print("1 2")
        print("1 3")
        print("2 3")
    elif N == 3:
        print(start, end)
        print(start, temp)
        print(end, temp)
        print(start, end)
        print(temp, start)
        print(temp, end)
        print(start, end)

    else:
        FuncA(start, temp, end, N-1)
        # 무조건 end(3)이 아닌 쪽으로 옮겨놔야 해 

        FuncB(start, end)
        # print(start, end)

        FuncA(temp, end, start, N-1)

    # calFunc(N-1)

    # startList = list1
    # endList = list2
    # tempList = list3

    # # if startPoint == 1:
    # #     startList = list1
    # # if endPoint == 2:
    # #     endList == list2
    # # if tempPoint == 3:
    # #     tempList = list3

    # lastVal = startList[-1]
    # startList.pop()
    # endList.append(lastVal)
    # # 1->3

    # lastVal = startList[-1]
    # startList.pop()
    # tempList.append(lastVal)
    # # 1->2

    # lastVal = endList[-1]
    # endList.pop()
    # tempList.append(lastVal)
    # # 3->2

    # lastVal = startList[-1]
    # startList.pop()
    # endList.append(lastVal)
    # # 1->3

    # lastVal = tempList[-1]
    # tempList.pop()
    # startList.append(lastVal)
    # # 2->1

    # lastVal = tempList[-1]
    # tempList.pop()
    # endList.append(lastVal)
    # # 2->3

    # lastVal = startList[-1]
    # startList.pop()
    # endList.append(lastVal)
    
def FuncB(start, end):
    # lastVal = list1[-1]
    # list1.pop()
    # list3.append(lastVal)
    print(start, end)

# def startFunc(N):
#     for i in range(N, 0, -1):
#         list1.append(i)

# def printFunc():
#     print("list1 = ", list1)
#     print("list2 = ", list2)
#     print("list3 = ", list3)

# startFunc(N)
N = int(input())
print((1 << N)-1)
if N<=20 :
    FuncA(1, 3, 2, N)
    # 시작할 때만 무조건 1에서 3으로 옮기는 게 목표
    # 안으로 들어가서는 계속 달라지지


