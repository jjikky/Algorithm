import sys
input = sys.stdin.readline
queue=[]
for _ in range(int(input())):
    sel = list(input().split())
    queue_len=len(queue)
    if sel[0]=='push':
        queue.append(int(sel[1]))
    if sel[0]=='pop':
        if queue_len>0:
            print(queue[0])
            queue.remove(queue[0])
        else:
            print(-1)
    if sel[0]=='size':
        print(queue_len)
    if sel[0]=='empty':
        print(1 if queue_len==0 else 0)
    if sel[0]=='front':
        print(queue[0] if queue_len>0 else -1)
    if sel[0]=='back':
        print(queue[-1] if queue_len>0 else -1)