n=int(input())
v = int(input())
# v의 좌표 저장할 변수
vx,vy=1,1

arr=[[0]*n for x in range(n)]
x,y=0,0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
dirNum=0;

arr[x][y]=n**2
now=n**2-1

while now>=1:
    nx = x+dx[dirNum]
    ny = y+dy[dirNum]
    if nx>=n or ny>=n or nx<0 or ny<0 or arr[nx][ny]!=0:
        dirNum = (dirNum+1)%4
    x = x+dx[dirNum]
    y = y+dy[dirNum]
    arr[x][y]=now
    # v 좌표 저장
    if now == v: 
        vx,vy=x+1,y+1
    now-=1
for i in arr:
    print(*i)
print(vx,vy)