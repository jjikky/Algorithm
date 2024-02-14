import sys

def print_score(arr):
    result = 0
    cnt=1
    for i in range(len(arr)):
        if arr[i]=="O":
            result += cnt
            cnt+=1
        else:
            cnt=1
    print(result)

input()
l = sys.stdin.read().splitlines()
for i in range(len(l)):
    print_score(l[i])
    
    