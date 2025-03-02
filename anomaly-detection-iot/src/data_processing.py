from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

def load_data(file_path):
    spark = SparkSession.builder.appName("IoT Data Processing").getOrCreate()
    return spark.read.csv(file_path, header=True, inferSchema=True)

def clean_data(df):
    # Remove rows with null values
    df = df.na.drop()
    return df

def transform_data(df):
    # Example transformation: Convert timestamp to a proper format
    df = df.withColumn("timestamp", col("timestamp").cast("timestamp"))
    return df

def aggregate_data(df, time_window="1 hour"):
    # Example aggregation: Group by device_id and time window
    return df.groupBy("device_id", "timestamp").agg({"value": "avg"})

def preprocess_data(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    df = transform_data(df)
    df = aggregate_data(df)
    return df