"""Map vs flatmap. Regular expressions. NLTK python libary could have helped"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("/Users/tom/Desktop/SparkCourse/Book.txt")
words = input.flatMap(lambda x: x.split())
#Count how much each unique value appears
wordCounts = words.countByValue()

for word, count in wordCounts.items():
    cleanWord = word.encode('ascii', 'ignore')
    if (cleanWord):
        print(cleanWord.decode() + " " + str(count))
