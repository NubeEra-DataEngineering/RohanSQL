# Databricks notebook source
df_remote_table = (spark.read
                   .format("sqlserver")
                   .option("host","rohanserver1.database.windows.net")
                   .option("port","1433")
                   .option("user","rohanadmin")
                   .option("password","rohan1234!")
                   .option("database","dbrohan")
                   .option("dbtable","dbo.iris_data")
                   .load()
                   )

# COMMAND ----------

print(df_remote_table.head())

# COMMAND ----------


