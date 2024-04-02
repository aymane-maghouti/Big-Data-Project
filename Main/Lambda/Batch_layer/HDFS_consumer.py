import ast

from kafka import KafkaConsumer
import json
from put_data_hdfs import  store_data_in_hdfs

def consum_hdfs():
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
            data = ast.literal_eval(data)
            store_data_in_hdfs(data)



            print("-------------------")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue


