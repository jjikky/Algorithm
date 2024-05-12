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
                move[i]=v

n,k = map(int,input().split())
MAX = 100000
visited = [0]*(100001)
move = [0]*(100001)

arr=[n]
print(bfs(n))

answer=[k]
target=k

while target!=n:
    answer.append(move[target])
    target=move[target]
print(*answer[::-1])

