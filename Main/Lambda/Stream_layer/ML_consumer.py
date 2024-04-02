from kafka import KafkaConsumer
import json

from transform import  transformation
from Stream_layer.insert_data_hbase import insert_dataHbase
def consum():
    # Kafka broker configuration
    bootstrap_servers = 'localhost:9092'
    topic = 'smartphoneTopic'

    # Create a Kafka consumer
    consumer = KafkaConsumer(topic,
                             group_id='my_consumer_group',
                             auto_offset_reset='latest',
                             bootstrap_servers=bootstrap_servers,
                             value_deserializer=lambda x: x.decode('utf-8'))



    for message in consumer:
        try:
            data = message.value
            print('before ml operation')
            res = transformation(data)
            print(res)
            insert_dataHbase(res)



            print("-------------------")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue


