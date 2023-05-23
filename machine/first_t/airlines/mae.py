import pandas as pd

def mae(target, predictions):
    return 1/len(target) * sum(abs(target - predictions))

target = pd.Series([-0.5, 2.1, 1.5, 0.3])
predictions = pd.Series([-0.6, 1.7, 1.6, 0.2])

print(mae(target, predictions))
