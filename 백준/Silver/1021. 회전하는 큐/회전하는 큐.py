from collections import deque
import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())
nums = deque(map(int,input().split()))

arr=deque(x for x in range(1,n+1))

answer=0

# nums의 첫번쨰 원소와 arr의 첫번쨰 원소가 같으면 바로 뽑기 가능
# 다르면 2번 or 3번의 연산을 수행해야함

while nums:
    if nums[0]==arr[0]:
        nums.popleft()
        arr.popleft()
    else:
        # 현재 빼야할 원소의 위치
        r = arr.index(nums[0])
        # 현재 빼야할 원소의 위치가 arr의 중앙 인덱스보다 작으면 왼쪽 회전
        if r < len(arr)/2:
            # 회전
            arr.rotate(-r)
            answer += r
        # 빼야할 원소가 중앙에 위치한 원소보다 안작으면 오른쪽 회전
        else:
            arr.rotate(len(arr)-r)
            answer+=len(arr)-r
print(answer)