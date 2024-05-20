import sys
input = sys.stdin.readline
n=int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)],key=lambda x:(x[1], x[0]))
cnt=1
k=0
for i in range(1,n):
    if time[i][0]>=time[k][1]:
        cnt+=1
        k=i
print(cnt)