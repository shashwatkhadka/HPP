import pandas as pd
from openpyxl import load_workbook

df = pd.read_excel('Data/DataSet.xlsx',sheet_name="amenities")

# Check if 'Parking' is present in the 'AMENROW' list and create a new column 'Has_Parking'
df['Has_Parking'] = df['AMENROW'].apply(lambda x: 'Parking' in x)
df['ER'] = df['AMENROW'].apply(lambda x: 'Earthquake Resistant' in x)
df['DW'] = df['AMENROW'].apply(lambda x: 'Drinking Water' in x)


# Save the 'Has_Parking' column to a new sheet in the Excel file
with pd.ExcelWriter('Data/DataSet.xlsx', engine='openpyxl', mode='a') as writer:
    df[['Has_Parking','ER','DW']].to_excel(writer, sheet_name='amen', index=False)

