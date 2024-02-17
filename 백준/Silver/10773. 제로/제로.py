import sys
input = sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    num = int(input())
    if num==0 and arr:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))