import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(input()))
stack=[]
arr2=[]
result=[]
cur=1
for i in range(n):
    while cur<=arr[i]:
        stack.append(cur)
        result.append("+")
        cur+=1
    if stack[-1]==arr[i]:
        arr2.append(stack.pop())
        result.append("-")

if arr==arr2:
    for i in result:
        print(i)
else:
    print("NO")