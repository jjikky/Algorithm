from collections import deque

def dfs(v):
    q = deque([v])
    visited[v]=1
    while q:
        now = q.popleft()
        for i in range(1,n+1):
            if visited[i]==0 and graph[v][i]!=0:
                q.append(i)
                dfs(i)
        
n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=graph[b][a]=1

# print(graph)

visited=[0]*(n+1)

dfs(1)
print(sum(visited)-1)