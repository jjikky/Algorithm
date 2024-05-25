import sys
import heapq

# 입력
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)


def dijkstra():
    # 최소 비용 저장할 리스트
    distance=[float("inf")]*(n+1)
    distance[x]=0
    
    q=[]
    heapq.heappush(q,x)
    
    while q:
        now = heapq.heappop(q)
            
        for i in graph[now]:
            cost = distance[now]+1
            if cost < distance[i]:
                distance[i]=cost
                heapq.heappush(q,i)
    return distance

arr = dijkstra()

NOT_EXIST= True
for i in range(1,n+1):
    if arr[i]==k:
        print(i)
        NOT_EXIST=False
if NOT_EXIST : print(-1)
        