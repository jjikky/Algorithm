# n개의 원판을 start에서 end로 이동
def hanoi(n,start,end):
    if n==1:
        print(start,end)
        return
    
    # 1단계 : n-1 개의 원판을 start에서 end와 start가 아닌 막대로 이동
    hanoi(n-1,start,6-start-end)
    
    # 2단계 : start에서 end 막대로 이동
    print(start,end)
    
    # 3단계 : 나머지 막대에 있던 n-1개의 원판을 end막대로 이동
    hanoi(n-1,6-start-end,end)
    
n = int(input())
print(2**n-1)
if(n<=20):
    hanoi(n,1,3)