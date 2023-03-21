import random
import pandas as pd
import matplotlib.pyplot as plt

def dice_roll():
    score = random.randint(1, 6)
    return score

def double_roll_score():
    first = dice_roll()
    second = dice_roll()
    score = first + second
    return score

experiments = []
for i in range(1000):
    score = double_roll_score()
    experiments.append(score)

df_experiments = pd.DataFrame(experiments)
df_experiments.hist(bins=11, range=(2, 12))
plt.show()
