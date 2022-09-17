n, k = input().split()
n = int(n)
k = float(k)

series_sum = 0.0

for i in range(1, n + 1):
    series_sum += i**k

print(round(series_sum, 3))
