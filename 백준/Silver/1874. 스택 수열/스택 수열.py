import sys
n, *arr = map(int, sys.stdin.buffer.read().splitlines())

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
    print('\n'.join(result))
else:
    print("NO")