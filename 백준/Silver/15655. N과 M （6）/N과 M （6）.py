n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))

arr = []

def dfs(start):
    if(len(arr)==m):
        print(' '.join(map(str,arr)))
        return
    for i in range(start,len(nums)):
        if nums[i] not in arr:
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()
dfs(0)