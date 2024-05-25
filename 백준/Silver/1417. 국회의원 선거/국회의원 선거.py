import sys
import heapq

input = sys.stdin.readline
n=int(input())
target=-int(input())

heap = []
answer=0

for _ in range(n-1):
    num = int(input())
    heapq.heappush(heap,-num)

while heap:
    max_v = heapq.heappop(heap)
    if max_v<=target:
        heapq.heappush(heap,max_v+1)
        target-=1
        answer+=1
    else:
        break
print(answer)

