x, y = map(int, input().split())
w = int(x/100) + (x%10) + (x%100//10)
i = int(y/100) + (y%10) + (y%100//10)

print(w == i)

