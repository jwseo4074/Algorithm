s = "aa"

# 1. 문자열 자르기 => 이거 잘라놓은걸로 한번 loop 진행, 한번의 단계(process)
answer = 1000

if len(s) == 1:
    answer = 1
    
for N in range(1, len(s)):
    # # 자르는건 최대 절반
    # sliceList = [s[i:i+N] for i in range(0, len(s), N)]
    # # N개로 잘라서 배열에 저장
    # print(N, "개로 잘라서 배열 만들기")
    # print("sliceList = ", sliceList)
    
    resultStr = ""
    cnt = 1
    tmp = s[:N]

    for i in range(N, N+len(s), N):
        # 시작점을 N으로 두면 돼
        if tmp == s[i:i+N]:
            # i에서 N만큼 건너 뛰면서 보면 돼
            # 만약에 같으면? 
            cnt += 1
            
        else:
            # 만약에 다르면? 
            if cnt == 1:
                # 처음들어왔단 말
                resultStr += tmp
            else:
                # 지금까지 같은게 여러 개 있었단 말
                resultStr += str(cnt) + tmp
            tmp = s[i:i+N] 
            # 다음 문자열로 바꿔줘
            cnt = 1
            # cnt 초기화

    answer = min(answer, len(resultStr))
print(answer)


    # for i in range(0, len(sliceList)-1):
    #     tmp = sliceList[i]
    #     # 비교할 대상 하나 정하기
    #     # 첫 번째 비교 대상 => aa
    #     print("i = ", i, " tmp = ", tmp)

    #     cnt = 1

    #     for j in range(i+1,len(sliceList)):
    #         print("j = ", j, " 비교할 문자열 = ", sliceList[j])
    #         if tmp == sliceList[j]:
    #             print("똑같은 거네?")
    #         # 바로 다음 문자열(bb)이랑 같은거면?
    #             cnt += 1
    #             print("cnt = ", cnt)

    #         else:
    #             # aa랑 bb랑 달라 -> 1aa
    #             print("다른거네")
    #             break
        
    #     if cnt == 1:
    #         resultStr += tmp
    #     else:
    #         resultStr += str(cnt) + tmp
        
    #     print("resultStr = ", resultStr)
    #     answer = min(answer, len(resultStr))

    
