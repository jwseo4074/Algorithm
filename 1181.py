
if __name__ == '__main__':
    input_num = int(input())
    count = 0
    str_list = []
    while(count != input_num):
        input_str = str(input())
        str_list.append(input_str)
        count += 1

    str_list.sort(reverse=False)
    ## 오름차순으로 정렬해놓고
    ##print(str_list)

    str_list.sort(key=len)
    ## key=len -> 원소 길이로 정렬
    ##print(str_list)

    new_str_list = []
    for a in str_list:
        if a not in new_str_list:
            new_str_list.append(a)

    for a in new_str_list:
        print(a)
