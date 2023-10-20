from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

spark = SparkSession.builder.appName("CustomerOrder").getOrCreate()

schema = StructType([ \
                     StructField("cust_id", IntegerType(), True), \
                     StructField("item_id", IntegerType(), True), \
                     StructField("item_price", FloatType(), True)])

# // Read the file as dataframe
df = spark.read.schema(schema).csv("/Users/tom/Desktop/SparkCourse/customer-orders.csv")
df.printSchema()

# Aggregate Customer to find out total spent
sumPrice = df.groupBy("cust_id").agg({"item_price":"sum"}).sort("sum(item_price)")
sumPriceF = sumPrice.withColumn("rounded", func.round("sum(item_price)",2)).select("cust_id", "rounded").sort("rounded")
sumPriceF.show(sumPriceF.count())


spark.stop()

                                                  