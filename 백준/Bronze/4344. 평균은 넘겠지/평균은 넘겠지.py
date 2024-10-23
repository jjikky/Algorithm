import sys

def is_over(n):
    return n>avg_row
        
arr=[list(map(int,input().split())) for x in range(int(input()))]

for row in arr:
    avg_row = (sum(row[1:]))/row[0]
    over_list = list(filter(is_over,row[1:]))
    print(f"{round((len(over_list))/row[0]*100,3)}{'%'}")

