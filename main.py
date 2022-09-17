numbers = list(map(int, input().split()))
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

