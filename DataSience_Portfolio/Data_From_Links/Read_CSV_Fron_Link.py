import os
import pandas as pd

link = "https://raw.githubusercontent.com/fivethirtyeight/data/master/thanksgiving-2015/thanksgiving-2015-poll-data.csv"
data = pd.read_csv(link)

print(data.head())