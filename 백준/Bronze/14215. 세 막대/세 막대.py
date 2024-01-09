arr= list(map(int, input().split()))
while max(arr) >= sum(arr)/2:
    arr[arr.index(max(arr))] -=1

print(sum(arr))