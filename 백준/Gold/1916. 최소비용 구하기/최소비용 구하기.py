import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start,dest):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for vv,ww in graph[now]:
            cost = dist+ww
            if cost < distance[vv]:
                distance[vv]=cost
                heapq.heappush(q,(cost,vv))
    return distance[dest]
    
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))

start,dest=map(int,input().split())

print(dijkstra(start,dest)) 