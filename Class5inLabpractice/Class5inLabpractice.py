import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime
plt.rcParams['font.sans-serif'] = ['SimHei']


import pandas as pd
filename = './data_weather_sitka_2014-07.csv'
with open(filename) as f:
    r=csv.reader(f)
    head_row=next(r)
    dates, highs, lows=[], [], []
    for row in r:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        high = eval(row[1])
        low = eval(row[3])

        dates.append(date)
        highs.append(high)
        lows.append(low)
fig=plt.figure()
plt.plot(dates, highs, c= 'blue')
plt.plot(dates, lows, c = 'black')
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.75)
fig.autofmt_xdate()
plt.show()