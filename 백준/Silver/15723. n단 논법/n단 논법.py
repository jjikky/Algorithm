import sys
input = sys.stdin.readline

n=int(input())

alpha=26

INF = int(1e9)

graph = [[INF]*(alpha+1) for _ in range(alpha+1)]

for a in range(1,alpha+1):
    for b in range(1,alpha+1):
        if a==b:
            graph[a][b]=0

# 그래프 입력
for _ in range(n):
    s = input().split()
    a,b=ord(s[0])-96,ord(s[2])-96
    graph[a][b]=1
    
for k in range(1,alpha+1):
    for a in range(1,alpha+1):
        for b in range(1,alpha+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 질문 입력
m = int(input())
for _ in range(m):
    s = input().split()
    a,b=ord(s[0])-96,ord(s[2])-96
    if graph[a][b]==INF:
        print("F")
    else: print("T")