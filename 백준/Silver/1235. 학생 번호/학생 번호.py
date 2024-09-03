import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(int(input()))]
origin_len = len(arr)


for di in range(len(arr[0])):
    temp=arr[:]
    for i in range(origin_len):
        temp[i]=temp[i][-1-di:]
    if len(set(temp))==origin_len:
        print(di+1)
        break

