import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n,l,r = map(int,input().split())
day=0

population=[]

for i in range(n):
    population.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    
# 국경선 열지 결정
def dfs(x,y,arr):
    visited[x][y]=True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if in_range(nx,ny):
            if l<=abs(arr[nx][ny]-arr[x][y])<=r and (not visited[nx][ny]):
                border_share.append((nx,ny))
                dfs(nx,ny,arr)
    return border_share

while True:
    visited = [[False]*n for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(n):
            border_share=[(i,j)]
            if not visited[i][j]:
                border_share = dfs(i,j,population)
            if len(border_share)>1:
                flag = True
                sum_population=0
                for x,y in border_share:
                    sum_population+=population[x][y]
                avg = sum_population//len(border_share)
                for x,y in border_share:
                    population[x][y] = avg
    if flag:
        day +=1
    else: 
        print(day)
        break
# print(population)
            