import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    word=input().rstrip()
    arr.append(word)
arr=list(set(arr))
result = sorted(arr,key=lambda x: (len(x),x))

for i in result:
    print(i)