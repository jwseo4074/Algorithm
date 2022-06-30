def solution(phone_book):
    answer = True

    # for i in range(len(phone_book)):
    #     for j in range(len(phone_book)):
    #         if i == j:
    #             continue
    #         if phone_book[i] in phone_book[j] and phone_book[i][0] == phone_book[j][0]:
    #                 return False
    # return True
    # # # 반례 =>  phone_book = ['123', '13123'] 

    # # ## 두 번째

    
    # print(phone_book)
    # phone_book.sort()
    # print(phone_book)

    # for i in range(len(phone_book) - 1):
    #     if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
    #         return False
    # return True

    ## 세 번째 => 정석

    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""

        for number in phone_number:
            temp += number

            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
    
phone_book = ["119", "97674223", "1195524421"]
# false
# phone_book = ["123","456","789"]	
# true
# phone_book = ["6","23","1235","12356", "12", "188988"]	
# phone_book = ["123", "1231197", "557713", "11987543"]
# phone_book = ["4321","432","122", "1334"]
# phone_book = ["113333","115555","345555","555555", "345444"]

# phone_book = ["119", "114", "112", "123223123", "1231231234"]
# false


print(solution(phone_book))