H, M = map(int, input().split())
# H시 M분
# 45분 전으로 재설정

# 10시 10분 -> 9시 25분
# 0시 30분 -> 23시 45분
# 23시 40분 -> 22시 55분
# 23시 50분 -> 23시 5분

if M < 45:
    M = M + 60 - 45
    if H == 0:
        H = 23
    else:
        H = H - 1
else:
    M = M - 45 

print(H, M)