# 2 1 1 0 인 경우
# 1인 사람 왼쪽에 2명
# 2인 사람 왼쪽에 1명
# 3인 사람 왼쪽에 1명
# 4인 사람 왼쪽에 0 명

# 해당 차례 때 자신보다 큰 수 개수 만큼 자리를 비워두고 배치
# 0 0 1 0
# 0 2 1 0
# 0 2 1 3
# 4 2 1 3

n = int(input())
arr = list(map(int,input().split()))

answer=[0]*n

for i in range(n):
    cnt=0
    for j in range(n):
        #  비워놓은 자리의 개수 == 요구사항 & 아직 안채워진 자리
        if cnt==arr[i] and answer[j]==0:
            answer[j]=i+1
            break
        # 비워놓은 자리의 개수 cnt에 추가가
        elif answer[j]==0:
            cnt+=1
print(*answer)

