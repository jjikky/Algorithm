from itertools import product

n,m=map(int,input().split())
arr=[x+1 for x in range(n)]
arr = list(product(arr,repeat=m))
for i in arr:
    print(*i)
