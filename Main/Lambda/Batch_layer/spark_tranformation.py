import pandas as pd
import  pickle
import ast
from xgboost import XGBRegressor
from transform import *
from hdfs import InsecureClient
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, StringType
from pyspark.ml.feature import VectorAssembler

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("Read CSV from HDFS to Spark") \
    .getOrCreate()


def return_spark_df():
    hdfs_client = InsecureClient('http://localhost:50070')

    with hdfs_client.read("/batch-layer/raw_data.csv") as reader:
        pandas_df = pd.read_csv(reader)

    spark_df = spark.createDataFrame(pandas_df)

    return spark_df





def spark_tranform():
    spark_df = return_spark_df()

    spark_df = spark_df.dropna()

    # Convert columns to numeric types
    spark_df = spark_df.withColumn("screen_size", spark_df["screen_size"].cast("float"))
    spark_df = spark_df.withColumn("ram", spark_df["ram"].cast("float"))
    spark_df = spark_df.withColumn("rom", spark_df["rom"].cast("float"))
    spark_df = spark_df.withColumn("battary", spark_df["battary"].cast("float"))

    # Define UDFs for mapping functions
    map_brand_udf = udf(lambda brand: map_brand_to_numeric(brand), IntegerType())
    map_sim_type_udf = udf(lambda sim_type: map_sim_type_to_numeric(sim_type), IntegerType())

    # Apply mapping functions
    spark_df = spark_df.withColumn("brand", map_brand_udf(spark_df["brand"]))
    spark_df = spark_df.withColumn("sim_type", map_sim_type_udf(spark_df["sim_type"]))

    # Load pre-trained XGBoost model
    model = pickle.load(open("xgb_model.pkl", "rb"))

    # Assemble features for prediction
    feature_cols = ["brand", "screen_size", "ram", "rom", "sim_type", "battary"]
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    assembled_df = assembler.transform(spark_df)

    # Predict prices
    predictions = model.predict(assembled_df.toPandas())
    ######################################################
    # Convert assembled Spark DataFrame to Pandas DataFrame
    assembled_pandas_df = assembled_df.toPandas()

    # Predict prices
    predictions = model.predict(assembled_pandas_df[feature_cols])

    # Convert predictions to a Pandas DataFrame
    predictions_df = pd.DataFrame(predictions, columns=["price"])

    # Add predicted prices as a new column to the assembled Pandas DataFrame
    assembled_pandas_df["price"] = predictions_df

    # Convert the assembled Pandas DataFrame back to a Spark DataFrame
    spark_df = spark.createDataFrame(assembled_pandas_df)

    print("data transformed successfully")
    return spark_df









