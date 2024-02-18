import sys
from collections import Counter
input = sys.stdin.readline
n=int(input())

# arr = sys.stdin.read().splitlines()

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

# r1 : avg
print(int(round(sum(arr)/n)))

# r2 : sort & 중앙에 위치한 값
print(arr[n//2])

# r3 : 최빈값
counter = Counter(arr)
counter_arr = counter.most_common()
maximum = counter_arr[0][1]
modes=[]
for num in counter_arr:
    if num[1] == maximum:
        modes.append(num[0])
if len(modes)==1:
    print(modes[0])
else:
    modes.sort()
    print(modes[1])
# r4 : 최대 - 최소
print(arr[-1]-arr[0])