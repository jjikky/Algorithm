n=int(input())
cnt=0
while(n%5):
    n-=3
    cnt+=1
print(n//5+cnt if n>=0 else -1)
