from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.avro.functions import from_avro
import requests

schemaregistry="http://localhost:8081"
topic="e-commerce-tiki-store-data-source"
response = requests.get('{}/subjects/{}-value/versions/latest/schema'.format(schemaregistry, topic))

# error check
response.raise_for_status()

# extract the schema from the response
schema = response.text

spark=SparkSession.builder.getOrCreate()

df=spark.read.format('kafka')\
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", topic) \
    .load()\
    .selectExpr("substring(value, 6) as value")\
    .withColumn('value',from_avro("value", schema))\
    .select('value.*')

df.show()
"""
+----------------+
|avg_rating_point|
+----------------+
|          4.6736|
|          4.6736|
+----------------+
"""
