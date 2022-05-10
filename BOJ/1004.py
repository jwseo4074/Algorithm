
t = int(input())
for _ in range(t):
    cnt = 0
    x1,y1,x2,y2 = map(int, input().split())
    n =int(input())
    for __ in range(n):
        cx,cy,cr = map(int, input().split())
        d1 = ( (x1-cx)**2 + (y1-cy)**2 )**0.5
        d2 = ( (x2-cx)**2 + (y2-cy)**2 )**0.5
        if (d1 > cr and d2 < cr) or (d1 < cr and d2 > cr):
            cnt += 1
    print(cnt)