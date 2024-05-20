n,k=map(int,input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp=[[0]*(k+1) for _ in range(n+1)]

# 물건 수
for i in range(1,n+1):
    # 버티는 무게
    for j in range(1,k+1):
        w=bag[i-1][0]
        v=bag[i-1][1]
        # 물건을 담을 수 있는 경우
        if j>=w:
            dp[i][j]=max(dp[i-1][j],v + dp[i-1][j-w])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][k])