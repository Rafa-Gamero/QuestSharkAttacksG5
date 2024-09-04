import pandas as pd
url = 'https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'

df = pd.read_excel(url)


def delete_columns(df):
    df_dropped_multiple = df.drop(['Year', 'Type','Location','Name','Sex','Age','Injury','Species','Source','pdf','href formula','href','Case Number','Case Number.1','original order','Unnamed: 21','Unnamed: 22','Unnamed: 11'], axis=1)
    return df_dropped_multiple


def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    #Delete null values
    df_nullValues = df.dropna()
    return df



def remove_prefix(date):
    # Make sure date is a string
    if isinstance(date, str) and date.startswith("Reported "):
        # If the date starts with "Reported", we return what comes after that
        return date[len("Reported "):]
    # Return the original value if its not a string or doesn't start with the prefix
    return date

def fix_format_date(date):
    # Make sure date is a string before trying to convert it
    if isinstance(date, str):
        try:
            # Convert the value to datetime format with the format dd-mmm-yyyy
            correct_date_format = pd.to_datetime(date, format='%d-%b-%Y', errors='raise')
            # Return the date in dd-mm-yyyy format
            return correct_date_format.strftime('%d-%m-%Y')
        except ValueError:
            return None
    # If date is not a string we return None
    return None