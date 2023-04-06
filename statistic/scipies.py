from scipy import stats as st

# математическое ожидание
mu = 1000
# стандартное отклонение
sigma = 100

# задаём нормальное распределение с математическим ожиданием 1000
# и стандартным отклонением 100
distr = st.norm(1000, 100)

# значение, для которого хотим найти вероятность
x = 1000

# считаем вероятность получить значение, равное x или меньше
result = distr.cdf(x)

print(result)

# значение, для которого хотим найти вероятность
x = 1150

# считаем вероятность получить значение больше x
result = 1 - distr.cdf(x)
print(result)

# Другой пример использования метода — найти вероятность попасть между значениями 900 и 1100.
# Для этого достаточно вычесть кумулятивную вероятность (cdf)
# меньшего значения из кумулятивной вероятности большего значения:
# «хвост» распределения левее меньшего значения сократится
# и останется только интервал между значениями.

x1 = 900
x2 = 1100

result = distr.cdf(x2) - distr.cdf(x1)

print(result)

# Hайдём значение по вероятности. В р1 зададим вероятность, примерно равную 84.13%
p1 = 0.841344746

result = distr.ppf(p1)
print(result)
# ЗАДАЧА 1
mu = 100500 # укажите, чему равно среднее значение распределения
sigma = 3500 # укажите, чему равно стандартное отклонение распределения

penalty_threshold = 92000 # укажите значение, по которому проходит граница для штрафа
bonus_threshold = 111000 # укажите значение, по которому проходит граница для бонуса

distr = st.norm(mu, sigma)# постройте нормальное распределение со средним mu и стандартным отклонением sigma

p_penalty = distr.cdf(penalty_threshold)# посчитайте вероятность получить штраф с помощью метода cdf()
p_bonus = 1 - distr.cdf(bonus_threshold)# посчитайте вероятность получить бонус с помощью метода cdf()

print('Вероятность штрафа:', p_penalty)
print('Вероятность бонуса:', p_bonus)

# ЗАДАЧА 2
mu = 420# укажите среднее значение распределения
sigma = 65# укажите стандартное отклонение распределения
prob = 0.9# укажите, с какой вероятностью нужно распродать весь товар

distr = st.norm(mu, sigma)# создайте требуемое распределение

n_shipment = distr.ppf(1 - prob)# укажите, сколько единиц товара нужно заказать

print('Нужно заказать единиц товара:', int(n_shipment))

# ЗАДАЧА 3

mu = 2400# укажите, чему равно среднее значение распределения
sigma = 320# укажите, чему равно стандартное отклонение распределения
threshold = 0.75# укажите, какая доля заказов должна быть дороже двух стоимостей доставки

max_delivery_price = (st.norm(mu, sigma).ppf(1 - threshold)) / 2# укажите, какую стоимость доставки установить

print('Максимальная стоимость доставки курьером:', max_delivery_price)
