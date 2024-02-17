n=int(input())
k=int(input())

start,end=1,k
#  어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지
while start<=end:
    mid = (start+end)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n) #mid 이하인 i의 배수 or N
    if cnt>=k:
        answer=mid
        end = mid-1
    else: start = mid+1

print(answer)
