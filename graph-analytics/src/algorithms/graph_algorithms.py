from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col
from pyspark.sql import Row
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, IntegerType
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql import Window

def calculate_pagerank(graph: DataFrame, max_iter: int = 10, tol: float = 1e-6) -> DataFrame:
    # Initialize PageRank values
    num_nodes = graph.select("src").distinct().count()
    ranks = graph.select("src").distinct().withColumn("rank", F.lit(1.0 / num_nodes))
    
    for _ in range(max_iter):
        # Join with graph to calculate new ranks
        contributions = graph.join(ranks, graph.src == ranks.src) \
            .groupBy(graph.dst) \
            .agg(F.sum(ranks.rank / F.count(graph.src)).alias("contribution"))
        
        # Update ranks
        new_ranks = contributions.withColumn("rank", F.lit(0.15) + F.lit(0.85) * F.coalesce(col("contribution"), F.lit(0)))
        
        # Check for convergence
        if new_ranks.join(ranks, "dst").select(F.abs(new_ranks.rank - ranks.rank)).agg(F.max("abs((rank - rank))")).first()[0] < tol:
            break
        
        ranks = new_ranks
    
    return ranks

def find_connected_components(graph: DataFrame) -> DataFrame:
    # Initialize connected components
    nodes = graph.select("src").union(graph.select("dst")).distinct()
    components = nodes.withColumn("component", col("src"))
    
    # Iteratively update components
    while True:
        updated_components = graph.join(components, graph.src == components.component) \
            .select(graph.dst, components.component) \
            .distinct() \
            .withColumnRenamed("dst", "component")
        
        if updated_components.count() == 0:
            break
        
        components = components.union(updated_components).distinct()
    
    return components

def find_shortest_path(graph: DataFrame, start_node: str, end_node: str) -> list:
    # Initialize distances
    distances = graph.select("src").distinct().withColumn("distance", F.lit(float("inf")))
    distances = distances.withColumn("distance", F.when(col("src") == start_node, 0).otherwise(col("distance")))
    
    # Initialize queue
    queue = [start_node]
    
    while queue:
        current_node = queue.pop(0)
        current_distance = distances.filter(col("src") == current_node).select("distance").first()[0]
        
        neighbors = graph.filter(col("src") == current_node).select("dst").collect()
        
        for neighbor in neighbors:
            neighbor_node = neighbor.dst
            new_distance = current_distance + 1  # Assuming each edge has a weight of 1
            
            if new_distance < distances.filter(col("src") == neighbor_node).select("distance").first()[0]:
                distances = distances.withColumn("distance", F.when(col("src") == neighbor_node, new_distance).otherwise(col("distance")))
                queue.append(neighbor_node)
    
    return distances.filter(col("src") == end_node).select("distance").first()[0]