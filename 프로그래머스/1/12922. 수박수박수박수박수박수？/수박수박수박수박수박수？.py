def solution(n):
    answer = ["박" if x%2==1 else "수" for x in range(n)]
    return ('').join(answer)