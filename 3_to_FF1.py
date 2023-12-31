import pandas as pd

df = pd.read_excel('Data/DataSet.xlsx', sheet_name='FF')

# Assuming df is your DataFrame and 'Column1', 'Column2', 'Column3' are the columns to remove outliers from
def remove_outliers(df, columns):
    df_no_outliers = df.copy()  # Create a copy of the DataFrame to preserve the original

    for column_name in columns:
        q1 = df_no_outliers[column_name].quantile(0.15)  # First quartile
        q3 = df_no_outliers[column_name].quantile(0.85)  # Third quartile

        # Calculating the Interquartile Range (IQR)
        iqr = q3 - q1

        # Define the lower and upper bounds for outlier detection
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Filtering the DataFrame to remove outliers for each column
        df_no_outliers = df_no_outliers[(df_no_outliers[column_name] >= lower_bound) & (df_no_outliers[column_name] <= upper_bound)]

    df_no_outliers = df_no_outliers.dropna(subset=columns)

    return df_no_outliers

columns_to_remove_outliers = ['PRICE_N']
df_no_outliers = remove_outliers(df, columns_to_remove_outliers)

cases=(df_no_outliers['PRICE_N'] < df_no_outliers['LA_N'] * 200000) | (df_no_outliers['LA_N'] < 1) | (df_no_outliers['RA_N'] > 20) | (df_no_outliers['RA_N'] < 6) | (df_no_outliers['BEDROOM'] > df_no_outliers['FLOOR']*4) | (df_no_outliers['BEDROOM'] < df_no_outliers['FLOOR']*1) | (df_no_outliers['FLOOR'] < 1) | (df_no_outliers['BATHROOM'] > (df_no_outliers['FLOOR']*2)) | (df_no_outliers['BATHROOM'] < (df_no_outliers['FLOOR']))

indices_to_drop = df_no_outliers[cases].index
df_no_outliers = df_no_outliers.drop(indices_to_drop)

def newcol(row):
    true_count = row.sum()  # Count the number of True values in a row
    if true_count == 3:
        return 150
    elif true_count == 2:
        return 100
    else:
        return 50 


df_no_outliers['val']=df[['Has_ParkingN','ER_N','DW_N']].apply(newcol,axis=1)






with pd.ExcelWriter('Data/DataSet.xlsx', mode='a',engine='openpyxl') as writer:
    df_no_outliers[['CITY','LA_N','RA_N','BY_N','FLOOR','BEDROOM','BATHROOM','FACING_N','PRICE_N','val']].to_excel(writer,sheet_name='FF1', index=False)