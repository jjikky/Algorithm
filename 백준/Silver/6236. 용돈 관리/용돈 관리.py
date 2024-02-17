import sys
n,m=map(int,input().split())
arr = [int(input()) for _ in range(n)]

start=min(arr)
end=sum(arr)

while start<=end:
    mid = (start+end)//2
    now,cnt=0,0
    for i in arr:
        if now<i:
            now=mid
            cnt+=1
        now-=i
        # 인출한 돈이 나갈 돈보다 적은 경우면 범위를 더높게 잡아야함
    if cnt>m or mid<max(arr):
        start = mid+1
    else:
        end = mid -1
        k=mid
print(k)