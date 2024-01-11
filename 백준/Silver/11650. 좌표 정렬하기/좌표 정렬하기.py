import sys
input = sys.stdin.readline
n = int(input())
arr=[[]]*n
for i in range(n):
    x,y = map(int, input().split())
    arr[i]=[x,y]
  
arr.sort(key=lambda x: (x[0], x[1]))  

for i in arr:
    print(i[0],i[1])
