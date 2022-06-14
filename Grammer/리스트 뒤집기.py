listA = [1,2,3,4,5]

listB = list(reversed(listA))
print("listB = ", listB)
# reversed() 내장함수는 주어진 시퀀스 (리스트, 튜플 등)에 대해 순서가 뒤집어진 
# iterator 객체의 형태로 반환하기 때문에 list() 로 형변환 해줘야 한다.

listC = listA[::-1]
print("listC = ", listC)
listA.reverse()
print("listA= ", listA)