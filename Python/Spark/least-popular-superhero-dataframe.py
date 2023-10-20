from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("MostPopularSuperhero").getOrCreate()

schema = StructType([ \
                     StructField("id", IntegerType(), True), \
                     StructField("name", StringType(), True)])

names = spark.read.schema(schema).option("sep", " ").csv("/Users/tom/Desktop/SparkCourse/Marvel+Names.txt")

lines = spark.read.text("/Users/tom/Desktop/SparkCourse/Marvel+Graph.txt")

connections = lines.withColumn("id", func.split(func.trim(func.col("value")), " ")[0]) \
    .withColumn("connections", func.size(func.split(func.trim(func.col("value")), " ")) - 1) \
    .groupBy("id").agg(func.sum("connections").alias("connections"))
    

#print all the superheros with 1 connection
filteredSuperheros = connections.filter(func.col("connections")==1)
oneConnectionSuperheros = filteredSuperheros.join(names, 'id').select("id", "name", "connections")\
    .sort(func.col("id").desc()).show(filteredSuperheros.count())


#print all the superheros with less than 1 connection
filertedSuperheros1 = connections.filter(func.col("connections")<1)
zeroConnectionSuperheros = filertedSuperheros1.join(names, 'id').select("id", "name", "connections")\
    .sort(func.col("id").desc()).show(filertedSuperheros1.count())

extra = connections.agg(func.min("connections")).first()[0]



