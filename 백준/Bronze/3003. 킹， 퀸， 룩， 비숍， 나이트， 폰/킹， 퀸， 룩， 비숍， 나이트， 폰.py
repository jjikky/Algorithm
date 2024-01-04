arr = [1,1,2,2,2,8]
input_arr = list(map(int,input().split()))
for i in range(len(arr)):
    print(arr[i]-input_arr[i],end=" ")