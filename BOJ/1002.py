def cal_distance(list):
    l0 = int(list[0])
    l1 = int(list[1])
    l2 = int(list[2])
    l3 = int(list[3])
    l4 = int(list[4])
    l5 = int(list[5])

    r1 = l2
    r2 = l5
    distance = ( (l3 - l0) ** 2 + (l4 - l1) ** 2 )**0.5  # 두 원의 거리 (원의방정식활용)

    if distance == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 때
        print(-1)
    elif(abs(r1-r2) < distance < (r1+r2) ):
    ##겹쳐질때
        print(2)
    elif (r1+r2 == distance or distance == abs(r1-r2)):
    ##접점 한개일때
        print(1)
    else:
    ## 외접
        print(0)

if __name__ == "__main__":
    count = int(input())
    i = 0
    input_list = []
    while(i != count):
        input_str = input()
        input_str = input_str.split(" ")
        input_list.append(input_str)
        i += 1
    i = 0
    while (i != count):
        cal_distance(input_list[i])
        i += 1
 ##       "print(answer)"

