n = int(input())
dp = [0]*(n+1)
def fibo(n):
    if n==0: return 0
    elif n==1: return 1
    
    if dp[n] ==0:
        dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]
    
print(fibo(n))