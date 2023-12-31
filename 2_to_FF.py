import pandas as pd

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FilteredData')

#convert LA_N and RA_N to float and remove those that cannot be changed
df['LA_N'] = pd.to_numeric(df['LA_N'], errors='coerce')
df['RA_N'] = pd.to_numeric(df['RA_N'], errors='coerce')
df['BY_N'] = pd.to_numeric(df['BY_N'], errors='coerce')
#coerce-> converts non-convertible values to NaN/null

# Check if 'Parking' is present in the 'AMENROW' list and create a new column 'Has_Parking'
df['Has_Parking'] = df['AMENROW'].apply(lambda x: 'Parking' in x)
df['ER'] = df['AMENROW'].apply(lambda x: 'Earthquake Resistant' in x)
df['DW'] = df['AMENROW'].apply(lambda x: 'Drinking Water' in x)

df['Has_ParkingN'] = df['Has_Parking'].replace({'TRUE': 1, 'FALSE': 0})
df['ER_N'] = df['ER'].replace({'TRUE': 1, 'FALSE': 0})
df['DW_N'] = df['DW'].replace({'TRUE': 1, 'FALSE': 0})


df.dropna(subset=['LA_N','RA_N','FACING_N'],inplace=True)
#subset parameter allows us to specify multipe columns


with pd.ExcelWriter('Data/DataSet.xlsx', mode='a',engine='openpyxl') as writer:
    df[['CITY','LA_N','RA_N','BY_N','FLOOR','BEDROOM','BATHROOM','FACING_N','PRICE_N','Has_ParkingN','ER_N','DW_N']].to_excel(writer,sheet_name='FF', index=False)