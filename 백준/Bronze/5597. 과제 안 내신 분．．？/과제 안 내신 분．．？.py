student_list=[i+1 for i in range(30)]
arr=[]
for i in range(28):
    arr.append(int(input()))
answer = list(set(student_list)-set(arr))
answer.sort()
for i in answer:
    print(i)
