number = int(input())
value: bool
if number > 2:
    for item in range(2, number - 1):
        if number % item == 0:
            value = False
            break
        else:
            value = True

else:
    value = True
print(value)
