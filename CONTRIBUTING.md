# Contributing Guidelines

Thank you for your interest in contributing to **AWS Glue Lab – Retail Transactions ETL**, a project developed by **Elevate AI Solutions**, a Marinia Group Company.  

While this repository primarily serves as a *portfolio and demonstration project*, we follow professional software development conventions for all contributions and updates.

---

## 🧭 Repository Purpose
This project demonstrates a full **AWS Glue ETL workflow**:
- Reading and cleaning messy CSV data stored in S3  
- Transforming and standardizing fields using PySpark  
- Writing clean Parquet files for analytics in Athena  

---

## ⚙️ Local Setup
1. Clone the repository  
   ```bash
   git clone https://github.com/Shani-Sambrano/aws-glue-lab.git
   cd aws-glue-lab
Create the required directories if missing:

bash
Copy code
mkdir -p data glue_scripts screenshots
Optional: Install Python 3.10+ and pyspark for local simulation.

bash
Copy code
pip install pyspark==3.5.0
🧩 Branching Convention
main → production-ready or demo-ready code

dev → active development branch

feature/<name> → new scripts or test features

docs/<update> → documentation or markdown edits

When ready, open a pull request (PR) into main.

🧠 Code Style
Follow PEP 8 for Python syntax.

Use snake_case for variable names.

Add comments for each transformation step.

Keep Glue scripts self-contained, portable, and parameterized.

📦 Commits
Use clear, conventional messages:

vbnet
Copy code
feat: add Glue ETL transformation for currency cleanup  
fix: correct date parsing formats  
docs: update README with architecture diagram  
🧾 Documentation Standards
All projects under Elevate AI Solutions must include:

README.md (overview + architecture)

LICENSE.md (Marinia Group proprietary notice)

CREDITS.md (authorship + brand)

PROJECT_STRUCTURE.md (repo layout)

CONTRIBUTING.md (this file)

🏢 Company Note
Elevate AI Solutions — A Marinia Group Company

“Our AI Agents talk to your data. Our DAGs do the rest.”

Website: https://elevate-aisolutions.com

© 2025 Marinia Group, Inc. – All rights reserved.
