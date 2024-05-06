import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y,height):
    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if not visited[nx][ny] and graph[nx][ny]>height:
                dfs(nx,ny,height)

dx,dy=[0,1,-1,0],[1,0,0,-1]
answer=0
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

start = min(map(min,graph))
end = max(map(max,graph))-1

answer=0
while start<=end:
    cnt=0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j]>start:
                dfs(i,j,start)
                cnt+=1
    if answer<cnt:
        answer=cnt
    start+=1

print(answer if answer!=0 else 1)