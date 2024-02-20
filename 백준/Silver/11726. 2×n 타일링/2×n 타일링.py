import sys

input = sys.stdin.readline

n = int(input())

dp=[0]*(n+1)

def sol(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    if dp[n]!=0:
        return dp[n]
    dp[n]=sol(n-1)+sol(n-2)
    return dp[n]
    
print(sol(n)%10007)