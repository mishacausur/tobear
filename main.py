first, second = map(int, input().split())
a = first % 10 == 0 or second % 10 != 0
b = first % 10 != 0 or second % 10 == 0
print(a != b)
print('first', a)
print('second', b)
