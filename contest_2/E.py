t = int(input().strip())
result = []
for i in range(t):
    a, b, c = map(int, input().split())

    if a + b >= 10 or a + c >= 10 or b + c >= 10:
        result.append("YES")
    else:
        result.append("NO")

print("\n".join(result))