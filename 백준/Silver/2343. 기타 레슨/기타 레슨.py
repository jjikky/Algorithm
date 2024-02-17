import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr = list(map(int,input().split()))
l,r=max(arr),sum(arr)

while l<=r:
    mid = (l+r)//2
    total,cnt =0,1
    for i in arr:
        if total+i>mid:
            total=i
            cnt+=1
        else:
            total+=i
    if cnt>m:
        l=mid+1
    else:
        ans=mid
        r=mid-1
    
print(ans)