import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# df.plot()

# df['Adj Close'].plot()

df[['High', 'Low']].plot()

plt.show()