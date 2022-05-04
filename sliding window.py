s = "abcabcbb"
# 채점할 때에는 s가 주어짐

ans = 0
pointL = 0
used = {}

for pointR, char in enumerate(s):
    # 만약에 a 가 또 나왔어, 이 때 pointR은 3이지, char은 a야
    if char in used and pointL <= used[char]:
        pointL = used[char] + 1
        # 왼쪽 커서를 중복 됐던 문자의 인덱스에 + 1 => 1로 설정
    
    else:
        # 처음 나오는 문자라면
        ans = max(ans, pointR - pointL + 1)
        # 중복 전까지 다른 문자가 연속된 최대 횟수
        # 오른쪽 - 왼쪽 + 1 => 그 사이에 몇개가 있나 ?
    used[char] = pointR
    # a : 3이 되겠지

# return ans

# 만약에 b차례야, char 은 b, pointR은 4가 나오지
# b는 이미 있는거고 used 에 b : 1 이 있어
# pointL 업데이트 값 업데이트 해줘