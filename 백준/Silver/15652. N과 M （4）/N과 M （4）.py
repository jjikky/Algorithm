from itertools import combinations_with_replacement

n,m=map(int,input().split())
arr=[str(x+1) for x in range(n)]
arr = list(combinations_with_replacement(arr,m))
print('\n'.join(list(map(" ".join,arr))))
