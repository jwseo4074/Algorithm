# n = 5
# plans = ['100 1 3', '500 4', '2000 5']
# clients = ['300 3 5', '1500 1', '100 1 3', '50 1 2']
# results = [3, 3, 1, 0]


n = 4
plans = ['38 2 3', '394 1 4']
clients = ['10 2 3', '300 1 2 3 4', '500 1']
# results = [3, 3, 1, 0]


def solution(n, plans, clients):
    # n = 부가서비스의 수
    # plans = 제공 데이터, 추가 부가서비스
    # clients = 이용 데이터, 이용 부가서비스 

    results = [0 for i in range(len(clients))]

    convert_p = [[] for _ in range(len(plans))]
    convert_s = [[] for _ in range(len(clients))]

    B = []
    for i in range(len(plans)):
        A = plans[i].split()
        # print("A = ", A)
        # A =  ['100', '1', '3']
        B = B + A[1:]
        # print(B)
        convert_p[i].append(A[0])
        convert_p[i].append(B)
        # print(convert_p)
        # [['100', ['1', '3']], ['500', ['1', '3', '4']], ['2000', ['1', '3', '4', '5']]]
    
    for i in range(len(clients)):
        # print(clients[i])
        # 300 3 5
        A = clients[i].split()
        # print("A = ", A)
        # A =  ['100', '1', '3']
        C = A[1:]
        # print(B)
        convert_s[i].append(A[0])
        convert_s[i].append(C)
        # print(convert_s)
        # [['300', ['3', '5']], ['1500', ['1']], ['100', ['1', '3']], ['50', ['1', '2']]]
    
    for i in range(len(convert_s)):
        for j in range(len(convert_p)):
            # print(convert_s[i][0])
            # print(convert_p[j][0])
            if int(convert_s[i][0]) > int(convert_p[j][0]):
                # print("데이터가 모자라")
                continue
            else:
                if i == 2:
                    print(j)
                    print(convert_s[i][1])
                    print(convert_p[j][1])

                status = True
                for k in range(len(convert_s[i][1])):
                    if convert_s[i][1][k] not in convert_p[j][1]:
                        status = False

                if status:
                    # print("찾았다")
                    results[i] = j+1
                    break

    return results

print(solution(5, plans, clients))