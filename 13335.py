# 강을 가로지르는 하나의 차선으로 된 다리가 하나 있다. 이 다리를 n 개의 트럭이 건너가려고 한다. 
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다. 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다. 
# 다리의 길이는 w 단위길이(unit distance)이며, 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다. 
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다. 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 
# 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.
# 예를 들어, 다리의 길이 w는 2, 다리의 최대하중 L은 10, 다리를 건너려는 트럭이 트럭의 무게가 [7, 4, 5, 6]인 순서대로 다리를 오른쪽에서 왼쪽으로 건넌다고 하자. 
# 이 경우 모든 트럭이 다리를 건너는 최단시간은 아래의 그림에서 보는 것과 같이 8 이다.

# 입력은 두 줄로 이루어진다. 입력의 첫 번째 줄에는 세 개의 정수 n (1 ≤ n ≤ 1,000) , w (1 ≤ w ≤ 100) and L (10 ≤ L ≤ 1,000)이 주어지는데, 
# n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다. 입력의 두 번째 줄에는 n개의 정수 a1, a2, ⋯ , an (1 ≤ ai ≤ 10)가 주어지는데, 
# ai는 i번째 트럭의 무게를 나타낸다.



# n은 트럭 수, w는 다리 길이, L은 다리 최대 하중(버틸 수 있는 무게)
# 4 2 10
# 7 4 5 6
# 정답 : 8



n, w, L = map(int, input().split())
carList = list(map(int, input().split()))
onRoad = [0] * w
# print(onRoad)

# sumW = 0
#  파이썬 내장 함수로 배열 안의 값들을 전부 합해주는 함수가 있다. 그걸 써본다
totalCnt = 0

while(onRoad):
    # 도로 위에 트럭이 없어질 때까지 ㄱ

    onRoad.pop(0) # 앞 자리 하나 비워

    if(carList):
        # 차가 있을 때
        oneValue = carList[0] # 이번에 다룰 차
    
        if sum(onRoad) + oneValue > L : # 무게 체크, 10보다 크면?
            # sum(배열) => 배열의 무게를 자동으로 계산해줌, 이걸 왜 몰랐을까? 알면서 안쓴건가
            onRoad.append(0)

        else: # 무게 체크, 10(w)보다 작으면? 
            onRoad.append(carList.pop(0)) # 2줄로 짤걸 한 줄로 줄여!!!!
            # carList에서 젤 앞에 있는 놈 -> truck 빼서 도로에 올려
    else:
        onRoad.append(0)
        if sum(onRoad) == 0:
            totalCnt += 1
            break
    
    # 한바퀴 돌리면 totalCnt ++
    totalCnt += 1
    # print(onRoad)
    # print("totalCnt = ", totalCnt)
    # input()

print(totalCnt)