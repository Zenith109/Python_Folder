from pyspark.sql import SparkSession
from data_processing import load_and_preprocess_data
from anomaly_detection import AnomalyDetector

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("IoT Anomaly Detection") \
        .getOrCreate()

    # Load and preprocess IoT data
    data = load_and_preprocess_data(spark, "data/raw/iot_data.csv")

    # Initialize anomaly detector
    anomaly_detector = AnomalyDetector()

    # Fit the model on the preprocessed data
    anomaly_detector.fit(data)

    # Predict anomalies
    anomalies = anomaly_detector.predict(data)

    # Output the detected anomalies
    anomalies.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()