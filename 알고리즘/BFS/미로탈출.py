from collections import deque

# BFS 구현
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 얘는 빼내고 
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향의 위치 확인
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx>=n or ny>=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                # 큐에 추가
                queue.append((nx,ny))
    return graph[n-1][m-1]

n,m=map(int,input().split())
graph = [list(map(int,list(input()))) for i in range(n)]

# 이동할 네 가지 방향 정의 (상,하,좌,우)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#BFS를 수행한 결과 출력
print(bfs(0,0))