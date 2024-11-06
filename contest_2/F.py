t = int(input().strip())
results = []
for i in range(t):

    n = int(input().strip())

    quality = -1
    win = -1 
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        if a <= 10:
            if b > quality:
                quality = b
                win = i
    if win == -1:
        results.append("NO")
    else:
        results.append(str(win))
print("\n".join(results))