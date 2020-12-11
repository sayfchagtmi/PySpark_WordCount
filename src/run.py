# Import pyspark and os
import pyspark, shutil, os

#Check if output directory already exists so we delete it in order to re-run the code
if os.path.exists('output/'):
   shutil.rmtree('output/')
# Create Spark context with necessary configuration where the first parameter is 
# the cluster URL to connect to (e.g. mesos://host:port, spark://host:port, local[4]) and 
# the second parameter is the name of the application, to display on the cluster web UI.
sc = pyspark.SparkContext("local","PySpark Word Count Exmaple")

# Read data from text file (here 'sample.txt') and split each line into words
words = sc.textFile("data/sample.txt").flatMap(lambda line: line.split(" "))

# Count the occurrence of each word
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

# Save the counts to output (here a file named 'part-00000.txt' in 'result' directory
wordCounts.saveAsTextFile("output")

# Close context
sc.stop()
