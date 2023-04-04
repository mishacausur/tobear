import numpy as np
import pandas as pd

spots = np.array([[2,3,4,5,6,7], # имя переменной spots по-английски значит «пятна»
    [3,4,5,6,7,8],
    [4,5,6,7,8,9],
    [5,6,7,8,9,10],
    [6,7,8,9,10,11],
    [7,8,9,10,11,12]])

spot_counts = {}
for a in range(0, 6):
    for s in range(0, 6):
        if spots[a][s] not in spot_counts.keys():
            spot_counts[spots[a][s]] = 1
        else:
            spot_counts[spots[a][s]] += 1
print(spot_counts)

spot_probs={k:spot_counts[k]/36 for k in spot_counts}
print(spot_probs)

x = pd.Series([1, 2, 3, 4, 5, 6, 2, 4, 6, 8, 10, 12, 3, 6, 9, 12, 15, 18, 4, 8, 12, 16, 20, 24, 5, 10, 15, 20, 25, 30, 6, 12, 18, 24, 30, 36])
x.hist(density=True, bins=36)

x_probs = {
        '3': 0.1,
        '4': 0.2,
        '5': 0.2,
        '7': 0.3,
        '11': 0.1,
        '16': 0.05,
        '18': 0.05
}

print()
[(print(x_i, x_probs[x_i])) for x_i in x_probs] # 3 0.1, 4 0.2, 5 0.2...18 0.05

expectation = [int(x_i)*x_probs[x_i] for x_i in x_probs]
print(expectation) # [0.30000000000000004, 0.8, 1.0, 2.1, 1.1, 0.8, 0.9]

expectation = sum([int(x_i)*x_probs[x_i] for x_i in x_probs])
print(expectation) # 7.000000000000001

# E(X): для каждого элемента словаря вычисляем произведение вероятности и значения
# случайной величины (целочисленное представление ключа словаря):
expectation1 = sum([int(x_i) * x_probs[x_i] for x_i in x_probs])
# (E(X))^2
square_of_expectation = expectation1 ** 2
# E(X^2)
expectation_of_squares = sum(
    [int(x_i) * int(x_i) * x_probs[x_i] for x_i in x_probs]
)
variance = expectation_of_squares - square_of_expectation
print(variance)

#Корень из дисперсии примерно равен четырём — это стандартное отклонение. Математическое ожидание равно семи.
#Правило трёх сигм работает: в промежутке 7 ± (4 * 2) расположены все значения, кроме 16 и 18, а в промежутке 7 ± (4 * 3) лежат все значения случайной величины.
