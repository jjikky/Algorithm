import sys
input = sys.stdin.readline
n,c=map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])

l,r= 1,arr[-1]-arr[0]

while l<=r:
    mid= (l+r)//2
    cur = arr[0]
    cnt=1
    for i in range(1,n):
        if arr[i]-cur >=mid:
            cur=arr[i]
            cnt+=1
    
    if cnt >= c:
        l=mid+1
        answer=mid
    else: r = mid-1
print(answer)