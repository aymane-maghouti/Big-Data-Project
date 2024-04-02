import time
from producer import send_message

from HDFS_consumer import consum_hdfs
import threading
from Stream_data.stream_data import generate_real_time_data


def producer_thread():
    while True:
        try:
            file_path = '../Stream_data/stream_data.csv'
            message = generate_real_time_data(file_path)

            send_message(message)
            print("Message sent to Kafka topic")

            # Sleep for 5 seconds before collecting and sending the next set of data
            time.sleep(5)

        except Exception as e:
            print(f"Error in producer_thread: {str(e)}")

def consumer_thread():
    while True:
        try:
            consum_hdfs()
            # Sleep for a short interval before consuming the next message
            time.sleep(3)
        except Exception as e:
            print(f"Error in consumer_thread: {str(e)}")

# Create separate threads for producer and consumer
producer_thread = threading.Thread(target=producer_thread)
consumer_thread = threading.Thread(target=consumer_thread)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for the threads to finish (which will never happen in this case as they run infinitely)
producer_thread.join()
consumer_thread.join()
