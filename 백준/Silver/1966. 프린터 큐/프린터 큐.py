from collections import deque
from sys import stdin
input = stdin.readline

t=int(input())
for i in range(t):
    n,index = map(int,input().split())
    imp = deque(map(int,input().split()))
    cnt=1
    target = imp[index]
    target_index=index
    
    while True:
        max_v = max(imp)
        if max_v == target and target_index==0: 
            print(cnt)
            break
        if imp[0]==max_v:
            if 0==target_index:
                target_index+=len(imp)-2
            else: target_index-=1
            imp.popleft()
            cnt+=1
        else:
            if 0==target_index:
                target_index+=len(imp)-1
            else: target_index-=1
            imp.append(imp.popleft())
