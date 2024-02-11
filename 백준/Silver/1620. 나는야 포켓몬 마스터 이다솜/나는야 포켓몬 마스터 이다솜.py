import sys

input = sys.stdin.readline
n,m = map(int,input().split())

dict={}

for i in range(1,n+1):
    a = input().strip()
    dict[str(i)]=a
    dict[a]=i
for i in range(m):
    q = input().strip()
    print(dict[q])