def solution(common):
    answer=0
    # 등차
    if common[1]-common[0]==common[2]-common[1]:
        answer=common[1]-common[0]+common[-1]
    # 등비
    else:
        answer = common[-1]*(common[1]//common[0])
        
        
    return answer