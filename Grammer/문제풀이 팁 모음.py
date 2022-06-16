# 1. 시간, 공간 복잡도 확인
# 코드 다 짰을 때 (최대 값-최악의 상황으로 가정, 넣었을 때) 시간 체크

import time
start_time = time.time()

# 프로그램 작성 -> 내가 짠 코드

end_time = time.time()
print("time :", end_time - start_time)


# 2. 입출력
# 3 3 3     <-- 변수로 저장
n, m, k = map(int, input().split())

# 2 4 5 2 3 <-- 배열로 저장
data = list(map(int, input().split()))

# 3. 데이터 입력 받기
# 데이터가 공백없는 형태로 입력될 때
# 12345 --> [1, 2, 3, 4, 5]
data.append(list(map(int, input())))

# 데이터가 공백을 두고 입력될 떄
# 1 2 3 4 5 --> [1, 2, 3, 4, 5]
data.append(list(map(int, input().split())))

# 3. 입력 시간 줄이기
import sys
input = sys.stdin.readline
# input 그대로 쓰면 됨

# 4. 정렬
# 내림차순 정렬
B = [1, 4, 5, 2, 3]
B.sort(reverse=True)

# 오름차순 정렬
B = [1, 4, 5, 2, 3]
B.sort()

#1 튜플리스트, 2차원리스트일 경우 여러 가지 기준으로 정렬하기.
# s_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

#2 튜플에 숫자형과 문자형이 섞여있을 경우 숫자형에 int()를 씌워주면
# bad operand type for unary -: 'str' 이슈를 해결할 수 있다
# s_list.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0] ))


#3 리스트에서 median 값 구하는 식
data[(n-1) // 2] # n은 리스트 길이

#4 sorted with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result2 = sorted(array, key = lambda x: x[1])
result1 = sorted(array, key = lambda x: x[1], reverse=True)
# 성적을 기준으로 오름차순정렬
print("내림차순 : ", result1)
print("오름차순 : ", result2)


#5 문자열, 배열, 튜플 등을 역순으로 출력(간결하게)
s = 'abcde'
print(s[::-1])  # 'edcba'
print(s[3:0:-1])  # dcba, 0~3인덱스를 역순으로

l = ['a', 'b', 'c', 'd', 'e']
print(l[::-1])  # ['e', 'd', 'c', 'b', 'a']
t = ('a', 'b', 'c', 'd', 'e')
print(t[::-1])  # ('e', 'd', 'c', 'b', 'a')

# 5. 2차원 배열 좌표 이동

n = int(input())
x, y = 1,1
plans = input().split()

## R, D, L, U
dx = [1, 0, -1, 0]
dy = [0,-1,  0, 1]
move = ['R', 'D', 'L', 'U']
# 오른쪽, 밑, 왼쪽, 위 => 시계 방향으로

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny


# 6. 2차원 배열 90도 회전
before = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
n = 5 
# len(a) # 행 길이 계산
m = 5
# len(a[0]) # 열 길이 계산
result = [[0] * n for _ in range(m)]
after1 = [] # 90도 회전된 배열 저장
after2 = [] # 90도 회전된 배열 저장

# 시계방향으로 회전
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(before[m-1-j][i])
    after1.append(tmp)

print("\n 시계 = ", after1)

# 반시계방향으로 회전
for i in range(m):
    tmp  = []
    for j in range(n):
        tmp.append(before[j][m-1-i]) 
        #반시계
    after2.append(tmp)

print("\n 반시계 after =", after2)

# eval() : 문자열로 표현된 수식의 계산 결과값을 반환
result = eval("(3+5)*7")
# --> 56

# 7. 순열과 조합
# 순열 : 주어진 데이터를 가지고 서로 다른 n 개를 선택하여 일렬로 나열하는 것 
from itertools import permutations

data = [1, 4, 5, 6, 7]
result = list(permutations(data,3))

# 조합 : 주어진 데이터를 가지고 서로 다른 n 개를 선택하는 것 
from itertools import combinations

data = [1, 4, 5, 6, 7]
result = list(combinations(data,3))
