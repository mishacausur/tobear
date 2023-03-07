import pandas as pd

df = pd.read_csv('logs.csv')
visits = df.groupby('source')['user_id'].count()
print(visits)

class Sourcer:
    def source(a, b):
        return a + b

    def stringer(*args, **kwargs):
        print('untitled args', args)
        print('key-value args', kwargs)

    def closer(x, y, z):
        return x + y + z

print(Sourcer.source(2, 3))

try:
     print(Sourcer.source([1, 2]))
except:
    print('Can\'t source')

print(Sourcer.source(*[10, 20]))

Sourcer.stringer(1,2,3, key='word', key2='word2')

xy = [1, 2]
z = {'z':3}

assert Sourcer.closer(*xy, **z) == 6

