cnt=0
for i in range(int(input())):
    s = input()
    result=dict()
    isGroup=1
    for i in range(len(s)):
        if s[i] in result.keys():
            if s[i-1]==s[i]:
                continue
            isGroup=0
        else:
            result[s[i]]=s[i]
    if isGroup: cnt+=1
print(cnt)