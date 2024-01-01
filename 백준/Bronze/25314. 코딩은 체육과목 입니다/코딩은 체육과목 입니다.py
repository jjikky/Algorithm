n = int(input())
cnt = n//4
if n%4!=0:
    cnt+=1
for i in range(cnt):
    print("long ",end="")
print("int")