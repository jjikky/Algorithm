from collections import deque
import sys
input = sys.stdin.readline

q=deque()

for _ in range(int(input())):
    sel=input().split()
    if sel[0]=='push_front':
        q.appendleft(sel[1])
    elif sel[0]=='push_back':
        q.append(sel[1])
    elif sel[0]=='pop_front':
        print(q.popleft() if q else -1)
    elif sel[0]=='pop_back':
        print(q.pop() if q else -1)
    elif sel[0]=='size':
        print(len(q))
    elif sel[0]=='empty':
        print(0 if q else 1)
    elif sel[0]=='front':
        print(q[0] if q else -1)
    elif sel[0]=='back':
        print(q[-1] if q else -1)
