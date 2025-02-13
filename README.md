# AWS Cost Optimizer

## 📌 Overview
AWS Cost Optimizer is a Python-based tool that analyzes AWS cost data using the AWS Cost Explorer API. It provides **daily cost breakdowns**, **identifies high-cost services**, and **suggests optimizations**.

## 🚀 Features
✅ Retrieves AWS cost usage for the last 7 days  
✅ Breaks down costs by **AWS service**  
✅ Exports data to **CSV format**  
✅ Can be extended to send alerts for high costs  

## 🛠️ Setup & Installation
### 1️⃣ Prerequisites
- **Python 3.7+**
- **AWS CLI configured** (`aws configure`)
- **IAM Role with `ce:GetCostAndUsage` permission**

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
