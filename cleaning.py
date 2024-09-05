import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = 'https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'

df = pd.read_excel(url)



# Cargar el DataFrame desde la URL
url = 'https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'
df = pd.read_excel(url)

# Función para eliminar columnas innecesarias
def delete_columns(df):
    df_dropped_multiple = df.drop(['Year', 'Type', 'Location', 'Name', 'Sex', 'Age', 'Injury',
                                   'Unnamed: 11', 'Time', 'Species ', 'Source', 'pdf', 'href formula',
                                   'href', 'Case Number', 'Case Number.1', 'original order',
                                   'Unnamed: 21', 'Unnamed: 22'], axis=1)
    return df_dropped_multiple

# Limpiar el DataFrame
df = delete_columns(df)

# Función para limpiar los datos
def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.drop_duplicates(inplace=True)
    df = df.dropna()
    return df

df= clean_data(df)

def get_mode_of_attacks(df):
    
    moda_country = df['country'].mode()[0]
    moda_state = df['state'].mode()[0]
    moda_activity = df['activity'].mode()[0]

    return {
        'most_attacked_country': moda_country,
        'most_attacked_state': moda_state,
        'most_common_activity': moda_activity
    }
    
result = get_mode_of_attacks(df)
print(f"The country with most attacks is: {result['most_attacked_country']}")
print(f"The state with most attacks is: {result['most_attacked_state']}")
print(f"The activity in which most attacks occurs is: {result['most_common_activity']}")

def top_country_state_activity(df, n=10):
 
    
    country_state_activity = df.groupby(['country', 'state', 'activity']).size().sort_values(ascending=False).head(n)
    print(f"Top {n} combinaciones país-estado-actividad más frecuentes:")
    return country_state_activity

top_activities = top_country_state_activity(df, 10)
print(top_activities)

# Función para remover el prefijo "Reported " de las fechas
def remove_prefix(date):
    if isinstance(date, str) and date.startswith("Reported "):
        return date[len("Reported "):]
    return date

# Función para corregir el formato de las fechas
def fix_format_date(date):
    if isinstance(date, str):
        try:
            correct_date_format = pd.to_datetime(date, format='%d-%b-%Y', errors='coerce')
            return correct_date_format.strftime('%d-%m-%Y') if correct_date_format else None
        except ValueError:
            return None
    return None

# Aplicar las funciones de limpieza de fechas
df['date'] = df['date'].apply(remove_prefix)
df['date'] = df['date'].apply(fix_format_date)

def filter_date(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df_filtered = df[df['date'] >= pd.to_datetime('2000-01-01')]
    return df_filtered

df = filter_date(df)
print(df)

def plot_top_countries_attacks(df_filtered, top_n=10):
    """
    Función que agrupa los ataques por país, estado, actividad y mes/año,
    y genera un gráfico de barras con los principales países afectados.
    
    Parámetros:
    df_filtered (DataFrame): DataFrame filtrado que contiene la columna 'date' en formato datetime.
    top_n (int): Número de países a mostrar en el gráfico. Por defecto es 10.
    """
    
    # Crear nueva columna de mes/año para agrupar
    df_filtered['month_year'] = df_filtered['date'].dt.to_period('M').astype(str)
    
    # Agrupar por país, estado, actividad y mes/año
    attacks_grouped = df_filtered.groupby(['country', 'state', 'activity', 'month_year']).size().reset_index(name='count')
    
    # Contar el número de ataques por país
    attacks_per_country = df_filtered.groupby('country').size().reset_index(name='count')

    # Obtener los principales países con más ataques
    top_countries = attacks_per_country.sort_values(by='count', ascending=False).head(top_n)
    
    # Graficar los ataques por país
    plt.figure(figsize=(14, 8))
    bars = plt.bar(top_countries['country'], top_countries['count'], color='lightblue')

    # Añadir los números dentro de las barras
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), va='bottom', ha='center', color='black')

    # Configuraciones del gráfico
    plt.xlabel('Country')
    plt.ylabel('Number of Attacks')
    plt.title(f'Top {top_n} Countries with the Most Shark Attacks (from 2000)')
    plt.gca().invert_xaxis()  # Invertir el eje X para que el país con más ataques esté al principio
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()