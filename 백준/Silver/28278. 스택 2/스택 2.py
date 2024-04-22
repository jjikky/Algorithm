import sys
input = sys.stdin.readline

stack = []

commands = {
    '1': lambda x: stack.append(x),
    '2': lambda: print(stack.pop() if stack else -1),
    '3': lambda: print(len(stack)),
    '4': lambda: print(0 if stack else 1),
    '5': lambda: print(stack[-1] if stack else -1)
}

for _ in range(int(input())):
    cmd, *args = input().split()
    if args:
        commands[cmd](args[0])
    else:
        commands[cmd]()
