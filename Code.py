import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import rcParams

sns.set() #sets the style of plots to be seaborn

df = pd.read_csv('/Users/shanehower/Desktop/vgd.csv' )
df['Critic_Score'] = df['Critic_Score'].fillna(0)
df['Critic_Count'] = df['Critic_Count'].fillna(0)
df['User_Score'] = df['User_Score'].fillna(0)
df['User_Count'] = df['User_Count'].fillna(0)
df['Rating'] = df['Rating'].fillna(0)
df['Year_of_Release'] = df['Year_of_Release'].fillna(0)
df.describe()[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]]
df

#group data by Genre and fine the mean sales of each genre
x1= df.groupby(['Genre'])
x2= pd.DataFrame()
x2['Sum of Global Sales'] = x1['Global_Sales'].sum()
x2['count'] = x1.size()
x2 = x2.reset_index()
print(df.describe()[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]])
print(x2)
x_axis = x2['Genre']
y_pos = np.arange(len(x_axis))
bar_width = 1
plt.barh(y_pos, x2['Sum of Global Sales'], bar_width, edgecolor = 'black', linewidth = 1.2, align = 'center')
plt.yticks(y_pos, x_axis)
plt.title('Global Sales by Genre')
plt.ylabel('Genre')
plt.xlabel('Sales')
plt.tight_layout()
plt.show()


d1 = ['Critic_Score', 'User_Score','Global_Sales','EU_Sales','JP_Sales']
sns.pairplot(df[d1], diag_kind="kde") #creates a pairplot
plt.suptitle("Pairplot Between Stats", x=0, y=1.02)
plt.show()

corr_stats = df[d1].corr() #looking at correlation between stats, this is a correlation matrix
fig = plt.figure(figsize =(12,10))
ax = plt.gca()
sns.heatmap(corr_stats, cmap = "inferno", annot = True, ax = ax) #creates a heat map using the matrix corr_stats
plt.suptitle("Correlation Heatmap Between Stats", x=0.44, y=0.92)
plt.show()
