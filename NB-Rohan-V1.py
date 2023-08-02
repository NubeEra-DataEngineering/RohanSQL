# Databricks notebook source
storage_account = "sarohanv1"
container_name = "container-rohanv1"
source_url = "wasbs://{0}@{1}.blob.core.windows.net".format(container_name,storage_account)

access_key = "o/AJ3mYq5Sp9beEOAydhCoRVgdSr5p11GXKR+lyXvdWtI8VeUW2VgM4rj3xdnyImZKDdr20coxQk+AStNnbHOQ=="
mount_point_url = "/mnt/gen1dataset"

extra_configs_key = f"fs.azure.account.key.{storage_account}.blob.core.windows.net"
extra_configs_value = access_key
extra_configs_dict = {extra_configs_key:extra_configs_value}

# COMMAND ----------

dbutils.fs.mount(source = source_url,
                 mount_point = mount_point_url,
                 extra_configs = extra_configs_dict)

# COMMAND ----------

dbutils.fs.ls(mount_point_url)

# COMMAND ----------


