n=int(input())
n_arr = list(map(int,input().split()))
m=int(input())
m_arr = list(map(int,input().split()))

dict={}

for i in n_arr:
    if i in dict.keys():
        pass
    else:
        dict[i]=1
for i in m_arr:
    if i in dict.keys():
        print(1)
    else:
        print(0)