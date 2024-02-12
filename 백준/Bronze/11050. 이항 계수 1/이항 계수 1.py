from itertools import combinations
n,k = map(int,input().split())
arr = [0]*n
print(len(list(combinations(arr,k))))