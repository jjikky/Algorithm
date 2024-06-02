import sys
input = sys.stdin.readline

n,m=map(int,input().split())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
answer=0
min_v=INF
for row in range(1,n+1):
    if sum(graph[row][1:n+1])<min_v:
        min_v = sum(graph[row][1:n+1])
        answer=row
print(answer)