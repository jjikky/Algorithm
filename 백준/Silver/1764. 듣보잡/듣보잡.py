from sys import stdin
N,M=map(int,stdin.readline().split())
l=stdin.read().splitlines()
s1=set(l[:N])
s2=set(l[N:])
r=sorted(list(s1&s2))
print(len(r),*r)