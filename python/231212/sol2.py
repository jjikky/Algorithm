# 1번
# def stock():
#     netprofit = 0  
#     a = int(input("투자 액수를 입력하세요 : "))
#     b = int(input("투자한 날짜 수를 입력하세요 : "))
#     result=a
#     if(100<=a<=10000) and (1<=b<=10):
#         for i in range(1,b+1):
#             print(i)
#             nums=int(input("%d일차 변동 데이터를 입력하세요: " %i))
#             netprofit = a*nums/100
#             result+=netprofit
#         if result>a:
#             print('이득입니다.')
#         elif result==a:
#             print('본전입니다.')
#         else:
#             print('손해입니다.')
#     else:
#         print('범위에 맞는 숫자를 입력해주세요.') 
# stock()

# 2번
# def maxFunc(A):
#     max=0
#     for i in A:
#         if i>max:
#             max=i
#     return max

# A = [1,2,3,4,5,6,73,8,10,54]
# maxNum = maxFunc(A)
# print(maxNum)

# 3번
# def my_func():
#     sum=0
#     for i in range(5):
#         num=int(input())
#         sum+=num
#     return sum
# total = my_func()
# print(total)


# 4번
# answer = input()
# answer=answer.split(' ')
# total =0
# current =1
# for i in range(len(answer)):
#     if answer[i]=='O':
#         total+=current
#         current+=1
#     elif answer[i]=='X':
#         current=1
# print(total)
