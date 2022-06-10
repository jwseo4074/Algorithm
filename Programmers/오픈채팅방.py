# record = ["Enter uid1234 Muzi", "Change uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo"]

# def solution():
#     answer = []
#     recordList = []

#     for oneVal in record:
#         recordList.append(oneVal.split())

#     memberList = []
#     leaveList = []

#     for oneVal in recordList:
#         if oneVal[0] == "Enter":
#             memberList.append((oneVal[1], oneVal[2]))

#         if oneVal[0] == "Leave":
#             for i in range(0, len(memberList)):
#                 if memberList[i][0] == oneVal[1]:
#                     memberList.remove(memberList[i])
#                     leaveList.append(memberList[i][1])
#                     break

#         if oneVal[0] == "Change":
#             for i in range(0, len(memberList)):
#                 if memberList[i][0] == oneVal[1]:
#                     memberList.remove(memberList[i])
#                     memberList.append((oneVal[1], oneVal[2]))
#                     break

#     for oneVal in recordList:
#         if oneVal[0] == "Enter":
#             for i in range(0, len(memberList)):
#                 if memberList[i][0] == oneVal[1]:
#                     answer.append(str(memberList[i][1])+"님이 들어왔습니다.")
#                     break

#         if oneVal[0] == "Leave":
#             answer.append(str(leaveList.pop(0))+"님이 나갔습니다.")
            
#     return answer

# print(solution())

def solution(record):

    answer = []
    actions = []
    userDB = {}
    recordList = []
    
    for oneVal in record:
        recordList.append(oneVal.split())
        
    for oneVal in recordList:
        if oneVal[0] in ("Enter", "Change"):
            userDB[oneVal[1]] = oneVal[2]
        actions.append((oneVal[0], oneVal[1]))
    
    
    for a in actions:
        if a[0] == 'Enter':
            answer.append(f'{userDB[a[1]]}님이 들어왔습니다.')
        elif a[0] == 'Leave':
            answer.append(f'{userDB[a[1]]}님이 나갔습니다.')
            
        
    return answer