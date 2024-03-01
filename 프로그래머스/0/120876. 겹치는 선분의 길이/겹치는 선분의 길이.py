def solution(lines):
    arr = [0]*201
    for l in lines:
        for num in range(l[0],l[1]):
            arr[num+100]+=1
    answer = 0
    for i in range(len(arr)):
        if arr[i]>1:
            answer+=1
    return answer