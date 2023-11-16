import psycopg2
from kafka import KafkaConsumer
import json
import pandas as pd
import joblib

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '******',
    'database': 'wkshp3'
}

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    consumer = KafkaConsumer(
        'kafka_lab2',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    model = joblib.load('modelo_regresion.pkl')

    for m in consumer:
        try:
            df_json = m.value['data']
            df_received = pd.read_json(df_json, orient='records')
            
            df_received.rename(columns={'Happiness Score': 'Happiness score'}, inplace=True)
            features = df_received[['GDP per capita', 'Life expectancy', 'Freedom', 'Happiness score']]
            predictions = model.predict(features)
            df_received['Predicted Happiness Score'] = predictions

            print("Received DataFrame from Kafka:")
            print(df_received)

            for index, row in df_received.iterrows():
                insert_query = """
                    INSERT INTO dbconsumer ("GDP per capita", "Life expectancy", "Freedom", "Happiness Score", "Predicted Happiness Score")
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (row['GDP per capita'], row['Life expectancy'], row['Freedom'], row['Happiness score'], row['Predicted Happiness Score']))

            conn.commit()

        except Exception as e:
            print(f"Error: {e}")

except psycopg2.Error as err:
    print(f"Error connecting to the database: {err}")

finally:
    if 'conn' in locals() and conn is not None:
        cursor.close()
        conn.close()
        print("Connection closed")

