#########################  Stream layer   #########################

#Start Apache zookeeper
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties

#Start Kafka server
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties

#Create Kafka topic
kafka-topics.bat --create --topic smartphoneTopic --bootstrap-server localhost:9092

#Run the kafka producer
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092

#Run the kafka consumer
kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092

#Run HDFS and yarn (start-all or start-dfs and start-yarn)
start-all  

#Run Hbase
hbase shell  

#Run thrift server (for Hbase)
hbase thrift start

#########################  Batch layer   #########################

#Start the Apache Airflow instance:
docker-compose up -d

#Start Apache Spark
spark-shell

#Start Apache zookeeper
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties

#Start Kafka server
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties

#Run the kafka producer
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092

#Run the kafka consumer
kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092

#Run HDFS and yarn (start-all means start-dfs and start-yarn)
start-all 

