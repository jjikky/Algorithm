import sys
input = sys.stdin.readline

n,m=map(int,input().split())

s = [input().rstrip() for i in range(n)]

s2 = [input().rstrip() for i in range(m)]
cnt=0
for i in s2:
    if i in s:
        cnt+=1
print(cnt)