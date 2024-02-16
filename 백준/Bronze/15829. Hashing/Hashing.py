l=int(input())
s = input()
result=0
for i in range(l):
    num = ord(s[i])-96
    result += num*(31**i)
print(result)