arr=list(map(int,input().split()))
print(sum(list(map(lambda n:n**2,arr)))%10)