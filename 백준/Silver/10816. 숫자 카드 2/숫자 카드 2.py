n = int(input())
n_arr = map(int,input().split())
m = int(input())
m_arr = map(int,input().split())

dict = {}

for i in n_arr:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
for i in m_arr:
    if i in dict.keys():
        print(dict[i],end=' ')
    else:
        print(0,end=' ')