import sys

n = int(input())

arr=[]
max_x,max_y=0,0
# arr = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    li = list(map(int,input().split()))
    arr.append(li)
    if li[0]>max_x:max_x=li[0]
    if li[1]>max_y:max_y=li[1]
    
    
answer = [[0]*(max_x+10) for _ in range(max_y+10)]

# answer[25][17]

# arr = [[3, 7], [15, 7], [5, 2]]
for i in arr:
    [x,y]=i
    # i = [3,7]
    for j in range(x,x+10):
        for k in range(y,y+10):
            answer[k][j]=1

sum_answer=0
for i in answer:
    sum_answer+=sum(i)
            
        
print(sum_answer)