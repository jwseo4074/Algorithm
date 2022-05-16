inputStr = input()
bombStr = input()
bombLen = len(bombStr)
bombLastChar = bombStr[-1]
Stack = []

for char in inputStr:
    Stack.append(char)		
    # 한 글자씩 스택에 넣는다

    if char == bombLastChar and ''.join(Stack[-bombLen:]) == bombStr:
    # 현재 스택에 넣은 문자가 폭발 문자열의 맨끝 문자와 일치하고,
    # 스택에서 폭발문자열의 길이만큼 문자열을 추출했을 때, 이 문자열이 폭발문자열과 일치한다면?
        del Stack[-bombLen:]			
        # 해당 문자열을 스택에서 제거한다.


if Stack:
    print("".join(Stack))
else:
    print("FRULA")

    
