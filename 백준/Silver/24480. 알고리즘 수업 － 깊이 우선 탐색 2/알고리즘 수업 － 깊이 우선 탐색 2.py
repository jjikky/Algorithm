import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r):
    global now
    visited[r]=now
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if not visited[i]:
            now+=1
            dfs(i)
    

answer=0
n,m,r=map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
now = 1

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs(r)

for i in range(1,n+1):
    print(visited[i])