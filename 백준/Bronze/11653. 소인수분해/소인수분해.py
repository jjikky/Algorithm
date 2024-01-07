n = int(input())

i=2
while(i<n):
    if(n%i==0):
        print(i)
        n/=i
        i-=1
    i+=1
if(n!=1):print(int(n))