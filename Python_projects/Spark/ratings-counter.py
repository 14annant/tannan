## to run. in terminal run "spark-submit ratings-counter.py" 
from pyspark import SparkConf, SparkContext #This will be included in most spark scripts
import collections #this will sort our results

'''local setMaster means script is running locally on single cluster. 
setAppName is naming the Spark Context '''
conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("/Users/tom/Desktop/SparkCourse/ml-100k/u.data")

#takes lines breaks it  up by white space then returns value of positon 2
ratings = lines.map(lambda x: x.split()[2])
#counts unique ratings and how much time they appear
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.items():
    print("%s %i" % (key, value))
