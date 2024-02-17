n=int(input())
arr = list(map(int,input().split()))
budget = int(input())

start = 0
end = max(arr)

while start<=end:
    total=0
    mid = (end+start)//2
    for i in arr:
        if i<=mid:
            total+=i
        else:
            total+=mid
    if total <= budget:
        start = mid+1
    else:
        end = mid-1
print(end)
            
