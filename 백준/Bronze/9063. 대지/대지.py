x_max,y_max=-10000,-10000
x_min,y_min=10000,10000
for _ in range(int(input())):
    x,y = map(int,input().split())
    if x>x_max:
        x_max=x
    if x<x_min:
        x_min=x
    if y>y_max:
        y_max=y
    if y<y_min:
        y_min=y
print((x_max - x_min) * (y_max - y_min))