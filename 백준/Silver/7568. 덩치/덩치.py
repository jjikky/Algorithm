import sys
input = sys.stdin.readline
n=int(input())
arr = [list(map(int,input().split())) for x in range(n)]
ranking=[]
for i in range(n):
    rank=1
    arr[0],arr[i]=arr[i],arr[0]
    for j in range(1,n):
        if arr[0][0]<arr[j][0] and arr[0][1]<arr[j][1]:
            rank+=1
    ranking.append(rank)
print(*ranking)