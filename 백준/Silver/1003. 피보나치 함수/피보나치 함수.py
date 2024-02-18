import sys
input = sys.stdin.readline

arr=[(1,0),(0,1)]
for i in range(2,41):
    arr.append((arr[i-1][0]+arr[i-2][0],(arr[i-1][1]+arr[i-2][1])))

n,*nums = map(int,sys.stdin.buffer.read().splitlines())
for i in nums:
    print(arr[i][0],arr[i][1])