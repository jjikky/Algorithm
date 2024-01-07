def isPerfect(n):
    arr=[i for i in range(1,n+1) if n%i==0 and i!=n]
    if(sum(arr) == n):
        print(n,end=" = ")
        for i in range(len(arr)):
            if(i==len(arr)-1):
                print(arr[i])
            else :
                print(arr[i],end=" + ")
    else:
        print(n,"is NOT perfect.")
while True:
    n = int(input())
    if(n==-1) :
        break
    isPerfect(n)