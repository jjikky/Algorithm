import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    
    while q:
        dist,now = heapq.heappop(q)
            
        for vv,ww in graph[now]:
            cost = dist+ww
            if cost < distance[vv]:
                distance[vv]=cost
                heapq.heappush(q,(cost,vv))
    return distance
    
n,d = map(int,input().split())
graph=[[] for _ in range(d+1)]
# 최소 비용 저장할 리스트
distance=[float("inf")]*(d+1)

# 거리 1로 초기화
for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    a,b,w=map(int,input().split())
    # 지름길 끝나는게 도착지점보다 멀면 무시시
    if b>d: continue
    graph[a].append((b,w))

arr = dijkstra(0)
print(arr[d])