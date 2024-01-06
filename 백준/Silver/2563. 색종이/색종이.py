arr=[0]*10000
for _ in range(int(input())):
    c,r = map(int,input().split())
    for i in range(c,c+10):
        for j in range(r,r+10):
            arr[i*100+j]=1
print(sum(arr))