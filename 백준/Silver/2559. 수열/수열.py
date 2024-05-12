n,k = map(int,input().split())
arr = list(map(int,input().split()))

part_sum = sum(arr[:k])
answer = part_sum

for i in range(n-k) :
  part_sum += arr[i+k] - arr[i]
  if answer < part_sum :
    answer = part_sum

print(answer)