def cal(dot1,dot2):
    x=dot1[0]-dot2[0]
    y=dot1[1]-dot2[1]
    return y/x
def solution(dots):
    answer = 0
    if cal(dots[0],dots[1]) == cal(dots[2],dots[3]) or cal(dots[1],dots[2]) == cal(dots[0],dots[3]) or cal(dots[3],dots[1]) == cal(dots[2],dots[0]):
        answer=1
    
        
    
    return answer