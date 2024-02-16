import sys

input = sys.stdin.readline

def answer(k,n):
    arr=[]
    for i in range(k):
        if not arr:
            arr.append([x for x in range(1,n+1)])
        else:
            ne = []
            for j in range(n):
                ne.append(sum(arr[i-1][:j+1]))
            arr.append(ne)
    print(sum(arr[-1]))
for i in range(int(input())):
    k=int(input())
    n=int(input())
    answer(k,n)