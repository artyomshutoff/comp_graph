# artyomshutoff

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd


df = pd.read_excel("Данные.xlsx", sheet_name="data").to_numpy()

x = df[:, 0]
y = np.array(df[:, 1], dtype=np.int0)

fig = plt.figure(
    num="Компьютерная графика. Лабораторная работа №1",
    figsize=(12.80, 7.20),
    dpi=100,
)

ax = fig.add_subplot(111)

x_label = "Численность населения"
y_label = "Города с численностью постоянного населения 1 млн. человек  и более"

ax.set_xlabel(x_label)
ax.set_ylabel(y_label)


ax.barh(x, y, color="maroon")
ax.invert_yaxis()

ax.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))

plt.tight_layout()
plt.show()
