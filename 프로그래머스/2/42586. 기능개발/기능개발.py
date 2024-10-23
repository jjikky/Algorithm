import math
def solution(p, s):
    answer = []
    li = []
    for i in range(len(p)):
        li.append(math.ceil((100-p[i])/s[i]))
        
    target=0
    
    for i in range(len(li)):
        if li[target]<li[i]:
            answer.append(i-target)
            target=i
    answer.append(len(li)-target)
            
    return answer