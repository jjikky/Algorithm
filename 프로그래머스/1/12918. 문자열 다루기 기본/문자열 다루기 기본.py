def solution(s):
    if len(s) == 4 or len(s) == 6 :
        for i in s :
            if not s.isdigit() :
                return False
        return True
    else :
        return False