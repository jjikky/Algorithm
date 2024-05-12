from collections import deque

def bfs(n):
    q=deque()
    q.append(n)
    
    while q:
        v=q.popleft()
        if v==k:
            return visited[k]
        for i in [v+1,v-1,v*2]:
            if 0<=i<=MAX and not visited[i]:
                visited[i]=visited[v]+1
                q.append(i)

n,k = map(int,input().split())
MAX = 10**5
visited = [0]*(MAX+1)
print(bfs(n))
