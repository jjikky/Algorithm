from collections import Counter
import sys

input = sys.stdin.readline
user=[]
for _ in range(int(input())):
    user.append(input().split()[0])

cnt = Counter(sorted(user)[::-1])
for e,c in cnt.items():
    if c%2==1 : print(e)
