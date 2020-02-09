import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Analyzing data
df = pd.read_csv('files/FullData.csv')
print(df.head(7))
del df['National_Kit']
print(df.head())

# Visualize data in plots
# figure out that country with most players
plt.figure(figsize=(15, 32))
# plot all nations on y-axis
sns.countplot(y=df.Nationality, palette='Set2')
plt.show()
