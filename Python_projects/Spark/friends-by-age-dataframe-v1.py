from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

#look at the csv file it has a header. assume that the schema is easily readable
people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("/Users/tom/Desktop/SparkCourse/fakefriends-header.csv")
    
'''print("Here is our inferred schema:")
people.printSchema()

print("Filter out anyone over 21:")
people.filter(people.age < 21).show()

print("Make everyone 10 years older:")
people.select(people.name, people.age + 10).show()
'''

print("Let's display the name, age, and friends columns:")
people.select("name","age","friends").show()

print("Group by age")
people.groupBy("age").count().sort("age").show()

print("For Each age what is the avg num of friends:")
people.groupBy("age").avg("friends").show()

#Needed when opening a session, need to close the session
spark.stop()



