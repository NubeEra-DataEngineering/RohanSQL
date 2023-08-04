# Databricks notebook source
dbutils.help()

# COMMAND ----------

dbutils.fs.ls("/tmp/")

# COMMAND ----------

dbutils.fs.put("/tmp/abc.txt","welcome to dbfs",True)

# COMMAND ----------


dbutils.fs.ls("s3://bkt-rohan/tmp/iris1.csv")
spark.sql("SELECT * from parquet.`s3://bkt-rohan/tmp/iris1.parquet`")


# COMMAND ----------

dbutils.fs.ls("s3://bkt-rohan/tmp/iris1.csv")

# COMMAND ----------

df = spark.sql("SELECT * from parquet.`s3://bkt-rohan/tmp/userdata1.parquet`")


# COMMAND ----------

df.head()

# COMMAND ----------


access_key = "xxxx"

secret_key = "xxxx"

encoded_secret_key = secret_key.replace("/", "%2F")

aws_bucket_name = "bkt-rohan"

mount_name = "rohans3"

dbutils.fs.mount("s3a://%s:%s@%s" % (access_key, encoded_secret_key, aws_bucket_name), "/mnt/%s" % mount_name)

display(dbutils.fs.ls("/mnt/%s" % mount_name))

mount_name = "rohans3"

file_name="iris1.csv"

df = spark.read.format("csv").load("/mnt/%s/%s" % (mount_name , file_name))

df.show()


# COMMAND ----------

strMountPointParquetFile="/mnt/%s/abc.parquet" % (mount_name)
df.write.parquet(strMountPointParquetFile)

# COMMAND ----------


