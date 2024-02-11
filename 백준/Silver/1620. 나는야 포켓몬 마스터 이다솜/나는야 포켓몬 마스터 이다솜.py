import sys

input = sys.stdin.readline
n,m = map(int,input().split())

arr = [input().strip('\n') for x in range(n)]
for i in range(m):
    q = input().strip("\n")
    if q.isdigit():
        print(arr[int(q)-1])
    else:
        print(arr.index(q)+1)