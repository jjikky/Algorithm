m,n = map(int, input().split())
arr = []
cnt=0
last=[0,0]

# 선이 꺾이는 횟수
if m > n:
    cnt=(n-1)*2 + 1
else:
    cnt=(m-1)*2

# 끝나는 점의 좌표
if m == n:
    if m % 2 == 1:
        last=[m//2+1,m//2+1]
    else:
        last=[m//2+1, m//2]
elif m > n:
    if n % 2 == 0:
        last=[n//2+1,n//2]
    else:
        last=[(n//2+1+(m-n)), n//2+1]
else:
    if m % 2 == 0:
        last=[m//2+1,m//2]
    else:
        last=[m//2+1, m//2+1+(n-m)]

print(cnt)
print(*last)