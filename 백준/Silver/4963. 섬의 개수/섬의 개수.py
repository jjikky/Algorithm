import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    visited[x][y]=1
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<m) and (0<=ny<n):
            if not visited[nx][ny] and graph[nx][ny]:
                dfs(nx,ny)

dx,dy=[0,1,-1,0,1,1,-1,-1],[1,0,0,-1,1,-1,1,-1]


while True:
    answer=0
    n,m= map(int,input().split())
    # 종료
    if n+m==0: break
    graph = [list(map(int,input().split())) for _ in range(m)]
    visited = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and graph[i][j]:
                dfs(i,j)
                answer+=1
    print(answer)