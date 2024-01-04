sub_num=20
table={
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0,
}
sum=0
sum_num=0
for i in range(20):
    name,num,grade = input().split()
    if grade=="P" :
        sub_num-=1
        continue
    sum+=table[grade]*float(num)
    sum_num+=float(num)
print(sum/sum_num)