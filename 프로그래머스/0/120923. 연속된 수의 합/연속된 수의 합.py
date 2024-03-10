def solution(num, total):
    # answer = []
    target = total//num
    if num%2==1:
        start = target-num//2
    else :
        start = target-num//2+1    
    answer=[x for x in range(start,start+num)]
    return answer