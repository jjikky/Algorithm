h,m=input().split()
t = int(input())
h=int(h)
m=int(m)
m+=t
while m>=60:
    h+=1
    m-=60  
while h>=24:
    h-=24
    
print(h,m)