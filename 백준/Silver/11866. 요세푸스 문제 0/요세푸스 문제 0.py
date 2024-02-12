n,k = map(int,input().split())
from collections import deque
q = deque([x for x in range(1,n+1)])

res=[]
# 1 2 3 4 5 6 7
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    res.append(str(q.popleft()))
print('<'+', '.join(res)+'>')
    