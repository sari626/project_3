import matplotlib.pyplot as plt
import seaborn as sns

# Crop distribution
plt.figure(figsize=(10, 4))
sns.countplot(data=df_clean, x='Item', order=df_clean['Item'].value_counts().head(10).index)
plt.xticks(rotation=45)
plt.title('Top 10 Most Cultivated Crops')
plt.tight_layout()
plt.show()

# Yearly production trend
yearly_prod = df_clean.groupby('Year')['Production'].sum().reset_index()
plt.plot(yearly_prod['Year'], yearly_prod['Production'])
plt.title('Total Crop Production Over Years')
plt.xlabel('Year')
plt.ylabel('Production (tons)')
plt.grid(True)
plt.show()

# Correlation
sns.heatmap(df_clean[['Area_harvested', 'Yield', 'Production']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
