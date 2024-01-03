n,m = map(int,input().split())
arr = [i+1 for i in range(n)]
for i in range(m):
    basket1,basket2 = map(int,input().split())
    arr[basket1-1],arr[basket2-1]=arr[basket2-1],arr[basket1-1]
print(*arr)