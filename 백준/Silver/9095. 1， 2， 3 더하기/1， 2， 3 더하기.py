import sys

def sol(num):
    d=[0]*(11)
    d[1],d[2],d[3]=1,2,4
    
    for i in range(4,num+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    return d[num]

input = sys.stdin.readline
t=int(input())
arr=[int(input()) for _ in range(t)]

for i in arr:
    print(sol(i))
