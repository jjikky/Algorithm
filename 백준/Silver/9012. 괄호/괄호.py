import sys
n=int(input())
l = sys.stdin.read().splitlines()
def isVps(l):
    while "()" in l :
        l=l.replace('()','')
    print("NO" if l else "YES")

for i in l:
    isVps(i)