l=int(input())
s = input()
result=0
m=1234567891
for i in range(l):
    num = ord(s[i])-96
    result += num*(31**i)
print(result%m)