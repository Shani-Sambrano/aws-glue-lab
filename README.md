# AWS Glue ETL Pipeline – Retail Transactions  
*Developed by Elevate AI Solutions*  
*A Marinia Group Company – Building Smart Cities*

---

### 🌐 Website  
**[https://elevate-aisolutions.com](https://elevate-aisolutions.com)**  

**Tagline:** *Our AI Agents talk to your data. Our DAGs do the rest.*

---

## 🧠 Overview
This project demonstrates a complete **AWS Glue ETL pipeline** for cleaning and transforming raw retail transaction data stored in Amazon S3.  
It showcases how Elevate AI Solutions helps clients automate data preparation, standardize analytics pipelines, and enable real-time insights using **serverless data engineering tools**.

---

## 🏗️ Architecture

Below is a visual overview of the pipeline:

![AWS Glue ETL Architecture](architecture_diagram.png)

**Flow:**
**S3 (raw)** → **Glue Crawler (Data Catalog)** → **Glue Spark ETL Job** → **S3 (clean / Parquet)** → **Athena (query-ready)**

---

## ⚙️ What the ETL Job Does
- Cleans inconsistent currency strings (`$, commas, USD`)
- Normalizes quantity values (`three → 3`)
- Standardizes date formats across multiple patterns
- Trims whitespace and fixes messy column names
- Drops duplicates and empty records
- Outputs optimized **Snappy Parquet** files partitioned by `year` and `month` for fast Athena queries

---

## 🚀 Quick Start
1. Upload the raw dataset to:  
   `s3://<your-bucket>/raw/retail_transactions_dirty.csv`

2. Create a Glue Database:  
   `glue_lab_db`

3. Run a Glue Crawler on the `raw/` folder to catalog schema.

4. Create a **Glue Spark Job** using the script:  
   `glue_scripts/retail_clean_job.py`

5. Add parameters:
--input_path s3://<your-bucket>/raw/retail_transactions_dirty.csv
--output_path s3://<your-bucket>/clean/retail_transactions_parquet/

pgsql
Copy code

6. Execute the job and query results in **Athena**.

---

## 🧩 Sample Athena Query
```sql
SELECT product,
    SUM(amount) AS total_revenue,
    SUM(quantity) AS total_qty
FROM glue_lab_db.clean_retail_parquet
GROUP BY product
ORDER BY total_revenue DESC;
🧰 Technologies Used
AWS Glue (Crawler + Spark ETL)

Amazon S3

Amazon Athena

PySpark

AWS IAM

📊 Example Dataset
A sample dataset (data/retail_transactions_dirty.csv) is included for demonstration.
It contains intentionally messy retail transaction data (inconsistent formats, extra whitespace, mixed currency symbols) — ideal for testing ETL pipelines.

🧭 About Elevate AI Solutions
Elevate AI Solutions provides AI-powered workflow orchestration and data infrastructure design for healthcare, government, and enterprise clients.
We specialize in intelligent automation, cloud-native architecture, and machine learning systems built on AWS.

Website: https://elevate-aisolutions.com
Parent Company: Marinia Group, Inc.
Tagline: “Don’t just get orchestration. Get it wired for your industry.”

🏢 © 2025 Marinia Group, Inc.
All rights reserved.
A Marinia Group Company – Building Smart Cities.

