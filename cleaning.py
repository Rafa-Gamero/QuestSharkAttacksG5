import pandas as pd
url = 'https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'

df = pd.read_excel(url)




def clean_data(df):
    df.isnull().sum()
    
    
    
    
def delete_columns(df,columns):
    df = df.drop(columns, axis=1)
    return df

