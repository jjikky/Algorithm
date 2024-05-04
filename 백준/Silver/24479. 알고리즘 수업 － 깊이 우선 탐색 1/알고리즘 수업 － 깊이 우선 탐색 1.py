import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v):
		# 방문 순서
    global now
    now +=1
    visited[v]=now
    
    # 인접 정점 오름차순 정렬
    graph[v].sort()

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
now=0
visited = [0]*(n+1)
dfs(r)

for i in range(1, n+1):
    print(visited[i])