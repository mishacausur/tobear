import random
import pandas as pd
import matplotlib.pyplot as plt

def bus_wait_time():
    return random.randint(0, 10)

def train_wait_time():
    return random.randint(0, 5)

def total_delay():

    return (
        bus_wait_time()
        + train_wait_time()
        + train_wait_time()
        + bus_wait_time()
    )

days = []

for i in range(365 * 5):
    delay = total_delay()
    days.append(delay)

df_days = pd.DataFrame(days)

df_days.hist(bins=10)
plt.show()
