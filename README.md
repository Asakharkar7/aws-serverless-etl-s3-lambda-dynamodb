# aws-serverless-etl-s3-lambda-dynamodb
Fully serverless ETL pipeline using AWS S3, Lambda, and DynamoDB. Automatically processes CSV files on S3 upload and loads transformed data into DynamoDB


# 🛰️ Serverless ETL Pipeline — S3 → Lambda → DynamoDB  

A fully automated, serverless ETL pipeline that processes CSV files the moment they are uploaded to Amazon S3. The pipeline extracts, transforms, and loads (ETL) the data into DynamoDB using AWS Lambda.  
This is a real-world industry pattern used in fintech, retail, and supply-chain data platforms.

---

## 🚀 Architecture Overview

<img width="1536" height="1024" alt="Architecture" src="https://github.com/user-attachments/assets/d345ed0f-603c-454c-9abf-3f6448cd0829" />


---

## 🧩 Components in This Repository

| Folder | Description |
|--------|-------------|
| `/lambda/` | Lambda ETL Python code |
| `/sample_data/` | Sample CSV used for testing |
| `/dynamodb_schema/` | Table design + PK notes |
| `/architecture/etl_diagram.png` | Diagram of S3 → Lambda → DynamoDB flow |
| `/tests/` | Local test events for Lambda |

---

## 🛠️ Technologies Used

- **AWS S3** – raw storage + event notifications  
- **AWS Lambda (Python 3.12)** – ETL transformation logic  
- **AWS DynamoDB** – NoSQL storage for clean data  
- **IAM Roles** – controlled access between services  
- **CloudWatch Logs** – logging & debugging  

---

## 🧠 What the Lambda Does

✔ Reads S3 event → extracts bucket and object key  
✔ Downloads CSV into `/tmp`  
✔ Cleans & transforms each row  
✔ Inserts items into DynamoDB  
✔ Logs successes / errors to CloudWatch  

---

## 📊 Example Input (CSV)

```csv
InvoiceNo,StockCode,Description,Quantity,UnitPrice,CustomerID,Country
536365,85123A,WHITE METAL LANTERN,6,3.39,17850,United Kingdom

## 📥 Example DynamoDB Item

{
  "InvoiceNo": "536365",
  "StockCode": "85123A",
  "Quantity": 6,
  "UnitPrice": 3.39,
  "Country": "United Kingdom"
}

🎯 Key Highlights

100% serverless — no EC2, no infrastructure

Event-driven ETL triggered automatically

Handles CSV files up to 50MB

IAM least-privilege implementation

CloudWatch-based monitoring and debugging

🔍 Learning Outcomes

S3 → Lambda event triggers

Python ETL logic inside Lambda

DynamoDB schema design

IAM access configuration

CloudWatch troubleshooting




