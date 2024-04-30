# n*m 격자에서 인접하지 않게 k개 선택: 최댓값
import sys
input = sys.stdin.readline

def dfs(start,level,sum_k):
    global answer
    # k개 선택하면 종료
    if level==k:
        answer=max(answer,sum_k)
        return
    
    for i in range(start,n*m):
        x=i%n
        y=i//n
        # 방문한 곳 제외
        if visited[x][y]: continue
    
        #선택한 곳중 인접한곳 있는지 체크
        isNext=0
        for now in range(4):
            nx,ny=dx[now]+x,dy[now]+y
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                isNext=1
        # 선택한 곳중 인접한 곳 없으면 방문 처리
        if not isNext:
            visited[x][y]=1
            dfs(i+1, level + 1, sum_k + arr[x][y])
            visited[x][y]=0
                        
n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
# 나올 수 있는 최솟값 -1
answer=-40001
dx,dy=[0,1,0,-1],[1,0,-1,0]
dfs(0,0,0)
print(answer)