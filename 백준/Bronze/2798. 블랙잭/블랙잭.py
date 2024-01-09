from itertools import combinations
_,m=map(int,input().split())
arr = list(map(int,input().split()))
max_v = 0
result = list(combinations(arr,3))
for i in result:
    sum_v = sum(i)
    if sum_v>max_v and sum_v<=m:
        max_v = sum_v
print(max_v)
    