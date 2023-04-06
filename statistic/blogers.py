from scipy import stats as st
import math as mt

# количество попыток
binom_n = 5000
# вероятность успеха
binom_p = 0.15

# целевое значение
bloger_clicks = 715

# считаем математическое ожидание
mu = binom_n * binom_p
# считаем стандартное отклонение
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

# строим нормальное распределение с параметрами mu и sigma
distr = st.norm(mu, sigma)

# Найдём вероятность получить 715 кликов или меньше, применив метод cdf()
p_clicks = distr.cdf(bloger_clicks)
print(p_clicks)

# Узнать вероятность получить 715 переходов и более
p_clicks = 1 - distr.cdf(bloger_clicks)
print(p_clicks)
