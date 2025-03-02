from pyspark.sql import SparkSession
from algorithms.graph_algorithms import calculate_pagerank, find_connected_components, find_shortest_path
from utils.helpers import load_data, preprocess_data

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Graph Analytics") \
        .getOrCreate()

    # Load and preprocess data
    data = load_data(spark, "data/sample_data.csv")
    preprocessed_data = preprocess_data(data)

    # Execute graph algorithms
    pagerank_results = calculate_pagerank(preprocessed_data)
    connected_components = find_connected_components(preprocessed_data)
    shortest_path = find_shortest_path(preprocessed_data, start_node="A", end_node="B")

    # Print results
    print("PageRank Results:", pagerank_results)
    print("Connected Components:", connected_components)
    print("Shortest Path from A to B:", shortest_path)

    # Stop Spark session
    spark.stop()

if __name__ == "__main__":
    main()