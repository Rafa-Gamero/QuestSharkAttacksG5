# QuestSharkAttacksG5

Proyecto: Análisis de Datos de Ataques de Tiburones
Este proyecto ha sido realizado por Almudena Ocaña,José Martín,Mario Jiménez y Rafael Gamero. Este proyecto se centra en la recolección, limpieza, y análisis de datos de ataques de tiburones a nivel global, con el objetivo de identificar tendencias y patrones en los ataques. Se utiliza Python junto con varias bibliotecas populares para manipulación y visualización de datos.

Aqui tenemos el enlace a la presentacion que hemos de realizado para este proyecto.
https://www.canva.com/design/DAGP5pNSUQA/3x50Dx_h9nqfgPP_SlYHxg/edit

Bibliotecas Usadas
pandas: Para la manipulación y análisis de datos.
matplotlib: Para la creación de gráficos visuales.
seaborn: Para visualizaciones de gráficos avanzadas.
cleaning: Un módulo personalizado para la limpieza y filtrado de datos.

Descripción del Dataset
El dataset se descarga de la URL: sharkattackfile.net. Este contiene información sobre los ataques de tiburones, incluyendo país, estado, actividad que realizaba la víctima, y la fecha del ataque.

![Captura2](https://github.com/user-attachments/assets/600637fc-f569-40f8-9cd0-e5bfaef148a2)

Pasos del Análisis
Cargar los Datos: Se descargan y leen los datos directamente desde un archivo Excel.

python
Copiar código
url = 'https://www.sharkattackfile.net/spreadsheets/GSAF5.xls'
df = pd.read_excel(url)

Limpieza de Datos: Se realiza una limpieza del dataset, eliminando columnas irrelevantes y corrigiendo el formato de fechas.

![Captura10](https://github.com/user-attachments/assets/03d1dd6d-cf34-4805-be4b-1d36af11575d)


Análisis Estadístico:

Top 10 países con más ataques: Se grafica el número de ataques por país desde el año 2000.
Top 5 actividades más peligrosas: Se identifican las actividades con mayor número de ataques.
Ataques por mes: Se agrupan los ataques por mes para observar patrones temporales.
Estados con más ataques: Se grafican los 5 estados/provincias con más ataques.
Frecuencia de ataques por estado y actividad: Se realiza una gráfica de barras apiladas que muestra la distribución de ataques en los principales estados y las actividades que realizaban las víctimas.

Visualizaciones
A lo largo del análisis se generan varias visualizaciones clave:

Gráfico de barras: Top 10 países con más ataques desde el año 2000.
Gráfico de barras: Top 5 actividades con mayor número de ataques.
Gráfico de barras: Distribución mensual de los ataques.
Gráfico apilado: Distribución de ataques por estado y actividad.


Conclusión
Este proyecto ayuda a visualizar y comprender mejor los patrones de ataques de tiburones en todo el mundo. A través del análisis de datos y visualizaciones, podemos identificar las actividades y regiones con mayor riesgo.

