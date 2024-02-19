import sys
input=sys.stdin.readline
n,m= map(int,input().split())

memo={}
for _ in range(n):
    site,pwd=input().rstrip().split()
    memo[site]=pwd
req=[input().rstrip() for _ in range(m)]

for i in range(m):
    print(memo[req[i]])
    
