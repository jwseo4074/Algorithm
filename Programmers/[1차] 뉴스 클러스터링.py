from curses.ascii import isalpha
from math import floor


# str1 = "FRANCE"
# str2 = "french"
# 16384

# str1 = "handshake"
# str2 = "shake hands"
# 65536

# str1 = "aa1+aa2"
# str2 = "AAAA12"
# 43690

str1 = "E=M*C^2"
str2 = "e=m*c^2"
# 65536

def solution(str1, str2):
    answer = 0
    A = []
    B = []
    for i in range(len(str1)-1):
        if isalpha(str1[i]) and isalpha(str1[i+1]):
            x = str1[i].upper() + str1[i+1].upper()
            A.append(x)
    for i in range(len(str2)-1):
        if isalpha(str2[i]) and isalpha(str2[i+1]):
            x = str2[i].upper() + str2[i+1].upper()
            B.append(x)
    

    # A = ["11", "11", "11"]
    # B = ["12", "20"]


    if len(A) == 0 and len(B) == 0:
        return 65536

    Adict = dict()
    Bdict = dict()
    
   

    for a in A:
        if a not in Adict.keys():
            Adict[a] = 1
        else:
            Adict[a] += 1
    for b in B:
        if b not in Bdict.keys():
            Bdict[b] = 1
        else:
            Bdict[b] += 1
    
    # print("Adict = ", Adict)
    # print("Bdict = ", Bdict)

    num1 = 0
    num2 = 0

    for a in Adict.keys():
        if a in Bdict.keys():
            num1 += min(Adict[a], Bdict[a])
            
    for a in Adict.keys():
        if a in Bdict.keys():
            num2 += max(Adict[a], Bdict[a])
            Bdict[a] = 0
        else:
            num2 += Adict[a]

    for b in Bdict.keys():
        num2 += Bdict[b]

    answer = floor(num1 / num2 * 65536)
    return answer

print(solution(str1, str2))
