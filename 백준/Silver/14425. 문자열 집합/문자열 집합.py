import sys
input = sys.stdin.readline

n,m=map(int,input().split())
a = sys.stdin.read().split('\n')
s = set(a[:n])
print(sum([i in s for i in a[n:]]))