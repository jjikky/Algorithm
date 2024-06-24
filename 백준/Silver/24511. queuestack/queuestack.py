import sys
from collections import deque
input = sys.stdin.readline

n=int(input()) # 4
a = list(map(int,input().split())) # 0 1 1 0
b = list(map(int,input().split())) # 1 2 3 4
m = int(input()) # 3
c = list(map(int,input().split())) # 2 4 7

qs=deque()

for i in range(n):
    if a[i]==0: qs.appendleft(b[i])
        
for i in range(m):
    qs.append(c[i])
    print(qs.popleft(), end=' ')