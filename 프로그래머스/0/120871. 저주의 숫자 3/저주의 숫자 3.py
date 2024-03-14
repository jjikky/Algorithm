def solution(n):
    arr=[0]*101
    now=1
    for i in range(1,101):
        while now%3== 0 or '3' in str(now):
            now+=1
        arr[i]=now
        now+=1
    return arr[n]