import sys
input = sys.stdin.readline
cnt=0
def isMirror(line):
    s=''
    for w in line:
        if w=='(' or w==')':
            s+=w
        elif w=='[' or w==']':
            s+=w
   
    while '()' in s:
        s=s.replace('()','')
        while '[]' in s:
            s=s.replace('[]','')
    while '[]' in s:
        s=s.replace('[]','')
        while '()' in s:
            s=s.replace('()','')
    if s:
        print('no')
    else: print('yes')
    
while True:
    line=input().strip('\n')
    if line=='.':break
    else:isMirror(line)
