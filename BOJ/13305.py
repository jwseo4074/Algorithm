# 4
# 2 3 1 - 거리
# 5 2 4 1 - 리터 당 가격
# 18

N = int(input())
distanceList = []
priceList = []
answer = 0

distanceList = list(map(int, input().split()))
priceList = list(map(int, input().split()))

for i in range(N):
    pass

# print("distanceList = ",distanceList)
# print("priceList = ", priceList)
print(answer)


# 구글링
# 핵심 : for 문을 돌면서 지금까지 주유 가격보다 이번 도시에서의 가격이 작으면 지금까지 왔던 거리 x 가장 작았던 주유 가격을 해서 결과에 더해준다.
