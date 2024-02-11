n,m = map(int,input().split())
n_set = set([input() for i in range(n)])
m_set = set([input() for i in range(m)])
result = n_set.intersection(m_set)
print(len(result))
for i in sorted(result):
    print(i)