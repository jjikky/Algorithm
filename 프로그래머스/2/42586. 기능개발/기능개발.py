def solution(p, s):
    answer = []
    day = 0
    cnt = 0
    while len(p)> 0:
        if p[0]+day*s[0]>=100:
            s.pop(0)
            p.pop(0)
            cnt+=1
        else:
            day+=1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
                
    answer.append(cnt)
    return answer