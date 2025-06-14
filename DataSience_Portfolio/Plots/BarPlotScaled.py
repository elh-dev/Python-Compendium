import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('avocado.csv')

datanew = data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum()


# Creates bar plot with log scale
plot = datanew.plot(kind='bar', figsize=(6, 8), color=['red', 'green', 'blue'], alpha=0.8)

# Set y-axis to logarithmic scale
plt.yscale('log')

# Add title and labels
plt.title('Total Bag by Type (Log Scale)')
plt.xlabel('Bag Size')
plt.ylabel('Total Bags (Log Scale)')
plt.legend(title='Type', labels=['Small', 'Large', 'XLarge'])
plt.tight_layout()

# Display the plot
plt.show()