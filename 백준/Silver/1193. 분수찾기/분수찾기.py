num=int(input())
lev=1

while num>lev:
    num-=lev
    lev+=1
if lev%2==0:
    a = num
    b =lev-num+1
else:
    b = num
    a =lev-num+1
    
print(f'{a}/{b}')