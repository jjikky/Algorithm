import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque([[x,y]])
    visited=[[0]*m for _ in range(n)]
    isShark=0
    while queue:
        x,y=queue.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
                if graph[nx][ny]==0:
                    queue.append([nx,ny])
                    visited[nx][ny]=visited[x][y]+1
                else:
                    answer=visited[x][y]+1
                    isShark=1
        if isShark:
            break
    return answer
    
n,m=map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

answer=0
for x in range(n):
    for y in range(m):
        if graph[x][y]!=1:
            if answer<bfs(x,y):
                answer = bfs(x,y)
print(answer)