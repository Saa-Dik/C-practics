n = int(input())
c= 0
for i in range(n):  
    p, v, t= map(int, input().split())
    if p+ v+ t>= 2:
        c+= 1
print(c)
