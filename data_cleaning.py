import pandas as pd

# Load Excel file
df = pd.read_excel("FAOSTAT_data.xlsx")

# View basic info
print(df.head())
print(df.columns)

# Filter only the rows for Area harvested, Yield, and Production
df = df[df['Element'].isin(['Area harvested', 'Yield', 'Production'])]

# Pivot the Element column to get Area harvested, Yield, and Production in separate columns
df_pivot = df.pivot_table(index=['Area', 'Item', 'Year'], 
                          columns='Element', 
                          values='Value', 
                          aggfunc='sum').reset_index()

# Rename for clarity
df_pivot.columns.name = None
df_pivot.rename(columns={
    'Area harvested': 'Area_harvested',
    'Yield': 'Yield',
    'Production': 'Production'
}, inplace=True)

# Drop rows with any missing data
df_clean = df_pivot.dropna()

# Save cleaned data for model building
df_clean.to_csv("cleaned_faostat.csv", index=False)

print(df_clean.head())
