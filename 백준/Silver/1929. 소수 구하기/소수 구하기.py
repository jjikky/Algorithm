import math
m,n = map(int,input().split())

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

for i in range(m,n+1):
    if(i==1):continue
    if isPrime(i):
        print(i)