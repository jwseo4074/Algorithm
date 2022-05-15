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

minPrice = priceList[0]
# 초기값 설정

for i in range(N-1):
    if minPrice > priceList[i]:
        minPrice = priceList[i]
    answer += minPrice * distanceList[i]

print(answer)

