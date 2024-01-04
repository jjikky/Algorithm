w=input().upper()
cnt= dict()
for i in range(len(w)):
    if w[i] in cnt.keys():
        cnt[w[i]]+=1
    else :
        cnt[w[i]]=1
max_v = max(cnt.values())
count =0
for i in cnt:
    if max_v==cnt[i]:
        count+=1
    if(count>1):
        print("?")
        break
        
if(count==1):
    for i in cnt:
        if max_v==cnt[i]:
            print(i)
            break