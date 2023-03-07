import pandas as pd

df = pd.read_csv('logs.csv')
visits = df.groupby('source')['user_id'].count()
print(visits)

class Sourcer:
    def source(a, b):
        return a + b

print(Sourcer.source(2, 3))

try:
     print(Sourcer.source([1, 2]))
except:
    print('Can\'t source')

print(Sourcer.source(*[10, 20]))
