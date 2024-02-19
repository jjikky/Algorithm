import sys
input=sys.stdin.readline
n,k=map(int,input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

cnt=0
target=k
arr=arr[::-1]
while target>0:
    len_arr = len(arr)
    if arr[0]==target:
        cnt+=1
        target=0
    elif arr[0]>target:
        arr.pop(0)
    else:
        cnt+=target//arr[0]
        target %= arr[0]
        
print(cnt)
        