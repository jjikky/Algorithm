from collections import deque

def dfs(v):
    visited_dfs[v]=1
    print(v,end=' ')
    
    for i in range(1, n + 1):
        #방문한적 없고 다른곳에 연결되어 있으면
        if not visited_dfs[i] and graph[v][i] == 1:
            dfs(i)
    
def bfs(v):
    queue = deque([v])
    visited_bfs[v]= 1
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in range(1, n + 1):
            #방문기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
            if not visited_bfs[i] and graph[v][i] == 1:
                queue.append(i)
                visited_bfs[i]=1
                
                
n,m,v=map(int,input().split())

# 그래프 생성
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

dfs(v)
print()
bfs(v)