m,n=map(int,input().split())

answer=0
arr=[[0]*n for x in range(m)]
x,y=0,0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dirNum=0;

arr[x][y]=1
now=2

while now<=n*m:
    nx = x+dx[dirNum]
    ny = y+dy[dirNum]
    if nx>=m or ny>=n or nx<0 or ny<0 or arr[nx][ny]!=0:
        dirNum = (dirNum+1)%4
        answer+=1
    x = x+dx[dirNum]
    y = y+dy[dirNum]
    arr[x][y]=now
    now+=1
print(answer)