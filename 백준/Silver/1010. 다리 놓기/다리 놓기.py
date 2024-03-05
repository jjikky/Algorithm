
import sys
input = sys.stdin.readline

n=int(input())
arr=[]
max_m=0
for i in range(n):
    n,m=map(int,input().split())
    if m>max_m:max_m=m
    arr.append([n,m])

dp=[0]*(m+1)
dp[1]=1
for i in range(2,m+1):
    dp[i]=i*dp[i-1]

for i in arr:
    n,m=i
    if n==m:
        print(1)
    else:
        print(int(dp[m]/(dp[n]*dp[(m-n)])))


    
    