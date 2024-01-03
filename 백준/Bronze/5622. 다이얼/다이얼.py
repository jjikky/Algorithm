word=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
t=0
s = input()
for i in s:
    for j in range(len(word)):
        if i in word[j]:
            t+=word.index(word[j])+3
print(t)