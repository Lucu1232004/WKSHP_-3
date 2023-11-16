# WKSHP_-3
Samuel Patiño Lucumí

###Taller de aprendizaje automático y transmisión de datos

Intro:
En este taller construi un modelo automático de regresión para predecir puntuaciones de felicidad en diferentes países utilizando datos de cinco archivos CSV correspondientes a diferentes años (df_2015, df_2016, df_2017, df_2018, df_2019). Todo el proceso lo hice con un EDA, operaciones de extracción, transformación y carga (ETL), selección de funciones, entrenamiento de modelos, transmisión de datos mediante Kafka y almacenamiento de predicciones en una base de datos en PostgreSQL.

##¿Qué utilicé?

#Tecnologías

-Python
-Jupyter Notebook
-Base de datos PostgreSQL
-Kafka
-Docker
-Zookeeper

#Librerias

-Scikit-learn - Esta me sirvió para hacer el modelo de regresión
-Pandas, Numpy, Matplotlib, Seaborn, Joblib, Psycopg2

#EDA:

Aquí se cargan y transforman individualmente cinco archivos CSV (df_2015, df_2016, df_2017, df_2018, df_2019), para después de la limpieza hacer un concat y crear df_unido
Luego se extraen las características relevantes y los datos se limpian y preprocesan.
Para pasar a los modelos

#Modelos:
Se hace el feature_selection para elegir las características más relevantes para el modelo de regresión.
Los datos se dividen en un conjunto de entrenamiento 70% y un conjunto de prueba 30%.
Se entrena un modelo de regresión en el conjunto de entrenamiento.

#Kafka:
Cree unos contenedores de Docker que están configurados para que Kafka y ZooKeeper administren el streaming.
Luego hice un archivo producer.py que envia el dataframe a Kafka dentro de un contenedor Docker.
El archivo consumer.py en Kafka, también dentro de un contenedor Docker, recupera los datos, utiliza el modelo entrenado para predecir puntuaciones de felicidad y almacena las predicciones junto con las funciones de entrada para después con el script.py enviar la base de datos a PostgreSQL.

#Base de datos:
Para aclarar mejor,  uso PostgreSQL como base de datos para almacenar las predicciones y las características que he eligido anteriormente para una fácil visualización.

##Instrucciones para ejecutar el código:

-Tener Python, Jupyter Notebook, Kafka y PostgreSQL instalados.
-Con Jupyter Notebook ejecutar los pasos del EDA de este repo, hacer selección de funciones, entrenamiento de modelos e integración de Kafka.
-Configurar productores y consumidores de Kafka para su respectivo entorno.
-Cree una base de datos PostgreSQL y haga la  conexión con el código para almacenar la tabla con las predicciones.
-Ejecute el productor Kafka para comenzar a transmitir datos.
-Ejecute el consumidor de Kafka para recibir datos, hacer predicciones y almacenar resultados en la base de datos PostgreSQL que creamos anteriormente.
