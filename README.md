<!-- Badges & Branding -->
<p align="center">
  <img src="architecture_diagram.png" width="600" alt="AWS Glue ETL Architecture"><br><br>
  <a href="https://elevate-aisolutions.com"><img src="https://img.shields.io/badge/Built%20By-Elevate%20AI%20Solutions-%238A2BE2?style=for-the-badge&logo=amazonaws&logoColor=white"></a>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/AWS%20Glue-Spark%20ETL-orange?style=for-the-badge&logo=apache-spark&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Portfolio%20Demo-green?style=for-the-badge&logo=github&logoColor=white">
</p>

---

# AWS Glue ETL Pipeline – Retail Transactions  

**Developed by [Elevate AI Solutions](https://elevate-aisolutions.com)**  
*A Marinia Group Company – Building Smart Cities*  

> **Tagline:** “Our AI Agents talk to your data. Our DAGs do the rest.”  

---

## 🧭 Overview  
This project demonstrates a complete **AWS Glue ETL pipeline** for cleaning and transforming raw retail transaction data stored in Amazon S3.  
It showcases how **Elevate AI Solutions** helps clients automate data preparation, standardize analytics pipelines, and enable real-time insights using **serverless data engineering tools**.

---

## 🧩 Architecture  
S3 (raw) → Glue Crawler (Data Catalog) → Glue Spark ETL → S3 (clean/Parquet, partitioned) → Athena  

![Architecture Diagram](architecture_diagram.png)

---

## ⚙️ Features  
- Cleans and standardizes messy retail CSV data  
- Normalizes currency, date formats, and text fields  
- Removes duplicates and empty rows  
- Writes **Snappy Parquet** files partitioned by `year` and `month`  
- Ready for querying in **Amazon Athena**  

---

## 🧰 Technologies Used  
- **AWS Glue** (Crawler + Spark ETL)  
- **Amazon S3**  
- **Amazon Athena**  
- **PySpark**  
- **AWS IAM**  

---

## 🧾 Example Dataset  
A sample dataset (`data/retail_transactions_dirty.csv`) is included for demonstration.  
It contains intentionally messy retail transaction data — perfect for testing ETL cleaning pipelines.

---

## 🧑‍💻 Local Simulation  
Run locally using PySpark for testing:  
```bash
python glue_scripts/retail_clean_job.py
🏢 Company Information
Elevate AI Solutions — A Marinia Group Company
Website: https://elevate-aisolutions.com

“Don’t just get orchestration. Get it wired for your industry.”

© 2025 Marinia Group, Inc. – All Rights Reserved.
