orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
# result = ["AC", "ACDE", "BCFG", "CDE"]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]
# result = ["ACD", "AD", "ADE", "CD", "XYZ"]

# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
# result = ["WX", "XY"]

from itertools import combinations

def solution(orders, course):
    answer = []
    # dictOrder2 = dict()
    # dictOrder3 = dict()
    # dictOrder4 = dict()
    

    for cnt in course:
        # print("cnt = ", cnt)
        dictOrder = dict()
        for order in orders:
            # print(order)
            A = list(order)

            # ABCFG 에 대해서 가능한 조합 만들어
            combiList = list(combinations(A, cnt))
            for combi in combiList:
                XX = list(combi)
                XX.sort()
                X = ''.join(XX)

                # if cnt == 2:
                if X in dictOrder.keys():
                    nowCnt = int(dictOrder[X])
                    nowCnt += 1
                    dictOrder[X] = nowCnt
                else:
                    dictOrder[X] = 1
        # print("dictOrder = ", dictOrder)
        
        # input()
        sortedDict = sorted(dictOrder.items(), key=lambda x: x[1], reverse=True)
        # print("sortedDict = ", sortedDict)
        if len(sortedDict) >= 1:
            maxInt = sortedDict[0][1]
            for dictOne in sortedDict:
                if dictOne[1] == maxInt and dictOne[1] >= 2:
                    answer.append(dictOne[0])
                else:
                    break
        # print("answer = ", answer)
        # print(answer)
                # if cnt == 3:
                #     if X in dictOrder3.keys():
                #         nowCnt = int(dictOrder3[X])
                #         nowCnt += 1
                #         dictOrder3[X] = nowCnt
                #     else:
                #         dictOrder3[X] = 1
                # if cnt == 4:
                #     if X in dictOrder4.keys():
                #         nowCnt = int(dictOrder4[X])
                #         nowCnt += 1
                #         dictOrder4[X] = nowCnt
                #     else:
                #         dictOrder4[X] = 1

    # sortedDict2 = sorted(dictOrder2.items(), key=lambda x: x[1], reverse=True)
    # sortedDict3 = sorted(dictOrder3.items(), key=lambda x: x[1], reverse=True)
    # sortedDict4 = sorted(dictOrder4.items(), key=lambda x: x[1], reverse=True)
    answer.sort()
    return answer

print(solution(orders, course))
