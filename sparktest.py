import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext()
print sc

