import sys
input = sys.stdin.readline

arr=[]
for i in range(int(input())):
    arr.append(input().split())
    arr[i].append(i)

arr = sorted(arr,key=lambda x : (int(x[0]),int(x[2])))

for i in arr:
    print(i[0],i[1])