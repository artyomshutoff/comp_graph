# artyomshutoff

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd


df = pd.read_excel("Данные.xlsx", sheet_name="data").to_numpy()

x = df[:, 0][::-1]
y = np.array(df[:, 1][::-1], dtype=np.int0)

fig = plt.figure(
    num="Компьютерная графика. Лабораторная работа №1",
    figsize=(12.80, 7.20),
    dpi=100,
)

print(" ".join([str(i) for i in y]))

ax = fig.add_subplot(111)
id
x_label = "Дата"
y_label = "Курс USDRUB"

ax.set_xlabel(x_label)
ax.set_ylabel(y_label)


ax.plot(x, y, color="maroon")

ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))

plt.tight_layout()
plt.show()
