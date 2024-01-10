n=int(input())
arr=[]
for x in range(int(n/5)+1):
    for y in range(int(n/3)+1):
        if(5*x+y*3 == n):
            arr.append(x+y)
if(len(arr)==0):
    print(-1)
else:
    print(min(arr))