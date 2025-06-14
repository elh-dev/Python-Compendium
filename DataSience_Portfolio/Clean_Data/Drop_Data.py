import pandas as pd

data = pd.read_csv('avocado.csv')
print(data.head())

# Drop Rows: Region Total US
print("_____________________________________________")
print("Drop Rows")
print("_____________________________________________")
print("Before:")
print(data.region.unique())
data = data[data['region'] != 'TotalUS']
print("_____________________________________________")
print("After:")
print(data.region.unique())

# Drop Columns 
print("_____________________________________________")
print("Drop Columns")
print("_____________________________________________")
print("Before:")
print(data.columns)
data = data.drop(columns = ['Unnamed: 0','4046', '4225', '4770'])
print("_____________________________________________")
print("After:")
print(data.columns)