import numpy as np

x_probs = {
    '-4': 0.05,
    '-2': 0.25,
    '0': 0.1,
    '1': 0.1,
    '5': 0.1,
    '7': 0.05,
    '15': 0.35,
}

expectation = sum([int(x)*x_probs[x] for x in x_probs])
variance = sum(int(x) * int(x) * x_probs[x] for x in x_probs) - (expectation ** 2)
print('Математическое ожидание равно', expectation)  # 5.5
print('Дисперсия равна', variance) # 55.349999999999994

# температура = 5 +/- ((корень из 55 ~ 7) * 3 (сигмы) = 21)
