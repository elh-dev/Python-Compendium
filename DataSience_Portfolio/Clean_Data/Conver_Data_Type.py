import pandas as pd

data = pd.read_csv('avocado.csv')
print(data.head())

# Converts object to date tipe
print("_____________________________________________")
print("Conver Type")
print("_____________________________________________")
print("Before:")
print(data.dtypes)
data['Date'] = pd.to_datetime(data['Date'])
print("_____________________________________________")
print("After:")
print(data.dtypes)