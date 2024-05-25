import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
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
    return distance
    
v,e = map(int,input().split())
graph=[[] for _ in range(v+1)]
# 최소 비용 저장할 리스트
distance=[INF]*(v+1)
start=int(input())

for _ in range(e):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))

answer = dijkstra(start) 

for i in range(1,v+1):
    if answer[i]==INF:print("INF")
    else : print(answer[i])