# Project Structure

This document summarizes the repository layout and the purpose of each folder/file.

aws-glue-lab/
├─ README.md # Project overview, setup, and usage
├─ LICENSE.md # Proprietary license (Marinia Group, Inc.)
├─ CREDITS.md # Author + brand acknowledgments
├─ PROJECT_STRUCTURE.md # (this file)
├─ .gitignore # Common dev artifacts ignored by git
├─ architecture_diagram.png # S3 → Glue → Athena pipeline diagram
│
├─ data/ # Sample input data (dirty CSV)
│ └─ retail_transactions_dirty.csv
│
├─ glue_scripts/ # AWS Glue Spark ETL jobs
│ └─ retail_clean_job.py
│
└─ screenshots/ # Proof of execution (add yours)
├─ glue_job_run.png # Glue job “Succeeded” screenshot
└─ athena_query_result.png # Athena query results screenshot

css
Copy code

## Folder Details

- **data/**  
  Contains intentionally messy CSV used to demonstrate cleaning and transformation.

- **glue_scripts/**  
  Production-style PySpark scripts for AWS Glue (Spark) jobs.

- **screenshots/**  
  Evidence for portfolio/review (Glue run, Athena query, etc.).  
  *Tip:* keep filenames descriptive and timestamped if you add multiple runs.

- **architecture_diagram.png**  
  Visual S3 → Glue Crawler → Glue ETL → S3 (Parquet) → Athena flow.

## Generate a live tree (optional)
Create a text snapshot of your current repo tree (Windows):
cmd.exe /c tree /F > repo_tree.txt

yaml
Copy code
Then commit it if you want a point-in-time view for audits/reviews.

---
*Developed by Elevate AI Solutions — A Marinia Group Company*
