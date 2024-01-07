def isPrime(n):
    if(n==1) : return 0
    if( n%2 == 0):
        if(n==2): return 1
        else : return 0
    
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1

m = int(input())
n = int(input())
arr = [i for i in range(m,n+1) if isPrime(i)]
if (len(arr)<1):
    print(-1)
else :
    print(sum(arr))
    print(min(arr))