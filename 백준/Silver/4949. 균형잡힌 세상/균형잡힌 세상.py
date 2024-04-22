import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break
    stack = []
    dict = {')' : '(', ']' : '['}

    result = "yes"
    for c in line:
        # 열린 괄호
        if c in '([':
            # 스택에 추가
            stack.append(c)
        # 닫힌 괄호
        if c in ')]':
            if stack:
                # TOP과 매칭 x
                if (dict[c] != stack.pop()):
                    result = "no"
                    break
            # 스택에 열린 괄호 x
            else:
                result = "no"
                break
    print("no" if stack else result)
