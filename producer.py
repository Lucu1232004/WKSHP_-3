from kafka import KafkaProducer
from json import dumps
import pandas as pd
from sklearn.model_selection import train_test_split


df_2015=pd.read_csv("./CSV WKSHP3/2015.csv")
df_2016=pd.read_csv("./CSV WKSHP3/2016.csv")
df_2017=pd.read_csv("./CSV WKSHP3/2017.csv")
df_2018=pd.read_csv("./CSV WKSHP3/2018.csv")
df_2019=pd.read_csv("./CSV WKSHP3/2019.csv")

#Le añadimos una columna del año, para que en el DF final aparezca
df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019

#Elimino de df_2015 y df_2016 la columna region que me irrelevante
# Elimina la columna "Region" de df_2015
if 'Region' in df_2015.columns:
    df_2015 = df_2015.drop('Region', axis=1)

# Elimina la columna "Region" de df_2016
if 'Region' in df_2016.columns:
    df_2016 = df_2016.drop('Region', axis=1)

#Ahora le cambio el nombre a las primeros 3 DF's para que al final sea mas facil combinar
df_2015.rename(columns={'Country': 'Country or region'}, inplace=True)
df_2016.rename(columns={'Country': 'Country or region'}, inplace=True)
df_2017.rename(columns={'Country': 'Country or region'}, inplace=True)

df_2017.rename(columns={'Happiness.Rank': 'Happiness Rank'}, inplace=True)
df_2018.rename(columns={'Overall rank': 'Happiness Rank'}, inplace=True)
df_2019.rename(columns={'Overall rank': 'Happiness Rank'}, inplace=True)

df_2017.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)
df_2018.rename(columns={'Score': 'Happiness Score'}, inplace=True)
df_2019.rename(columns={'Score': 'Happiness Score'}, inplace=True)

#Elimino estas columnas ya que no estan en los otros dataframes
if 'Standard Error' in df_2015.columns:
    df_2015 = df_2015.drop('Standard Error', axis=1)
    
if 'Lower Confidence Interval' in df_2016.columns:
    df_2016 = df_2016.drop('Lower Confidence Interval', axis=1)
if 'Upper Confidence Interval' in df_2016.columns:
    df_2016 = df_2016.drop('Upper Confidence Interval', axis=1)

if 'Whisker.high' in df_2017.columns:
    df_2017 = df_2017.drop('Whisker.high', axis=1)
if 'Whisker.low' in df_2017.columns:
    df_2017 = df_2017.drop('Whisker.low', axis=1)

#Elimino la columna Family
if 'Family' in df_2015.columns:
    df_2015 = df_2015.drop('Family', axis=1)
if 'Family' in df_2016.columns:
    df_2016 = df_2016.drop('Family', axis=1)
if 'Family' in df_2017.columns:
    df_2017 = df_2017.drop('Family', axis=1)

if 'Happiness Rank' in df_2015.columns:
    df_2015 = df_2015.drop('Happiness Rank', axis=1)
if 'Happiness Rank' in df_2016.columns:
    df_2016 = df_2016.drop('Happiness Rank', axis=1)
if 'Happiness Rank' in df_2017.columns:
    df_2017 = df_2017.drop('Happiness Rank', axis=1)
if 'Happiness Rank' in df_2018.columns:
    df_2018 = df_2018.drop('Happiness Rank', axis=1)
if 'Happiness Rank' in df_2019.columns:
    df_2019 = df_2019.drop('Happiness Rank', axis=1)

df_2015.rename(columns={'Economy (GDP per Capita)': 'GDP per capita'}, inplace=True)
df_2016.rename(columns={'Economy (GDP per Capita)': 'GDP per capita'}, inplace=True)
df_2017.rename(columns={'Economy..GDP.per.Capita.': 'GDP per capita'}, inplace=True)

df_2015.rename(columns={'Health (Life Expectancy)': 'Life expectancy'}, inplace=True)
df_2016.rename(columns={'Health (Life Expectancy)': 'Life expectancy'}, inplace=True)
df_2017.rename(columns={'Health..Life.Expectancy.': 'Life expectancy'}, inplace=True)
df_2018.rename(columns={'Healthy life expectancy': 'Life expectancy'}, inplace=True)
df_2019.rename(columns={'Healthy life expectancy': 'Life expectancy'}, inplace=True)

df_2018.rename(columns={'Freedom to make life choices': 'Freedom'}, inplace=True)
df_2019.rename(columns={'Freedom to make life choices': 'Freedom'}, inplace=True)

df_2015.rename(columns={'Trust (Government Corruption)': 'Corruption'}, inplace=True)
df_2016.rename(columns={'Trust (Government Corruption)': 'Corruption'}, inplace=True)
df_2017.rename(columns={'Trust..Government.Corruption.': 'Corruption'}, inplace=True)
df_2018.rename(columns={'Perceptions of corruption': 'Corruption'}, inplace=True)
df_2019.rename(columns={'Perceptions of corruption': 'Corruption'}, inplace=True)

if 'Social support' in df_2018.columns:
    df_2018 = df_2018.drop('Social support', axis=1)
if 'Social support' in df_2019.columns:
    df_2019 = df_2019.drop('Social support', axis=1)
    
if 'Dystopia Residual' in df_2015.columns:
    df_2015 = df_2015.drop('Dystopia Residual', axis=1)
if 'Dystopia Residual' in df_2016.columns:
    df_2016 = df_2016.drop('Dystopia Residual', axis=1)
if 'Dystopia.Residual' in df_2017.columns:
    df_2017 = df_2017.drop('Dystopia.Residual', axis=1)
    
df_unido = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], ignore_index=True)

X = df_unido[['GDP per capita', 'Life expectancy', 'Freedom']]
y = df_unido['Happiness Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

df_test = pd.concat([X_test, y_test], axis=1)

def kafka_producer(df):
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092'],
    )

    # Convertir DataFrame a formato JSON
    df_json = df.to_json(orient='records')

    # Enviar el DataFrame como mensaje
    producer.send("kafka_lab2", value={"data": df_json})
    print("DataFrame sent to Kafka")

# Llama a la función con tu DataFrame df_test
kafka_producer(df_test)
    
