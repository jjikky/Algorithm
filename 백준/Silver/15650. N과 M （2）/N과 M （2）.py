from itertools import combinations

n,m=map(int,input().split())
arr=[x+1 for x in range(n)]
arr = list(combinations(arr,m))
for i in arr:
    print(*i)
