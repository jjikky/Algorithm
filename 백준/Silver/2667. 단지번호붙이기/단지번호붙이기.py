import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    global now
    # 단지수 +1
    answer[now]+=1
    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if not visited[nx][ny] and graph[nx][ny]=="1":
                dfs(nx,ny)

dx,dy=[0,1,-1,0],[1,0,0,-1]


n= int(input())
answer=[]
now=0

graph = [input() for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]=="1":
            answer.append(0)
            dfs(i,j)
            now+=1
print(len(answer))
answer.sort()
print('\n'.join(map(str,answer)))