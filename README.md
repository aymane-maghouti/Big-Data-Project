# Smartphone Price Prediction in Big Data Environment

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Technologies Used](#2-technologies-used)
3. [Architecture](#3-architecture)
4. [Repository Structure](#4-repository-structure)
5. [Software Requirements for Running the Project](#5-software-requirements-for-running-the-project)
6. [How to Run](#6-how-to-run)
7. [Dashboards](#7-dashboards)
8. [Acknowledgments](#8-acknowledgments)
9. [Conclusion](#9-conclusion)
10. [Contacts](#10-contacts)

## 1. Project Overview
This project aims to predict smartphone prices using a combination of batch and stream processing techniques in a Big Data environment. The architecture follows the Lambda Architecture pattern, providing both real-time and batch processing capabilities to users.

## 2. Technologies Used
* **Ingestion Layer:** Apache Kafka (message broker)
* **Stream Layer:** XGBoost (machine learning model), Apache HBase (real-time View)
* **Batch Layer:** Apache Spark (data processing framework), Apache Airflow (workflow orchestration), PostgreSQL (data warehouse (Batch View))
* **Visualization:** Spring Boot (web application framework), Power BI (interactive dashboards)


## 3. Architecture

- Here is the architecture :
 ![architecture](images/architecture.png)


The project architecture consists of five main layers: the ingestion layer, the batch layer, the stream layer, the serving layer and the visualization layer.

### Ingestion Layer
- **Apache Kafka**: Utilized for real-time data ingestion from an API providing smartphone data.
   - **Consumer**: Collects data from the API and feeds it into the stream and batch layer.

### Stream Layer
- **Producer**: A machine learning model developed using XGBoost to estimate smartphone prices. This model runs in real-time and stores predictions in a realtime view. (details about the model <a href="https://github.com/aymane-maghouti/Sentiment-Analysis-for-Jumia-Reviews-and-Smartphone-Price-Prediction-System" target="_blank">here</a> )

### Batch Layer
- **HDFS**: Data from the API is stored in HDFS as part of the data lake solution.
 - **PySpark**: Performs data transformation on stored data using PySpark.
 - **Apache Airflow**: Orchestrates the batch processing workflow.
### Serving Layer
- **Realtime View**: Implemented using HBase to provide real-time access to predicted smartphone prices.
- **Batch View**: Transformed data is stored in PostgreSQL, as the data warehouse solution.
### Visualization Layer
- **Spring Boot Web Application**: Provides a user interface to view real-time smartphone prices.
- **Power BI Dashboard**: Provides batch users with a visualization of processed data.


## 4. Repository Structure
The repository is organized as follows:
```batch 
Big-Data-Project:.
|   README.md
|
+---images
|       architecture.png
|       dashboard_phone.png
|       run_web_app.png
|       spring_boot_web_app.png
|
\---Main
    |   commands.sh
    |   Dashboard.pbix
    |
    +---.idea
    |       workspace.xml
    |
    +---Lambda
    |   |   docker-compose.yaml
    |   |   producer.py
    |   |   transform.py
    |   |
    |   +---.idea
    |   |   |   .gitignore
    |   |   |   .name
    |   |   |   misc.xml
    |   |   |   modules.xml
    |   |   |   price prediction (big data envirnment).iml
    |   |   |   vcs.xml
    |   |   |   workspace.xml
    |   |   |
    |   |   \---inspectionProfiles
    |   |           profiles_settings.xml
    |   |
    |   +---Batch_layer
    |   |   |   batch_layer.py
    |   |   |   batch_pipeline.py
    |   |   |   HDFS_consumer.py
    |   |   |   put_data_hdfs.py
    |   |   |   save_data_postgresql.py
    |   |   |   spark_tranformation.py
    |   |   |   __init__.py
    |   |   |
    |   |   +---dags
    |   |   |       syc_with_Airflow.py
    |   |   |       __init__.py
    |   |   |
    |   |   \---__pycache__
    |   |           batch_layer.cpython-310.pyc
    |   |           HDFS_consumer.cpython-310.pyc
    |   |           put_data_hdfs.cpython-310.pyc
    |   |           save_data_postgresql.cpython-310.pyc
    |   |           spark_tranformation.cpython-310.pyc
    |   |           __init__.cpython-310.pyc
    |   |
    |   +---ML_operations
    |   |   |   xgb_model.pkl
    |   |   |
    |   |   \---__pycache__
    |   +---real_time_web_app(Flask)
    |   |   |   app.py
    |   |   |   get_Data_from_hbase.py
    |   |   |
    |   |   +---static
    |   |   |   +---css
    |   |   |   |       style.css
    |   |   |   |
    |   |   |   \---js
    |   |   |           script.js
    |   |   |
    |   |   +---templates
    |   |   |       index.html
    |   |   |
    |   |   \---__pycache__
    |   |           get_Data_from_hbase.cpython-310.pyc
    |   |
    |   +---Stream_data
    |   |   |   stream_data.csv
    |   |   |   stream_data.py
    |   |   |
    |   |   \---__pycache__
    |   +---Stream_layer
    |   |       insert_data_hbase.py
    |   |       ML_consumer.py
    |   |       stream_pipeline.py
    |   |       __init__.py
    |   |
    |   \---__pycache__
    |           producer.cpython-310.pyc
    |           transform.cpython-310.pyc
    |
    \---real_time_app(Spring boot)
        |   .classpath
        |   .gitignore
        |   .project
        |   HELP.md
        |   mvnw
        |   mvnw.cmd
        |   pom.xml
        |
        +---.mvn
        |   \---wrapper
        |           maven-wrapper.jar
        |           maven-wrapper.properties
        |
        +---.settings
        |       org.eclipse.core.resources.prefs
        |       org.eclipse.jdt.core.prefs
        |       org.eclipse.m2e.core.prefs
        |
        +---src
        |   +---main
        |   |   +---java
        |   |   |   \---com
        |   |   |       \---example
        |   |   |           \---demo
        |   |   |               |   RealTimeAppApplication.java
        |   |   |               |
        |   |   |               +---controller
        |   |   |               |       IndexController.java
        |   |   |               |
        |   |   |               \---service
        |   |   |                       HbaseService.java
        |   |   |
        |   |   \---resources
        |   |       |   application.properties
        |   |       |
        |   |       +---static
        |   |       |   +---css
        |   |       |   |       style.css
        |   |       |   |
        |   |       |   \---js
        |   |       |           script.js
        |   |       |
        |   |       \---templates
        |   |               index.html
        |   |
        |   \---test
        |       \---java
        |           \---com
        |               \---example
        |                   \---demo
        |                           RealTimeAppApplicationTests.java
        |
        \---target
            +---classes
            |   |   application.properties
            |   |
            |   +---com
            |   |   \---example
            |   |       \---demo
            |   |           |   RealTimeAppApplication.class
            |   |           |
            |   |           +---controller
            |   |           |       IndexController.class
            |   |           |
            |   |           \---service
            |   |                   HbaseService.class
            |   |
            |   +---META-INF
            |   |   |   MANIFEST.MF
            |   |   |
            |   |   \---maven
            |   |       \---com.example
            |   |           \---real_time_app
            |   |                   pom.properties
            |   |                   pom.xml
            |   |
            |   +---static
            |   |   +---css
            |   |   |       style.css
            |   |   |
            |   |   \---js
            |   |           script.js
            |   |
            |   \---templates
            |           index.html
            |
            \---test-classes
                \---com
                    \---example
                        \---demo
                                RealTimeAppApplicationTests.class


```

## 5. Software Requirements for Running the Project

This project requires the following software to be installed and configured on your system:

**Big Data Stack:**

* **Apache Kafka (version 2.6.0)**
* **Apache HBase (version 1.2.6)** 
* **Apache Hadoop (version 2.7.0)** 
* **Apache Spark (version 3.3.4)** 
* **PostgreSQL database**

**Programming Languages and Frameworks:**

* **Python (version 3.10.x or later)** 
* **Java 17 (or compatible version)** 
* **Spring Boot** 

**Machine Learning Library:**

* **XGBoost** 

**Additional Tools:**

* **Apache Airflow** 
* **Power BI Desktop** 


By installing and configuring these tools, you will have the necessary environment to run this project and leverage its real-time and batch processing capabilities for smartphone price prediction and analysis.

## 6. How to Run
To set up and run the project locally, follow these steps:

  - Clone the repository:
   ```bash
   git clone https://github.com/aymane-maghouti/Big-Data-Project
   ```


#### **1. Stream Layer**
   - Start Apache zookeeper

   ```batch 
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties
```
   - Start Kafka server

   ```batch 
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties
```
   - Create Kafka topic

   ```batch 
kafka-topics.bat --create --topic smartphoneTopic --bootstrap-server localhost:9092
```

  - Run the kafka producer

   ```batch 
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092
```

  - Run the kafka consumer

   ```batch 
kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092
```

  - Start HDFS and yarn (start-all or start-dfs and start-yarn)

   ```batch 
start-all  
```
   - Start Hbase
   ```batch 
start-hbase  
```
   - Run thrift server (for Hbase)
   ```batch 
hbase thrift start
```

after all this run `stream_pipeline.py` script.

and then open the spring boot appliation in your idea and run  it (you can access to the web app locally on  `localhost:8081/`)

---

![spring_boot](images/run_web_app.png)


note that there is another version of the web app developed using Flask micro-framework(watch the demo video for mor details)

#### **2. Batch Layer**
   - Start the Apache Airflow instance: 

   ```batch 
docker-compose up -d
```
   Access the Apache Airflow web UI (localhost:8080) and run the DAG
   - Start Apache Spark

   ```batch 
spark-shell
```

   - Start Apache zookeeper

   ```batch 
zookeeper-server-start.bat C:/kafka_2.13_2.6.0/config/zookeeper.properties
```
   - Start Kafka server

   ```batch 
kafka-server-start.bat C:/kafka_2.13_2.6.0/config/server.properties
```

  - Run the kafka producer

   ```batch 
kafka-console-producer.bat --topic smartphoneTopic --bootstrap-server localhost:9092
```

  - Run the kafka consumer

   ```batch 
kafka-console-consumer.bat --topic smartphoneTopic --from-beginning --bootstrap-server localhost:9092
```

  - Run HDFS and yarn (start-all or start-dfs and start-yarn)

   ```batch 
start-all  
```
   - Open power BI file `dashboard.pbix` attached with this project 

after all this run `syc_with_Airflow.py` script.


## 7. Dashboards

This project utilizes two dashboards to visualize smartphone price predictions and historical data:

#### **1. Real-Time Dashboard (Spring Boot Application):**

- This dashboard is built using a Spring Boot web application.
- It displays the **predicted price of smartphones in real-time**.
- Users can access this dashboard through a web interface. 


Here is the UI of th Spring Boot web application:


![spring_boot_web_ap](images/spring_boot_web_app.png)


#### **2. Batch Dashboard (Power BI):**

- This dashboard leverages Power BI for interactive data exploration.
- It provides insights into **historical smartphone price trends**.
- This dashboard is designed for batch users interested in historical analysis.


Here is the  Dashboard created in Power BI:

![Phone Dashboard](images/dashboard_phone.png)


## 8. Acknowledgments

- Special thanks to the open-source communities behind `Python`, `Kafka`, `HDFS` , `Spark`,`Hbase`,`Spring Boot`and `Airflow`

## 9. Conclusion

- This big data architecture effectively predicts smartphone prices in real-time and provides historical analysis capabilities. The Lambda architecture facilitates efficient stream processing for real-time predictions using XGBoost and HBase, while Apache Airflow orchestrates batch processing with Spark to populate the PostgreSQL data warehouse for historical insights. This solution empowers real-time and batch users with valuable price information, enabling data-driven decision-making.

you can watch the demo video <a href="https://youtu.be/iClZyC_TZyA" target="_blank">here</a> 

## 10. Contacts

For any inquiries or further information, please contact:
- **Name:** Aymane Maghouti
- **Email:** aymanemaghouti16@gmail.com
- **LinkedIn:** <a href="https://www.linkedin.com/in/aymane-maghouti/" target="_blank">Aymane Maghouti</a><br>
