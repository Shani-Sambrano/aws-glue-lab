# AWS Glue ETL Pipeline – Retail Transactions

End-to-end AWS Glue ETL pipeline that cleans messy retail data in S3 and outputs partitioned Parquet files for Athena analytics.

## Architecture
S3 (raw) → Glue Crawler (Data Catalog) → Glue Spark ETL → S3 (clean/Parquet, partitioned) → Athena

## What the job does
- Standardizes column names & trims whitespace  
- Parses multiple date formats into one date column  
- Cleans currency strings (`$`, commas, “USD”) into numeric `amount`  
- Normalizes `quantity` (e.g., “three” → 3)  
- Drops duplicates & all-null rows  
- Writes **Snappy Parquet** partitioned by `year`/`month`

## How to run (quick)
1. Upload CSV to `s3://<your-bucket>/raw/retail_transactions_dirty.csv`
2. Create Glue Database `glue_lab_db` and run a Crawler on `raw/`
3. Create a Glue **Spark** job with the script in `glue_scripts/retail_clean_job.py`
4. Set:
   - `--input_path  s3://<your-bucket>/raw/retail_transactions_dirty.csv`
   - `--output_path s3://<your-bucket>/clean/retail_transactions_parquet/`
5. Query the Parquet in **Athena**.

## Sample Athena query
```sql
SELECT product, SUM(amount) AS total_revenue, SUM(quantity) AS total_qty
FROM glue_lab_db.clean_retail_parquet
GROUP BY product
ORDER BY total_revenue DESC;


## 3) (Optional) Add a minimal `.gitignore`
```bash
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.DS_Store
.vscode/
.ipynb_checkpoints/
.env
