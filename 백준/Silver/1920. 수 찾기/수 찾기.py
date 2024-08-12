import sys

input = sys.stdin.readline

n=int(input())
num_dict = {}
n_arr = set(map(int,input().split()))

for num in n_arr:
    num_dict[num]=True
m=int(input())
m_arr = map(int,input().split())

for target in m_arr:
    if num_dict.get(target)==None:
        print(0)
    else: print(1)