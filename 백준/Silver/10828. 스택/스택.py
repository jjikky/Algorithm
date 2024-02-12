import sys
input = sys.stdin.readline

arr=[]
for _ in range(int(input())):
    sel=input().split()
    if sel[0]=='push':
        arr.append(sel[1])
    elif sel[0]=='pop':
        if arr:
            q=arr.pop()
            print(q)
        else: print(-1)
    elif sel[0]=='size':
        print(len(arr))
    elif sel[0]=='empty':
        print(0 if arr else 1)
    elif sel[0]=='top':
        if arr:
            print(arr[-1])
        else: print(-1)