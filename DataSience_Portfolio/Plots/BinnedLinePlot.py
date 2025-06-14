import pandas as pd
import matplotlib.pyplot as plt
# write your code here
import seaborn as sns

data = pd.read_csv('avocado.csv')


# Before Solution
# # write your code here
# datanew = data[data['region'].isin(['TotalUS','West', 'WestTexNewMexico'])]
# print(datanew)
# sns.boxplot(x='year', y='Total Volume',hue='region', data=datanew, width=0.5, palette={'TotalUS': 'blue','West':'orange', 'WestTexNewMexico': 'green'})
# # create a categorical plot with the specified conditions
# plt.title('Total Volume by Year')
# plt.xlabel('year')
# plt.ylabel('Total Volume')
# plt.show()


data['Total Bags Binned'] = pd.cut(data['Total Bags'], bins=4)


binpoint = data.groupby('Total Bags Binned',observed=True)['Total Bags'].mean()


data['binlabel'] = data['Total Bags Binned'].map(binpoint)


data['Total Bags Binned'] = data['Total Bags Binned'].astype(str)


datanew = data.groupby('binlabel', as_index=False, observed= True)['AveragePrice'].mean()


sns.lineplot(data=datanew, x='binlabel', y='AveragePrice')

plt.title('Average Price by Total Bags Averaged')
plt.ylabel('Average Price')
plt.xlabel('Total Bags Binned')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()  

plt.show()

