arr=[]

for i in range(int(input())):
    arr.append([0]*4)
    m = int(input())
    while m>0:
        if(m>=25):
            arr[i][0]+=m//25
            m%=25
        elif(m>=10):
            arr[i][1]+=m//10
            m%=10
        elif m>=5:
            arr[i][2]+=m//5
            m%=5
        else:
            arr[i][3]+=m//1
            m=0
for i in arr:
    for j in i:
        print(j,end=" ")
    print("")