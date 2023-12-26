import pandas as pd

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FilteredData')

#convert LA_N and RA_N to float and remove those that cannot be changed
df['LA_N'] = pd.to_numeric(df['LA_N'], errors='coerce')
df['RA_N'] = pd.to_numeric(df['RA_N'], errors='coerce')
df['BY_N'] = pd.to_numeric(df['BY_N'], errors='coerce')
#coerce-> converts non-convertible values to NaN/null

df.dropna(subset=['LA_N','RA_N','FACING_N'],inplace=True)
#subset parameter allows us to specify multipe columns


with pd.ExcelWriter('Data/DataSet.xlsx', mode='a',engine='openpyxl') as writer:
    df.to_excel(writer,sheet_name='FF', index=False)