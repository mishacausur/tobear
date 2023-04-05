from matplotlib import pyplot as plt
from math import factorial

# 1
n = 5 # количество попыток
p = 0.5 # вероятность успеха

distr = []

# Если вероятность успеха равна вероятности неудачи (то есть обе равны  50%),
# распределение будет симметричным. Проверим это на графике.
# Допустим, эксперимент повторили 5 раз, то есть n=5,
# и вероятность успеха равна 50% на каждом повторении, то есть p=0.5.

for k in range(0, n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * p**k * (1 - p)**(n - k)
    distr.append(prob)

plt.bar(range(0, n + 1), distr)
plt.show()

# 2
n = 25 # количество попыток
p = 0.5 # вероятность успеха

distr = []

for k in range(0, n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * p**k * (1 - p)**(n - k)
    distr.append(prob)

plt.bar(range(0, n + 1), distr)

# Если вероятность успеха не равна 50%, а n при этом не слишком велико,
# распределение получается скошенным: вправо,
# если вероятность успеха маленькая; влево — если большая.
# Построим график для n=30 и p=0.07:

#3
n = 30 # количество попыток
p = 0.07 # вероятность успеха

distr = []

for k in range(0, n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * p**k * (1 - p)**(n - k)
    distr.append(prob)

plt.bar(range(0, n + 1), distr)

# График показывает, что при вероятности успеха 7%,
# и 30 попытках вероятность, что случится больше 8 успехов, крайне мала.
# График для n=26 и p=0.9 выглядит так:

#4
n = 26 # количество попыток
p = 0.9 # вероятность успеха

distr = []

for k in range(0, n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * p**k * (1 - p)**(n - k)
    distr.append(prob)

plt.bar(range(0, n + 1), distr)
