from itertools import permutations

n,m = map(int,input().split())
data = [i+1 for i in range(n)]

result = list(permutations(data,m))
for i in result:
    for j in i:
        print(j, end=" ")
    print("")