import pandas as pd
import numpy as np

# открываем файлы
# возьмём индекс '0', чтобы перевести данные в pd.Series
target = pd.read_csv('eng_target.csv')['0']
probabilities = pd.read_csv('eng_probabilities.csv')['0']

def revenue(target, probabilities, count):
    probs_sorted = probabilities.sort_values(ascending=False)
    selected = target[probs_sorted.index][:count]
    return 1000 * selected.sum()

state = np.random.RandomState(12345)

values = []
for i in range(1000):
    target_s = target.sample(n=25, replace=True, random_state=state)
    prob_s = probabilities[target_s.index]
    values.append(revenue(target_s, prob_s, 10))

values = pd.Series(values)
lower = values.quantile(0.01)

mean = values.mean()
print("Средняя выручка:", mean)
print("1%-квантиль:", lower)
