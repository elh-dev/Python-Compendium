import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('avocado.csv')

# Add title and labels
plt.figure(figsize=(8, 6))
plt.scatter(data['AveragePrice'],data['Total Volume'], color='blue', alpha=0.7)

plt.title('Scatter Plot of ')
plt.xlabel('AveragePrice')
plt.ylabel('Total Volume')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
