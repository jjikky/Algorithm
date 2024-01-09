def convert(n):
    result=n
    while n>0:
        result+=n%10
        n//=10
    return result
    
n=int(input())
cnt=0

if(n<100):
    for i in range(1,n+1):
        if(convert(i)==n):
            cnt+=1
            print(i)
            break
else:
    start=int(n*0.9)
    for i in range(start,n+1):
        if(convert(i)==n):
            cnt+=1
            print(i)
            break

if(cnt==0):
    print(0)