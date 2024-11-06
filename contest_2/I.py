N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for i in range(N)]
dp = [0] * (W + 1)
for weight, value in items:
    for w in range(W, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[W])