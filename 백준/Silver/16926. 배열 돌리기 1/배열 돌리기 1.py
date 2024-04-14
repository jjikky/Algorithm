# 2차원 배열이 주어졌을 때, 이를 반시계 방향으로 R번 회전시킨 결과를 출력

import sys
from collections import deque

input = sys.stdin.readline
n,m,r= map(int,input().split())
answer = [[0]*m for _ in range(n)]
arr=[]
deq=deque()

# 입력 
for _ in range(n):
    arr.append(list(map(int,input().split())))


loops = min(n,m)//2
for i in range(loops):
    # 2차원 배열을 1차원으로 변형
    deq.clear()
    deq.extend(arr[i][i:m-i])	# 위쪽
    deq.extend([row[m-i-1] for row in arr[i+1:n-i-1]]) 	# 오른쪽
    deq.extend(arr[n-i-1][i:m-i][::-1]) 		# 아래쪽
    deq.extend([row[i] for row in arr[i+1:n-i-1]][::-1]) 	# 왼쪽
    
    # 회전
    deq.rotate(-r)
    
    
    for j in range(i, m-i):    # 위쪽
            answer[i][j] = deq.popleft()
    for j in range(i+1, n-i-1):  # 오른쪽
        answer[j][m-i-1] = deq.popleft()
    for j in range(m-i-1, i-1, -1): # 아래쪽
        answer[n-i-1][j] = deq.popleft()  
    for j in range(n-i-2, i, -1):  # 왼쪽
        answer[j][i] = deq.popleft()    

for line in answer:
    print(*line)