import pandas as pd
import matplotlib.pyplot as plt
# write your code here
import seaborn as sns

data = pd.read_csv('avocado.csv')


datanew = data[data['region'].isin(['TotalUS','West', 'WestTexNewMexico'])]

sns.catplot(data=datanew,kind='bar', x='year', y='Total Volume', hue='region',palette={'TotalUS': 'blue','West':'orange', 'WestTexNewMexico': 'green'})

plt.xlabel('Year')
plt.title('Total Volume by Year')

plt.show()
