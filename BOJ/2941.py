# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.


# 방법 1, 문자열 순회하면서 조건 맞는거 찾아가는 방법

# inputStr = input()
# # ljes=njak

# domainList = [ "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# cnt = 0

# i = 0

# # for i in range(0, len(inputStr)):
# while(1):
#     print("i = ", i)
#     if inputStr[i] == "c":
#         # 시작이 c 이면
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         i += 1
#         if inputStr[i] == "=":
#             cnt += 1
#             print("c=", cnt)
            
#             # i += 1
#         elif inputStr[i] == "-":
#             cnt += 1
#             print("c-")
            
#             # i += 1
#         else:
#             cnt += 1
#             print("아무것도 아님")
            
#     elif inputStr[i] == "d":
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         i += 1
#         if inputStr[i] == "z":
#             i += 1
#             if inputStr[i] == "=":
#                 cnt += 1
#                 print("dz=", cnt)
                
#             # i += 1
#         elif inputStr[i] == "-":
#             cnt += 1
#             print("d-", cnt)
#             # i += 1
#         else:
#             cnt += 1
#             print("아무것도 아님" , cnt)

#     elif inputStr[i] == "s":
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         i += 1
#         if inputStr[i] == "=":
#             cnt += 1
#             print("s=", cnt)
#         else:
#             cnt += 1
#             print("아무것도 아님" , cnt)
#     elif inputStr[i] == "z":
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         i += 1
#         if inputStr[i] == "=":
#             cnt += 1
#             print("z=", cnt)
#         else:
#             cnt += 1
#             print("아무것도 아님" , cnt)   
#     elif inputStr[i] == "l":
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         print("i = ", i)
#         i += 1
#         print("i = ", i)
#         if inputStr[i] == "j":
#             cnt += 1
#             print("lj", cnt)
#         else:
#             cnt += 1
#             print("아무것도 아님" , cnt) 
#     elif inputStr[i] == "n":
#         # if i != len(inputStr):
#             # 제일 마지막 문자가 아닐 때
#         i += 1
#         if inputStr[i] == "j":
#             cnt += 1
#             print("nj", cnt)
#         else:
#             cnt += 1
#             print("아무것도 아님" , cnt) 
#     else:
#         # i = i + 2
#         cnt += 1
#         print("아무것도 아님" , cnt) 

# 방법 1 => 너무 당연하지만 for 문을 돌아가는 인자 i를 for 문 안에서 컨트롤 할 수 없다. 
# 그래서 전역 변수로 하나 잡아두고 문자열을 순회해봤지만, index를 초과해서 읽어버리는 경우의 예외가 너무 다양하고 많다

#  방법 2 , 문자열안에 그게 들어있나? in, find메소드를 이용해서 체크

# inputStr = input()
# # ljes=njak

# domainList = [ "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# cnt = 0

# # text = "ababHello Worldabca" 
# # print("text = ", text)
# # text = text.strip("a""b""c")
# # print("text = ", text)

# while(1):
#     if "c=" in inputStr:
#         findIndex = inputStr.find("c=")
#         print("before : ", inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("c=")
#         print("after : ", inputStr)
#         cnt += 1

#     elif "c-" in inputStr:
#         findIndex = inputStr.find("c-")
#         print(inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("c-")
#         print(inputStr)
#         cnt += 1

#     elif "dz=" in inputStr:
#         # print("ㅇㅇ")
#         # findIndex = inputStr.find("dz=")
#         # print("findIndex ", findIndex)
#         print("befor : ", inputStr)

#         # inputStr1 = inputStr[:findIndex]
#         # inputStr2 = inputStr[findIndex+3:]

#         # print("inputStr1 : ", inputStr1)
#         # print("inputStr2 : ", inputStr2)

#         # inputStr = inputStr1+"a"+inputStr2
#         inputStr = inputStr.replace("dz=", "a")
#         # replace 함수가 한번만 수행하는게 아니고 dz=를 찾아서 전부 다 바꾼다

#         # print(inputStr)
#         # inputStr = inputStr.strip("dz=")
#         print("after : ", inputStr)
#         cnt += 1

#     elif "d-" in inputStr:
#         findIndex = inputStr.find("d-")
#         print(inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("d-")
#         print(inputStr)
#         cnt += 1

#     elif "lj" in inputStr:
#         findIndex = inputStr.find("lj")
#         print(inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("lj")
#         print(inputStr)
#         cnt += 1

#     elif "nj" in inputStr:
#         findIndex = inputStr.find("nj")
#         print(inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("nj")
#         print(inputStr)
#         cnt += 1

#     elif "s=" in inputStr:
#         findIndex = inputStr.find("s=")
#         print(inputStr)
#         inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.strip("s=")
#         print(inputStr)
#         cnt += 1

#     elif "z=" in inputStr:
#         print("z= 가 없다고? 여기 안들어와?")
#         findIndex = inputStr.find("z=")
#         print("before : ", inputStr)
#         # inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#         inputStr = inputStr.replace("z=","a")
#         print("after : ",inputStr)
#         cnt += 1

#     else:
#         print(cnt)
#         print(inputStr)
#         inputStr = inputStr.replace("a","")
#         print(inputStr)
#         cnt += len(inputStr)
#         print(cnt)
#         break
    
# print(cnt)

# 방법 2 => inputStr = inputStr[:findIndex]+"a"+inputStr[findIndex+2:]
#          inputStr = inputStr.strip("s=")
# 예외 : "ddz=z=" 일 때 다 없어져버린다.
# strip => 또한 인자를 하나의 독립적인 개체로 보기떄문에 865를 8,6,5 따로따로 인자로 본것 이므로 568 을 입력하였을때도 동일한 결과과 나온다.


# inputStr = input()
# cnt = 0

# while(1):
#     if "c=" in inputStr:
#         inputStr = inputStr.replace("c=", "@")
#         cnt += 1

#     elif "c-" in inputStr:
#         inputStr = inputStr.replace("c-", "@")
#         cnt += 1

#     elif "dz=" in inputStr:
#         inputStr = inputStr.replace("dz=", "@")
#         cnt += 1

#     elif "d-" in inputStr:
#         inputStr = inputStr.replace("d-", "@")
#         cnt += 1

#     elif "lj" in inputStr:
#         inputStr = inputStr.replace("lj", "@")
#         cnt += 1

#     elif "nj" in inputStr:
#         inputStr = inputStr.replace("nj", "@")
#         cnt += 1

#     elif "s=" in inputStr:
#         inputStr = inputStr.replace("s=", "@")
#         cnt += 1

#     elif "z=" in inputStr:
#         inputStr = inputStr.replace("z=", "@")
#         cnt += 1

#     else:
#         inputStr = inputStr.replace("@","")
#         # print(inputStr)
#         cnt += len(inputStr)
#         # print(cnt)
#         break
    
# print(cnt)

# # replace : 같은 문자열을 다 바꿔 버리니까 예외 => "c=c=" 이게 1이 나옴
# 주의할 점 :inputStr.replace("c=", "@") 이렇게 했으면 이걸 다시 inputStr 에다가 할당해줘야 함!!!! 
# replace 메서드는 새로운 문자열을 만드는 함수이기 때문



# 정답 코드

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
alpha = input() 
for t in a: 
    alpha = alpha.replace(t, '*') 
print(len(alpha))