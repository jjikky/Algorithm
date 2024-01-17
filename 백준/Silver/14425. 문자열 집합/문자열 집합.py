import sys
input = sys.stdin.readline

n,m=map(int,input().split())

s = [input() for i in range(n)]
print(sum([1 for i in range(m) if input() in s]))