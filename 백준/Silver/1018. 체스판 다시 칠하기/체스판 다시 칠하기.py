row,col=map(int,input().split())
arr=[]
for i in range(row):
    arr.append(input())

min_v=32
for i in range(row-7):
    for j in range(col-7):
        start_b=0
        start_w=0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if(x+y)%2==0:
                    if(arr[y][x]=="B"):
                        start_w+=1
                    else:
                        start_b+=1
                else:
                    if(arr[y][x]=="B"):
                        start_b+=1
                    else:
                        start_w+=1
        if( min_v>min(start_w,start_b)):
            min_v =  min(start_w,start_b)
print(min_v)