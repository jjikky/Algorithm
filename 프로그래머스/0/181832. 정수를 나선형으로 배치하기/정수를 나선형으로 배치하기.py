def solution(n):
    answer = [[0]*n for _ in range(n)]
    # 우 하 좌 상
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    x,y=0,0
    answer[x][y]=1
    now = 2
    while now<=n**2:
        for i in range(4):
            while True:
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=n or ny>=n or nx<0 or ny<0 or answer[nx][ny]!=0:
                    break
                else:
                    answer[nx][ny]=now
                    x=nx
                    y=ny
                    now+=1

    return answer