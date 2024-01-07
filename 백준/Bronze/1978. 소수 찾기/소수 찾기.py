def isPrime(n):
    if(n==1) : return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
cnt=0
input()
num = map(int,input().split())
for i in num:
    if(isPrime(i)):
        cnt+=1
print(cnt)