import pandas as pd
import numpy as np

# столбец со значениями
data = pd.Series([11.2, 20.5, 22.35, 31.1, 32.05, 33.8, 41.2, 42.15, 43.5, 44.123, 51.1, 52.712, 53.053, 54.012, 55.2, 61.987, 62.123, 63.123, 64.12, 65.5678, 66.16, 71.051, 72.531, 73.121, 74.71, 75.1233, 76.51, 77.12, 81.005, 82.01, 83.5, 84.323, 85.1, 86.1, 87.1, 88.12, 91.56, 92.056, 93.651, 94.777, 95.102, 96.105, 97.503, 98.003, 99.00005])

# строим гистограмму с 4 корзинами, задаём аргумент bins — количество интервалов, целым числом
# аргумент alpha задаёт непрозрачность графика, 1 — полностью непрозрачный график
data.hist(bins=4, alpha=0.5)

# строим гистограмму с 9 корзинами, границы которых перечислены в списке
# от 11 до 20, от 20 до 30, от 30 до 40 и так далее
# аргумент alpha задаёт непрозрачность графика, 1 — полностью непрозрачный график
data.hist(bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99], alpha=0.7)

# стандартное отклонение (корень из дисперсии совокупности)
standard_deviation = np.std(data)
print (standard_deviation)
# стандартное отклонение выборки
standard_deviation = np.std(data, ddof=1)
print (standard_deviation)
# корень из дисперсии будет равен стандартному отклонению:
variance = 2.9166666666666665
standard_deviation = np.sqrt(variance)
print(standard_deviation)
# дисперсия генеральной совокупности
variance = np.var(data)
print(variance)

adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var)# рассчитайте стандартное отклонение

adv_time = adv_mean + (adv_std * 3)# рассчитайте время показа пользователю всплывающего сообщения

print(f'Время показа сообщения {adv_time}')
