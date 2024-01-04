arr = [list(map(int, input().split())) for _ in range(9)]

a_max=0
row,col=0,0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i][j]>=a_max):
            a_max=arr[i][j]
            row,col=i+1,j+1
print(a_max)
print(row,col)