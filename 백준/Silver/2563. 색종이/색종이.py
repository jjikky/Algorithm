col,row=[],[]
cnt=0
for _ in range(int(input())):
    c,r = map(int,input().split())
    col.append(c)
    row.append(r)

arr = [[0]*(max(col)+10) for _ in range(max(row)+10)]

for n in range(len(col)):
    for i in range(row[n],row[n]+10):
        for j in range(col[n],col[n]+10):
            if arr[i][j] ==0:
                arr[i][j]=1
                cnt+=1
print(cnt)