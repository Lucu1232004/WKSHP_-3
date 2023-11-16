from kafka import KafkaConsumer
from json import loads
import pandas as pd
import joblib

def kafka_consumer():
    model = joblib.load('modelo_regresion.pkl')

    consumer = KafkaConsumer(
        'df_test',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for m in consumer:
        try:
            df_json = m.value['data']
            df_received = pd.read_json(df_json, orient='records')

            features = df_received[['GDP per capita', 'Life expectancy', 'Freedom']]
            predictions = model.predict(features)
            df_received['Predicted Happiness Score'] = predictions

            print("Received DataFrame from Kafka:")
            print(df_received)

        except Exception as e:
            print(f"Error: {e}")

kafka_consumer()
