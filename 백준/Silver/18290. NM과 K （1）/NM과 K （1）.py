# n*m 격자에서 인접하지 않게 k개 선택: 최댓값
import sys
input = sys.stdin.readline

def dfs(x,y,level,sum_k):
    global answer
    # k개 선택하면 종료
    if level==k:
        answer=max(answer,sum_k)
        return
    else:
        for i in range(x, n):
            for j in range(y if i == x else 0, m):
                if [i, j] not in visited:
                    #선택한 것중 인접한것 있는지 체크
                    isNext=0
                    for now in range(4):
                        nx,ny=dx[now]+i,dy[now]+j
                        if [nx,ny] in visited:
                            isNext=1
                    if not isNext:
                        visited.append([i, j])
                        dfs(i, j, level + 1, sum_k + arr[i][j])
                        visited.pop()

n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited=[]
# 나올 수 있는 최솟값 -1
answer=-40001
dx,dy=[0,0,-1,1],[-1,1,0,0]
dfs(0,0,0,0)
print(answer)