import sys
input=sys.stdin.readline
n=int(input())
p=list(map(int,input().split()))
arr =[]
for i in range(n):
    arr.append([i+1,p[i]])

arr.sort(key=lambda x:x[1])
result=0
for i in range(n):
    result+=arr[i][1]*(n-i)
print(result)