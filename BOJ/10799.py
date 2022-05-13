inputStr = input()
answer = 0
openCharCnt = 0

for i in range(len(inputStr)):
    if i == len(inputStr)-1:
        # i + 1 하면 에러, 젤 마지막은 무조건 ")" 이겠지
        answer += 1
        break

    if inputStr[i] == "(":
        # "(" 일 때
        if inputStr[i+1] == ")":
            # () 일 때
            # print("계산하기")
            answer += openCharCnt
            # 계산하기
        else:
            # (( 일 때
            # print("push")
            openCharCnt += 1

    else:
        # ")" 일 때
        if inputStr[i-1] == "(":
            continue
        # print("pop 하고 개수 1 추가")
        openCharCnt -= 1
        answer += 1
    # print("openCharCnt = ",openCharCnt)
    # print("answer = ", answer)

print(answer)

