def solution(numlist, n):
    arr=list(map(lambda x:(x,abs(x-n)),numlist))
    arr.sort(key=lambda x: (x[1],-x[0]))
    return [x[0] for x in arr]