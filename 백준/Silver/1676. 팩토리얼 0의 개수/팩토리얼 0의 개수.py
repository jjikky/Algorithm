n=int(input())

def factorial(n):
    if(n<=1):
        return 1
    else:
        return n*(factorial(n-1))
        
cnt=0
for i in str(factorial(n))[::-1]:
    if i=='0':
        cnt+=1
    else:break
print(cnt)