"""sorting, regular expression to cleanse text data"""

import re
from pyspark import SparkConf, SparkContext

def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("/Users/tom/Desktop/SparkCourse/Book.txt")
words = input.flatMap(normalizeWords)

"""makes a key with the value then counts how much times it appears.
Count have used countByValue but decided to do it the long way to give more control
"""
wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
#Flips the (word,count) pair to (count, word) then sorts by key which is count
wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
results = wordCountsSorted.collect()

for result in results:
    count = str(result[0])
    word = result[1].encode('ascii', 'ignore')
    if (word):
        print(word.decode() + ":\t\t" + count)
