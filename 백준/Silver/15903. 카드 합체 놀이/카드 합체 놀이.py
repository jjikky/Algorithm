import sys
from queue import PriorityQueue

input = sys.stdin.readline
n,m=map(int,input().split())

q = PriorityQueue(maxsize=n)

arr=list(map(int,input().split()))

for i in arr:
    q.put(i)

for i in range(m):
    a=q.get()
    b=q.get()
    q.put(a+b)
    q.put(a+b)

answer = 0
while not q.empty():
    answer += q.get()

print(answer)