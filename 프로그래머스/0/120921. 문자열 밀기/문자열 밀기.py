from collections import deque

def solution(A, B):
    answer = 0
    if A==B : return answer
    len_A = len(A)
    for i in range(len_A):  
        A = A[-1]+A[0:len_A-1]
        print(A,B, A==B)
        answer+=1
        if A==B : return answer
    return -1