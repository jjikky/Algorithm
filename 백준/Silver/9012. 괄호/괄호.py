arr = [input() for _ in range(int(input()))]

def isVps(s):
    for _ in range(len(s)//2):
        if not s: break
        s=s.replace("()","")
    if s:
        return "NO"
    return "YES"

for s in arr:
    print(isVps(s))