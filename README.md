Taller de Aprendizaje Automático y Transmisión de Datos
Autor: Samuel Patiño Lucumí

Introducción
En este taller, se construyó un modelo automático de regresión para predecir puntuaciones de felicidad en diferentes países utilizando datos de cinco archivos CSV correspondientes a diferentes años (df_2015, df_2016, df_2017, df_2018, df_2019). El proceso incluyó Análisis Exploratorio de Datos (EDA), operaciones de Extracción, Transformación y Carga (ETL), selección de funciones, entrenamiento de modelos, transmisión de datos mediante Kafka y almacenamiento de predicciones en una base de datos PostgreSQL.

Tecnologías Utilizadas
Python
Jupyter Notebook
Base de datos PostgreSQL
Kafka
Docker
Zookeeper
Librerías Utilizadas
Scikit-learn: Para construir el modelo de regresión
Pandas, Numpy, Matplotlib, Seaborn, Joblib, Psycopg2: Herramientas para EDA, manipulación de datos y conexión a la base de datos.
Análisis Exploratorio de Datos (EDA)
En esta fase, se cargaron y transformaron individualmente cinco archivos CSV (df_2015, df_2016, df_2017, df_2018, df_2019). Después de la limpieza, se concatenaron para crear el DataFrame df_unido. Luego, se extrajeron las características relevantes, y los datos se limpiaron y preprocesaron antes de pasar a los modelos.

Modelos
Se aplicó la técnica de feature selection para elegir las características más relevantes para el modelo de regresión. Los datos se dividieron en un conjunto de entrenamiento (70%) y un conjunto de prueba (30%). Posteriormente, se entrenó un modelo de regresión en el conjunto de entrenamiento.

Kafka
Se crearon contenedores de Docker configurados para que Kafka y ZooKeeper gestionaran el streaming. Se desarrolló un archivo producer.py que envía el DataFrame a Kafka dentro de un contenedor Docker. El archivo consumer.py, también en Kafka y dentro de un contenedor Docker, recupera los datos, utiliza el modelo entrenado para predecir puntuaciones de felicidad y almacena las predicciones junto con las características de entrada.

Base de Datos
Se utilizó PostgreSQL como base de datos para almacenar las predicciones y las características seleccionadas anteriormente para una fácil visualización.

Instrucciones para Ejecutar el Código
Tener instalados Python, Jupyter Notebook, Kafka y PostgreSQL.
Ejecutar los pasos del EDA en Jupyter Notebook, realizar la selección de funciones, entrenamiento de modelos e integración de Kafka.
Configurar productores y consumidores de Kafka para su entorno.
Crear una base de datos PostgreSQL y establecer la conexión con el código para almacenar la tabla con las predicciones.
Ejecutar el productor de Kafka para iniciar la transmisión de datos.
Ejecutar el consumidor de Kafka para recibir datos, realizar predicciones y almacenar resultados en la base de datos PostgreSQL creada anteriormente.
