numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
if num in numbers:
    print(numbers[:num-1])
else:
    print(numbers)
