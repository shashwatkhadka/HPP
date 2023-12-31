import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FF1')

y="PRICE_N"
x="val"


# Scatterplot using Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x=x, y=y)
plt.xlabel(x)
plt.ylabel(y)

plt.grid(True)


heatmap_col=["LA_N","RA_N","FLOOR","BEDROOM","BATHROOM","PRICE_N"]
df1=df[heatmap_col]
cormatrix=df[heatmap_col].corr()

plt.figure(figsize=(8,6))
plt.title("Correlation Heatmap")
sns.heatmap(cormatrix, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 10})
plt.show()