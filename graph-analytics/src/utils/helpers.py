def load_data(file_path):
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("GraphAnalytics").getOrCreate()
    data = spark.read.csv(file_path, header=True, inferSchema=True)
    return data

def preprocess_data(data):
    # Example preprocessing: removing duplicates and null values
    data = data.dropDuplicates()
    data = data.na.drop()
    return data

def visualize_graph(graph):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.Graph()
    for row in graph.collect():
        G.add_edge(row['src'], row['dst'])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10)
    plt.show()