input()
arr1 = list(map(int,input().split()))
n=int(input())
arr2=list(map(int,input().split()))
result = [0]*n

t=dict()
for i in arr1:
    t[i]=1

for i in arr2:
    try:
        if t[i] ==1:
            print(1, end=" ")
    except:
        print(0, end=" ")

