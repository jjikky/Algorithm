while True:
    arr = sorted(list(map(int,input().split())))
    if sum(arr)==0: break
    print("right" if arr[-1]**2 == arr[0]**2+arr[1]**2 else "wrong" )