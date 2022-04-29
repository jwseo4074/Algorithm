answer = []
while(1):
    try:
        a, b = map( int, input().split())
        answer.append(a + b)
    except:
        for i in answer:
            print(i)
        break



# 입력을 안받았을 경우에 어떻게 처리해줄건가?
# 그냥 엔터를 치는 경우?

# 에러가 발생하는 경우에 프린트를 하면 된다.