n = int(input().strip())
arr = list(map(int, input().strip().split()))
max_len = 1
len = 1
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        len += 1
    else:
        len = 1
    max_len = max(max_len, len)
print(max_len)
