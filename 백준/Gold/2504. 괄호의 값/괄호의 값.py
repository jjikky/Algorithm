s = input()
stack=[]
answer=0
temp=1

for i in range(len(s)):
    now=s[i]
    # 열린거 : 스택에 넣기
    if now=="(" : 
        temp*=2
        stack.append(now)
    elif now=="[":
        temp*=3
        stack.append(now)
    # 닫힌거
    elif now==")":
        # stack 비어있거나 탑이 현재 문자와 다르면
        if not stack or stack[-1]=='[':
            answer=0
            break
        if s[i-1]=='(':
            answer += temp
        temp//=2
        stack.pop()
    elif now=="]":
        if not stack or stack[-1]=='(':
            answer=0
            break
        if s[i-1]=='[':
            answer += temp
        temp//=3
        stack.pop()
           
print(0 if stack else answer)