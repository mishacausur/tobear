from matplotlib import pyplot as plt
from math import factorial, sqrt
from scipy.stats import norm

# биномиальное распределение
p = 0.8
n = 50

binom = []
for k in range(0,n + 1):
    choose = factorial(n) / (factorial(k) * factorial(n - k))
    prob = choose * p**k * (1 - p)**(n - k)
    binom.append(prob)

# нормальное распределение
mu = n * p
var = n * p * (1-p)
sigma = sqrt(var)

x = range(25, n + 1)

plt.bar(range(25, n + 1), binom[25:], alpha=0.3)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.show()
