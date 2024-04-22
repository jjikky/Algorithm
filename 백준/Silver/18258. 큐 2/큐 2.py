import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

commands = {
    'push': lambda x: q.append(x),
    'pop': lambda: print(q.popleft() if q else -1),
    'size': lambda: print(len(q)),
    'empty': lambda: print(0 if q else 1),
    'front': lambda: print(q[0] if q else -1),
    'back': lambda: print(q[-1] if q else -1)
}

for _ in range(int(input())):
    cmd, *args = input().split()
    if args:
        commands[cmd](args[0])
    else:
        commands[cmd]()