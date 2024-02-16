import sys
input = sys.stdin.readline
n=int(input())
nums=sorted([int(input()) for x in range(n)])

if n==0:print(0)
else:
    v = int(n*(0.15)+0.5)
    print(int(sum(nums[v:n-v])/(n-2*v)+0.5))