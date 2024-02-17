import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr = [int(input()) for _ in range(n)]

start=1
end=sum(arr)//m

while start<=end:
    mid = (start+end)//2
    cnt=0
    for i in arr:
        cnt +=i//mid
    if cnt >= m:
        start = mid+1
    else :
        end = mid-1
print(end)  
