# periods
# [20, 23, 24], 

# payments
# [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], 
# [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], 
# [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],

# estimates
#  [100000, 100000, 100000]


periods = [24, 59, 59, 60]

payments = [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], 
[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], 
[350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000],
[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
 
estimates = [350000, 50000, 40000, 50000]

# periods = [20, 23, 24]

# payments = [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], 
# [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], 
# [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]

# estimates = [100000, 100000, 100000]

def solution(periods, payments, estimates):
    answer = []
    answer.append(0)
    answer.append(0)

    for i in range(len(periods)):
        # 1. 기간 체크
        # print( "i = ", i)
        if periods[i] + 1 < 24:
            # 2년 미만 
            # print("2년이 안되서 VIP 안돼")
            continue
        else:
            # 원래 2년 이상이거나 1개월 더 넣으면 VIP 될 가능성도 있다.
            
            # 1. 1개월 더 넣으면 2년 이상이 되는 경우 + 
            if periods[i] == 23:
                if sum(payments[i]) - payments[i][0] + estimates[i] >= 900000:
                    answer[0] += 1
                    # print("23개월에서 1개월 더 넣고 24개월 됐고, 금액이 원래 안됐다가 이번 달 넣고 VIP 됐음")
                    continue
                
                        
            # 2. 2년 이상 5년 미만인 경우
            # 2-1. 금액이 원래 안됐다가 이번 달 넣고 VIP 되는 경우
            # 2-2. 원래 VIP 였는데 이번 달 넣고 VIP가 안되는 경우

            if 24 <= periods[i] < 58:
                # 이전까지 납부한 금액
                sumPayment = sum(payments[i])
                
                # 지금이 VIP 인가? 
                if sumPayment >= 900000:
                    # print("지금 이미 VIP 맞다")
                    if sumPayment - payments[i][0] + estimates[i] < 900000:
                        # print("VIP 박탈")
                        answer[1] += 1
                else:
                    # print("지금 VIP 아니다")
                    # 이전에 VIP가 아니었는데 돈 내고 나면 VIP 인가?
                    if sumPayment - payments[i][0] + estimates[i] >= 900000:
                        # print("VIP 획득")
                        answer[0] += 1
                continue

            # 3. 5년 이상인 경우
            # 3-1. 59개월에서 1개월 더 넣어서 VIP 기준이 올라가는 경우
            # 3-2. 원래 60개월 이상인 경우
                # 3-2-1. 금액이 원래 안됐다가 이번 달 넣고 VIP 되는 경우
                # 3-2-2. 원래 VIP 였는데 이번 달 넣고 VIP가 안되는 경우
            
            if periods[i] == 59:
                # print("59개월일 때")
                # 이전까지 납부한 금액
                sumPayment = sum(payments[i])
                
                if sumPayment < 900000:
                    # 88만원으로 골드였는데 1개월 더 넣고 5년 이상 되서 VIP 되는 경우
                    if sumPayment - payments[i][0] + estimates[i] >= 600000:
                        answer[0] += 1
                else:
                    # 원래 VIP 였는데 한달 더 넣고 60만원을 못맞추는 경우
                    if sumPayment - payments[i][0] + estimates[i] < 600000:
                        answer[1] += 1
                continue

            if periods[i] >= 60:
                # 이전까지 납부한 금액
                sumPayment = sum(payments[i])
            
                # 지금이 VIP 인가? 
                if sumPayment >= 600000:
                    # print("지금 이미 VIP 맞다")
                    if sumPayment - payments[i][0] + estimates[i] < 600000:
                        # print("VIP 박탈")
                        answer[1] += 1
                else:
                    # print("지금 VIP 아니다")
                    # 이전에 VIP가 아니었는데 돈 내고 나면 VIP 인가?
                    if sumPayment - payments[i][0] + estimates[i] >= 600000:
                        # print("VIP 획득")
                        answer[0] += 1
                continue

    return answer

print(solution(periods, payments, estimates))




