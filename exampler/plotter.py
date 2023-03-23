import pandas as pd
import matplotlib.pyplot as plt

# creating dataframe and show it's basic plot
df = pd.DataFrame({'a': [2, 3, 4, 5], 'b': [4, 9, 16, 25]})
print(df)
df.plot()
plt.show()

# changing title
df.plot(title='A и B')

# dot style
df.plot(style='o')

# x style
df.plot(style='x')

# dot and line style
df.plot(style='o-')

# changing fundamental of plot - it depends on columns now
df.plot(x='b', y='a', style='o-')

# fit plot for comfort
df.plot(x='b', y='a', style='o-', xlim=(0, 30))

# adding grid
df.plot(x='b', y='a', style='o-', xlim=(0, 30), grid=True)

# creating with special size
# small
df.plot(x='b', y='a', style='o-', xlim=(0, 30), grid=True, figsize=(1, 1))

# big
df.plot(x='b', y='a', style='o-', xlim=(0, 30), grid=True, figsize=(10, 3))
