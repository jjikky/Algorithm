n=int(input())
d=[0]*(n+1)
def fib(n):
    if n==1 or n==2:
        return 1
    if d[n]!=0:
        return d[n]
    d[n]=fib(n-1)+fib(n-2)
    return d[n]
print(fib(n))