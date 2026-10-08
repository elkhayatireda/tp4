from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, sum, count, when 
from pyspark.sql.window import Window

spark = SparkSession.builder\
    .appName("interview_job")\
        .getOrCreate()

df = spark.read.option("header","true").option("inferSchema","true").csv("stores.csv")

df1 = df.groupBy("store_id").agg(
    sum(when(col("status")=="Completed",col("emount").cast("int")).otherwise(0)).alias("total_completed_orders"),
    count(when(col("status")=="Cancelled",1).otherwise(0)).alias("nbr_cancelled"),
)

df1.show()