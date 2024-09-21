def solution(myString):
    answer = list(map(lambda x: len(x), myString.split("x")))
    return answer
