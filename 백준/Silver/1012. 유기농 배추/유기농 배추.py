import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(x,y):
    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= nx < n) and (0 <= ny < m):
            if not visited[nx][ny] and graph[nx][ny]==1:   
                dfs(nx,ny)
    
dx,dy = [0,0,-1,1],[1,-1,0,0]

for _ in range(int(input())):
    answer=0
    m,n,k=map(int,input().split())
    graph = [[0]*(m) for _ in range(n)]
    visited=[[0]*(m) for _ in range(n)]
    
    # 행렬 생성
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
        
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]==1:
                dfs(i,j)
                answer +=1
    print(answer)
