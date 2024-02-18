import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    n, idx = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    que = deque([(i, li[i]) for i in range(len(li))])
    li.sort(reverse=True)
    cnt = 0
    for el in li:
        while que[0][1] != el:
            que.append(que.popleft())
        cnt += 1
        if que.popleft()[0] == idx:
            break
    print(cnt)