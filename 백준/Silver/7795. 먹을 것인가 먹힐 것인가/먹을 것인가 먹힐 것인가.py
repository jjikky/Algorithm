import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer=0
    
    a,b=map(int,input().split())
    
    arr1 = sorted(list(map(int,input().split())))
    arr2 = sorted(list(map(int,input().split())))[::-1]
    
    for i in range(len(arr1)):
        for _ in range(len(arr2)):
            if arr1[i]>arr2[-1]:
                answer += len(arr1)-i
                arr2.pop()
            else:
                break
    print(answer)