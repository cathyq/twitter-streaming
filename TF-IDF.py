from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF
sc = SparkContext(appName = "twitter-stream")

# Read a set of text files as TF vectors
rdd = sc.wholeTextFiles("data").map(lambda (name, text): text.split())
tf = HashingTF()
tfVectors = tf.transform(rdd).cache()

# Compute the IDF, then the TF-IDF vectors
idf = IDF()
IDFModel = idf.fit(tfVectors)
tfIdfVectors = IDFModel.transform(tfVectors)
tfIdfVectors.foreach(print)
