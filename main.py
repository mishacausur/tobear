number = 125
x, y, z = (int(number / 100), int((number % 100) / 10), number % 10)
print(x + y + z)
