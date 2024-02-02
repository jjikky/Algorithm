a,p=map(int,input().split())
arr=[a]

while 1:
    tmp=0
    for s in str(arr[-1]):
        tmp += int(s)**p
    if tmp in arr:
        break
    arr.append(tmp)
print(arr.index(tmp))
        