from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("CustomerOrders")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amnt_spent = round(float(fields[2]),2)
    return (customer_id, amnt_spent)

lines = sc.textFile("/Users/tom/Desktop/SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)
"""
rdd = key, value . mapvalues treats value as x. reduceByKey makes sure the key is unique
"""
totalsByCustomer = rdd.reduceByKey(lambda x,y: x+y)
totalSpentSorted = totalsByCustomer.map(lambda x: (x[1], x[0])).sortByKey()
totalSpentSorted = totalSpentSorted.map(lambda x: (x[1], x[0]))
#results = totalSpentSorted.take(10)
results = totalSpentSorted.collect()

for result in results:
    print(result)


'''
totalsByCustomer = rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
#50 (23.57,1
#4 (24.66,1
#50 (12.99,2
totalSpent = totalsByCustomer.mapValues(lambda x: x[0] + x[1])
totalSpentSorted = totalSpent.map(lambda x: (x[1], x[0])).sortByKey()
results = totalSpent.collect()
'''