import sys
input = sys.stdin.readline

result = "Invalid Equilateral Isosceles Scalene".split(" ")
while(True):
    arr= list(map(int, input().split()))
    if sum(arr)==0: break
    if max(arr) >= sum(arr)/2: 
        print(result[0])
    else:
        arr = set(arr)
        print(result[len(arr)])
    