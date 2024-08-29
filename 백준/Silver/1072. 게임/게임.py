# 풀이 참고함
# 이진 탐색
import sys
input = sys.stdin.readline
x,y=map(int,input().split())

left,right=0,x
z = y*100//x
ans=x

if z>=99:
    print(-1)
else:
    while left<=right:
        mid = (left+right)//2
        if (y+mid)*100//(x+mid)>z:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    print(ans)