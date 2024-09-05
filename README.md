# QuestSharkAttacksG5

 Descripción del proyecto
Este proyecto utiliza datos de ataques de tiburones registrados en un archivo Excel disponible en la Global Shark Attack File. El objetivo principal es limpiar y filtrar los datos para obtener un subconjunto que contenga información relevante a partir del año 2020.

Requisitos
Para ejecutar este código, se necesitan las siguientes bibliotecas de Python:

pandas
matplotlib
seaborn

Descripción del código
1. Cargar el archivo de datos
El código carga el archivo de datos de ataques de tiburones desde la URL proporcionada en formato Excel, utilizando pandas:

![Captura2](https://github.com/user-attachments/assets/600637fc-f569-40f8-9cd0-e5bfaef148a2)

2. Eliminar columnas innecesarias
Se define una función delete_columns(df) para eliminar las columnas que no son relevantes para el análisis:
![Captura3](https://github.com/user-attachments/assets/f7d5b978-00b9-4748-a55f-e9984c8053d1)

3. Limpiar el DataFrame
La función clean_data(df) se utiliza para:

Estandarizar los nombres de las columnas.
Eliminar duplicados.
Remover filas con valores nulos.
![Captura4](https://github.com/user-attachments/assets/e16ce968-3ca3-4704-ad36-a32f33f22ec3)

4. Limpieza de las fechas
Se incluyen dos funciones para limpiar y corregir el formato de las fechas:

remove_prefix(date) elimina el prefijo "Reported" de las fechas.
fix_format_date(date) convierte las fechas a un formato estándar (dd-mm-yyyy).
![Captura5](https://github.com/user-attachments/assets/a184b153-c2f0-4013-b29f-6cd0d342ecac)

5. Filtrar los datos desde 2020
La función filter_date(df) convierte la columna de fechas a un tipo datetime y filtra los registros a partir del 1 de enero de 2020:
![Captura6](https://github.com/user-attachments/assets/bbe6636b-ba32-4727-950c-23ac021ed6d8)

6. Imprimir el DataFrame filtrado
Finalmente, el código imprime el DataFrame filtrado con los datos de ataques de tiburones registrados desde 2020:
![image](https://github.com/user-attachments/assets/d0f83703-3b05-4a87-bc88-0754e18937e6)




