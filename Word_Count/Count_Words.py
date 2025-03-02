from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("WordCountAnalysis") \
    .getOrCreate()

# Load the text file into an RDD
text_file = spark.sparkContext.textFile("path/to/your/textfile.txt") # Replace with the path to your text file

# Split each line into words
words = text_file.flatMap(lambda line: line.split(" "))

# Map each word to a key-value pair (word, 1)
word_pairs = words.map(lambda word: (word, 1))

# Reduce by key to count the occurrences of each word
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

# Sort the word counts in descending order
sorted_word_counts = word_counts.map(lambda x: (x[1], x[0])).sortByKey(False)

# Collect the results and print them
for count, word in sorted_word_counts.collect():
    print(f"{word}: {count}")

# Stop the Spark session
spark.stop()