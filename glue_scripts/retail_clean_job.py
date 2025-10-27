# Glue version: 4.0 or 5.0 | Job type: Spark
# Author: Shani Sambrano | Elevate AI Solutions
# Name suggestion: retail_clean_job

import sys, re
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType, IntegerType

# Optional args for flexibility
args = {}
try:
    args = getResolvedOptions(sys.argv, ["JOB_NAME", "input_path", "output_path"])
    input_path = args["input_path"]
    output_path = args["output_path"]
except Exception:
    input_path = "s3://shani-glue-lab-usw2/raw/retail_transactions_dirty.csv"
    output_path = "s3://shani-glue-lab-usw2/clean/retail_transactions_parquet/"

sc = SparkContext()
glueCtx = GlueContext(sc)
spark = glueCtx.spark_session
job = Job(glueCtx)
job.init(args.get("JOB_NAME", "retail_clean_job"), args)

# 1) Read raw CSV from S3
df = (spark.read.option("header", True)
               .option("mode", "PERMISSIVE")
               .csv(input_path))

# 2) Normalize column names
def norm(c):
    return re.sub(r"[^a-z0-9_]", "", c.strip().lower().replace(" ", "_"))
df = df.select([F.col(c).alias(norm(c)) for c in df.columns])

# 3) Trim whitespace
for c, t in df.dtypes:
    if t == "string":
        df = df.withColumn(c, F.trim(F.col(c)))

# 4) Clean numerics
df = (
    df.withColumn("amount", F.regexp_replace(F.col("amount"), r"[$,]", ""))
      .withColumn("amount", F.regexp_replace(F.col("amount"), r"\s*USD\s*", ""))
      .withColumn("amount", F.col("amount").cast(DoubleType()))
      .withColumn("quantity",
        F.when(F.lower(F.col("quantity")) == "three", F.lit(3))
         .otherwise(F.col("quantity").cast(IntegerType())))
)

# 5) Parse multiple date formats into one standardized date column
fmts = ["yyyy-MM-dd", "MM/dd/yyyy", "dd-MMM-yyyy"]
df = df.withColumn("tx_date", F.coalesce(*[F.to_date(F.col("transaction_date"), f) for f in fmts]))

# 6) Drop nulls & duplicates
df = df.dropna(how="all")
if "transaction_id" in df.columns:
    df = df.dropDuplicates(["transaction_id"])
else:
    df = df.dropDuplicates()

# 7) Add year/month partitions for optimized storage
df = df.withColumn("year", F.year("tx_date")).withColumn("month", F.month("tx_date"))

# 8) Write clean data as Parquet to S3
(df.write.mode("overwrite")
    .partitionBy("year", "month")
    .parquet(output_path))

job.commit()
